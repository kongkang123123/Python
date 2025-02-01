rivers = {
    'nile' : 'egypt',
    'han' : 'south korea',
    'missisisppi' : 'usa',
    }

for river in rivers:
    print("The "+ river + " river is in " + rivers[river]) 

print("\n")
for river in sorted(rivers.keys()):
    print(river)

print("\n")
for river in rivers.values():
    print(river)