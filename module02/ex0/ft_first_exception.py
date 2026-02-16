# def check_temperature(temp_st: str) -> int:
#     try:
#         temp = int(temp_st)
#         if temp < 0:
#             raise ValueError(f"{temp}°C is too cold for plants (min 0°C)\n")
#         if temp > 0:
#             raise ValueError(f"{temp}°C is too hot for plants (max 40°C)\n")
#         return temp
#     except ValueError:
#         raise


# def test_temperature_input() -> None:
#     print("=== Garden Temperature Checker ===\n")
#     tests = ["25", "abc", "100", "-50"]
#     for value in tests:
#         print(f"Testing temperature: {value}")
#         try:
#             temp = check_temperature(value)
#             print(f"Temperatue {temp}°C is perfect for plants!")
#         except ValueError as error:
#             print(f"Error: {error}")

#     print("All tests completed - program didn't crash!")


# if __name__ == "__main__":
#     test_temperature_input()


def check_temperature(temp_str: str) -> None:
    print(f"Testing temperature: {temp_str}")
    try:
        temperature = int(temp_str)

        if temperature < 0:
            print(f"Error: {temperature}°C is too cold for plants (min 0°C)\n")
        elif temperature > 40:
            print(f"Error: {temperature}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Temperature {temperature}°C is perfect for plants!\n")

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    tests = ["25", "abc", "100", "-50"]
    for test in tests:
        check_temperature(test)
    print("All tests completed - program didn't crash!")
