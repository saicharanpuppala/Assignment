# user input
name = input("your name please :")
age = int(input("your age please :"))
country = input("where are you from :")
marks = float(input("enter the marks you secured :"))
condition = bool(input("passed the exam :"))
print(name,age,country,marks,condition)
print(type(name))
print(type(age))
print(type(country))
print(type(marks))
print(type(condition))

#for loop
totalinput = list()
for i in range(5):
    totalinput.append(input('please enter fav sports : '))
print(totalinput)
for i in totalinput:
    print(i)
for i in totalinput:
    print(i,totalinput.index(i))
for i in range(len(totalinput)):
    print(i,totalinput[i])
print(*totalinput,sep ='-')
for i in totalinput:
    print(i,end= "--")

#if elif else (conditions)
for i in totalinput:
    if i.startswith('p'):
        print(f"\n{i} is very intresting sport")
    elif i.startswith('r'):
        print(f"\n{i} is kind of intresting of intresting sport")
    elif i.startswith('s'):
        print(f"\n{i} nice....intelligent sport")
    else:
        print(f"\n{i} its intresting")
options = [2,'a',True,2.5,4,'s',False]
for i,j in enumerate(options):
    print(i,j, type(j))
for i,j in enumerate(options):
    if type(j)==int:
        print(f"this is an integer : {j}")
    elif type(j)==str:
        print(f"this is a string : {j}")
    elif type(j)==bool:
        print(f"this is a boolean : {j}")
    else:
        print(f"this is a float : {j}")