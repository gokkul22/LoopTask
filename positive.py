list=[]
n=int(input("Enter no.of elements of list \n"))
print("Enter elements \n")                            
for i in range(0,n):                                  #user inputing elements of string
    x=int(input())
    list.append(x)
    
print("The list is \n")    
print(list)
print("Postive numbers are: \n")
for j in list:
    if j>0:
        print(j)
        print(" ")


Output:

Enter no.of elements of list 
4
Enter elements 

-5
23
-55
45
The list is 

[-5, 23, -55, 45]
Postive numbers are: 

23
 
45
