# ensemble désordonné et sans doublon

avengers = {
    "hulk",
    "iron-man",
    "spiderman"
}
print(type(avengers))

print(avengers)

# ajout
avengers.add('ant-man')
avengers.add('ant-man')
avengers.add('ant-man')
avengers.add('ant-man')

print(avengers)

# suppression
avengers.remove('ant-man')
print(avengers)

for element in avengers:
    print(element)

# exemple typique : supprimer des doublons
liste = ["France", "Allemagne", "Allemagne", "France"]
print(liste)
mon_set = set(liste)
print(mon_set)
print(mon_set)
print(mon_set)
print(mon_set)
print(mon_set)
print(list(mon_set))