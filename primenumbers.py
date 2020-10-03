def is_prime(t):
    if t != 1:
        if t == 2:
            return True
        elif t % 2 == 0:
            return False
        else:
            for i in range(3, int(t ** (1 / 2)) + 1, 2):
                if t % i == 0:
                    return False
            return True
    else:
        return False


# function that gives the prime factors of a number

def factors(n):
	if is_prime(n):
		return n
    a = []
    for i in range(1,n//2+1):
        while is_prime(i) and n%i==0:
            a.append(i)
            n = n/i
    a = Counter(a)
    for i,j in a.items():
        print(f'{i}**{j}')
    return ''
	
	
