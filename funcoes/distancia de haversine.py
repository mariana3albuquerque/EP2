import math
def haversine(r,phi1,lambda1,phi2,lambda2):
    dentro_raiz = (math.sin(math.radians((phi2-phi1)/2)))**2 + (math.cos(math.radians(phi1))*math.cos(math.radians(phi2))*(math.sin(math.radians((lambda2-lambda1)/2)))**2)
    return 2*r*math.asin(math.sqrt(dentro_raiz))