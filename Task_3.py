from pprint import pprint
file1 = {}
# file2 = {}
# file3 = {}
with open('1.txt', 'rt', encoding='utf-8') as file:
    a1 = 0
    i = 0

    for line in file:
        print(line)
        a1 += 1
        i += 1
        file1[i] = line

with open('2.txt', 'rt', encoding='utf-8') as file:
    a2 = 0
    for line in file:
        print(line)
        a2 += 1
        i += 1
        file1[i] = line

with open('3.txt', 'rt', encoding='utf-8') as file:
    a3 = 0
    for line in file:
        print(line)
        a3 += 1
        i += 1
        file1[i] = line

print (a1, a2, a3)

with open('Task_3.txt', 'wt') as f:

    if a2 < a1 < a3:
        f.write(f'2.txt\n{a2}\n')
        i = a1 + 1
        while i <= a1 + a2:
            f.write(file1[i])
            i += 1

        f.write(f'\n1.txt\n{a1}\n')
        i = 1
        while i <= a1:
            f.write(file1[i])
            i += 1

        f.write(f'\n3.txt\n{a3}\n')
        i = a1 + a2 + 1
        while i <= a1 + a2 + a3:
            f.write(file1[i])
            i += 1

    if a2 < a3 < a1:
        f.write(f'2.txt\n{a2}\n')
        i = a1 + 1
        while i <= a1 + a2:
            f.write(file1[i])
            i += 1

        f.write(f'\n3.txt\n{a3}\n')
        i = a1 + a2 + 1
        while i <= a1 + a2 + a3:
            f.write(file1[i])
            i += 1

        f.write(f'\n1.txt\n{a1}\n')
        i = 1
        while i <= a1:
            f.write(file1[i])
            i += 1

    if a1 < a2 < a3:
        f.write(f'1.txt\n{a1}\n')
        i = 1
        while i <= a1:
            f.write(file1[i])
            i += 1

        f.write(f'\n2.txt\n{a2}\n')
        i = a1 + 1
        while i <= a1 + a2:
            f.write(file1[i])
            i += 1

        f.write(f'\n3.txt\n{a3}\n')
        i = a1 + a2 + 1
        while i <= a1 + a2 + a3:
            f.write(file1[i])
            i += 1


    if a1 < a3 < a2:
        f.write(f'1.txt\n{a1}\n')
        i = 1
        while i <= a1:
            f.write(file1[i])
            i += 1

        f.write(f'\n3.txt\n{a3}\n')
        i = a1 + a2 + 1
        while i <= a1 + a2 + a3:
            f.write(file1[i])
            i += 1

        f.write(f'\n2.txt\n{a2}\n')
        i = a1 + 1
        while i <= a1 + a2:
            f.write(file1[i])
            i += 1


    if a3 < a1 < a2:
        f.write(f'3.txt\n{a3}\n')
        i = a1 + a2 + 1
        while i <= a1 + a2 + a3:
            f.write(file1[i])
            i += 1


        f.write(f'\n1.txt\n{a1}\n')
        i = 1
        while i <= a1:
            f.write(file1[i])
            i += 1

        f.write(f'\n2.txt\n{a2}\n')
        i = a1 + 1
        while i <= a1 + a2:
            f.write(file1[i])
            i += 1


    if a3 < a2 < a1:
        f.write(f'3.txt\n{a3}\n')
        i = a1 + a2 + 1
        while i <= a1 + a2 + a3:
            f.write(file1[i])
            i += 1

        f.write(f'\n2.txt\n{a2}\n')
        i = a1 + 1
        while i <= a1 + a2:
            f.write(file1[i])
            i += 1

        f.write(f'\n1.txt\n{a1}\n')
        i = 1
        while i <= a1:
            f.write(file1[i])
            i += 1