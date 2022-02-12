#Python program for find flames using 2 names
name1=input("Enter the first name.....")
print("The first name is ",name1)
name2=input("Enter the second name.....")
print("The second name is ",name2)
list1=list(name1)
list2=list(name2)
list1.extend(list2)
print(list1)