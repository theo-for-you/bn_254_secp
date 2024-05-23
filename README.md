
# generators.py

get_generators(n)

Generates n approximately random points from bn254 generator.

# bn254.py

Converts a bn254 point from secp256k1 base point.

## Parameters

Tonelli-Shanks algorithm was taken from https://rosettacode.org/wiki/Tonelli-Shanks_algorithm 

bn254 params https://hackage.haskell.org/package/elliptic-curve-0.3.0/docs/src/Data.Curve.Weierstrass.BN254.html

secp256k1 params https://neuromancer.sk/std/secg/secp256k1

## Used libs 

- [EcPy](https://pypi.org/project/ECPy/)
