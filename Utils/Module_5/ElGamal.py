import random

class ElGamal:

    def __init__(self, p: int, a: int, d: int = None):
        if not d:
            d = random.randint(2, p - 2)  # Private key
        print(self.generate_keypair(p, a, d))


    def generate_keypair(self, p: int, a: int, d: int):
        beta = pow(a, d, p)
        kpub = (p, a, beta)  # Public key
        kpriv = d
        return kpub, kpriv

def encrypt(message, p, a, beta, v = None):
    if not v:
        v = random.randint(2, p - 2)
    c1 = pow(a, v, p)
    c2 = pow(beta, v, p) * message % p
    return c1, c2

def encrypt_without_beta(message, p, a, b, v):
    return encrypt(message=message, p=p, a=a, beta=pow(a,b,p), v=v)

def decrypt(c1, c2, d, p):
    return (c2 * pow(c1, -d, p)) % p

def sign(message, p, a, d, h = None):
    if not h:
        h = random.randint(2, p - 2)
    r = pow(a, h, p)
    s = (message - d * r) * pow(h, -1, p - 1) % (p - 1)
    return r, s