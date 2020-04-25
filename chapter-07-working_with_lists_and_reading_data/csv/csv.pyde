csv = loadStrings('playlist.csv')

for entry in csv[1:]:
    track = entry.split(',')
    print('{}. {}'.format(track[4], track[1]))
