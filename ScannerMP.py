import socket
import multiprocessing
from multiprocessing import Pool
import datetime

pocetak = datetime.datetime.now()

print("Program se izvodi na ovom racunalu:")
print(datetime.datetime.now())

from Local_Machine_Info import print_machine_info

print_machine_info()
print("--------------------------")


def scan(info):
    target_ip = info
    port = info

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    try:
        sock.connect((target_ip, port))
        sock.close()

        return port, True

    except (socket.timeout, socket.error):
        return port, False


if __name__ == '__main__':
    pocetak = datetime.datetime.now()

    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    target = input("Unesite adresu hosta kojeg zelite skenirati: ")
    print("Skeniram...", target)

    print("Od kojeg do kojeg porta zelite skenirati? ")

    p1 = input("Od: ")
    p2 = input("Do: ")

    p1 = int(p1)
    p2 = int(p2)

    ports = range(p1, p2)
    lista = [(target, port) for port in ports]

    pool = Pool(multiprocessing.cpu_count() * 2)

    for port, status in pool.imap(scan, lista):
        if status:
            print('Port', port, ' je otvoren!!!')

    kraj = datetime.datetime.now()
    print('Vrijeme potrebno za izvedbu: ' + kraj - pocetak)