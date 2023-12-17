print("Your First Digit:")
n1 = int(input())
print("Your Second digit")
n2 = int(input())
print("Calculate through (*/+/-/'/'):")
output = input()
if output == '+':
    print(int(n1)+int(n2))
elif output == '-':
    print(int(n1)-int(n2))
elif output == '*':
    print(int(n1)*int(n2))
elif output == '/':
    print(int(n1)/int(n2))
else:
    print("Error Bro 😂😂😂")
