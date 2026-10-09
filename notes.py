##Question 1
hobby = str(input("Hello. What is your hobby? :"))
score = int(input("How much did you score out of 100? :"))
print("Great!","Your hobby is",hobby,",","and you also be able to score",score,"!","Congratulations.")
##Question 2
value = str(input("Enter a value:"))
value = int(input("Enter a value again:"))
print(value)
##Question 3
score = input("Enter a value:")
total = score + "10"
print(total)
##Question 4
r = int(input("Write the radius of the circle:"))
area = 3.14 * (r * r)
print("The area of the circle with radius",r,"is",area,".")
##Question 5
score = 13
score = score
print()
##Question 6
print("Hello. What is your name?")
name = str(input())
print("Hello",name,".","How are you?")
condition = str(input())
print("Good to know you are",condition,".")
print("What is your age",name,"?")
age = int(input())
print("Glad to know you are",age,"years old.")
##Question 7
Dt_1 = "Shivam Kumar"
Dt_2 = 2
Dt_3 = 3.4
Dt_4 = [1.2,3.4,5.6,1,8]

print("Dt_1 is of type",type(Dt_1))
print("Dt_2 is of type",type(Dt_2))
print("Dt_3 is of type",type(Dt_3))
print("Dt_4 is of type",type(Dt_4))

print("The Data Type is",type(Dt_4[2]))
##Question 8
Exp = [1,"Shivam"]
print(Exp)
Exp_2 = [[2,3,4],[5,6,7]]
print(Exp_2)
Exp_3 = [1,[2,3,4]]
print(Exp_3)
Exp_4 = ["Shivam",[2,3,4]]
print(Exp_4)

print(type("[1,3,3]"))

##Question 9
i = 23
f = 45.87
s = "Shivangi"
ls = [1,2,3,4,"Shivam",True]
b1 = True
b2 = False

print(i, type(i))
print(f, type(f))
print(s, type(s))
print(ls, type(ls))
print(b1, type(b1))
print(b2, type(b2))

##Data Type Conversion

dc1 = type(int(8))
dc2 = type(int(8.0))
dc3 = type(int("10"))
dc4 = type(int(True))
dc5 = type(int(False))
dc6 = type(int())


print(dc1)
print(dc2)
print(dc3)
print(dc4)
print(dc5)
print(dc6)


da1 = type(float(8))
da2 = type(float(8.0))
da3 = type(float("10"))
da4 = type(float(True))
da5 = type(float(False))
da6 = type(float())


print(da1)
print(da2)
print(da3)
print(da4)
print(da5)
print(dc6)


de1 = type(str(8))
de2 = type(str(8.2))
de3 = type(str(True))
de4 = type(str(False))
de5 = type(str([1,2]))
de6 = type(str("Shivam"))
de7 = type(str("10"))
de8 = type(str())
de9 = type(str(""))

print(de1)
print(de2)
print(de3)
print(de4)
print(de4)
print(de5)
print(de6)
print(de7)
print(de8)
print(de9)

##print(type(list(7)))
##print(type(list(3.4)))
print(type(list("Shivam")))
print(type(list("10")))
##print(type(list(True)))
##print(type(list(False)))
print(type(list("")))
print(type(list()))
print(type(list([1,2])))

print(type(bool(4)))
print(type(bool(5.4)))
print(type(bool("Shivam")))
print(type(bool("1")))
print(type(bool("")))
print(type(bool()))
print(type(bool(True)))
print(type(bool(False)))
print(type(bool([1,2])))

print(bool(4))
print(bool(5.4))
print(bool("Shivam"))
print(bool("1"))
print(bool(""))
print(bool())
print(bool(True))
print(bool(False))
print(bool([1,2]))

#Point 10

##Arithmentic Operators

#Addition = +
#Subtraction = -
#Multiplication = *
#Division = /
#Floor_Division = //
#Modulus_Operator = %
#Exponentiation_Operator = **

#Result Format = Numeric

a = 10 + 12
print(a)

b = (15 + 56 )//4
print(b)

print(a ** b )

##Relational Operators

#Greater Than = >
#Less Than = <
#Equal To = ==
#Greater Than And Equal To = >=
#Less Than And Equal To = <=
#Not Equal To = !=

#Result Format = Boolean ( True, False )

a = 5 > 4
print(a)

print(5 == 5)
print(10>= 7)
print(23<34)
print(5 != 5)
print(5 != 8)

new = int(input("Enter a Value:"))
print(new >= 4 )

##Logical Operators

#AND
#OR
#NOT

#Result Format = Boolean ( True or False )

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not(True))
print(not(False))

a = 2 ** 3
b = 3 ** 2
print(a == b, a >= b, a != b)

##Question 11
x = "Chennai"
b = 0
result = (x and b) or (b or x)
print(result)

##Question 12
print(-13 // 4)
print(-13 % 4)

   #Use this formula: Remainder =a−(b×quotient)

   ##Question 13

#Note: Comma also occupies the index number.
prac = "0,1,2,3,4,5,6,7,8,9"
a = prac[4]
b = prac[8]
c = a + b
print(c)

prac2 = "0,1,2,3,4,5,6,7,8,9"
a1 = int(prac2[4])
b2 = int(prac2[8])
print(a1 + b2)

#Solution : Remove Comma

prac = "0123456789"
a = prac[4]
b = prac[8]
c = a + b
print(c)

prac2 = "0123456789"
a1 = int(prac2[4])
b2 = int(prac2[8])
print(a1 + b2)

##Topic 14 : Applying Multiplication Operator on String Literal

name = "Shivam Kumar" #name = variable; Shivam Kumar = String_literal
print(name * 5) #To see "Shivam Kumar" 5 times
print(name[5] * 5) #To see "m" 5 times from the word "Shivam"
print(name[1:6] * 5) #To see "hivam" 5 times from the word "Shivam"
print(name[-10] * 5) #To see "i" 5 times from the word "Shivam"

##Topic 15 : Applying Negative Indexing on String Literal

name = "Shivam Kumar"
print(name[-4]) #Showing "U" from the word "Kumar"
#print(name[-5,-3]) #wrong code
print(name[1:-2]) #Showing "hivam Kum" from "Shivam Kumar"
print(name[-2:-5]) #wrong execution of code, but code is working
print(name[:-8]) #Shows "Shiv" from "Shivam Kumar"
print(name[::-4]) #Shows every 4th letter inversly from Shivam Kumar ;  Result : rKv
print(name[-2:1]) #wrong execution of code, but code is working; 1 is blocking the result to show "hivam kuma"

##Topic 17 : Comparison Operators on String Literal

print("Shivam" > "Apple") 
print("Apple" > "Age")
print("Apple" == "Apple")
print("Apple" >= "Shivam")
print("Apple" <= "Mango")
print("Apple" <= "Mango" and "Shivam" >= "Age")
print("Apple" <= "Mango" or "Shivam" >= "Age")
print(not("Apple" == "Mango" ))
print(not("Apple" < "Shivam"))

##Topic 18 : Finding Length of String Literal

name = "Shivam Kumar"
print(len(name))

s = "123456789"
print(len(s))