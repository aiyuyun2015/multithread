from threading import Thread
import socket
from multiprocessing import Process


def run_server(host='127.0.0.1', port=33334):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen()
    while True:
        client_sock, addr = sock.accept()
        print('Connection from', addr)
        Thread(target=handle_client, args=(client_sock,)).start()


def handle_client(sock):
    while True:
        received_data = sock.recv(4096)
        if not received_data:
            break
        sock.sendall(received_data)

    print('Client disconnected:', sock.getpeername())
    sock.close()


def compute():
    n = 0
    while True:
        n += 1
        n -= 1
if __name__ == '__main__':
    # without this line, the, package received is about 30k
    # after add this, it's about 100, why?
    # the CPU bound thread, will interfere with the I/O thread, making it slower.
    # since GIL is constantly checking the "compute" function and run it.
    # Thread(target=compute).start()

    # If we use Process instead, then the speed is the same.
    # GIL will not affect this.
    Process(target=compute).start()

    run_server()