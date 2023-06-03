def get_protocol_step_3(r, base, p, b, x):
    c = pow(p,base,x)
    b = 1
    h = (r + (b*x))%(p-1)
    return h


r = 27
base = 7
p = 418
x = 599
b = 0
print(get_protocol_step_3(r, base, p, b, x))
