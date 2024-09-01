import socket

# Konfiguro parametra
TARGET_IP = '89.185.85.62'  # Zëvendëso me IP-në që dëshiron të dërgosh
TARGET_PORT = 80          # Zëvendëso me portin që dëshiron të dërgosh
DATA_SIZE = 2 * 1024 * 1024 * 1024  # 2GB në byte

def send_udp_data(ip, port, data_size):
    """Dërgon të dhëna në IP dhe port të caktuar përmes UDP."""
    # Krijo një socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Krijo një burim të dhënash të rastësishme
    data = b'x' * 1024  # 1KB të dhëna për paketë

    bytes_sent = 0
    while bytes_sent < data_size:
        try:
            # Dërgo paketën
            sock.sendto(data, (ip, port))
            bytes_sent += len(data)
            if bytes_sent % (1024 * 1024) == 0:  # Printo status çdo 1MB
                print(f"Sent {bytes_sent / (1024 * 1024):.2f} MB")
        except Exception as e:
            print(f"Error sending data: {e}")
            break

    print(f"Total bytes sent: {bytes_sent / (1024 * 1024):.2f} MB")
    sock.close()

if __name__ == "__main__":
    send_udp_data(TARGET_IP, TARGET_PORT, DATA_SIZE)
