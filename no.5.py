
print("Infuse Rate Calculator")

#user input
volume = int(input("volume to be infused (ml): "))
minutes = int(input("minutes over which to infuse: "))
ratecount =  volume / (minutes/60)
    
print (f"VTBI: {volume} ml")
print (f"Rate: {ratecount} ml/hr")
