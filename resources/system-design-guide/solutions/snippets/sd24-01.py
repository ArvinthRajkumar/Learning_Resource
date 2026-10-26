import math
BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz"
def encode(lat, lng, precision=7):
    lat_r, lng_r, bits, even, out, ch, n = [-90.0, 90.0], [-180.0, 180.0], [16, 8, 4, 2, 1], True, "", 0, 0
    while len(out) < precision:
        rng, val = (lng_r, lng) if even else (lat_r, lat)
        mid = (rng[0] + rng[1]) / 2
        if val >= mid: ch |= bits[n]; rng[0] = mid
        else: rng[1] = mid
        even = not even
        if n < 4: n += 1
        else: out += BASE32[ch]; ch, n = 0, 0
    return out
def haversine(a, b):
    R = 6371000
    p1, p2 = math.radians(a[0]), math.radians(b[0])
    dl, dp = math.radians(b[1] - a[1]), p2 - p1
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))
print("geohash of (57.64911, 10.40744):", encode(57.64911, 10.40744, 11), "(the standard reference is u4pruydqqvj)")
here = (37.7749, -122.4194)                       # San Francisco
print("a 5 m move keeps the 6-char cell:", encode(*here, 6) == encode(37.77494, -122.41940, 6))
for p in (4, 5, 6, 7):
    print(f"precision {p}: {encode(*here, p)}")
print("distance to Oakland:", round(haversine(here, (37.8044, -122.2712)) / 1000, 1), "km")
