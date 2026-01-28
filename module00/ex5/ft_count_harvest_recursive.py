def ft_count_harvest_recursive():
    days = int(input("Days untill harvest: "))
    # print(f"Days untill harvest: {days}")

    def count_days(current_day, total_day):
        if current_day > total_day:
            print("Harvest time!")
            return
        print(f"Day {current_day}")
        count_days(current_day + 1, total_day)
    count_days(1, days)
