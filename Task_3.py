from pprint import pprint

with open('1.txt', 'rt', encoding='utf-8') as file1:
    a1 = 0
    for line1 in file1:
        print(line1)
        a1 += 1

with open('2.txt', 'rt', encoding='utf-8') as file2:
    a2 = 0
    for line2 in file2:
        print(line2)
        a2 += 1

with open('3.txt', 'rt', encoding='utf-8') as file3:
    a3 = 0
    for line3 in file3:
        print(line3)
        a3 += 1

dict (a1, a2, a3)