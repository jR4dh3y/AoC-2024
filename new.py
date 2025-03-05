with open('input.txt', 'r') as file:
    dt = file.read()

with open('input.txt', 'r') as file:
    data_1 = file.read()


import re
pattern = r'(XMAS|SAMX)'
data= data_1.split("\n")
pivoted = [''.join(row) for row in zip(*data)]
diagonal1 = []
diagonal2 = []

for num in range(len(data)):
    down = num
    right = 0
    goo = True
    word = ''
    while goo:
        try:
            word = word + data[down][right]
            right += 1
            down += 1
        except:
            diagonal1.append(word) 
            goo = False

for num in range(len(data[0])):
    down = 0
    right = num +1
    goo = True
    word = ''
    while goo:
        try:
            word = word + data[down][right]
            right += 1
            down += 1
        except:
            diagonal1.append(word) 
            goo = False   

for num in range(len(data)):
    down =  (num + 1)*-1
    right = 0
    goo = True
    word = ''
    while goo:
        try:
            word = word + data[down][right]
            right += 1
            down -= 1
        except:
            diagonal2.append(word) 
            goo = False

for num in range(len(data[0])):
    down = -1
    right = (num + 1)
    goo = True
    word = ''
    while goo:
        try:
            word = word + data[down][right]
            right += 1
            down -= 1
        except:
            diagonal2.append(word) 
            goo = False



all = data + pivoted +diagonal1 + diagonal2
total = 0


for c in all:
    matches = re.findall(pattern, c)
    total += int(len(matches))
total

data= data_1.split("\n")
good = 0
for row in range(len(data)-1):
    for col in range(len(data[0])-1):
        if data[row][col] == 'A':
            x = data[row+1][col+1] + 'A' + data[row-1][col-1] 
            y = data[row+1][col-1] + 'A' + data[row-1][col+1]
            if x in ('SAM', 'MAS') and y in ('SAM', 'MAS'):
                good += 1
    
good

