# CSV Spreadsheet

import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    rooms = []
    colors = []

    for row in readCSV:
        room = row[2]
        color = row[3]
        rooms.append(room)
        colors.append(color)

    print(rooms)
    print(colors)

    try:
        what_color = input('What color do you want to select?: ')
        color_index = colors.index(what_color.lower())
        print(color_index)
        print('The room for ', what_color, 'is', rooms[color_index])

    except Exception as e:
        print(e)
