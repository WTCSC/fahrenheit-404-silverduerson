print("wlecome to Fehrenheit 404: The Temp Translator")
print("what would you like to do?")
print("1. Convery Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")

choice = input("Emter your choice (1 or 2): ")

if choice == "1":
    celsius = float(input("Enter tempature in celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print (f"\n{celsius:.1f}°C is equal to {fahrenheit:.1f}°F")
elif choice == "2":
    fahrenheit = float(input("\nEnter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"\n{fahrenheit:.1f}°F is equal to {celsius:.1f}°C")
else:
    print("\nThat is not a valid tempature silly.")

print("\nThank you for using the Temp Translator!")

