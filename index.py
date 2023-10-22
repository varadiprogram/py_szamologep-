import time

#opciók
print("Számológép \n"
      "\n"
      "+(1) \n"
      "-(2) \n"
      "*(3) \n"
      "/(4) \n"
      "%(5) \n")

#opció választó
menu_pont_valszto = int(input("Válasszon(1-5): "))
#szűnet
time.sleep(0.2)
#sor kihagyas
print("")
#első és második szám megadása

szam1 = int(input("első szám: "))
szam2 = int(input("második szám: "))
#sor kihagyas
print("")
#összeadás
if menu_pont_valszto == 1:
      vegeredmeny = szam1 + szam2
      print(szam1, "+" ,szam2, "=" ,vegeredmeny)

#kivonás  
elif menu_pont_valszto == 2:
      vegeredmeny = szam1 - szam2
      print(szam1, "-" ,szam2, "=" ,vegeredmeny)      

#szorzás
elif menu_pont_valszto == 3:
      vegeredmeny = szam1 * szam2
      print(szam1, "*" ,szam2, "=" ,vegeredmeny)

#osztás
elif menu_pont_valszto == 4:
      if(szam2 == 0):
            print("Nullával nem lehet osztani")
      else:
            vegeredmeny = szam1 / szam2
            print(szam1, "/" ,szam2, "=" ,vegeredmeny)      

#maradékos osztás
elif menu_pont_valszto == 5:
      if(szam2 == 0):
            print("Nullával nem lehet osztani")
      else:
            vegeredmeny = szam1 % szam2
            print(szam1, "%" ,szam2, "=" ,vegeredmeny)      

#hiba estén
else:
      print("Valamit elgépelt vagy rosszul adott meg.")

#szűnet
time.sleep(1.2)
#sor kihagyas      
print("")
#kilépés
print("By: Váradi Zsolt")
input("nyomj egy Entert a kilépéshez")



      