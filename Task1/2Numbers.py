def format_example(num, char):
    return "{}{}".format(num, char)

def pond_water():
    pi = 3.14
    radius = 84
    area = pi * (radius ** 2)  # Circle Area = π r^2

    water_per_sq_meter = 1.4
    total_water = area * water_per_sq_meter  # Total water

    print(int(total_water))  # Print without decimals

def calculate_speed():
    distance = 490  # meters
    time_minutes = 7
    time_seconds = time_minutes * 60  # Convert minutes to seconds
    speed = distance / time_seconds  # Speed formula

    print(int(speed))  # Print without decimals

if __name__ == "__main__":
    result = format_example(145, 'o')
    print(result)  # Output: 145o
    
    pond_water()
    
    calculate_speed()