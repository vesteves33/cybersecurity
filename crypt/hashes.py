import hashlib

def hash():

    file1 = 'arquivo1'
    file2 = 'arquivo2'

    hash1 = hashlib.new('ripemd160')
    hash2 = hashlib.new('ripemd160')

    hash1.update(open(file1, 'rb').read())
    hash2.update(open(file2, 'rb').read())

    if hash1.digest() == hash2.digest():
        print('The files are identical')
        print(f'Hash do arquivo "a" é: {hash1.hexdigest()}')
        print(f'Hash do arquivo "b" é: {hash2.hexdigest()}')


    else:
        print('The files are different')

if __name__ == '__main__':
    hash()