favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

voters = [
    'phil', 'elynor', 'micheal' 
    ]

for voter in voters:
    if(voter in favorite_languages.keys()):
        print(voter + ", " + "Thank you for voting")
    else:
        print(voter + ", " + "Please take our poll")