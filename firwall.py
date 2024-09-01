import socket
import time

# Parametrat e dërgimit
TARGET_IP = '192.168.1.100'  # Zëvendëso me IP-në që dëshiron të dërgosh
TARGET_PORT = 12345          # Zëvendëso me portin që dëshiron të dërgosh
TOTAL_SIZE = 50 * 1024 * 1024 * 1024  # 50GB në byte
SEND_DURATION = 5  # Koha për dërgim në sekonda

def send_large_udp_data(ip, port, total_size, duration):
    """Dërgon të dhëna në IP dhe port të caktuar përmes UDP për një kohë të caktuar."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Përcakto madhësinë e paketës për dërgim
    packet_size = 65507  # Maksimumi i madhësisë së paketës UDP
    num_packets = total_size // packet_size
    packets_per_second = num_packets / duration
    
    # Burim i dhënash
    data = b'x' * packet_size
    
    start_time = time.time()
    bytes_sent = 0
    
    while time.time() - start_time < duration:
        try:
            # Dërgo paketat në mënyrë të përsëritur
            for _ in range(int(packets_per_second)):
                sock.sendto(data, (ip, port))
                bytes_sent += packet_size
                if bytes_sent % (1024 * 1024 * 1024) == 0:  # Printo status çdo 1GB
                    print(f"Sent {bytes_sent / (1024 * 1024 * 1024):.2f} GB")
        except Exception as e:
            print(f"Error sending data: {e}")
            break
    
    print(f"Total bytes sent: {bytes_sent / (1024 * 1024 * 1024):.2f} GB")
    sock.close()

if __name__ == "__main__":
    send_large_udp_data(TARGET_IP, TARGET_PORT, TOTAL_SIZE, SEND_DURATION)
