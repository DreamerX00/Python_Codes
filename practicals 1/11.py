file = open(r"test.txt",'r')
print(file.read())

file.seek(0)
print("Initial Position of Cursor is -- >> ",file.tell())

initial = file.seek(4)
print("\nMoving The Cursor Position to 4 -- >> ",file.tell())

print("\nNext 5 Character From Cursor Position are -- >> ",file.read(5))

file.seek(10+initial)
print("\nCurrent Cursor Position is -- >> ",file.tell())

print("\nNext 10 Character From Cursor Position are -- >> ",file.read(10))