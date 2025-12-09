import socket

def start_server():
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Configure server
    host = '127.0.0.1'  # localhost
    port = 12345        # port number
    
    # Bind socket to address
    server_socket.bind((host, port))
    
    # Listen for connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    
    # Accept client connection
    client_socket, client_address = server_socket.accept()
    print(f"Connected to client: {client_address}")
    
    # Send messages to client
    while True:
        message = input("Enter message to send (type 'exit' to quit): ")
        
        if message.lower() == 'exit':
            break
        
        # Send message to client
        client_socket.send(message.encode())
        print(f"Sent: {message}")
    
    # Cleanup
    client_socket.close()
    server_socket.close()
    print("Server closed")

if __name__ == "__main__":
    start_server()