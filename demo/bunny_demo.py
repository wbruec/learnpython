import json
from serialization_demo import *

#bun = Bunny("Gandalf")
#print(bun)

#data = json.dumps(bun)

z = 1 + 3j
#print(type(z))
#print(z.real, z.imag)

num = 99

def encode_complex(anumber):
    if isinstance(anumber, complex):
        return [anumber.real, anumber.imag]
    else:
        return TypeError("only complex")

class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)

#print(encode_complex(num))

data = json.dumps(z, cls=ComplexEncoder)
print(data)

"""
def decode_complex(carray):
    return complex(carray[0], carray[1])


data2 = json.loads(data)
print(isinstance(complex(data2[0], data2[1]), complex))
"""