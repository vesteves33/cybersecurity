import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("Socket created")

    host  = 'localhost'
    port  = 5432

    s.bind((host, port))

    message = '\nServer ta on'

    while True:
        data, address = s.recvfrom(4096)
    
        if data:
            print('Servidor enviando mensagem...')
            s.sendto(data + (message.encode()), address)

if __name__ == '__main__':
    main()