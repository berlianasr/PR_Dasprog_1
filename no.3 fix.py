
print("Estimation of the temperature in a freezer")
print("How long it has been since the power failure? ")

#user input
hours1 = int(input("Input the number of hours: "))
minutes = int (input("Input the number of minutes: "))

hours = hours1 + minutes/60
temperature = 4*hours**2 / (hours+2) - 20

print (f"It's been {hours} hours since the power failure. The temperature estimation in the freezer is {temperature:.2f} °C")