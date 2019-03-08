import math, time
from multiprocessing import Pool

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    for num in PRIMES:
        print('%d is prime: %s' % (num, is_prime(num)))

def main1():
    pool = Pool(3)
    res_l = []
    for prime  in PRIMES:
        res = pool.apply_async(func=is_prime, args=(prime,))
        res_l.append(res)
    pool.close()
    pool.join()
    for num, prime in zip(PRIMES, res_l):
        print('%d is prime: %s' % (num, prime.get()))

if __name__ == '__main__':
    t1 = time.time()
    main1()
    t2 = time.time()
    print('运行时间:', t2 - t1)

