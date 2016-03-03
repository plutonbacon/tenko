def arp_pkt_processor(pkt, session):
    """Parse, process and record ARP packets."""

    # Protocol address of the sender of this packet
    spa = pkt.sprintf("%ARP.psrc%")

    # Protocol address of the target of this packet (if known).
    tpa = pkt.sprintf("%ARP.pdst")

    # Hardware address of the sender of this packet.
    sha = pkt.sprintf("%ARP.hwsrc%")

    # Opcode (either request or reply)
    op = pkt.sprintf("%ARP.op%")
