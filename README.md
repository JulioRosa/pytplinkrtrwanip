# pytplinkrtrwanip
Retrieve WAN IP from TP-Link Routers


# 🛰️ pytplinkrtrwanip

Bypass CGNAT and expose your TP-Link router's WAN IP to the internet using DuckDNS and motionEyeOS.

This project is based on [AlexandrErohin/TP-Link-Archer-C6U](https://github.com/AlexandrErohin/TP-Link-Archer-C6U) and specially adapted for the **TP-Link Archer MR200** router.

> This tool allows you to self-host services even if you're behind CGNAT, by retrieving your router's WAN IP and updating your DuckDNS record.

---

## 📡 What It Does

- Logs into your TP-Link **Archer MR200** router
- Retrieves the **actual WAN IP** (not the one behind (CGNAT) Carrier-Grade Network Address Translation from services like IPChicken.com)
- Updates your **DuckDNS** subdomain with that IP
- Enables self-hosting (websites, services, etc.) despite CGNAT limitations

---

## 🛠️ Requirements

- webhosting service (e.g. Nginx on RPI3)
- tested and functional on TP-Link Archer MR200 router
- Python 3.x
- [DuckDNS account](https://www.duckdns.org/)
- Router admin login credentials

---

## 🚀 Getting Started

### 1. Clone the project

```bash
git clone https://github.com/JuioRosa/pytplinkrtrwanip.git
cd pytplinkrtrwanip

### 🕒 Setting up a Cron Job for pytplinkrtrwanip

To keep your WAN IP synced with DuckDNS, run the script automatically using `cron`.

## ⏱️ Example: Check router wan IP Every 5 Minutes

1. Open crontab:
   ```in Linux:
   crontab -e
#updates every 5 minutes
*/5 * * * * /usr/bin/python3 /full/path/to/pytplinkrtrwanip/main.py >> /full/path/to/pytplinkrtrwanip/cron.log 2>&1

