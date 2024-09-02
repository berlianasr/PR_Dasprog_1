print ("BTUs Calculator")

#user input
gallons = int(input("number of gallons: "))
efficiency = int(input("efficiency: "))
efficiency = efficiency/100

barrel= gallons/42
heat = barrel*(efficiency*5800000)

print(f"by {gallons} gallons and efficiency of {efficiency}, The BTUs of heat delivered to the house are {heat}")