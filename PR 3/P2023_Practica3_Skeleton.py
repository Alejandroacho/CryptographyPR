#!/usr/bin/env python3
# -*- coding: utf-8 -*-


P_INFINITY = (None, None)


# --- IMPLEMENTATION GOES HERE -----------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed

def is_quadratic_residue(n, p):
    return pow(n, (p - 1) // 2, p) == 1

def modular_sqrt(n, p):
    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)
    elif p % 8 == 5:
        v = pow(2 * n, (p - 5) // 8, p)
        i = pow(2 * n * v * v, (p - 1) // 4, p)
        return (n * v * (i - 1) // 2) % p
    else:
        # En otros casos, se puede utilizar fuerza bruta para encontrar la raíz cuadrada
        for i in range(p):
            if i * i % p == n:
                return i
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



    # --------------------------------
    return result





def uoc_OrderPoint(curve, P):
    """
    EXERCISE 3.3: Point order
    :curve: a list with the curve values [a, b, p]
    :n: constant to multiply
    :P: a point as a pair (x, y)
    :return: nP
    """

    point_order = None

    #### IMPLEMENTATION GOES HERE ####


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


    # --------------------------------
    return shared
