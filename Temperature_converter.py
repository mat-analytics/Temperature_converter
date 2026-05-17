# The program starts by asking user to type in value between 1-6. Each decision offers different option of 
# temperature conversion.

Decision = input("Type 1 to convert value from Celsius degrees to Fahrenheit degrees \n" \
"Type 2 to convert value from Fahrenheit degrees to Celsius degrees \n" \
"Type 3 to convert value from Celsius degrees to Kelwin degrees \n" \
"Type 4 to convert value from Fanhrenheit degrees to Kelwin degrees \n" \
"Type 5 to convert value from Kelwin degrees to Celsius degrees \n" \
"Type 6 to convert value from Kelwin degrees to Fahrenheit degrees \n"
)

# Below we have conversion for every decision

if Decision == "1":
    Celsius = float(input("What value would you like to convert? \n"))
    Fahrenheit = (Celsius*1.8) + 32
    print(f"{Celsius: .2f} °C = {Fahrenheit: .2f} °F")

elif Decision == "2":
    Fahrenheit = float(input("What value would you like to convert? \n"))
    Celsius = (Fahrenheit - 32)*(5/9)
    print(f"{Fahrenheit: .2f} °F = {Celsius: .2f} °C")

elif Decision == "3":
    Celsius = float(input("What value would you like to convert? \n"))
    Kelwin = Celsius + 273.15
    print(f"{Celsius: .2f} °C = {Kelwin: .2f} K")

elif Decision == "4":
    Fahrenheit = float(input("What value would you like to convert? \n"))
    Kelwin = ((Fahrenheit-32)*5/9)+273.15
    print(f"{Fahrenheit: .2f} °F = {Kelwin: .2f} K")

elif Decision == "5":
    Kelwin = float(input("What value would you like to convert? \n"))
    Celsius = Kelwin - 273.15
    print(f"{Kelwin: .2f} K = {Celsius: .2f} °C")

elif Decision == "6":
    Kelwin = float(input("What value would you like to convert? \n"))
    Fahrenheit = ((Kelwin - 273.15)*9/5)+32
    print(f"{Kelwin: .2f} K = {Fahrenheit: .2f} °F")

else:
    print("Unnknown decision. Please type decision within 1-6 range.")
