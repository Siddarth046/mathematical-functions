def is_prime(t):
    if t == 2:
        return True
    elif t % 2 == 0:
        return False
    else:
        for m in range(3, int(t ** (1 / 2)) + 1, 2):
            if t % m == 0:
                return False
        return True
    

def hcf(x, y):
    while y:
        x, y = y, x % y
    return x


for _ in range(1, 1 + int(input())):
    n, l = map(int, input().split())
    encrypted_string = list(map(int, input().split()))[:l]
    alphabets = list(chr(j) for j in range(65, 91))
    prime_chars = [encrypted_string[0] // hcf(encrypted_string[0], encrypted_string[1])]
    for i in range(1, len(encrypted_string)):
        prime_chars.append(hcf(encrypted_string[i - 1], encrypted_string[i]))
    prime_chars.append(encrypted_string[-1] // hcf(encrypted_string[-1], encrypted_string[-2]))
    clan = sorted(list(set(prime_chars)))
    pangrams = {number: letter for letter, number in zip(alphabets, clan)}
    prime_chars = [pangrams[j] for j in prime_chars]
    print("Case #{0}: {1}".format(_, ''.join(prime_chars)))
