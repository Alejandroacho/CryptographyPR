from math import gcd
from random import randint

class RSA:

    def __init__(self, p: int = None, q: int = None, e: int = None) -> None:
        if not p:
            p: int = self.get_input("p")
        if not q:
            q: int = self.get_input("q")
        n: int = self.get_n(p, q)
        phi: int = self.get_phi(p, q)
        if not e:
            e: int = self.get_e(phi)
        d: int = self.get_d(e, phi)
        print(f"Kpub = ({n},{e})")
        print(f"Kpriv = {d}")

    def get_input(self, variable: str) -> int:
        while True:
            try:
                _input = int(input(f"Type the value for {variable}: "))
                break
            except:
                print("Error, please type a valid number")
        return _input

    def get_n(self, p: int, q: int) -> int:
        return p * q

    def get_phi(self, p: int, q:int) -> int:
        return (p-1)*(q-1)

    def get_e(self, phi: int):
        while True:
            random = randint(1, phi)
            if self.check_if_random_number_is_applicable(random, phi):
                return random

    def check_if_random_number_is_applicable(self, e: int, phi: int):
        return gcd(e, phi) == 1

    def get_d(self, e: int, phi: int):
        return pow(e, -1, phi)


def encrypt_RSA_message(message: int, n: int, e: int) -> int:
    return pow(message, e, n)

def decrypt_RSA_message(message: int, n: int, d: int) -> int:
    return pow(message, d, n)

def get_d(n: int, e: int) -> int:
    def calculate_phi(n: int) -> int:
        factors: list = factorize(n)
        phi_n: int = 1
        for factor in factors:
            phi_n *= (factor - 1)
        return phi_n

    def factorize(n: int) -> list:
        factors: list = []
        i: int = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    d: int = pow(e, -1, calculate_phi(n))
    return d

def decrypt_RSA_message_without_d(message: int, n: int, e: int) -> str:
    d: str = get_d(n, e)
    return decrypt_RSA_message(message, n, d)

def sign_RSA_message(message: int, n: int, d: int) -> str:
    return pow(message, d, n)
