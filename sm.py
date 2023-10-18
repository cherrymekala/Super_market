from datetime import datetime

name=input("Enter your name: ")
l1='''

Rice    Rs 20/kg
Sugar   Rs 30/kg
Salt    Rs 20/kg
Oil     Rs 80/liter
paneer  Rs 110/kg
Maggi   Rs 50/kg
Boost   Rs 90/each
Closeup Rs 85/each

'''

price=0
price_list=[]
tot=0
final_price=0
item_list=[]
quantity_list=[]
plist=[]

items={'Rice':20,'Sugar':30,'Salt':20,'Oil':80,'Paneer':110,'Maggi':50,'Boost':90,'Closeup':85}
opt=int(input("For list of items press 1:"))
if opt==1:
	print(l1)
for i in range(len(items)):
	choice=int(input("If you want to buy press 1 or to exit please press 2:"))
	if choice==2:
		break
	if choice==1:
		item=input("Enter your items:")
		quantity=int(input("Enter your quantity:"))
		if item in items.keys():
			price=quantity*(items[item])
			price_list.append((item,quantity,items,price))
			tot+=price
			item_list.append(item)
			quantity_list.append(quantity)
			plist.append(price)
			gst=(tot*5)/100
			final_price=gst+tot
		else:
			print("Your entered item isn't available:")
	else:
		print("You have entered wrong input:")
	inp=input("Do you want to bill your items:")
	if inp=="yes":
		pass
		if final_price!=0:
			print(25*"=","Sharan Mart",25*"=")
			print(28*" ","Vijayawada")
			print("Name: ",name,30*" ","Date:",datetime.now())
			print(75*"-")
			print("Sno",8*" ","items",8*" ","Quantity",3*" ","price")
			for i in range(len(price_list)):
				print(i,8*' ',5*' ',item_list[i],3*' ',quantity_list[i],8*" " ,plist[i])
			print(75*"-")
			print(50*" ",'TotalAmount: ','Rs',tot)	
			print("gst amount",40*" ",'Rs',gst)
			print(75*"-")
			print(50*" ",'finalAmount:','Rs',final_price)
			print(75*"-")
			print(20*" ","Thanks for visiting")
			print(75*"-")
			
