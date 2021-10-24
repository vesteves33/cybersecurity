import itertools

string = input("Enter a string: ")

list = itertools.permutations(string, len(string))

for i in list:
    print(''.join(i))