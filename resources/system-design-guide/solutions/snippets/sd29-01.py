def first_byte_ms(rtt, dns=1, tcp=1, tls=1, request=1, server=20, reuse=False):
    rtts = request if reuse else dns + tcp + tls + request
    return rtts * rtt + server
for rtt in (10, 50, 100, 250):
    print(f"RTT {rtt:>3} ms: cold connection {first_byte_ms(rtt):>5} ms | reused connection {first_byte_ms(rtt, reuse=True):>4} ms | TLS 1.2 (2 RTTs) cold {first_byte_ms(rtt, tls=2):>5} ms")
