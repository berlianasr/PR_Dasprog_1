print ("TAXI FARE CALCULATOR")

#user input
start = float(input("enter beginning odometer reading=> ")) # float u/ angka desimal
stop = float(input("Enter ending odometer reading=> ")) 

distance = stop-start #panjang jarak yang ditempuh
rpm = 1.50 #harga per mil
fare = distance*rpm #harga akhir


print (f"You traveled a distance of {distance:.1f} miles. At ${rpm:.2f} per mile, your fare is ${fare:.2f}.")
#fungsi f-string u/ menyisipkan variabel dan ekspresi Python langsung ke dalam string dengan menggunakan tanda {}.
#x pada .xf u/ menentukan banyaknya angka desimal yang ingin ditampilkan  setelah koma; f untuk menandakan itu angka desimal.