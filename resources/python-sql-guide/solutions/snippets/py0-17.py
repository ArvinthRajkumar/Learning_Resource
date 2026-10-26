def bad(item, bucket=[]):
    bucket.append(item)
    return bucket
print(bad(1), bad(2))          # the same list is reused!

def good(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
print(good(1), good(2))
