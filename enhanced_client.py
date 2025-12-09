import socket
import subprocess
import os

def execute_command(command):
    """Execute command and return output"""
    try:
        # Execute command
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            timeout=10
        )
        
        # Return combined stdout and stderr
        if result.stdout:
            output = result.stdout
        else:
            output = result.stderr
        
        return f"Exit Code: {result.returncode}\nOutput:\n{output}"
    
    except subprocess.TimeoutExpired:
        return "Error: Command timed out"
    except Exception as e:
        return f"Error executing command: {str(e)}"

def start_enhanced_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    host = '127.0.0.1'
    port = 12346
    
    try:
        client_socket.connect((host, port))
        print(f"Connected to enhanced server at {host}:{port}")
        
        while True:
            # Receive command from server
            command = client_socket.recv(1024).decode()
            
            if not command:
                break
            
            print(f"\nReceived command: {command}")
            
            # Execute command locally
            print("Executing command...")
            result = execute_command(command)
            
            # Send result back to server
            client_socket.send(result.encode())
    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_enhanced_client()