import socket

def start_client():
    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Server details
    host = '127.0.0.1'  # localhost
    port = 12345        # port number
    
    try:
        # Connect to server
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        
        # Receive messages from server
        while True:
            # Receive message
            message = client_socket.recv(1024).decode()
            
            if not message:
                break
            
            print(f"Received from server: {message}")
    
    except ConnectionRefusedError:
        print("Connection refused. Make sure server is running.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Client closed")

if __name__ == "__main__":
    start_client()