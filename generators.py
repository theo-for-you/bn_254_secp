from ecpy.curves import WeierstrassCurve, Point
import hashlib

order = 21888242871839275222246405745257275088548364400416034343698204186575808495617
field = 21888242871839275222246405745257275088696311157297823662689037894645226208583

curve = {
        'name':      "bn254",
        'type':      "weierstrass",
        'size':      254,
        'field':     field,
        'generator': (1,2),
        'order':     order,
        'cofactor':  1,
        'a':         0,
        'b':         3,

    }


cv = WeierstrassCurve(curve)



def get_generators(n: int):
    x = 1
    generators = [Point(x,2, cv)]
    
    while len(generators) < n:
        # x = int.from_bytes(hashlib.sha256(x.to_bytes(32)).digest()) % field
        x += 1
        y = cv.y_recover(x)
        if not y:
            continue
        generators.append(Point(x,y, cv))
        
    return generators
        

