import socket

target = input("اكتب 127.0.0.1 واضغط Enter: ")
ports = [21, 22, 80, 443]

print(f"جاري الفحص على: {target}")

for port in ports:
    s  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"المنفذ {port}: مفتوح")
    else:
        print(f"المنفذ {port}: مغلق")
    s.close()
