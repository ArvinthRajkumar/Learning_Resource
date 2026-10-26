def append_to(item, bucket=[]):
    bucket.append(item); return bucket
print(append_to(1), append_to(2), append_to.__defaults__)
def append_safe(item, bucket=None):
    bucket = [] if bucket is None else bucket
    bucket.append(item); return bucket
print(append_safe(1), append_safe(2))
