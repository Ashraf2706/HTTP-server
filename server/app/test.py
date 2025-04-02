#!/usr/bin/env python3
import socket

HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 4221

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on port {PORT}")
        
        while True:
            conn, addr = s.accept()
            print(f"Connection from {addr}")
            conn.close()  # Immediately close the connection for this test

if __name__ == "__main__":
    main()