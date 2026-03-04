from queue import Queue
import socket
import threading

# Sockets will be used for all connection attempts to the host at a specific port
# Threading will allow me to scan multiple ports at once
# Queue will help to make sure every port is scanned once 

# GLOBAL VARIABLES
queue = Queue()
open_ports = [] # Stores open port numbers at the end

def portscan(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket using IPv4
        sock.settimeout(5)
        sock.connect((target, port))
        sock.close()
        return True # Port is Open
    except Exception as e:
        print(f"Port {port} scan error: {e}")
        return False


"""Four Modes"
Mode 1 = Scan 1023 Standardized Ports
Mode 2 = 48,123 Reserved Ports
Mode 3 = Scan Most Common Ports
Mode 4 = Custom Ports
"""

def get_ports(mode):
    if mode == 1:
        for port in range (1, 1024):
            queue.put(port)

    elif mode == 2:
        for port in range(1, 49152):
            queue.put(port)

    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443] # Common ports
        for port in ports:
            queue.put(port)

    elif mode == 4:
        ports = input("Enter your ports (seperate by commas): ")
        ports = ports.split(",") # Split user input into list
        ports = list(map(int, ports)) # Map typecasting function of the integer data type to every element of the list
        for port in ports:
            queue.put(port)


def worker(target): # Worker function to get port numbers from queue, scan and print results
    while True:
        port = queue.get()
        if portscan(target, port):
            print(f"Port {port} is open!")
            open_ports.append(port)
        queue.task_done()


def run_scanner(target, threads, mode):
    get_ports(mode)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker, args=(target,))
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    queue.join()

    print("Open ports are:", sorted(open_ports))


# Entry Point
if __name__ == "__main__":
    print("******************\nZEEN PORT SCANNER\n******************\nPort Scanner Modes:\nMode 1 = Scan 1023 Standardized Ports\nMode 2 = 48,123 Reserved Ports\nMode 3 = Scan Most Common Ports\nMode 4 = Custom Ports\n******************")
    target = input("Enter IPv4: ")
    mode = int(input("Select Mode (1-4): "))
    threads = int(input("Number of threads: "))

    print(f"Scanning {target} with {threads} threads...")
    run_scanner(target, threads, mode)

SystemExit