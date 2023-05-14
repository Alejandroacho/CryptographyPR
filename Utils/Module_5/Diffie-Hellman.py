def calculate_shared_secret(p, alpha, a, b):
    # Cálculo de A y B
    A = pow(alpha, a, p)
    B = pow(alpha, b, p)

    # Cálculo del secreto compartido
    secret_A = pow(B, a, p)
    secret_B = pow(A, b, p)

    # Comprobación de que ambos cálculos son iguales
    if secret_A == secret_B:
        return secret_A
    else:
        return None

# Valores proporcionados
p = 1091
alpha = 2
a = 999
b = 724

# Cálculo del secreto compartido
shared_secret = calculate_shared_secret(p, alpha, a, b)

if shared_secret is not None:
    print("El secreto compartido es:", shared_secret)
else:
    print("No se pudo calcular el secreto compartido.")
