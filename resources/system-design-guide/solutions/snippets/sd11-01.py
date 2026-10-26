import hashlib, os
salt = os.urandom(16)
pw = b"correct horse battery staple"
slow = hashlib.scrypt(pw, salt=salt, n=2**12, r=8, p=1)
print(len(slow), "byte derived key; same input with a different salt gives:", hashlib.scrypt(pw, salt=os.urandom(16), n=2**12, r=8, p=1) != slow)
