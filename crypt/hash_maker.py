import hashlib


def hash_maker():

    string = input("Enter a string to hash: ")
    
    result = hashlib.sha512(string.encode('utf-8'))

    print('Result is: ', result.hexdigest())

if __name__ == '__main__':
    hash_maker()