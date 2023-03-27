phi = 22/7

#volume 3 Dimensi
def kubus(s):
    return s*s*s

def balok(p,l,t):
    return p*l*t

def tabung(r,t):
    return phi*r*r*t

def kerucut(r,t):
    return 1/3*phi*r*r*t

def limas(l_alas,t):
    return 1/3*l_alas*t

def prisma(l_alas,t):
    return l_alas*t

#luas 2 Dimensi
def persegi(s):
    return s*s

def p_panjang(p,l):
    return p*l

def segitiga(a,t):
    return 1/2*a*t

def lingkaran(r):
    return phi*r*r

def jajargenjang(a,t):
    return a*t

def trapesium(a,b,t):
    return 1/2*t(a+b)