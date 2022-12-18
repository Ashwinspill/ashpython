x=int(input("enter starting yr :"))
y=int(input("entr the end yr:"))
print("these are the leap yr.")
for i in range(x,y+1):
   if((i%400==0) or (i%100!=0) and (i%4==0)):
    print(i)