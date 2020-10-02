from itertools import combinations


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


def list_of_primes(end, start=2):
    """Returns a list of primes till end integer,
with a start value"""
    answer = [i for i in range(start, end + 1) if is_prime(i)]
    return answer


def powerset(se):
    """se can be a 1-D set or a list
"""
    ans = []
    for i in range(len(se) + 1):
        ans.extend(list(combinations(se, i)))
    ans = list(map(set, ans))
    return ans


o = int(input())
queries = list(map(int, input().split()))[:o]
for n in queries:
    count = 0
    poweset_of_primes_till_n = powerset(list_of_primes(n))
    for t in poweset_of_primes_till_n:
        if is_prime(sum(t)):
            count += 1
    print(count, end=' ')
