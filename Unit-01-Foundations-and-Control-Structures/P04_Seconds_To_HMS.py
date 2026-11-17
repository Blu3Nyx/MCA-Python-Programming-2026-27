# Unit 1 - P04: Convert seconds into hours, minutes and seconds

total_seconds = int(input("Enter time in seconds: "))

hours = total_seconds // 3600          # 1 hour = 3600 seconds
remaining = total_seconds % 3600       # seconds left after taking hours
minutes = remaining // 60              # 1 minute = 60 seconds
seconds = remaining % 60               # seconds left after taking minutes

print("\n----- Converted Time -----")
print(f"{total_seconds} seconds = {hours} hours, {minutes} minutes, {seconds} seconds")
