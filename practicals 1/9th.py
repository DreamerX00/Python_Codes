def Info(N,G,P):
    if G == "M" or G == "m":
        g = "Male"
    else:
        g = "Female"
    return print(P+N+" Is Your Name And Your Gender is "+g)

Name = input("Enter Your Name -- >> ")
Gender = input("Enter Your Gender As M or F -- >> ")


if Gender == "M":
    Prefix = "Mr."
elif Gender == "F":
    Prefix = "Mrs."
else:
    print("Invalid Gender Input")

Info(Name,Gender,Prefix)
    
    
