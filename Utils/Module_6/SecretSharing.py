def generate_fragments(p, polynomial, components):
    fragments = []

    for x in components:
        a = sum([polynomial[i] * (x ** i) % p for i in range(len(polynomial))]) % p
        fragments.append(a)

    return fragments


p = 1931
polynomial = [673, 806, 436]
components = [1, 2, 3, 4, 5]

fragments = generate_fragments(p, polynomial, components)
print("Fragmentos generados:", fragments)
