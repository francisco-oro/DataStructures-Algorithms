days = int(input("How many day's temperature? "))
daily_temps = [0] * days
for i in range(days):
    daily_temps[i] = int(input(f"Day {i+1}'s high temp: "))

average = sum(daily_temps) / days
count = 0 
for temp in daily_temps:
    if temp > average:
        count += 1
        
print(f"\nAverage = {average}")
print(f"{count} day(s) above average")