import math

# gravity (Earth)
g = 9.80665
# molar mass of air (Earth)
M = 0.0289644
# Universal gas constant
R = 8.31432
# Pressure at sea level
p0 = 1
# Altitude at sea level
h0 = 0

#Placeholder value
h = "0"


def calculatePressure(g, M, R, p0, h0, h, T):
    return (p0 * math.e)**(-g * M * (h - h0)/(R * T))


print("Enter a value or press enter to exit the program.")


while h.isnumeric():
    # Altitude entered by user
    h = input("Altitude: ")
    if h.isnumeric() is False:
        break
    # Temperature entered by user in celsius and converted to Kelvin
    T = float(input("Temperature: ")) + 273.15
    print(calculatePressure(g, M, R, p0, h0, float(h), T))