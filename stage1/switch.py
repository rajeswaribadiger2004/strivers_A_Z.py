def printDay(day):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    if day in days:
        print(days[day])
    else:
        print("Invalid")


# Example usage
printDay(1)   # Output: Monday
printDay(5)   # Output: Friday
printDay(9)   # Output: Invalid
