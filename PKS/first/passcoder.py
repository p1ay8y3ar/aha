'''
Description: use Rabin PK to en/decrypt
Author: p1ay8y3ar
Date: 2021-03-30 14:22:56
LastEditor: p1ay8y3ar
LastEditTime: 2021-03-30 17:01:06
Email: p1ay8y3ar@gmail.com
'''
import random


class PrimeTools:
    @staticmethod
    def euclid(a: int, b: int) -> int:
        '''
        gcd
        '''
        while a != 0:
            a, b = b % a, a
        return b

    @staticmethod
    def exEuclid(a: int, b: int) -> tuple:
        """
        extend euclid
        input : int， int
        output:tuple(gcd,x,y)
        """
        if b == 0:
            return (a, 1, 0)
        else:
            gcd, x_tmp, y_tmp = PrimeTools.exEuclid(b, a % b)
            x = y_tmp
            y = x_tmp - int(a / b) * y_tmp
            return (gcd, x, y)

    @staticmethod
    def modular_inverse(a: int, n: int) -> int:
        """
        xa(mod n)=1 -> x=a^-1 mod(n)
        input: a , base
        output: n
        """
        _, x, _ = PrimeTools.exEuclid(a, n)
        if x < 0:
            x += n
        return x

    @staticmethod
    def fast_mod(x: int, n: int, p: int) -> int:
        """
            快速幂算法
            x^n mod p
        """
        res = 1
        while n != 0:
            if n & 1 == 1:
                res = (res * x) % p
            n >>= 1
            x = (x * x) % p
        return res

    @staticmethod
    def MillerRabin(i: int, n: int) -> bool:
        '''
        Miller-Rabin prime test
        input: i random int to test,n:number need to be tested
        output:bool prime -True and not False
        '''
        d = n - 1
        while d != 1:
            if PrimeTools.fast_mod(i, d, n) == 1:
                if d % 2 != 0:
                    return True
                d = d // 2
                if PrimeTools.fast_mod(i, d, n) == n - 1:
                    return True
            else:
                return False
        return True

    @staticmethod
    def MBTest(num: int, r: round) -> bool:
        '''
        使用Miller-Rabin 进行多次检测
        '''
        while r > 0:
            i = random.randint(2, num - 1)
            if not PrimeTools.MillerRabin(i, num):
                return False
            r -= 1
        return True

    @staticmethod
    def gen_big_prime(size: int) -> int:
        """
        产生大质数
        generate big prime number
        input: size of length your want gen
        output:prime nubmer (not sure,should test again)
        """
        list = []
        list.append('1')
        for _ in range(size - 2):
            c = random.choice(['0', '1'])
            list.append(c)
        list.append('1')  # 最低位定为1
        res = int(''.join(list), 2)
        return res

    @staticmethod
    def prime(bit: int) -> int:
        while True:
            prime_number = PrimeTools.gen_big_prime(bit)  # 产生bit位的素数
            for i in range(50):  # 伪素数附近50个奇数都没有真素数的话，重新再产生一个伪素数
                u = PrimeTools.MBTest(prime_number, 8)  # 检验8个a来判断产生的是不是素数
                if u:
                    break
                else:
                    prime_number = prime_number + 2 * (i)
            if u:
                return prime_number
            else:
                continue


print(PrimeTools.euclid(42382, 100))
print(PrimeTools.exEuclid(6, 5))
print(PrimeTools.fast_mod(82387283, 9999999999999232399, 13))

print(PrimeTools.modular_inverse(789, 5))
big_p = PrimeTools.gen_big_prime(2048)
print(big_p)
print(PrimeTools.MBTest(PrimeTools.prime(1024), 10))
