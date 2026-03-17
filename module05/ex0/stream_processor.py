from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    """Abstract base class defining the common processing interface."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string (default implementation)."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor specialized for numeric data (lists of numbers)."""

    def process(self, data: Any) -> str:
        """Process numeric data: compute count, sum, and average."""
        try:
            if not self.validate(data):
                return "Error: Invalid numeric data"
            total: float = sum(data)
            count: int = len(data)
            avg: float = total / count
            return f"Processed {count} numeric values, sum={total}, avg={avg}"
        except Exception as e:
            return f"Error processing numeric data: {e}"

    def validate(self, data: Any) -> bool:
        """Validate that data is a non-empty list of numbers."""
        try:
            if not data or not (
                type(data) is list
            ):
                return False
            for item in data:
                if not (
                    type(item) is int or type(item) is float
                ):
                    return False
            return True
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        """Format output with numeric processor prefix."""
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    """Processor specialized for text data (strings)."""

    def process(self, data: Any) -> str:
        """Process text data: compute character and word counts."""
        try:
            if not self.validate(data):
                return "Error: Invalid text data"
            char_count: int = len(data)
            word_count: int = len(data.split())
            return (
                f"Processed text: {char_count} characters, {word_count} words"
            )
        except Exception as e:
            return f"Error processing text data: {e}"

    def validate(self, data: Any) -> bool:
        """Validate that data is a non-empty string."""
        try:
            return type(data) is str and len(data) > 0
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        """Format output with text processor prefix."""
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    """Processor specialized for log entry data."""

    def process(self, data: Any) -> str:
        """Process log data: detect log level and extract message."""
        try:
            if not self.validate(data):
                return "Error: Invalid log data"
            log_str: str = str(data)
            level: str = "UNKNOWN"
            message: str = log_str
            if ":" in log_str:
                parts: List[str] = log_str.split(":", 1)
                level = parts[0].strip()
                message = parts[1].strip()
            return f"[ALERT] {level} level detected: {message}"
        except Exception as e:
            return f"Error processing log data: {e}"

    def validate(self, data: Any) -> bool:
        """Validate that data is a non-empty string (log entry)."""
        try:
            return type(data) is str and len(data) > 0
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        """Format output with log processor prefix."""
        return f"Output: {result}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    numeric: DataProcessor = NumericProcessor()
    num_data: List[int] = [1, 2, 3, 4, 5]
    print(f'Processing data: "{num_data}"')
    print(
        f"Validation: "
        f"{(
            'Numeric data verified'
            if numeric.validate(num_data)
            else 'Invalid'
        )}")
    print(numeric.format_output(numeric.process(num_data)))

    print("\nInitializing Text Processor...")
    text: DataProcessor = TextProcessor()
    text_data: str = "Hello Nexus World"
    print(f'Processing data: "{text_data}"')
    print(
        f"Validation: "
        f"{('Text data verified'
            if text.validate(text_data)
            else 'Invalid')}"
    )
    print(text.format_output(text.process(text_data)))

    print("\nInitializing Log Processor...")
    log: DataProcessor = LogProcessor()
    log_data: str = "ERROR: Connection timeout"
    print(f'Processing data: "{log_data}"')
    print(
        f"Validation: "
        f"{'Log entry verified' if log.validate(log_data) else 'Invalid'}"
    )
    print(log.format_output(log.process(log_data)))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]
    test_data: List[Any] = [
        [1, 2, 3],
        "Nexus Online",
        "INFO: System ready",
    ]

    for i, (proc, data) in enumerate(zip(processors, test_data)):
        result: str = proc.process(data)
        print(f"Result {i + 1}: {result}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")
