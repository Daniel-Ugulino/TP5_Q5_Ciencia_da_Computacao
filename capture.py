from scapy.all import sniff, wrpcap

PORTA = 8443
ARQUIVO = 'captura.pcap'
QUANTIDADE = 20

pacotes = sniff(
    filter=f"tcp port {PORTA}",
    count=50,
    iface="lo"
)

print(f"{len(pacotes)} pacotes capturados")
wrpcap('captura.pcap', pacotes)
