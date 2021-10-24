import random, string


def password_maker():

    try:
        print('='*60)
        size = int(input('Quantos caracteres voce deseja na sua senha? '))

        chars = string.ascii_letters + string.digits + string.punctuation

        rng = random.SystemRandom()

        print(''.join(rng.choice(chars) for i in range(size)))
        print('='*60)
    except ValueError:
        print('Oops! Valor invalido!')



if __name__ == '__main__':
    password_maker()