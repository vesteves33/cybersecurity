import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    host = 'localhost'
    port = 5433
    message = 'Whats up?'

    try:
        print(f'Client: {message}')
        s.sendto(message.encode(), (host, 5432))
    
        data, server = s.recvfrom(4096)
        data = data.decode()
        print(f'Client: {data}')

    finally:
        print('Client closing conection')
        s.close()

if __name__ == '__main__':
    main()