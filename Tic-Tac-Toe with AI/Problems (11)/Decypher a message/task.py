s = input().encode()
n = sum((int(input())).to_bytes(2, 'little'))
print(''.join([chr(x + n) for x in s]))
