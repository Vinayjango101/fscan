import dns.resolver
import whois
import requests
import socket
import threading
from enum import Enum
import sys

# -------------------------------
# ENUMERATION TASK DEFINITIONS
# -------------------------------

class EnumTask(Enum):
    DNS_LOOKUP = "DNS Records"
    WHOIS = "WHOIS"
    PORT_SCAN = "Port Scan"
    SUBDOMAIN_ENUM = "Subdomain Enumeration"
    ROBOTS_CHECK = "robots.txt"


# -------------------------------
# THREADING UTILITY
# -------------------------------

def threaded_task(func, *args):
    thread = threading.Thread(target=func, args=args)
    thread.start()
    return thread


# -------------------------------
# TASK IMPLEMENTATIONS
# -------------------------------

# DNS Lookup
def dns_lookup(domain):
    print(f"\n[🔎 DNS LOOKUP] {domain}")
    for rtype in ["A", "MX", "TXT", "NS", "CNAME"]:
        try:
            result = dns.resolver.resolve(domain, rtype)
            for r in result:
                print(f"  [{rtype}] {r.to_text()}")
        except Exception:
            continue


# WHOIS Lookup
def whois_lookup(domain):
    print(f"\n[📄 WHOIS LOOKUP] {domain}")
    try:
        w = whois.whois(domain)
        print(f"  Registrar     : {w.registrar}")
        print(f"  Creation Date : {w.creation_date}")
        print(f"  Expiry Date   : {w.expiration_date}")
    except Exception as e:
        print(f"  WHOIS error   : {e}")


# robots.txt Check
def check_robots(domain):
    print(f"\n[🤖 ROBOTS.TXT CHECK] {domain}")
    url = f"http://{domain}/robots.txt"
    try:
        r = requests.get(url, timeout=5)
        print(f"  Found robots.txt ({len(r.text)} bytes):\n")
        print(r.text.strip())
    except Exception:
        print("  Not found or error")


# Port Scanning (common ports)
def port_scan(domain):
    print(f"\n[🛠️ PORT SCAN] {domain}")
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]
    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((domain, port))
            if result == 0:
                print(f"  [OPEN] Port {port}")
            sock.close()
        except Exception:
            continue


# Subdomain Enumeration (brute-force demo)
def subdomain_enum(domain):
    print(f"\n[🌐 SUBDOMAIN ENUMERATION] {domain}")
    subdomains = ['www', 'mail', 'ftp', 'test', 'dev']
    for sub in subdomains:
        full_domain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(full_domain)
            print(f"  [FOUND] {full_domain} -> {ip}")
        except socket.gaierror:
            continue


# -------------------------------
# RUNNER
# -------------------------------

def run_all_tasks(domain):
    print(f"🚀 Starting reconnaissance for: {domain}")
    tasks = [
        threaded_task(dns_lookup, domain),
        threaded_task(whois_lookup, domain),
        threaded_task(check_robots, domain),
        threaded_task(port_scan, domain),
        threaded_task(subdomain_enum, domain)
    ]
    for t in tasks:
        t.join()
    print("\n✅ Recon complete!")


# -------------------------------
# MAIN EXECUTION
# -------------------------------

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fscan.py <domain>")
        sys.exit(1)

    target_domain = sys.argv[1]
    run_all_tasks(target_domain)
