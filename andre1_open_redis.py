import socket

target = "ssh.0x10.cloud"
port = 6379

print(f"[*] Connecting to {target} on port {port} (Redis)...")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)

try:
    sock.connect((target, port))
    print("[+] Connection established!")
    
    # Redis requires a command. Let's send "PING\r\n" (with carriage return + newline)
    sock.sendall(b"PING\r\n")
    
    # Wait for the response
    response = sock.recv(1024).decode('utf-8', errors='ignore').strip()
    
    if response == "+PONG":
        print(f"[+] VULNERABILITY CONFIRMED: Unauthenticated Redis Database!")
        print(f"    Sent: PING")
        print(f"    Received: {response}")
        print("    Risk: No password is required. Attackers can steal data,")
        print("    overwrite files, or gain root access to the server.")
    else:
        print(f"[-] Received unexpected response: {response}")
        
except Exception as e:
    print(f"[-] Error: {e}")
finally:
    sock.close()