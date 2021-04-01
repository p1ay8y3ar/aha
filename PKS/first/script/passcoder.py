'''
Description: use Rabin PKS to en/decrypt
Author: p1ay8y3ar
Date: 2021-03-30 14:22:56
LastEditor: p1ay8y3ar
LastEditTime: 2021-04-01 18:36:48
Email: p1ay8y3ar@gmail.com
'''
import random
import math
import sys
import base64
import hashlib
import binascii


class Utils:
    @staticmethod
    def gray(data):
        print("\033[37m {} \033[0m".format(data))

    @staticmethod
    def red(data):
        print("\033[31m {} \033[0m".format(data))

    @staticmethod
    def num2str(num: int) -> str:
        n_bits = num.bit_length()
        n_bytes = (n_bits + 7) >> 3
        return num.to_bytes(n_bytes, "big")

    @staticmethod
    def str2num(s: str) -> int:
        return int.from_bytes(s.encode('utf-8'), "big")


class ErrorPrint(Exception):
    pass


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


class PKSRabin:
    '''
    基于rabin的公钥系统，注意 public key= n, private key=p,q e=2
    '''
    e = 2
    __utils = Utils()
    __is_debug = None
    tools = PrimeTools()

    def __init__(self, is_debuging=False) -> None:

        self.__is_debug = is_debuging  # 设置调试模式的日志标志

    def _debug_print(self, data, color=1) -> None:
        "just use for  debug"
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

    def encrypt(self, pubkey: int, data: str) -> str:
        '''
            encrypt data
            input:
                pubkey:int
                data:str
            output:
                encrypted string(as base32 encode)
        '''
        try:
            m = self.__utils.str2num(data)
            c = self.tools.fast_mod(m, self.e, pubkey)
            # print("加密后的c", c)
        except Exception as e:
            self.__utils.red("error to encrypt,{}".format(e))
            self._debug_print(
                "{},error:{}".format(sys._getframe().f_code.co_name, e), 2)
        return base64.b32encode(str(c).encode('utf-8')).decode('utf-8')

    def decrypt(self, p: int, q: int, data: str) -> str:
        '''
            decrypt messages
            input : 
                p:int ,prime
                q:int ,prime
                data:encrypted data
            output:
                decrypted  message string
        '''
        try:
            data = int(base64.b32decode(data.encode('utf-8')))

            n = p * q
            m_p = self.tools.fast_mod(data, (p + 1) // 4, p)
            m_q = self.tools.fast_mod(data, (q + 1) // 4, q)
            _, t_1, t_2 = self.tools.exEuclid(p, q)
            a = (t_1 * p * m_q + t_2 * q * m_p) % n
            b = n - a
            c = (t_1 * p * m_q - t_2 * q * m_p) % n
            d = n - c
            return self._right_m([a, b, c, d])
        except Exception as e:
            print("decrypt wrong", e)

    def _right_m(self, num_list: list) -> str:
        '''
            choice the right string from  4 result
            input:num_list:list
            output:str,the right string
        '''
        for i in num_list:
            try:
                m = self.__utils.num2str(i).decode("utf-8")
                return m
            except Exception:
                continue
        return "WRONG KEY"


class RsaSign(PKSRabin):
    __utils = Utils()

    def __init__(self, is_debuging=False) -> None:
        super(RsaSign, self).__init__(is_debuging)

    def eu_fun(self, p: int, q: int) -> int:
        """
        euler function
        """
        if self.tools.euclid(p, q) != 1:
            raise ErrorPrint("not support now")
        return (p - 1) * (q - 1)

    def k_gen(self, bit: int) -> tuple:
        p, q, _ = self.keygen(bit)
        f_n = self.eu_fun(p, q)
        # it's a prime,do not need test again
        while 1:
            e = self.tools.prime(bit)
            if self.tools.euclid(e, f_n) != 1:
                continue
            break
        d = self.tools.modular_inverse(e, f_n)
        return (p, q, e, d)

    def sign(self, d: int, p: int, q: int, msg: str) -> str:
        '''
        digital sign for message
            input:
                int,int,int,string
            output:
                string
                signature, show as b32 encoded
        '''
        digest = binascii.crc32(msg.encode('utf-8'))
        # print("哈希", digest)
        # m = self.__utils.str2num(digest)
        # print("这是m", m)
        c = self.tools.fast_mod(digest, d, p * q)
        # print("这是c", c)
        return base64.b32encode(str(c).encode('utf-8')).decode('utf-8')

    def unsign(self, e: int, n: int, signature: str) -> str:
        '''
            unsign the signature
            input:
                e:int,n:int as public key{e,n}
                signature:
                    str
            output:
                string
                sha1 digest
        '''
        # print("gg", base64.b32decode(signature.encode('utf-8')))
        c = int(base64.b32decode(signature.encode('utf-8')))
        # print("unsign c", c)
        h = self.tools.fast_mod(c, e, n)
        
        return h


class BussinessLogic:
    pass


# print(PrimeTools.euclid(42382, 100))
# print(PrimeTools.exEuclid(6, 5))
# print(PrimeTools.fast_mod(82387283, 9999999999999232399, 13))

# print(PrimeTools.modular_inverse(12, 5))
# big_p = PrimeTools.gen_big_prime(2048)
# print(big_p)
# print(PrimeTools.MBTest(PrimeTools.prime(1024), 10))
# print("进行公私钥生成")
# xx = PKSRabin(is_debuging=True)
# p, q, n = xx.keygen(512)
# c = xx.encrypt(n, 'hello my world this is a long message')
# print(xx.decrypt(p, q, c))
# rsa = RsaSign()

# p, q, e, d = rsa.k_gen(32)
# print("p", p)
# print("q", q)
# print("e", e)
# print("d", d)
# print("n", p * q)
# print(PrimeTools.modular_inverse(e, (p - 1) * (q - 1)))
# msg = Utils.str2num("hellowo")
# print("msg", msg)
# tmp = PrimeTools.fast_mod(msg, e, p * q)
# print("tmp", tmp)
# de = PrimeTools.fast_mod(tmp, d, p * q)
# print("de大小",de)
# print(Utils.num2str(de))

# print("----")
# signed = rsa.sign(d, p, q, "hello")

# unsigned = rsa.unsign(e, p * q, signed)
# print(unsigned)