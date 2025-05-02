# Write a function to make an hour-to-minute converter.

def hour_to_minute(hour):
    minute=hour*60
    return minute

hour=float(input("Enter the hour:"))
print(f"{hour} hour = {hour_to_minute(hour)} minutes")
    