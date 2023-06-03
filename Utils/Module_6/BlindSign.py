def blind_sign_with_rsa(r, eB, nB, dB, m):
    t = pow(r, eB, nB)
    _m = pow(m*t, 1, nB)
    s_ = pow(_m, dB, nB)
    return s_


nA = 21971
eA = 4019
dA = 3683

nB = 21079
eB = 18089
dB = 17977

r = 19213

m = 17678

second_step = blind_sign_with_rsa(r, eB, nB, dB, m)
print("Second step:", second_step)