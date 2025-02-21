def make_album(musician, title):
    album = {'musician':musician, 'title':title}
    
    return album

while(True):
    m = input("Input musician name: ")
    t = input("Input album title: ")

    print(make_album(m, t))

    f = input("Enter 'q' if you want to stop this program: ")

    if(f == 'q'):
        break