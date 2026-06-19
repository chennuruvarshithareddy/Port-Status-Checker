import socket

host = input("Enter host/IP address: ")
port = int(input("Enter port number: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)

result = sock.connect_ex((host, port))

if result == 0:
    print(f"Port {port} is OPEN on {host}")
else:
    print(f"Port {port} is CLOSED on {host}")

sock.close()