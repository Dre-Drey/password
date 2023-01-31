from passlib.hash import sha256_crypt

password = sha256_crypt.encrypt("mot2passe")
password2 = sha256_crypt.encrypt("mot2passe")
print(password)
print(password2)
print(sha256_crypt.verify("mot2passe", password))