from zipfile import ZipFile
import pandas as pd
import csv
import random
from tabulate import tabulate


file_name="archive.zip"

with ZipFile(file_name,'r') as zip:
    zip.printdir()
    zip.extractall()

with open('muse_v3.csv', newline='',encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)

for i in data:
    del i[0]
    del i[3]
    del i[4]
    del i[5]
del data[0]
print(data[1])
for i in data:
    del i[3]
print(data[1])
for i in data:
    del i[3]
print(data[1])
# print(data)

temp=[]
for i in data:
    for j in i:
        if j=='':
            j="No Info"
        # print(j)
        temp.append(j)
# print(temp)
composite_list = [temp[x:x+5] for x in range(0, len(temp),5)]
# print (composite_list)


for i in composite_list:
    name = i[2]
    name1 = name.replace("[", "")
    name1 = name1.replace("]", "")
    name1 = name1.replace("'", "")
    # print(name1)
    i.insert(2, name1)
    i.remove(name)
# print(composite_list)


fields = ['track','artist','seeds','spotify_id','genre']

# data rows of csv file
rows = composite_list

with open('GFG.csv', 'w',encoding="utf8") as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)

    write.writerow(fields)
    write.writerows(rows)


# Playlist generation
# ----------------------------------------------------- sad playlist ----------------------------------------
print("")
print("")
print("----------------------------------------------------- sad playlist ----------------------------------------")
print("")
print("")

sad_playlist=[]
for i in composite_list:
    if i[4]=="blues" or i[4]=="blues rock":
        sad_playlist.append(i[0])
        sad_playlist.append(i[1])
        # sad_playlist.append(i[2])
        sad_playlist.append(i[3])
sad_playlist = [sad_playlist[x:x+3] for x in range(0, len(sad_playlist),3)]

sad_PL=[]

for i in sad_playlist:
    if i[2] == "No Info":
        pos = sad_playlist.index(i)
        del sad_playlist[pos]
    else:
        sad_PL.append(i)


# print(sad_PL)

rand_sad_PL=random.sample(sad_PL, 20)


table = tabulate(rand_sad_PL, headers=['Name', 'Artist', 'Spotify id'], tablefmt='orgtbl')
print(table)

# ----------------------------------------------------- happy playlist ----------------------------------------
print("")
print("")
print("----------------------------------------------------- happy playlist ----------------------------------------")
print("")
print("")

happy_playlist=[]
for i in composite_list:
    if i[4]=="pop" or i[4]=="dance":
        happy_playlist.append(i[0])
        happy_playlist.append(i[1])
        happy_playlist.append(i[3])
happy_playlist = [happy_playlist[x:x+3] for x in range(0, len(sad_playlist),3)]

happy_PL=[]

for i in happy_playlist:
    if i[2] == "No Info":
        pos = happy_playlist.index(i)
        del happy_playlist[pos]
    else:
        happy_PL.append(i)

# print(happy_PL)

rand_happy_PL=random.sample(happy_PL, 20)


table = tabulate(rand_happy_PL, headers=['Name', 'Artist', 'Spotify id'], tablefmt='orgtbl')
print(table)

# ----------------------------------------------------- Tired ----------------------------------------
print("")
print("")
print("----------------------------------------------------- Tired ----------------------------------------")
print("")
print("")
tired_playlist=[]
for i in composite_list:
    if i[4]=="classical" or i[4]=="jazz":
        tired_playlist.append(i[0])
        tired_playlist.append(i[1])
        tired_playlist.append(i[3])
tired_playlist = [tired_playlist[x:x+3] for x in range(0, len(sad_playlist),3)]

tired_PL=[]

for i in tired_playlist:
    if i[2] == "No Info":
        pos = tired_playlist.index(i)
        del tired_playlist[pos]
    else:
        tired_PL.append(i)

# print(tired_PL)

rand_tired_PL=random.sample(tired_PL, 20)


table = tabulate(rand_tired_PL, headers=['Name', 'Artist', 'Spotify id'], tablefmt='orgtbl')
print(table)


# ----------------------------------------------------- Angry ----------------------------------------
print("")
print("")
print("----------------------------------------------------- Angry ----------------------------------------")
print("")
print("")
Angry_playlist=[]
for i in composite_list:
    if i[4]=="hip-hop" or i[4]=="metal":
        Angry_playlist.append(i[0])
        Angry_playlist.append(i[1])
        Angry_playlist.append(i[3])
Angry_playlist = [Angry_playlist[x:x+3] for x in range(0, len(sad_playlist),3)]

Angry_PL=[]

for i in Angry_playlist:
    if i[2] == "No Info":
        pos = Angry_playlist.index(i)
        del Angry_playlist[pos]
    else:
        Angry_PL.append(i)

# print(Angry_PL)

rand_Angry_PL=random.sample(Angry_PL, 20)


table = tabulate(rand_Angry_PL, headers=['Name', 'Artist', 'Spotify id'], tablefmt='orgtbl')
print(table)

# ----------------------------------------------------- Focus ----------------------------------------
print("")
print("")
print("----------------------------------------------------- Focus ----------------------------------------")
print("")
print("")
Focus_playlist=[]
for i in composite_list:
    if i[4]=="ambient":
        Focus_playlist.append(i[0])
        Focus_playlist.append(i[1])
        Focus_playlist.append(i[3])
Focus_playlist = [Focus_playlist[x:x+3] for x in range(0, len(sad_playlist),3)]

Focus_PL=[]

for i in Focus_playlist:
    if i[2] == "No Info":
        pos = Focus_playlist.index(i)
        del Focus_playlist[pos]
    else:
        Focus_PL.append(i)

# print(Focus_PL)

rand_focus_PL=random.sample(Focus_PL, 20)


table = tabulate(rand_focus_PL, headers=['Name', 'Artist', 'Spotify id'], tablefmt='orgtbl')
print(table)
