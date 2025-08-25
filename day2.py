#Task 1

# mark=[10,20,30,40,50,60]
# result=[]
# for i in range(len(mark)-1,-1,-1):
#     result.append(mark[i])
# print(result)

#Task 2

# num=[1,2,3,4,5,6,7]
# num2=0
# for i in num:
#     num2 += i
# print(num2)

#Task 3
# num=[1,2,3,4,5,5,56,6,6,7,8,9]
# result=[]
# for i in num:
#     if i not in result:
#         result.append(i)
# print(result)

#TAsk 4

# val=(1,2,3,4,5,6,7,8,9)
# print(val[1])
# print(val[3])

#TAsk 5
# val=(10,20,30,40,50)
# t=int(input("Enter a value:"))
# if t in val:
#     print(t, "It exists")
# else:
#     print(t, "It Doesn't exist")

#Task 6

# fruits={"apple":24, "orange":23, "grapes":68, "cucumber":45}
# for fruit, price in fruits.items():
#         if price >50:
#                 print(fruit)

# Task 7

# fruits={"apple":50,"mango":90}
# fruits["banana"]=60
# print(fruits)

#Task 8
# dict1={"a":46,"b":20}
# dict2={"c":24,"d":90}
# merge=dict1.copy()
# merge.update(dict2)
# print(merge)

#Task 9
# val1={1,2,3,4,5,6}
# val2={3,4,5,6,7}
# union_result=val1.union(val2)
# intersection_result=val1.intersection(val2)
# print(union_result,intersection_result)

#Task 10
# li=[10,12,13,14,15,16]
# val=int(input("Enter a value:"))
# if val in li:
#     print("Value already stored in the list")
# else:
#     print("given value not in list")

#Task 11
# li=input("Enter a sentence:")
# rev=""
# for i in li:
#     rev= i + rev

# if li == rev:
#     print("Given is palindrome")
# else:
#     print("Given is not a palindrome")

#Task 12
# val=input("Enter a value:")
# count=0
# for i in val:
#     if i in["a","e","i","o","u"]:
#         count +=1
# print(count)

#Task 13
# tab=int(input("Enter a number: "))
# print("Multiplication table for",tab)        
# for i in range(1,11):
#     print(i,"*",tab,"=", i * tab)

#Task 14
# i=1
# while i<=50:
#     print(i)
#     i+=1

#Task 15
# while True:
#     user=input("Enetr something:")
#     if user == "exit":
#         break