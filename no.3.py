print("Estimation of the temperature in a freezer")
print("How long it has been since the power failure? ")

#def untuk mendefinisikan sebuah fungsi. Fungsi adalah blok kode yang dapat digunakan kembali untuk melakukan tugas tertentu.
#Kode di bawah baris def merupakan tubuh dari fungsi hitung_suhu. Kode ini akan dijalankan setiap kali fungsi dipanggil.
"""Di dalam tubuh fungsi, waktu dalam jam dikonversi menjadi angka desimal, suhu dihitung menggunakan rumus yang diberikan
dan hasilnya dikembalikan dengan menggunakan pernyataan return."""

def tempcounter (hours, minutes):
    hours = hours + minutes/60

    temperature = 4*hours**2 / (hours+2) - 20
    return temperature


#user input
hours = int(input("Input the number of hours: "))
minutes = int (input("Input the number of minutes: "))

temperature = tempcounter(hours,minutes) #fungsi dipanggil untuk mengisi temperature
print (f"It's been {hours} hours and {minutes} minutes since the power failure. The temperature estimation in the freezer is {temperature:.2f} °C")