r1 = int(input("Enter the Start Range -- >> "))
r2 = int(input("Enter the End Range -- >> "))

print("Prime numbers between", r1, "and", r2, "are -- > ")

for val in range(r1, r2):
  if val > 1:
    for i in range(2, val):
      if (val % i) == 0:
        break
    else:
      print(val, end=" ")