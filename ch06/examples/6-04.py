terminologies = {
    'dictionary' : 'key-vlaue',
    'if-elif-else': 'condition statement',
    'list' : 'similar to array',
    'tuple' : 'similar to list. immutuable',
    'variable' : 'space svaing value',
    }


for terminology in terminologies:
    print(terminology + ": " + terminologies[terminology])

print("\n")
for terminology in terminologies.values():
    print(terminology)

print("\n")
for terminology in set(terminologies.values()):
    print(terminology)

print("\n")
for terminology in sorted(terminologies.values()):
    print(terminology)