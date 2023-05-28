#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


P_INFINITY = (None, None)


# --- IMPLEMENTATION GOES HERE -----------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed

def multiply_point(P, n, curve):
    a, b, p = curve
    Q = None
    # Duplicar el punto P de la curva n veces
    for bit in bin(n)[2:]:
        Q = uoc_AddPoints(curve, Q, Q)
        if bit == '1':
            Q = uoc_AddPoints(curve, P, Q)
    return Q
# ----------------------------------------------------------------------------



def uoc_ComputePoints(curve):
    """
    EXERCISE 1.1: Count the points on an elliptic curve
    :curve: a list with the curve values [a, b, p]
    :return: number of points on the curve
    """

    num_points = 0

    #### IMPLEMENTATION GOES HERE ####

    # We first get the values of the curve
    a = curve[0]
    b = curve[1]
    p = curve[2]
    # We add the Pinfinity point
    num_points = num_points+ 1
    # We iterate over all the possible values of p over x and y
    for x in range(p):
        for y in range(p):
            # We check if the point is on the curve by checking if
            # y^2 (mod p) = x^3 + ax + b (mod p)
            if (y * y) % p == (x * x * x + a * x + b) % p:
                # If it is, we add it to the number of points
                num_points += 1
    # --------------------------------

    return num_points



def uoc_VerifyNumPoints(curve, n):
    """
    EXERCISE 1.2: Verify group order
    :curve: a list with the curve values [a, b, p]
    :n: number of points
    :return: True if it satisfies the equation or False
    """

    result = False

    #### IMPLEMENTATION GOES HERE ####
    # We first get the values of the curve
    num_points = uoc_ComputePoints(curve)
    # We assign the result of the comparison to the variable result
    result = num_points == n
    # --------------------------------

    return result



def uoc_AddPoints(curve, P, Q):
    """
    EXERCISE 2.1: Add two points
    :curve: a list with the curve values [a, b, p]
    :P: a point as a pair (x, y)
    :Q: another point as a pair (x, y)
    :return: P+Q
    """

    # R = P+Q
    suma = None

    #### IMPLEMENTATION GOES HERE ####
    # We first get the values of the curve
    a = curve[0]
    b = curve[1]
    p = curve[2]

    if P is None:
        return Q
    if Q is None:
        return P

    # We get the values of the points
    x1 = P[0]
    y1 = P[1]
    # We get the values of the points
    x2 = Q[0]
    y2 = Q[1]

    # If one element is P_INFINITY, we return the other
    if x1 in P_INFINITY or x2 in P_INFINITY or y1 in P_INFINITY or y2 in P_INFINITY:
        return P if x2 in P_INFINITY else Q

    # We check if the points are equal
    if x1 != x2:
        # If they are, we compute the slope of the tangent line P-Q
        sc = (y2 - y1) * pow(x2 - x1, p - 2, p)
        # We compute the new x and y coordinates
        x3 = ((sc * sc) - x1 - x2) % p
        y3 = (sc * (x1 - x3) - y1) % p

    # If P = Q, we use the tangent method
    elif P == Q and y1 != 0:
        # We compute the slope of the tangent line in P
        st = (3 * x1 * x1 + a) * pow(2 * y1, p - 2, p)
        # We compute the new x and y coordinates
        x3 = ((st * st) - x1 - x2) % p
        y3 = (st * (x1 - x3) - y1) % p

    # If x1 = x2 and y1 = -y2, we return P_INFINITY
    else:
        x3 = P_INFINITY[0]
        y3 = P_INFINITY[1]

    suma = (x3, y3)
    # --------------------------------
    return suma



def uoc_SelfProductPoint(curve, n, P):
    """
    EXERCISE 3.1: Multiplication of a scalar by a point
    :curve: a list with the curve values [a, b, p]
    :n: constant to multiply
    :P: a point as a pair (x, y)
    :return: nP
    """

    # R = nP
    product = None

    #### IMPLEMENTATION GOES HERE ####
    # We first get the values of the curve
    a = curve[0]
    b = curve[1]
    p = curve[2]
    # We get the values of the point
    x = P[0]
    y = P[1]
    # We initialize the result to P_INFINITY
    product = P_INFINITY
    # We iterate over the bits of n
    for bit in bin(n)[2:]:
        # We double the point
        product = uoc_AddPoints(curve, product, product)
        # If the bit is 1, we add the point
        if bit == '1':
            product = uoc_AddPoints(curve, product, P)
    # --------------------------------
    return product



def uoc_IsGroup(curve):
    """
    EXERCISE 3.2: xxx
    :curve: check if the curve is a group
    :n: constant to multiply
    :P: a point as a pair (x, y)
    :return: nP
    """

    result = None

    #### IMPLEMENTATION GOES HERE ####
    # We first get the values of the curve
    a = curve[0]
    b = curve[1]
    p = curve[2]

    # We check if the curve is a group
    result = (4 * pow(a, 3, p) + 27 * pow(b, 2, p)) % p != 0
    # --------------------------------
    return result



def uoc_OrderPoint(curve, P):
    """
    EXERCISE 3.3: Point order
    :curve: a list with the curve values [a, b, p]
    :P: a point as a pair (x, y)
    :return: nP
    """

    point_order = None

    #### IMPLEMENTATION GOES HERE ####
    point_order = 1
    k = 1
    while k != P_INFINITY:
        point_order += 1
        k = uoc_SelfProductPoint(curve, point_order, P)
    # --------------------------------
    return point_order



def uoc_GenKey(curve, P):
    """
    EXERCISE 4.1: Generate a pair of keys
    :curve: a list with the curve values [a, b, p]
    :P: a point as a pair (x, y)
    :return: a pair of keys (pub, priv)
    """

    key = (None, None)

    #### IMPLEMENTATION GOES HERE ####
    a, b, p = curve
    # Generar un número aleatorio para la clave privada
    priv = randint(1, p-1)
    # Calcular la clave pública multiplicando el generador P por la clave privada
    pub = multiply_point(P, priv, curve)
    key = (pub, priv)
    # --------------------------------
    return key



def uoc_SharedKey(curve, priv_user1, pub_user2):

    """
    EXERCISE 4.2: Generate a shared secret
    :curve: a list with the curve values [a, b, p]
    :pub_user1: a public key
    :pub_user2: a private key
    :return: shared secret
    """

    shared = None

    #### IMPLEMENTATION GOES HERE ####
    shared = multiply_point(pub_user2, priv_user1, curve)
    # --------------------------------
    return shared
