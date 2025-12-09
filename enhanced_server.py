import socket
import subprocess

def start_enhanced_server():
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Configure server
    host = '127.0.0.1'
    port = 12346  # Different port to avoid conflict
    
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Enhanced Server listening on {host}:{port}")
    
    client_socket, client_address = server_socket.accept()
    print(f"Connected to client: {client_address}")
    
    while True:
        # Get command from server user
        command = input("\nEnter command to execute on client (or 'exit'): ")
        
        if command.lower() == 'exit':
            break
        
        # Send command to client
        client_socket.send(command.encode())
        
        # Wait for result (optional - could be one-way)
        response = client_socket.recv(4096).decode()
        print(f"Command result:\n{response}")
    
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_enhanced_server()