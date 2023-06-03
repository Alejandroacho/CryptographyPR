def interpolate_secret(shares, prime):
    secret = 0
    for i in range(len(shares)):
        xi, yi = shares[i]
        numerator = denominator = 1

        for j in range(len(shares)):
            if i != j:
                xj, _ = shares[j]
                numerator *= (-xj)
                denominator *= (xi - xj)

        inverse_denominator = pow(denominator, -1, prime)
        term = (numerator * inverse_denominator) % prime
        secret = (secret + (term * yi)) % prime

    return secret


shares = [(1080, 1732), (348, 486), (784, 1730), (1516, 2665), (334, 1835)]
prime = 2749
secret = interpolate_secret(shares, prime)
print("Secret is:", secret)

