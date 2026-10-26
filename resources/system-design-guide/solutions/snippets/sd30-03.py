service_ms = 10                                    # time to process one request
for util in (0.3, 0.5, 0.7, 0.8, 0.9, 0.95, 0.99):
    response = service_ms / (1 - util)
    print(f"utilisation {util:>4.0%}: average response {response:>7.1f} ms ({response / service_ms:>5.1f}x the service time)")
