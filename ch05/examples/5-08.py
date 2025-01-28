users = ['tom', 'admin', 'felix', 'zoe', 'dewey']

for user in users:
    if(user != 'admin'):
        print("Hello, " + user + "Thank you for logging in again.")
    else:
        print("Hello, " + user + ". Would you like to see the status report?")