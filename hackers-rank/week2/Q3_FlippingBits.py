# hackers rank week2, Flipping Bits

def flippingBits(n):
    bit = list(bin(n)[2:].zfill(32))
    result = ''
    for i in range(len(bit)):
        if bit[i] == '0': result += '1'
        elif bit[i] == '1': result += '0'

    return int(result, 2)



print(flippingBits(4))
print(flippingBits(123456))
