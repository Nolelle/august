# (Celsius × 9/5) + 32 = 32°F
# (Fahrenheit − 32) × 5/9 = 0°C


def celsius_to_fahrenheit(celsius):
    return celsius * (9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)


print(f"25 celsius is equal to {celsius_to_fahrenheit(25):.0f} fahrenheit")
print(f"82 fahrenheit is equal to {fahrenheit_to_celsius(82):.0f} degree celsius.")
