file = open("test.txt",'a+',)


file.seek(5)
print(file.tell())
file.write("Bch Ain't Loyal")

# file1 = open("test.txt",'r')

print(file.tell())

# print(file1.read())

file.close()