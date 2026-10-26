def pick_rendition(throughput_kbps, ladder=((240, 400), (480, 1000), (720, 2500), (1080, 5000)), safety=0.8):
    usable = throughput_kbps * safety
    best = ladder[0]
    for res, bitrate in ladder:
        if bitrate <= usable: best = (res, bitrate)
    return best
for kbps in (300, 1200, 3000, 20000):
    res, br = pick_rendition(kbps)
    print(f"measured {kbps:>6} kbps -> play {res}p at {br} kbps")
