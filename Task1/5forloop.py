import random

def format_example():
    print("Formatted Output:", format(145, 'o'))

def pond_area():
    pi = 3.14
    r = 84
    area = int(pi * (r ** 2))  # Remove decimal
    water = int(area * 1.4)  # Remove decimal
    print("Pond Area:", area)
    print("Total Water:", water)

def calculate_speed():
    distance = 490
    time = 7 * 60  # Convert minutes to seconds
    speed = distance // time  # Remove decimal
    print("Speed:", speed)

def justice_league_operations():
    justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
    print("Original List:", justice_league)
    
    justice_league.extend(["Batgirl", "Nightwing"])
    print("After Recruitment:", justice_league)
    
    justice_league.insert(0, justice_league.pop(justice_league.index("Wonder Woman")))
    print("Wonder Woman as Leader:", justice_league)
    
    justice_league.insert(4, "Superman")
    print("Conflict Resolution:", justice_league)
    
    justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
    print("New Justice League:", justice_league)
    
    justice_league.sort()
    print("Sorted Justice League:", justice_league)

def bmi_calculator():
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kg: "))
    bmi = weight / (height ** 2)
    
    if bmi >= 30:
        category = "Obesity"
    elif bmi >= 25:
        category = "Overweight"
    elif bmi >= 18.5:
        category = "Normal"
    else:
        category = "Underweight"
    
    print("BMI Category:", category)

def city_to_country():
    country_dict = {
        "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
        "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
        "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
    }
    city = input("Enter a city name: ")
    
    for country, cities in country_dict.items():
        if city in cities:
            print(f"{city} is in {country}")
            return
    print("City not found in database.")

def same_country_check():
    country_dict = {
        "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
        "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
        "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
    }
    city1 = input("Enter first city: ")
    city2 = input("Enter second city: ")
    
    country1, country2 = None, None
    
    for country, cities in country_dict.items():
        if city1 in cities:
            country1 = country
        if city2 in cities:
            country2 = country
    
    if country1 and country2:
        if country1 == country2:
            print(f"Both cities are in {country1}")
        else:
            print("They don't belong to the same country")
    else:
        print("One or both cities not found.")

def dice_rolling_simulation():
    rolls = [random.randint(1, 6) for _ in range(20)]
    count_6 = rolls.count(6)
    count_1 = rolls.count(1)
    count_double_6 = sum(1 for i in range(len(rolls)-1) if rolls[i] == rolls[i+1] == 6)
    
    print("Dice Rolls:", rolls)
    print("Number of 6s:", count_6)
    print("Number of 1s:", count_1)
    print("Number of consecutive 6s:", count_double_6)

def workout_routine():
    total_jumping_jacks = 100
    completed = 0
    
    while completed < total_jumping_jacks:
        completed += 10
        print(f"Completed {completed} jumping jacks")
        
        tired = input("Are you tired? (yes/no): ").strip().lower()
        if tired in ["yes", "y"]:
            skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
            if skip in ["yes", "y"]:
                print(f"You completed a total of {completed} jumping jacks.")
                return
        remaining = total_jumping_jacks - completed
        if remaining > 0:
            print(f"{remaining} jumping jacks remaining.")
        else:
            print("Congratulations! You completed the workout.")
            return

# Running all functions
def main():
    format_example()
    pond_area()
    calculate_speed()
    justice_league_operations()
    # Uncomment these to enable user input functions
    # bmi_calculator()
    # city_to_country()
    # same_country_check()
    dice_rolling_simulation()
    workout_routine()

if __name__ == "__main__":
    main()