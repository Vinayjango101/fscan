

---

# ⚡ fscan

> A fast, parallelized, real-time reconnaissance framework built in Python — ideal for CTFs, red teaming, bug bounties, and network audits.

**fscan** performs multi-faceted reconnaissance against a target domain or IP using Python multithreading for speed and efficiency. Designed for hackers, pentesters, and CTF players, it provides fast insights through concurrent DNS lookups, WHOIS, port scanning, subdomain brute-forcing, and more.

---

## ✨ Features

* 🔍 **DNS Enumeration** – Resolves A, MX, TXT, NS, and CNAME records.
* 🌐 **Subdomain Brute-force** – Discover subdomains using a configurable wordlist.
* 🛠 **Port Scanning** – Scans top common ports for open services.
* 📄 **WHOIS Lookup** – Fetches domain registration and expiration details.
* 🤖 **robots.txt Inspection** – Downloads and prints disallowed paths.
* ⚡ **Multithreaded Execution** – Fast concurrent recon using threads.
* 💡 **Real-time Output** – Results appear as soon as tasks complete.
* ✅ **Extensible Architecture** – Easy to add your own recon modules.

---

## 🚀 Quick Start

### 🔧 Installation


**Manuall install:**

```bash
pip install dnspython python-whois requests
```

---

### 🧪 Usage

```bash
python fscan.py example.com
```

---

## 🗂 Tasks Included

| Task            | Description                              |
| --------------- | ---------------------------------------- |
| DNS Lookup      | Resolve A, MX, TXT, NS, CNAME records    |
| WHOIS           | Domain registration details              |
| Port Scan       | Check for open ports from a default list |
| Subdomain Brute | Discover subdomains via wordlist         |
| robots.txt      | Pull and parse `robots.txt`              |

---

## 📌 To Do / Coming Soon

* [ ] Output results to JSON/CSV
* [ ] Add `asyncio` version for ultra-fast scans
* [ ] Support IP ranges & CIDRs
* [ ] Add full subdomain wordlist support
* [ ] WAF detection & TLS fingerprinting

---

## 📜 License

MIT License

---

## 🤝 Contributing

Pull requests are welcome! Please submit an issue for feature requests or bugs.

---

Want me to help with anything else?
