def m_to_km(meters):
    kilometer = meters / 1000
    return kilometer

# Taking the user input
meters = float(input("Enter the value in meters: "))

# Converting M to Km
kilometer = m_to_km(meters)

# Showing the result
print(f"{meters} meter is {kilometer} kilometers")