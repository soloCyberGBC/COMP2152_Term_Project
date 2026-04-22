import urllib.request

target = "http://blog.0x10.cloud"

print(f"[*] Checking security headers on {target}...")
try:
    response = urllib.request.urlopen(target, timeout=5)
    headers = dict(response.headers)
    
    print("[+] Headers retrieved. Checking for missing security headers...")
    
    missing = []
    if "X-Frame-Options" not in headers:
        missing.append("X-Frame-Options")
    if "X-Content-Type-Options" not in headers:
        missing.append("X-Content-Type-Options")
    if "Strict-Transport-Security" not in headers:
        missing.append("Strict-Transport-Security")
        
    if missing:
        print(f"[+] VULNERABILITY CONFIRMED: Missing {len(missing)} security headers!")
        print(f"    Missing: {', '.join(missing)}")
        print("    Risk: Without these, the site is vulnerable to Clickjacking,")
        print("    MIME-sniffing, and protocol downgrade attacks.")
    else:
        print("[-] Headers look secure.")
        
except Exception as e:
    print(f"[-] Error: {e}")