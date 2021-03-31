'''
Description: use Rabin PKS to en/decrypt
Author: p1ay8y3ar
Date: 2021-03-30 14:22:56
LastEditor: p1ay8y3ar
LastEditTime: 2021-03-31 17:23:48
Email: p1ay8y3ar@gmail.com
'''
import random
import math
import sys
import base64


class Utils:
    @staticmethod
    def gray(data):
        print("\033[37m {} \033[0m".format(data))

    @staticmethod
    def red(data):
        print("\033[31m {} \033[0m".format(data))


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
            快速幂算法 Montgomery
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
    def MBTest(num: int, r: int) -> bool:
        '''
        使用Miller-Rabin 进行多次检测
        input:
            num:tested number
            r:how round to test it
        output:
            prime:True
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
                u = PrimeTools.MBTest(prime_number, math.ceil(math.log2(bit)))
                if u:
                    break
                else:
                    prime_number = prime_number + 2 * (i)
            if u:
                return prime_number
            else:
                continue

    @staticmethod
    def myPow(x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


class PKSRabin:
    '''
    基于rabin的公钥系统，注意 public key= n, private key=p,q e=2
    '''
    p: int
    q: int
    n: int
    e = 2
    __utils = Utils()
    __is_debug = None
    tools = PrimeTools()

    def __init__(self, is_debuging=False) -> None:

        self.__is_debug = is_debuging  # 设置调试模式的日志标志

    def _debug_print(self, data, color=1) -> None:

        if self.__is_debug:
            if color == 1:
                self.__utils.gray("PKSRabin Debug--> {}".format(data))
            elif color == 2:
                self.__utils.red("PKSRabin Error--> {}".format(data))

    def keygen(self, bit=256) -> tuple:
        '''
        generate public key and private key
        input:
            bit:[option]
        output:
            tuple(p,q,n)
        '''

        self._debug_print("now starting in: {}".format(
            sys._getframe().f_code.co_name))
        while 1:

            p = self.tools.prime(bit)
            if p % 4 != 3:
                continue
            self._debug_print("find p :{}".format(p))
            break
        while 1:
            q = self.tools.prime(bit)
            if q % 4 != 3 or q == p:
                continue
            self._debug_print("find q :{}".format(q))
            break
        self.p, self.q, self.n = p, q, p * q
        self._debug_print("ready to return p:{}\n q:{}\n n:{}\n".format(
            self.p, self.q, self.n))
        return (self.p, self.q, self.n)

    def encrypt(self, pubkey, data) -> str:
        try:
            m = int(''.join([str(ord(x)) for x in list(data)]))
            print("进行转换", m)
            c = self.tools.fast_mod(m, self.e, pubkey)
            print("加密后的c", c)
        except Exception as e:
            self.__utils.red("error to encrypt,{}".format(e))
            self._debug_print(
                "{},error:{}".format(sys._getframe().f_code.co_name, e), 2)
        return base64.b32encode(str(c).encode('utf-8')).decode('utf-8')

    def decrypt(self, p, q, data) -> str:
        try:

            data = int(base64.b32decode(data.encode('utf-8')))
            print("解密后的c", data)
            n = p * q
            m_p = self.tools.fast_mod(data, (p + 1) // 4, p)
            m_q = self.tools.fast_mod(data, (q + 1) // 4, q)
            gcd, t_1, t_2 = self.tools.exEuclid(p, q)
            print(gcd, t_1, t_2)
            a = (t_1 * p * m_q + t_2 * q * m_p) % n
            b = n - a
            c = (t_1 * p * m_q - t_2 * q * m_p) % n
            d = n - c
            print(a, b, c, d)
        except Exception as e:
            print("错误", e)

    def sign():
        pass


# print(PrimeTools.euclid(42382, 100))
# print(PrimeTools.exEuclid(6, 5))
# print(PrimeTools.fast_mod(82387283, 9999999999999232399, 13))

# print(PrimeTools.modular_inverse(789, 5))
# big_p = PrimeTools.gen_big_prime(2048)
# print(big_p)
# print(PrimeTools.MBTest(PrimeTools.prime(1024), 10))
# print("进行公私钥生成")
xx = PKSRabin(is_debuging=True)
n = 7018221061760091733732578227300176401325002700414774359785301229462398414224337391052484099656308778387521412668889226698212483163837949462399856412292653
q = 97808415276944083596322722245170868319106988509057121910861925410038775898919
p = 71754777356202231425189567948224179978078430140634671157658118607008406069387
p, q, n = xx.keygen(128)
c = xx.encrypt(n, 'hello')
xx.decrypt(p, q, c)
