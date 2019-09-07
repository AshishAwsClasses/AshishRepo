#!/usr/bin/python

Name = str(input("Welcome, Please Provide Your Name : "))
Item_1 = input ("Please Provide First Item : ")
Item_2 = input ("Please Provide Second Item : ")
Item_3 = input ("Please Provide Third Item : ")
Item_1p = int(input("Please Enter %r Price : " % (Item_1)))
Item_2p = int(input("Please Enter %r Price : " % (Item_2)))
Item_3p = int(input("Please Enter %r Price : " % (Item_3)))
Item_1q = int(input("Please Enter %r Quantity : " % (Item_1)))
Item_2q = int(input("Please Enter %r Quantity : " % (Item_2)))
Item_3q = int(input("Please Enter %r Quantity : " % (Item_3)))

print ("\n")

print ("Welcome To Hotel EATBUDS")

print ("\n")

print ("******Please Provide Your Order******")

print ("\n")

print ("1. %s ------> Q. %s " % (Item_1, Item_1q))
print ("2. %s ------> Q. %s " % (Item_2, Item_2q))
print ("3. %s ------> Q. %s " % (Item_3, Item_3q))


print ("\n")

print ("*****TOTAL AMOUNT******")

print ("\n")

Item1_tp = Item_1p * Item_1q
Item2_tp = Item_2p * Item_2q
Item3_tp = Item_3p * Item_3q
Total = Item1_tp + Item2_tp + Item3_tp


print ("Hello %s Your Total is : %s " % (Name, Total))

print ("\n")

print ("Thank You %s Visit Again" % (Name))



