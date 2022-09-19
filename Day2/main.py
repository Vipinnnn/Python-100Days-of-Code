print("Welcome to tip calculator")
total = float(input("What was the total bill? "))
percentage = int(input("What % would you like to give?"))
split_btn = int(input("Between how many people you want to split the bill? "))
per_person = round((total+(total*percentage/100))/split_btn, 2)

print(f"Split Between each is {per_person}")
