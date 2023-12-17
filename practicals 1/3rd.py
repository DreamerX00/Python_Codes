num = int(input("Enter The Number -- >> "))
f = 1
if num < 0:
   print("INVALID INPUT")
elif num == 0:
   print("The Factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       f = f*i
   print("The Factorial of",num,"is",f)