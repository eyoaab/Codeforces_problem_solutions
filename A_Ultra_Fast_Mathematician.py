binary1 = input()
binary2 = input()
answer =''

binary1 = list(binary1)
for i in range(len(binary1)):
    if binary1[i] != binary2[i]:
        binary1[i] = '1'
    else:
        binary1[i] = '0'

print(''.join(binary1))


