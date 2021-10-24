import os, time

def ping():
    try:
        with open('hosts') as file:
            dump = file.read()
            dump = dump.splitlines()
        
        for ip in dump:
            print('Verificando o ip', ip.upper())
            print('='*60)
            os.system(f'ping -c 4 {ip}')
            time.sleep(3)
        
    
    except FileNotFoundError:
        print('File not found')
    
    #host = input("Enter Ip or hostname: ")
    


if __name__ == '__main__':
    ping()