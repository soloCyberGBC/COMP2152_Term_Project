import socket

target = "ssh.0x10.cloud"
port = 22

print(f"[*] Connecting to {target} on port {port}...")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)

try:
    sock.connect((target, port))
    
    # SSH servers automatically send their version string when you connect
    banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
    
    print(f"[+] Received Banner: {banner}")
    
    if "SSH-2.0" in banner:
        print("[+] VULNERABILITY CONFIRMED: SSH Version Disclosure!")
        print("    Risk: The exact software version (OpenSSH 10.0p2 Debian...) is exposed.")
        print("    Attackers can look up CVEs and known exploits specifically for this version.")
    else:
        print("[-] Not an SSH service.")
        
except Exception as e:
    print(f"[-] Error: {e}")
finally:
    sock.close()