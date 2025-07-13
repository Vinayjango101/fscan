# ⚡fscan
fscan is a lightweight, multithreaded reconnaissance tool built in Python for CTFs and penetration testing. It performs real-time enumeration of DNS records, WHOIS info, common ports, subdomains, and robots.txt — all in parallel for speed and efficiency.

🔍 Features
DNS record resolution (A, MX, TXT, NS, CNAME)

WHOIS information lookup

Port scanning (common ports)

Subdomain brute-forcing (demo list)

robots.txt detection

Real-time multithreaded output

🚀 Usage
# ``python fscan.py example.com``

🛠 Requirements
Install dependencies:
# ``pip install dnspython python-whois requests``
