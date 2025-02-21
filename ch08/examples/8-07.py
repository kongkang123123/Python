def make_album(musician, title, count=''):
    album = {'musician':musician, 'title':title}

    if(count):
        album['track_count'] = count
    
    return album

print(make_album('hi', 'hello'))
print(make_album('bye', 'see you'))
print(make_album('nice to', 'meet you', count=3))