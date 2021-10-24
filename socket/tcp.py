import socket, sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
       # s.connect((sys.argv[1], int(sys.argv[2])))
       # s.send(sys.argv[3].encode())
       # data = s.recv(1024)
       # print(data.decode())
        #s.close()

    except socket.error as e:
        print(e)
        sys.exit(1)

    targetHost = input("Enter target host: ")
    doorHost = input("Enter door host: ")

    try:
        s.connect((targetHost, int(doorHost)))
        print(f'Connected successful to {targetHost} on port {doorHost}')
        s.shutdown(2)

    except socket.error as e:
        print(e)
        sys.exit(1)



if __name__ == '__main__':
    main()