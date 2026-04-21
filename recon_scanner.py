import socket
import time

target_host = "api.0x10.cloud" 

ports_to_check = [21, 22, 23, 25, 80, 443, 2121, 2323, 2525, 6379, 8080, 8443]

print(f"[*] Starting stealth scan on {target_host}...")
print(f"[*] Checking {len(ports_to_check)} ports...\n")

# Open a file to save our results
with open("scan_results.txt", "w") as f:
    f.write(f"Scan Results for {target_host}\n")
    f.write("="*30 + "\n")
    
    for port in ports_to_check:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2) # Dont hang forever if a port is filtered
        
        # connect_ex returns 0 if the port is OPEN
        result = sock.connect_ex((target_host, port))
        
        if result == 0:
            message = f"[+] OPEN PORT FOUND: {port}\n"
            print(message, end="")
            f.write(message)
            
            # Try to grab a banner
            try:
                sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
                banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
                if banner:
                    banner_msg = f"    Banner: {banner.splitlines()[0]}\n"
                    print(banner_msg, end="")
                    f.write(banner_msg)
            except:
                # Some services don't send banners immediately
                pass
        else:
            f.write(f"[-] Port {port} is closed.\n")
            
        sock.close()
        
        # Sleep to obey the 10 requests/second rule
        time.sleep(0.15) 

print("\n[*] Scan complete. Check scan_results.txt for the full log.")