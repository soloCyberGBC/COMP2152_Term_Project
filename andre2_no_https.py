import urllib.request

target = "http://api.0x10.cloud"

print(f"[*] Checking if {target} enforces HTTPS...")
try:
    response = urllib.request.urlopen(target, timeout=5)
    final_url = response.url
    
    print(f"    Initial request: http://api.0x10.cloud")
    print(f"    Final URL landed on: {final_url}")
    
    if final_url.startswith("http://"):
        print("[+] VULNERABILITY CONFIRMED: Site does NOT force HTTPS!")
        print("    Risk: Any credentials or data sent by a user can be intercepted")
        print("    in plain text by an attacker on the same network (Man-in-the-Middle).")
    else:
        print("[-] Site properly redirects to HTTPS.")
        
except Exception as e:
    print(f"[-] Error: {e}")