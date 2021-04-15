'''
Description: Editor's info in the top of the file
Author: p1ay8y3ar
Date: 2021-04-14 14:10:53
LastEditor: p1ay8y3ar
LastEditTime: 2021-04-15 23:41:39
Email: p1ay8y3ar@gmail.com
'''
import random
import math
from functools import reduce
import argparse
import os
from func_timeout import func_set_timeout
import func_timeout
from datetime import datetime


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
        产生大质数 size是10进制
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
    def Erato(num: int) -> list:
        """
        筛选出num中的所有质数
        """
        if num <= 0: return []
        # 1 从2开始，套选出所有的数字
        number_list = [i for i in range(2, num + 1)]
        # 2 剔除列表中所有2的倍数
        prime_index = 2
        index = 0
        number_list = [i for i in number_list if i % prime_index != 0]
        number_list.insert(0, 2)
        while 1:
            if math.pow(number_list[index], 2) >= num:
                break
            else:
                index += 1
                prime_index = number_list[index]
                number_list = [i for i in number_list if i % prime_index != 0]
                number_list.insert(index, prime_index)

        return number_list


class UselessGen:
    @staticmethod
    def smooth_gen(bit: int) -> tuple:
        '''
        input:
            bit: 
                bit to gen rsa ,it's binary length
                should convert to decimal length  first
        output:
            tuple
                (e,d,n)
        '''
        tools = PrimeTools()
        decimal_length = math.floor(math.log10(2**bit))
        p = tools.prime(decimal_length)
        while 1:
            q = tools.prime(decimal_length)
            if q == p: continue
            break
        f_n = (p - 1) * (q - 1)
        while 1:
            e = tools.prime(decimal_length)
            if tools.euclid(e, f_n) != 1:
                continue
            break
        d = tools.modular_inverse(e, f_n)
        return (e, d, p * q)

    @staticmethod
    def small_d_gen(bit: int) -> int:
        tools = PrimeTools()
        decimal_length = math.floor(math.log10(2**bit))
        p = tools.prime(decimal_length)
        while 1:
            q = tools.prime(decimal_length)
            if q == p: continue
            break
        f_n = (p - 1) * (q - 1)
        limit = math.floor(1 / 3 * pow(p * q, 0.25))
        # print("生成的limit,n,fn", limit, p * q, f_n)
        while 1:
            d = random.randint(2, limit)
            e = tools.modular_inverse(d, f_n)
            # print("生成 的e", e)
            if tools.euclid(e, f_n) != 1 or e > (p * q):
                continue
            break
        return (e, d, p * q)


class Factor:
    _n: int
    _e: int
    _p_tool = PrimeTools()

    def __init__(self, e: int, N: int) -> None:
        '''
        
        '''
        self._e = e
        self._n = N
        assert not self._p_tool.MBTest(
            self._n, math.ceil(math.log2(math.log2(10**len(str(self._n))))))
        Pprint.gray("receive e:{},n:{}".format(self._e, self._n))

    def pollard_p_1(self) -> tuple:
        '''
        pollard p-1 method to factor big number
        '''
        if self._n <= 2: return None

        def factorial(num: int) -> int:
            '''
            阶乘 num!
            '''
            return reduce(lambda x, y: x * y, range(1, num + 1))

        def solve(b):
            '''
            try p-1 method
            b:is base 
            '''
            k = 2
            while k < b:
                n = self._p_tool.fast_mod(b, factorial(k), self._n)
                gcd = self._p_tool.euclid(n - 1, self._n)
                if gcd != 1:
                    return gcd
                k += 1
            return -1  # don't match

        b = 2
        f = -1
        while b < self._n:
            f = solve(b)
            # Pprint.gray("solve f:{}".format(f))

            if f != -1:
                p = f
                q = int(self._n / p)
                Pprint.green("found p:{},q:{}".format(p, q))
                return (p, q)  # return value here

            b += 1
        Pprint.red("not found p,q")
        return (-1, -1)

    def pollard_rho(self):
        '''pass so slow'''
        def f(x, c):
            return (x * x - 1) % self._n

        c = random.randint(1, self._n - 2) % self._n + 1
        print('这是选择的c', c)
        t = 0
        r = 0

        while 1:
            t = f(t, c)
            r = f(f(r, c), c)
            if t == r:
                t = 0
                r = 0
                c = random.randint(1, self._n - 2) % self._n + 1

                continue
            d = abs(t - r) % self._n
            if self._p_tool.euclid(d, self._n) != 1 and self._n % d == 0:
                return (d, int(self._n / d))

    def pollard_rho_bent_circle(self, c=1):
        n = self._n
        r = 2
        limit = 10**10
        i = 1
        x = r
        y, k = r, 2
        while i < limit:
            i += 1
            x = (self._p_tool.fast_mod(x, 2, n) + c) % n
            g = self._p_tool.euclid(x - y, n)
            if 1 < g and g < n:
                Pprint.green("found p:{},q:{}".format(g, int(self._n / g)))
                return (g, int(self._n / g))
            if i == k:
                y = x
                k *= 2
        return (-1, -1)

    def wiener(self):
        '''
        wiener attack
        '''
        def continued_fra(x, y):
            '''
            求连分数
            '''
            r = []
            while y:
                r.append(int(x / y))
                x, y = y, x % y
            Pprint.gray("continued fractions list:{}".format("".join(
                str(i) for i in r)))
            return r

        def progressive_fra(x, y):
            '''
            求渐进分数
            '''
            r = []
            c_f_l = continued_fra(x, y)  #求连分数的列表

            c_f_l_len = len(c_f_l)
            for i in range(1, c_f_l_len):
                r.append(expand(c_f_l[0:i]))

            Pprint.gray("progressive fractions list:{}".format("".join(
                str(i) for i in r)))
            return r

        def expand(temp_cflist):
            tmp = temp_cflist
            tmp.reverse()
            num = 0
            denominator = 1  #分母为1
            for x in tmp:
                num, denominator = denominator, x * denominator + num
            return (num, denominator)

        def f_solve(a, b, c):
            '''
            ax^2 +bx + c = 0
            '''
            # p = math.pow(b * b - 4 * a * c, 0.5)
            p = (b * b - 4 * a * c)**0.5
            return (-b + p) / (2 * a), (-b - p) / (2 * a)

        r = progressive_fra(self._e, self._n)

        for (d, k) in r:
            if k == 0: continue
            if (self._e * d - 1) % k != 0: continue
            phi = (self._e * d - 1) / k
            p, q = f_solve(1, self._n - phi + 1, self._n)
            if p * q == self._n:
                Pprint.green("found p:{},q:{}".format(int(abs(p)),
                                                      int(abs(q))))

                return (int(abs(p)), int(abs(q)))  #返回找到的值

    def franklin_reiter(self):
        plaintext = random.randint(2, self._n - 2)  #有点傻，随机生成一个吧
        Pprint.green("pick a random message:{}".format(plaintext))
        r = 2
        a = 1
        plaintext2 = plaintext * a + r  # m2=f(m1) f=ax+b

        #进行加密
        cipher1 = self._p_tool.fast_mod(plaintext, 3, self._n)
        Pprint.gray("encrytped message:{}".format(cipher1))
        cipher2 = self._p_tool.fast_mod(plaintext2, 3, self._n)

        # attack
        f = r * (cipher2 + 2 * (a**3) * cipher1 - r**3) % self._n
        Pprint.gray("attack f:{}".format(f))
        g = a * (cipher2 - a**3 * cipher1 + 2 * r**3) % self._n
        Pprint.gray("attack g:{}".format(g))

        gi = self._p_tool.modular_inverse(g, self._n)
        Pprint.gray("attack gi:{}".format(gi))
        m = f * gi % self._n
        Pprint.green("recovery message:{}".format(m))

    def iter_attack(self):
        m = random.randint(1, self._n - 2)
        c = self._p_tool.fast_mod(m, self._e, self._n)
        p = self._p_tool.euclid(abs(c - m), self._n)
        while p == 1:
            c = self._p_tool.fast_mod(c, self._e, self._n)
            p = self._p_tool.euclid(abs(c - m), self._n)

        Pprint.green("found p:{},q:{}".format(p, int(self._n / p)))


class Pprint:
    @staticmethod
    def green(data):
        print("\033[32m{}>>>>>>>>{} \033[0m".format(datetime.now(), data))

    @staticmethod
    def gray(data):
        print("\033[37m{}>>>>>>>>{} \033[0m".format(datetime.now(), data))

    @staticmethod
    def red(data):
        print("\033[31m{}>>>>>>>>{} \033[0m".format(datetime.now(), data))


class Logic:
    def p1g_run(self, timeout, bit):
        @func_set_timeout(timeout)
        def p1g_go(bit):
            try:
                e, d, n = UselessGen.smooth_gen(bit)
                Pprint.green(" e :{}, d: {}, n:{} \n".format(e, d, n))
                Pprint.gray("now attack n:{} use pollard p-1 method".format(n))
                f = Factor(e, n)
                f.pollard_p_1()

            except func_timeout.exceptions.FunctionTimedOut:
                Pprint.red("timeout exiting...")
                os._exit(0)

        p1g_go(bit)

    def wg_run(self, timeout, bit):
        @func_set_timeout(timeout)
        def wg_go(bit):
            try:
                e, d, n = UselessGen.small_d_gen(bit)
                Pprint.green(" e :{}, d: {}, n:{} \n".format(e, d, n))
                Pprint.gray("now attack n:{} use wenier.attack".format(n))
                f = Factor(e, n)
                f.wiener()
            except func_timeout.exceptions.FunctionTimedOut:
                Pprint.red("timeout exiting...")
                os._exit(0)

        wg_go(bit)

    def p1_run(self, timeout, e, n):
        @func_set_timeout(timeout)
        def p1_go(e, n):
            try:
                f = Factor(e, n)
                f.pollard_p_1()
            except func_timeout.exceptions.FunctionTimedOut:
                Pprint.red("timeout exiting...")
                os._exit(0)

        p1_go(e, n)

    def rho_run(self, timeout, e, n):
        @func_set_timeout(timeout)
        def rho_go(e, n):
            try:
                f = Factor(e, n)
                f.pollard_rho_bent_circle()
            except func_timeout.exceptions.FunctionTimedOut:
                Pprint.red("timeout exiting...")
                os._exit(0)

        rho_go(e, n)

    def w_run(self, timeout, e, n):
        @func_set_timeout(timeout)
        def w_go(e, n):
            try:
                f = Factor(e, n)
                f.wiener()
            except func_timeout.exceptions.FunctionTimedOut:
                Pprint.red("timeout exiting...")
                os._exit(0)

        w_go(e, n)

    def iter_run(self, timeout, e, n):
        @func_set_timeout(timeout)
        def iter_go(e, n):
            try:
                f = Factor(e, n)
                f.iter_attack()
            except func_timeout.exceptions.FunctionTimedOut:
                Pprint.red("timeout exiting...")
                os._exit(0)

        iter_go(e, n)

    def f_run(self, timeout, e, n):
        @func_set_timeout(timeout)
        def f_go(e, n):
            try:
                f = Factor(e, n)
                f.franklin_reiter()
            except func_timeout.exceptions.FunctionTimedOut:
                Pprint.red("timeout exiting...")
                os._exit(0)

        f_go(e, n)

    def command_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-e", type=int, help="public e")
        parser.add_argument("-n", type=int, help='public n')
        parser.add_argument("-b", type=int, help='bits length')
        parser.add_argument("-t", type=int, help='time in seconds')
        parser.add_argument("-p1",
                            action='store_true',
                            help="pollard p-1 factor n")
        parser.add_argument("-rho",
                            action='store_true',
                            help="pollard rho facotr (use brent)")
        parser.add_argument("-w", action='store_true', help="wiener")
        parser.add_argument("-iter", action='store_true', help="iter attack")
        parser.add_argument("-f", action='store_true', help="franklin reiter")
        parser.add_argument("-p1g",
                            action='store_true',
                            help="pollard p-1 test")
        parser.add_argument("-wg", action='store_true', help="wiener test")
        args = parser.parse_args()

        if not args.t:
            Pprint.red("please set time limit use -t in seconds")
            os._exit(0)

        if (args.p1g and args.wg) and (not args.e or args.n):
            Pprint.red("please make sure to input e and n or choose test mode")
            os._exit(0)
        Pprint.red("mission start")
        if args.p1g:

            self.p1g_run(args.t, args.b)
        elif args.wg:

            self.wg_run(args.t, args.b)
        elif args.p1:
            self.p1_run(args.t, args.e, args.n)
        elif args.rho:
            self.rho_run(args.t, args.e, args.n)
        elif args.w:
            self.w_run(args.t, args.e, args.n)
        elif args.iter:
            self.iter_run(args.t, args.e, args.n)
        elif args.f:
            self.f_run(args.t, args.e, args.n)


if __name__ == "__main__":

    Logic().command_parser()