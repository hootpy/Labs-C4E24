def is_inside(a,b):
    s1 = b[3]*abs(a[0]-b[0])
    s2 = b[3]*abs(b[0]+b[2]-a[0])
    s3 = b[2]*abs(a[1]-b[1])
    s4 = b[2]*abs(b[1]+b[3]-a[1])
    s = b[3]*b[2]
    if s1 + s2 + s3 + s4 == 2*s:
        return True
    else:
        return False