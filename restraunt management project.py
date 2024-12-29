order=[]
cost=[]
TotalCost=0
print("\t\t\tWELCOME TO HERBIVORIA ")

print("WE ARE DELIGHTED TO HAVE YOU"\
      "WE HOPE YOU WILL HAVE A GREAT VISIT HERE")
print("THE MENU LIST IS DISPLAYED BELOW-:")
f=open("MENU.TXT","w")
list1=["STARTERS-:\t\t","PRICE\n",
       "s1.veg spring roll\t","250\n",
       "s2.crispy corn\t\t","200\n",
       "s3.veg hakka noodles\t","180\n",
       "s4.schezwan fried rice\t","200\n",
       "s5.manchurian\t\t","150\n",
       "s6.paneer chilli\t","250\n",
       "s7.chinese bhel\t\t","230\n",
       "s8.paneer 65\t\t","190\n",
       "s9.paneer manchurian\t","260\n",
       "s10.baby corn fry\t","200\n"]
f.writelines(list1)
list2=["BREAKFAST AND SNACKS-:\t","PRICE\n",
       "b1.chole bhature\t","100\n",
       "b2.papdi chaat\t\t","90\n",
       "b3.samosa chaat\t\t","80\n",
       "b4.veg sandwich\t\t",
       "120\n","b5.pani puri\t\t",
       "60\n","b6.samosa\t\t","50\n",
       "b7.veg roll\t\t","100\n",
       "b8.paneer roll\t\t","120\n",
       "b9.litti choka\t\t","60\n",
       "b10.dahi vada\t\t","90\n"]
f.writelines(list2)
list3=["SOUTH INDIAN-:\t\t","PRICE\n",
       "i1.plain dosa\t\t","120\n",
       "i2.masala dosa\t\t","150\n",
       "i3.idli sambhar\t\t","100\n",
       "i4.sambhar vada\t\t","120\n",
       "i5.uttapam\t\t","100\n"]
f.writelines(list3)
list4=["MAIN COURSE-:\t\t","PRICE\n",
       "m1.butter naan\t\t","12\n",
       "m2.garlic naan\t\t","20\n",
       "m3.stuffed kulcha\t","25\n",
       "m4.tandoori roti\t","15\n",
       "m5.aloo do pyaaza\t","200\n",
       "m6.kadhai paneer\t","190\n",
       "m7.paneerbuttermasala\t","200\n",
       "m8.daal makhani\t\t","180\n",
       "m9.yellow daal\t\t","200\n",
       "m10.jeera rice\t\t","160\n",
       "m11.fried rice\t\t","180\n",
       "m12.curry chawal\t","150\n",
       "m13.aloo jeera\t\t","180\n"]
f.writelines(list4)
list5=["SIDES-:\t\t\t","PRICE\n",
       "sd1.papad\t\t","15\n",
       "sd2.salad\t\t","50\n",
       "sd3.mineralwater\t","30\n"]
f.writelines(list5)
list6=["SOUPS-:\t\t\t","PRICE\n",
       "so1.manchow soup\t","150\n",
       "so2.hot&sour soup\t","150\n",
       "so3.sweetcorn soup\t","150\n",
       "so4.tomato soup\t\t","150\n"]
f.writelines(list6)
list7=["DESERTS&BEVERAGES\t:","PRICE\n",
       "d1.cold coffee\t\t","120\n",
       "d2.hot chocolate\t","100\n",
       "d3.lassi\t\t","50\n",
       "d4.masala coke\t\t","60\n",
       "d5.BrownieWithIceCream\t","150\n",
       "d6.lemon ice tea\t","100\n",
       "d7.peach ice tea\t","140\n"]
f.writelines(list7)
f.close()
w=open("MENU.txt","r")
string=w.read()
print(string)
w.close()
print("NOW SELECT YOUR CHOICES-:")
S_check=input("ENTER YES IF YOU WANT TO"\
              "ORDER SOMETHING FROM STARTERS")
if S_check=="YES" or S_check=="yes":
    print('''INSTRUCTIONS TO ENTER YOUR CHOICES:
1)ENTER THE CODE PROVIDED BEFORE
YOUR DESIRED FOOD ITEM
LIKE s1,s2...SO ON.
2)ENTER 0 ONCE YOU ARE DONE ORDERING
FROM STARTERS CORNER''')
    while True:
        chS=input("ENTER THE CODE")
        if chS=="s1" or chS=="S1":
            order.append("VEG SPRING ROLL")
            Q=int(input("enter the quantity"))
            c=250*Q
            cost.append(c)
        elif chS=="s2" or chS=="S2":
            order.append("CRISPY CORN")
            Q=int(input("enter the quantity"))
            c=200*Q
            cost.append(c)
        elif chS=="s3" or chS=="S3":
            order.append("  VEG HAKKA NOODLES")
            Q=int(input("enter the quantity"))
            c=180*Q
            cost.append(c)
        elif chS=="s4" or chS=="S4":
            order.append("SCHEZWAN FRIED RICE")
            Q=int(input("enter the quantity"))
            c=200*Q
            cost.append(c)
        elif chS=="s5" or chS=="S5":
            order.append("MANCHURIAN")
            Q=int(input("enter the quantity"))
            c=150*Q
            cost.append(c)
        elif chS=="s6" or chS=="S6":
            order.append("PANEER CHILLI")
            Q=int(input("enter the quantity"))
            c=190*Q
            cost.append(c)
        elif chS=="s7" or chS=="S7":
            order.append("CHINESE BHEL")
            Q=int(input("enter the quantity"))
            c=230*Q
            cost.append(c)
        elif chS=="s8" or chS=="S8":
            order.append("PANEER 65")
            Q=int(input("enter the quantity"))
            c=190*Q
            cost.append(c)
        elif chS=="s9" or chS=="S9":
            order.append("PANEER MANCHURIAN")
            Q=int(input("enter the quantity"))
            c=260*Q
            cost.append(c)
        elif chS=="s10" or chS=="S10":
            order.append("BABY CORN FRY")
            Q=int(input("enter the quantity"))
            c=200*Q
            cost.append(c)
        elif chS=="0":
            break;
        else:
            print("ENTER ACCORDING TO THE INSTRUCTIONS")
print("MOVING ON TO THE BREAKFAST OR SNACKS SECTION:")
B_check=input('''ENTER YES IF YOU WANT TO
ORDER FROM THIS SECTION''')
if B_check=="YES" or B_check=="yes":
    print('''INSTRUCTIONS TO ENTER YOUR CHOICES:
1)ENTER THE CODE PROVIDED BEFORE
YOUR DESIRED FOOD ITEM
LIKE b1,b2...SO ON.
2)ENTER 0 ONCE YOU ARE DONE ORDERING FROM
BREAKFAST AND SNACKS CORNER''')
    while True:
        chB=input("enter the code")
        if chB=="b1" or chB=="B1":
            order.append("CHOLE BHATURE")
            Q=int(input("ENTER THE QUANTITY"))
            c=100*Q
            cost.append(c)
        elif chB=="b2" or chB=="B2":
            order.append("PAPDI CHAAT")
            Q=int(input("ENTER THE QUANTITY"))
            c=90*Q
            cost.append(c)
        elif chB=="b3" or chB=="B3":
            order.appendd("SAMOSA CHAAT")
            Q=int(input("ENTER THE QUANTITY"))
            c=80*Q
            cost.append(c)
        elif chB=="b4" or chB=="B4":
            order.append("VEG SANDWICH")
            Q=int(input("ENTER THE QUANTITY"))
            c=120*Q
            cost.append(c)
        elif chB=="b5" or chB=="B5":
            order.append("PANI PURI")
            Q=int(input("ENTER THE QUANTITY"))
            c=60*Q
            cost.append(c)
        elif chB=="b6" or chB=="B6":
            order.append("SAMOSA")
            Q=int(input("ENTER THE QUANTITY"))
            c=50*Q
            cost.append(c)
        elif chB=="b7" or chB=="B7":
            order.append("VEG ROLL")
            Q=int(input("ENTER THE QUANTITY"))
            c=100*Q
            cost.append(c)
        elif chB=="b8" or chB=="B8":
            order.append("PANEER ROLL")
            Q=int(input("ENTER THE QUANTITY"))
            c=120*Q
            cost.append(c)
        elif chB=="b9" or chB=="B9":
            order.append("LITTI CHOKA")
            Q=int(input("ENTER THE QUANTITY"))
            c=60*Q
            cost.append(c)
        elif chB=="b10" or chB=="B10":
            order.append("DAHI VADA")
            Q=int(input("ENTER THE QUANTITY"))
            c=90*Q
            cost.append(c)
        elif chB=="0":
            break;
        else:
            print("enter according to instructions")
print("MOVING ON TO THE SOUTH INDIAN SECTION:")
I_check=input('''ENTER YES IF YOU WANT TO ORDER
FROM THIS SECTION''')
if I_check=="YES" or I_check=="yes":
    print('''INSTRUCTIONS TO ENTER YOUR CHOICES:
1)ENTER THE CODE PROVIDED BEFORE
YOUR DESIRED FOOD ITEM
LIKE i1,i2...SO ON.
2)ENTER 0 ONCE YOU ARE DONE ORDERING FROM
SOUTH INDIAN CORNER''')
    while True:
        chI=input("enter the code")
        if chI=="i1" or chI=="I1":
            order.append("PLAIN DOSA")
            Q=int(input("enter the quantity"))
            c=120*Q
            cost.append(c)
        elif chI=="i2" or chI=="I2":
            order.append("MASALA DOSA")
            Q=int(input("enter the quantity"))
            c=150*Q
            cost.append(c)
        elif chI=="i3" or chI=="I3":
            order.append("IDLI SAMBHAR")
            Q=int(input("enter the quantity"))
            c=100*Q
            cost.append(c)
        elif chI=="i4" or chI=="I4":
            order.append("SAMBHAR VADA")
            Q=int(input("enter the quantity"))
            c=120*Q
            cost.append(c)
        elif chI=="i5" or chI=="I5":
            order.append("UTTAPAM")
            Q=int(input("enter the quantity"))
            c=100*Q
            cost.append(c)
        elif chI=="0":
            break;
        else:
            print("enter according to the instructions")
print("MOVING ON TO THE MAIN COURSE SECTION:")
M_check=input('''ENTER YES IF YOU WANT TO ORDER
FROM THIS SECTION''')
if M_check=="YES" or M_check=="yes":
    print('''INSTRUCTIONS TO ENTER YOUR CHOICES:
1)ENTER THE CODE PROVIDED BEFORE
YOUR DESIRED FOOD ITEM
LIKE m1,m2...SO ON.
2)ENTER 0 ONCE YOU ARE DONE ORDERING FROM
MAIN COURSE CORNER''')
    while True:
        chM=input("enter the code")
        if chM=="m1" or chM=="M1":
            order.append("BUTTER NAAN")
            Q=int(input("enter the quantity"))
            c=12*Q
            cost.append(c)
        elif chM=="m2" or chM=="M2":
            order.append("GARLIC NAAN")
            Q=int(input("enter the quantity"))
            c=20*Q
            cost.append(c)
        elif chM=="m3" or chM=="M3":
            order.append("STUFFED KULCHA")
            Q=int(input("enter the quantity"))
            c=15*Q
            cost.append(c)
        elif chM=="m4" or chM=="M4":
            order.append("TANDOORI ROTI")
            Q=int(input("enter the quantity"))
            c=15*Q
            cost.append(c)
        elif chM=="m5" or chM=="M5":
            order.append("ALOO DO PYAAZA")
            Q=int(input("enter the quantity"))
            c=2-0*Q
            cost.append(c)
        elif chM=="m6" or chM=="M6":
            order.append("KADHAI PANEER")
            Q=int(input("enter the quantity"))
            c=190*Q
            cost.append(c)
        elif chM=="m7" or chM=="M7":
            order.append("PANEER BUTTER MASALA")
            Q=int(input("enter the quantity"))
            c=200*Q
            cost.append(c)
        elif chM=="m8" or chM=="M8":
            order.append("DAAL MAKHANI")
            Q=int(input("enter the quantity"))
            c=180*Q
            cost.append(c)
        elif chM=="m9" or chM=="M9":
            order.append("YELLOW DAAL")
            Q=int(input("enter the quantity"))
            c=200*Q
            cost.append(c)
        elif chM=="m10" or chM=="M10":
            order.append("JEERA RICE")
            Q=int(input("enter the quantity"))
            c=160*Q
            cost.append(c)
        elif chM=="m11" or chM=="M11":
            order.append("FRIED RICE")
            Q=int(input("enter the quantity"))
            c=180*Q
            cost.append(c)
        elif chM=="m12" or chM=="M12":
            order.append("CURRY CHAWAL")
            Q=int(input("enter the quantity"))
            c=150*Q
            cost.append(c)
        elif chM=="m13" or chM=="M13":
            order.append("ALOO JEERA")
            Q=int(input("enter the quantity"))
            c=180*Q
            cost.append(c)
        elif chM=="0":
            break;
        else:
            print("enter according to the instructions")
print("MOVING ON TO THE SIDES SECTION:")
sd_check=input('''ENTER YES IF YOU WANT TO ORDER
FROM THIS SECTION''')
if sd_check=="YES" or sd_check=="yes":
    print('''INSTRUCTIONS TO ENTER YOUR CHOICES:
1)ENTER THE CODE PROVIDED BEFORE
YOUR DESIRED FOOD ITEM
LIKE sd1,sd2...SO ON.
2)ENTER 0 ONCE YOU ARE DONE ORDERING
FROM SIDES CORNER''')
    while True:
        chsd=input("enter the code")
        if chsd=="sd1" or chsd=="sd1":
            order.append("PAPAD")
            Q=int(input("enter the quantity"))
            c=15*Q
            cost.append(c)
        elif chsd=="sd2" or chsd=="sd2":
            order.append("SALAD")
            Q=int(input("enter the quantity"))
            c=50*Q
            cost.append(c)
        elif chsd=="sd3" or chsd=="sd3":
            order.append("MINERAL WATER")
            Q=int(input("enter the quantity"))
            c=30*Q
            cost.append(c)
        elif chsd=="0":
            break;
        else:
            print("enter according to the instructions")
print("MOVING ON TO THE SOUP SECTION:")
SO_check=input('''ENTER YES IF YOU WANT TO ORDER
FROM THIS SECTION''')
if SO_check=="YES" or SO_check=="yes":
    print('''INSTRUCTIONS TO ENTER YOUR CHOICES:
1)ENTER THE CODE PROVIDED BEFORE
YOUR DESIRED FOOD ITEM
LIKE so1,so2...SO ON.
2)ENTER 0 ONCE YOU ARE DONE ORDERING
FROM SOUP CORNER''')
    while True:
        chso=input("enter the code")
        if chso=="so1" or chso=="so1":
            order.append("MANCHOW SOUP")
            Q=int(input("enter the quantity"))
            c=150*Q
            cost.append(c)
        elif chso=="so2" or chso=="so2":
            order.append("HOT&SOUR SOUP")
            Q=int(input("enter the quantity"))
            c=150*Q
            cost.append(c)
        elif chso=="so3" or chso=="so3":
            order.append("SWEET CORN SOUP")
            Q=int(input("enter the quantity"))
            c=150*Q
            cost.append(c)
        elif chso=="so4" or chso=="SO4":
            order.append("TOMATO SOUP")
            Q=int(input("enter the quantity"))
            c=150*Q
            cost.append(c)
        elif chso=="0":
            break;
        else:
            print("enter according to the instructions")
print("MOVING ON TO THE DESERT&BEVERAGES SECTION:")
D_check=input('''ENTER YES IF YOU WANT TO ORDER
FROM THIS SECTION''')
if D_check=="YES" or D_check=="yes":
    print('''INSTRUCTIONS TO ENTER YOUR CHOICES:
1)ENTER THE CODE PROVIDED BEFORE
YOUR DESIRED FOOD ITEM
LIKE d1,d2...SO ON.
2)ENTER 0 ONCE YOU ARE DONE ORDERING
FROM THISCORNER''')
    while True:
        chd=input("enter the code")
        if chd=="d1" or chd=="D1":
            order.append("COLD COFFEE")
            Q=int(input("enter the quantity"))
            c=120*Q
            cost.append(c)
        elif chd=="d2" or chd=="D2":
            order.append("HOT CHOCOLATE")
            Q=int(input("enter the quantity"))
            c=100*Q
            cost.append(c)
        elif chd=="d3" or chd=="D3":
            order.append("LASSI")
            Q=int(input("enter the quantity"))
            c=50*Q
            cost.append(c)
        elif chd=="d4" or chd=="D4":
            order.append("MASALA COKE")
            Q=int(input("enter the quantity"))
            c=60*Q
            cost.append(c)
        elif chd=="d5" or chd=="D5":
            order.append("BROWNIE WITH ICE CREAM")
            Q=int(input("enter the quantity"))
            c=150*Q
            cost.append(c)
        elif chd=="d6" or chd=="D6":
            order.append("LEMON ICE TEA")
            Q=int(input("enter the quantity"))
            c=100*Q
            cost.append(c)
        elif chd=="d7" or chd=="D7":
            order.append("PEACH ICE TEA")
            Q=int(input("enter the quantity"))
            c=140*Q
            cost.append(c)
        elif chd=="0":
            break;
        else:
            print("enter according to instructions")
print('''*******************************************
****************************************************''')
for i in cost:
    TotalCost+=i
        

print('''YOU WOULD LIKE
1.DINING
2.DELIVERY
3.RESERVATION ''')
n=int(input('enter your preference from 1,2,3'))
if n==1:
    print('''PLEASE BE SEATED WHILE YOUR
FOOD IS BEING PREPARED''')
elif n==2:
    ADD=input('ENTER YOUR ADDRESS')
    print('DELIVERY CHARGES WILL BE RUPEES 50')
    TotalCost+=50
    
    print('Thank you for ordering')
    print('''Your food is being prepared
and will be delivered soon''')
elif n==3:
    print('''number of total
          seatings available is 50''')
    while True:
        seat=int(input('''ENTER NUMBER OF
SEATS TO BE BOOKED'''))
        remain= 50-seat
        break
    print('remaining seatings available are ',remain) 
    occ=input('ENTER THE OCCASION')
    date=input('ENTER THE DATE DD/MM/YYYY')
    time=input('ENTER THE TIME')
    print('Your table for',seat)
    print("people is booked for",date,'at',time)
    print('''Extra charges for reservation
would be rupees 500''')
    TotalCost+=500
    
    
    
else:
    print("enter the correct option")


print("THE FINAL DETAILS OF YOUR ORDER ARE:")
print("ITEMS ADDED ARE:")
for m in order:
    print(m)
print("RESPECTIVE COSTS OF THE ITEMS ADDED")
for c in cost:
    print(c)
print("GST APPLIED:18%")
bill=TotalCost+(18/100)*TotalCost
print("THE FINAL AMOUNT IS",bill)
print('''ENTER YOUR PAYMENT OPTION:
1.Cash
2.UPI
3.Credit/Debit card''')
Po=int(input("enter your choice from 1-3"))
if Po==1:
    print('''YOUR ORDER WILL SOON BE PREPARED!!
THANKS FOR ORDERING!!''')
elif Po==2:
    print('''YOUR ORDER WILL SOON BE PREPARED!!
THANKS FOR ORDERING!!''')
elif Po==3:
    acc=int(input("enter your acc no"))
    cvv=int(input("enter your cvv"))
    exp=input("enter your expiry in the form of MM/YY")
    print('''YOUR ORDER WILL SOON BE PREPARED!!
THANKS FOR ORDERING!!''')
