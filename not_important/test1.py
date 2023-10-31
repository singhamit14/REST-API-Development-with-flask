import hashlib

string = 'Amit'

hashed_string = hashlib.sha256(string.encode('utf-8')).hexdigest()
print(hashed_string)