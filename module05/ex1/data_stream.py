from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class with core streaming functionality."""

    def __init__(self, stream_id: str) -> None:
        """Initialize stream with an ID and processing counters."""
        self.stream_id: str = stream_id
        self.total_processed: int = 0
        self.errors: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data (abstract)."""
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter data based on criteria (default: return all)."""
        if criteria is None:
            return list(data_batch)
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        return {
            "stream_id": self.stream_id,
            "total_processed": self.total_processed,
            "errors": self.errors,
        }


class SensorStream(DataStream):
    """Stream specialized for environmental sensor data."""

    def __init__(self, stream_id: str) -> None:
        """Initialize sensor stream."""
        super().__init__(stream_id)
        self.stream_type: str = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process sensor readings: extract numeric values and avg."""
        try:
            if not isinstance(data_batch, list) or len(data_batch) == 0:
                self.errors += 1
                return "Error: Empty or invalid sensor batch"
            readings: List[float] = []
            count: int = len(data_batch)
            for item in data_batch:
                if isinstance(item, dict) and "value" in item:
                    readings.append(float(item["value"]))
                elif isinstance(item, (int, float)):
                    readings.append(float(item))
                elif isinstance(item, str) and ":" in item:
                    parts: List[str] = item.split(":")
                    if parts[0] == "temp":
                        try:
                            readings.append(float(parts[1]))
                        except (ValueError, IndexError):
                            pass
            self.total_processed += count
            if len(readings) == 0:
                return f"Sensor analysis: {count} readings processed"
            avg: float = sum(readings) / len(readings)
            return (
                f"Sensor analysis: {count} readings processed, "
                f"avg temp: {avg}\u00b0C"
            )
        except Exception as e:
            self.errors += 1
            return f"Error processing sensor batch: {e}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter sensor data, 'critical' keeps high values."""
        if criteria == "critical":
            result: List[Any] = []
            for item in data_batch:
                val: Optional[float] = None
                if isinstance(item, dict) and "value" in item:
                    val = float(item["value"])
                elif isinstance(item, (int, float)):
                    val = float(item)
                if val is not None and val > 30.0:
                    result.append(item)
            return result
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return sensor-specific stats."""
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["stream_type"] = self.stream_type
        return stats


class TransactionStream(DataStream):
    """Stream specialized for financial transaction data."""

    def __init__(self, stream_id: str) -> None:
        """Initialize transaction stream."""
        super().__init__(stream_id)
        self.stream_type: str = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process transactions: count ops and compute net flow."""
        try:
            if not isinstance(data_batch, list) or len(data_batch) == 0:
                self.errors += 1
                return "Error: Empty or invalid transaction batch"
            count: int = 0
            net_flow: float = 0.0
            for item in data_batch:
                if isinstance(item, dict):
                    action: str = item.get("action", "")
                    amount: float = float(item.get("amount", 0))
                    if action == "buy":
                        net_flow -= amount
                    elif action == "sell":
                        net_flow += amount
                    count += 1
                elif isinstance(item, str) and ":" in item:
                    parts: List[str] = item.split(":")
                    action = parts[0].strip()
                    try:
                        amount = float(parts[1])
                    except (ValueError, IndexError):
                        amount = 0.0
                    if action == "buy":
                        net_flow -= amount
                    elif action == "sell":
                        net_flow += amount
                    count += 1
            self.total_processed += count
            sign: str = "+" if net_flow >= 0 else ""
            return (
                f"Transaction analysis: {count} operations, "
                f"net flow: {sign}{net_flow} units"
            )
        except Exception as e:
            self.errors += 1
            return f"Error processing transaction batch: {e}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter transactions, 'large' keeps amount > 100."""
        if criteria == "large":
            result: List[Any] = []
            for item in data_batch:
                amount: float = 0.0
                if isinstance(item, dict):
                    amount = float(item.get("amount", 0))
                elif isinstance(item, str) and ":" in item:
                    parts: List[str] = item.split(":")
                    try:
                        amount = float(parts[1])
                    except (ValueError, IndexError):
                        pass
                if amount > 100:
                    result.append(item)
            return result
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return transaction-specific stats."""
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["stream_type"] = self.stream_type
        return stats


class EventStream(DataStream):
    """Stream specialized for system event data."""

    def __init__(self, stream_id: str) -> None:
        """Initialize event stream."""
        super().__init__(stream_id)
        self.stream_type: str = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process events: count total and detect errors."""
        try:
            if not isinstance(data_batch, list) or len(data_batch) == 0:
                self.errors += 1
                return "Error: Empty or invalid event batch"
            count: int = len(data_batch)
            error_count: int = len(
                [e for e in data_batch if "error" in str(e).lower()]
            )
            self.total_processed += count
            error_msg: str = ""
            if error_count > 0:
                error_msg = f", {error_count} error detected"
            return f"Event analysis: {count} events{error_msg}"
        except Exception as e:
            self.errors += 1
            return f"Error processing event batch: {e}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter events, 'errors' keeps only error events."""
        if criteria == "errors":
            return [
                e for e in data_batch if "error" in str(e).lower()
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return event-specific stats."""
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["stream_type"] = self.stream_type
        return stats


class StreamProcessor:
    """Manager that handles multiple stream types polymorphically."""

    def __init__(self) -> None:
        """Initialize the stream processor."""
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Register a stream for processing."""
        self.streams.append(stream)

    def process_all(
        self, data_map: Dict[str, List[Any]]
    ) -> Dict[str, str]:
        """Process data for all registered streams by stream_id."""
        results: Dict[str, str] = {}
        for stream in self.streams:
            batch: List[Any] = data_map.get(stream.stream_id, [])
            try:
                results[stream.stream_id] = stream.process_batch(batch)
            except Exception as e:
                results[stream.stream_id] = f"Error: {e}"
        return results

    def filter_all(
        self,
        data_map: Dict[str, List[Any]],
        criteria: Optional[str] = None
    ) -> Dict[str, List[Any]]:
        """Filter data for all registered streams."""
        results: Dict[str, List[Any]] = {}
        for stream in self.streams:
            batch: List[Any] = data_map.get(stream.stream_id, [])
            try:
                results[stream.stream_id] = stream.filter_data(
                    batch, criteria
                )
            except Exception as e:
                results[stream.stream_id] = []
                print(f"Filter error on {stream.stream_id}: {e}")
        return results

    def get_all_stats(
        self,
    ) -> List[Dict[str, Union[str, int, float]]]:
        """Get statistics from all registered streams."""
        return [stream.get_stats() for stream in self.streams]


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    # --- Individual stream demos ---
    print("\nInitializing Sensor Stream...")
    sensor: DataStream = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    sensor_batch: List[Any] = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(
        "Processing sensor batch: "
        "[temp:22.5, humidity:65, pressure:1013]"
    )
    print(sensor.process_batch(sensor_batch))

    print("\nInitializing Transaction Stream...")
    trans: DataStream = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans.stream_id}, Type: Financial Data")
    trans_batch: List[Any] = ["sell:100", "buy:150", "sell:75"]
    print(f"Processing transaction batch: [{', '.join(trans_batch)}]")
    print(trans.process_batch(trans_batch))

    print("\nInitializing Event Stream...")
    event: DataStream = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: System Events")
    event_batch: List[str] = ["login", "error", "logout"]
    print(f"Processing event batch: [{', '.join(event_batch)}]")
    print(event.process_batch(event_batch))

    # --- Polymorphic processing demo ---
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor: StreamProcessor = StreamProcessor()
    sensor2: DataStream = SensorStream("SENSOR_002")
    trans2: DataStream = TransactionStream("TRANS_002")
    event2: DataStream = EventStream("EVENT_002")
    processor.add_stream(sensor2)
    processor.add_stream(trans2)
    processor.add_stream(event2)

    data_map: Dict[str, List[Any]] = {
        "SENSOR_002": [25.0, 31.5],
        "TRANS_002": ["buy:50", "sell:200", "buy:30", "sell:80"],
        "EVENT_002": ["login", "error", "logout"],
    }

    results: Dict[str, str] = processor.process_all(data_map)
    print("\nBatch 1 Results:")
    print(f"- Sensor data: {results['SENSOR_002']}")
    print(f"- Transaction data: {results['TRANS_002']}")
    print(f"- Event data: {results['EVENT_002']}")

    # --- Filtering demo ---
    filter_data_map: Dict[str, List[Any]] = {
        "SENSOR_002": [25.0, 31.5, 35.0],
        "TRANS_002": ["buy:50", "sell:200", "buy:30"],
        "EVENT_002": ["login", "error", "logout"],
    }
    print("\nStream filtering active: High-priority data only")
    sensor_filtered: List[Any] = sensor2.filter_data(
        filter_data_map["SENSOR_002"], "critical"
    )
    trans_filtered: List[Any] = trans2.filter_data(
        filter_data_map["TRANS_002"], "large"
    )
    print(
        f"Filtered results: {len(sensor_filtered)} critical sensor alerts, "
        f"{len(trans_filtered)} large transaction"
    )

    print("\nAll streams processed successfully. Nexus throughput optimal.")
