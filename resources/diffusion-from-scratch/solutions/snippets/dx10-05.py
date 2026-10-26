def bucket(width, height, buckets=((1024, 1024), (1152, 896), (896, 1152), (1344, 768), (768, 1344))):
    ar = width / height
    return min(buckets, key=lambda b: abs(b[0] / b[1] - ar))
for size in [(4000, 3000), (1080, 1920), (1000, 1000), (3000, 1300)]:
    print(f"{size} (aspect {size[0] / size[1]:.2f}) -> trained in bucket {bucket(*size)}")
