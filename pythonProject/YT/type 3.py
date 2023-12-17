"""
print("Type your first no.")
n1 = input()
print("Type your second no.")
n2 = input()
print("type your third no.")
n3 = input()
print("This in The Resuld of Addition",int(n1)+int(n2)+int(n3))
"""
#d1 = {'8:30':"Breakfast",'10:00':"Study",'12:00':"Lunch"}
#print(type(d1))
##print(d1.items())
#print(d1['8:30'])
#d2 = {"Akash":"Breakfast"}
#d1 = d2
#print(d1)


d1 = {"Minecraft":"Survival",
      "Pubg":"Battle Royale",
      "Fortnite":"Battle Royale",
      "Valorant":"Teamdeathmatch",
      "Bgmi":"New Pubg"}
#n1 = input()
#print(d1[n1])
del d1 ["Minecraft"]
n2 = input()
d1.update({"Minecraft":"Open world"})



print(d1[n2])





