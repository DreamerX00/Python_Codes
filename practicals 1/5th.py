s1 = input("Enter Your First Name -- >> ")
s2 = input("Enter Your Second Name -- >> ")
   
print("\nStrings before Swapping: " + s1 + " " + s2)  
   
s1 = s1 + s2  

s2 = s1[0 : (len(s1) - len(s2))]  

s1 = s1[len(s2):]  
   
print("\nStrings after Swapping: " + s1 + " " + s2)