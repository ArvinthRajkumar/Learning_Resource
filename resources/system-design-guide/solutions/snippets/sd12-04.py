def geohash_encode(lat, lon, bits=20):
    lat_lo, lat_hi, lon_lo, lon_hi = -90.0, 90.0, -180.0, 180.0
    out, even = 0, True
    for _ in range(bits):
        if even:
            mid = (lon_lo + lon_hi) / 2
            bit = lon >= mid
            lon_lo, lon_hi = (mid, lon_hi) if bit else (lon_lo, mid)
        else:
            mid = (lat_lo + lat_hi) / 2
            bit = lat >= mid
            lat_lo, lat_hi = (mid, lat_hi) if bit else (lat_lo, mid)
        out = (out << 1) | int(bit)
        even = not even
    return format(out, "0%db" % bits)

print(geohash_encode(48.8566, 2.3522))    # Paris
print(geohash_encode(48.8606, 2.3376))    # nearby, shares a long prefix
print(geohash_encode(40.7128, -74.0060))  # New York, very different prefix
