print("How many miles did you run today ?")
miles = input()
kilometers = float(miles) * 1.60934
kilometers = round(kilometers,2)
print(f"You've run {miles} miles or {kilometers} kilometers")
