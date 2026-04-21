import socket

target = "ssh.0x10.cloud"
port = 2323

print(f"[*] Connecting to {target} on port {port}...")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)

try:
    sock.connect((target, port))
    
    # Wait a moment for the server to send its welcome banner
    banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
    
    print(f"[+] Received Banner: {banner}")
    
    # Check if the banner contains words that indicate cleartext protocols
    if "Ubuntu" in banner or "server" in banner:
        print("[+] VULNERABILITY CONFIRMED: Telnet service exposed!")
        print("    Risk: Telnet does not encrypt traffic. Any credentials typed")
        print("    here (like usernames/passwords) can be sniffed by attackers on the network.")
    else:
        print("[-] Service detected, but not clearly identified as Telnet.")
        
except Exception as e:
    print(f"[-] Error: {e}")
finally:
    sock.close()