import tkinter as tk
from tkinter import messagebox
def sema():

   satır1 = satır.get()
   satır2 = satırr.get()
   satır3 = satırrr.get()
   satır4 = satırrrr.get()

   if list(satır1[-1]) == list(satır2[-1]) == list(satır3[-1]) == list(satır4[-1]):
       sonuc1['text'] = "a"
       sonuc2['text'] = "a"
       sonuc3['text'] = "a"
       sonuc4['text'] = "a"
       kafiyetipi['text'] = "Düz Kafiye"
   else:
       sonuc1['text'] = "a"
       sonuc2['text'] = "b"
       sonuc3['text'] = "c"
       sonuc4['text'] = "d"
   if list(satır1[-1]) == list(satır2[-1]) == list(satır4[-1]) != list(satır3[-1]):
       sonuc1['text'] = "a"
       sonuc2['text'] = "a"
       sonuc3['text'] = "b"
       sonuc4['text'] = "a"
       kafiyetipi['text'] = "Mani tipi"
   if list(satır1[-1]) == list(satır3[-1]) != list(satır2[-1]) == list(satır4[-1]):
       sonuc1['text'] = "a"
       sonuc2['text'] = "b"
       sonuc3['text'] = "a"
       sonuc4['text'] = "b"
       kafiyetipi['text'] = "Çapraz Kafiye"
   if list(satır1[-1]) == list(satır2[-1]) != list(satır3[-1]) == list(satır4[-1]) :
       sonuc1['text'] = "a"
       sonuc2['text'] = "a"
       sonuc3['text'] = "b"
       sonuc4['text'] = "b"
       kafiyetipi['text'] = " "
   if list(satır1[-1]) == list(satır4[-1]) != list(satır2[-1]) == list(satır3[-1]):
       sonuc1['text'] = "a"
       sonuc2['text'] = "b"
       sonuc3['text'] = "b"
       sonuc4['text'] = "a"
       kafiyetipi['text'] = "Sarmal Kafiye "
   if list(satır1[-1]) == list(satır3[-1]) == list(satır4[-1]) != list(satır2[-1]) and list(satır1[-1]) != list(satır2[-1]) and list(satır1[-1]) != list(satır4[-1]):
       sonuc1['text'] = "a"
       sonuc2['text'] = "b"
       sonuc3['text'] = "a"
       sonuc4['text'] = "a"
       kafiyetipi['text'] = " "
   if list(satır1[-1]) != list(satır2[-1]) != list(satır3[-1]) == list(satır4[-1]):
       sonuc1['text'] = "a"
       sonuc2['text'] = "b"
       sonuc3['text'] = "c"
       sonuc4['text'] = "c"
       kafiyetipi['text'] = " "
   if list(satır2[-1]) == list(satır3[-1]) == list(satır4[-1]) != list(satır1[-1]) and list(satır2[-1]) == list(satır4[-1]):
       sonuc1['text'] = "a"
       sonuc2['text'] = "b"
       sonuc3['text'] = "b"
       sonuc4['text'] = "b"
       kafiyetipi['text'] = " "
   if list(satır1[-1]) == list(satır2[-1]) != list(satır3[-1]) != list(satır4[-1]) and list(satır1[-1]) != list(satır4[-1]):
       sonuc1['text'] = "a"
       sonuc2['text'] = "a"
       sonuc3['text'] = "b"
       sonuc4['text'] = "c"
       kafiyetipi['text'] = " "
   if  list(satır1[-1]) == list(satır4[-1]) != list(satır2[-1]) != list(satır3[-1]):
       sonuc1['text'] = "a"
       sonuc2['text'] = "b"
       sonuc3['text'] = "c"
       sonuc4['text'] = "a"
       kafiyetipi['text'] = " "
   if  list(satır1[-1]) == list(satır3[-1]) != list(satır2[-1]) != list(satır4[-1]):
       sonuc1['text'] = "a"
       sonuc2['text'] = "b"
       sonuc3['text'] = "a"
       sonuc4['text'] = "c"
       kafiyetipi['text'] = " "
   if  list(satır2[-1]) == list(satır4[-1]) != list(satır1[-1]) != list(satır3[-1]):
       sonuc1['text'] = "a"
       sonuc2['text'] = "b"
       sonuc3['text'] = "c"
       sonuc4['text'] = "b"
       kafiyetipi['text'] = " "
   if  list(satır2[-1]) == list(satır3[-1]) != list(satır1[-1]) != list(satır4[-1]):
       sonuc1['text'] = "a"
       sonuc2['text'] = "b"
       sonuc3['text'] = "b"
       sonuc4['text'] = "c"




pencere = tk.Tk()
pencere.title("Kafiye şema")
pencere.geometry("400x200")
satır = tk.Entry(width=50)
satır.place(x=50,y=10)

satırr = tk.Entry(width=50)
satırr.place(x=50,y=40)

satırrr = tk.Entry(width=50)
satırrr.place(x=50,y=70)

satırrrr = tk.Entry(width=50)
satırrrr.place(x=50,y=100)


sonuc1 = tk.Label(text= ":", bg="red")
sonuc1.place(x=380, y=10)

sonuc2 = tk.Label(text= ":", bg="green")
sonuc2.place(x=380, y=40)

sonuc3 = tk.Label(text= ":", bg="blue")
sonuc3.place(x=380, y=70)

sonuc4 = tk.Label(text= ":", bg="purple")
sonuc4.place(x=380, y=100)

kafiyetipi = tk.Label(text="Kafiye Tipi:", bg="gray",font="Verdana 18 bold")
kafiyetipi.place(x=150, y=140)


bsonuc = tk.Button(text="Bul", font="Verdana 18 bold", command=sema).place(x=50, y=130)

pencere.mainloop()