from scapy.all import rdpcap
from scapy.layers.inet import IP, TCP

ARQUIVO = 'captura.pcap'

pacotes = rdpcap(ARQUIVO)
print(f"Total de pacotes: {len(pacotes)}\n")
print(f"{'#':<5} {'IP Origem':<18} {'IP Destino':<18} {'Porta Orig':<12} {'Porta Dest':<12} {'Flags':<10} {'Tamanho'}")

for i, pkt in enumerate(pacotes):
    if IP in pkt and TCP in pkt:
        ip  = pkt[IP]
        tcp = pkt[TCP]

        flags_map = {
            'F': 'FIN', 'S': 'SYN', 'R': 'RST',
            'P': 'PSH', 'A': 'ACK', 'U': 'URG'
        }
        flags = ','.join(nome for bit, nome in flags_map.items() if bit in str(tcp.flags))

        print(f"{i+1:<5} {ip.src:<18} {ip.dst:<18} {tcp.sport:<12} {tcp.dport:<12} {flags:<10} {len(pkt)} bytes")