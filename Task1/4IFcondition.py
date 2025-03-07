def calculate_bmi():
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))
    bmi = weight / (height ** 2)
    
    if bmi >= 30:
        print("Obesity")
    elif 25 <= bmi < 30:
        print("Overweight")
    elif 18.5 <= bmi < 25:
        print("Normal")
    else:
        print("Underweight")

def find_country():
    city_to_country = {
        "Sydney": "Australia", "Melbourne": "Australia", "Brisbane": "Australia", "Perth": "Australia",
        "Dubai": "UAE", "Abu Dhabi": "UAE", "Sharjah": "UAE", "Ajman": "UAE",
        "Mumbai": "India", "Bangalore": "India", "Chennai": "India", "Delhi": "India"
    }
    city = input("Enter a city name: ")
    country = city_to_country.get(city, "Unknown")
    if country != "Unknown":
        print(f"{city} is in {country}")
    else:
        print("City not found in the database.")

def check_same_country():
    city_to_country = {
        "Sydney": "Australia", "Melbourne": "Australia", "Brisbane": "Australia", "Perth": "Australia",
        "Dubai": "UAE", "Abu Dhabi": "UAE", "Sharjah": "UAE", "Ajman": "UAE",
        "Mumbai": "India", "Bangalore": "India", "Chennai": "India", "Delhi": "India"
    }
    city1 = input("Enter the first city: ")
    city2 = input("Enter the second city: ")
    
    country1 = city_to_country.get(city1, "Unknown")
    country2 = city_to_country.get(city2, "Unknown")
    
    if country1 == "Unknown" or country2 == "Unknown":
        print("One or both cities are not in the database.")
    elif country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")

# Run the functions
def main():
    print("1. Calculate BMI")
    calculate_bmi()
    print("\n2. Find Country of a City")
    find_country()
    print("\n3. Check if Two Cities Belong to the Same Country")
    check_same_country()

if __name__ == "__main__":
    main()
