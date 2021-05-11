'''
Description: Editor's info in the top of the file
Author: p1ay8y3ar
Date: 2021-05-11 11:46:56
LastEditor: p1ay8y3ar
LastEditTime: 2021-05-11 20:07:10
Email: p1ay8y3ar@gmail.com
'''
import math
import random
from func_timeout import func_set_timeout
import func_timeout
from datetime import datetime, time


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
    def p_root(p):
        # 求p的本原元（原根）
        k = (p-1)//2
        for i in range(2, p-1):
            if PrimeTools.fast_mod(i, k, p) != 1:
                return i

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
        if num <= 0:
            return []
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


class Factor:
    @staticmethod
    def factor_with_count(n):
        '''
        对一个数进行分解，比如40={2:3,5:1}
            40/2/2/2/5=1
        '''
        divider_seed = 2
        factor_list = []

        while divider_seed < math.sqrt(n):
            if n % divider_seed == 0:
                factor_list += [divider_seed]
                n //= divider_seed
            else:
                divider_seed += 1
        factor_list += [n]
        return sorted([(divider, factor_list.count(divider)) for divider in set(factor_list)], key=lambda x: x[0])


class WeakGamalPubKeyGen:
    def gen(self, n: int) -> tuple:
        '''
        产生一个脆弱的gamal
            h=g^x mod q
            g root
            q prime
        input:
            n:length of q
        output:
            tuple(h,g,q)
        代码生产思路
            1：首先生成一个质数q
            2：求这是质数的本原根
            3：然后 随机选一个 1<x<q-1
            4:求出h
        '''

        # 生成一个质数
        p = PrimeTools.prime(bit=n)
        # 产生本原
        a = PrimeTools.p_root(p)
        # 选择一个随机的x
        x = random.randint(1, p-1)
        # 计算得出h
        h = PrimeTools.fast_mod(a, x, p)

        return (h, a, p)


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


class Attacker:

    def Babystep_Giantstep(self, h, g, p, timeout: int, verbose=False):

        @func_set_timeout(timeout)
        def run():
            # if not PrimeTools.MillerRabin(p, math.ceil(math.log2(p))):
            #     Pprint.red(" p is not prime")
            #     raise "P is not prime"
            if verbose:
                Pprint.green(
                    "runing babystep-gaintstep algo,solving x for {}^x={}mod{}".format(g, h, p))
            # phi(p) is p-1 if p is prime
            m = math.ceil(math.sqrt(p-1))
            if verbose:
                Pprint.gray("Babystep_Giantstep:√p-1={}".format(m))
            # dict for g^(1...m) modp
            b_dict = {PrimeTools.fast_mod(g, i, p): i for i in range(m)}
            if verbose:
                Pprint.gray("Babystep_Giantstep:build dict:{}".format(b_dict))

            # 根据费马小定理 fm.l.t
            c = PrimeTools.fast_mod(g, m*(p-2), p)

            # 进行 搜索
            for i in range(m):
                y = (h*PrimeTools.fast_mod(c, i, p)) % p
                if verbose:
                    Pprint.gray("Babystep_Giantstep:trying {}".format(y))
                if y in b_dict:
                    if verbose:
                        Pprint.green(
                            "Babystep_Giantstep:found it x={}".format(i*m+b_dict[y]))
                    return i*m+b_dict[y]
            return -1
        return run()

    def pohilg_hellman(self, h, g, p, timeout):

        @func_set_timeout(timeout)
        def run_crt(h, g, p, timeout):
            factors = Factor.factor_with_count(p-1)
            a = []
            for (p_i, e_i) in factors:
                p_e = p_i ** e_i
                o = p_e-1
                Pprint.gray("{}=mod{}^{}".format(p_e, p_i, e_i))
                l = []
                a_i = 0
                for k in range(e_i):
                    base = PrimeTools.fast_mod(g, (p-1)//p_i, p)
                    t_exp = 0
                    for i in range(k):
                        t_exp += l[i]*p_i**i
                    tmp_base = PrimeTools.fast_mod(g, (p-1)//(p_i**(k+1)), p)
                    tmp_power = PrimeTools.fast_mod(tmp_base, t_exp, p)
                    tmp_power = PrimeTools.modular_inverse(tmp_power, p)
                    power = (PrimeTools.fast_mod(
                        h, (p-1)//(p_i**(k+1)), p)*tmp_power) % p

                    # bsgs
                    lk = self.Babystep_Giantstep(
                        power, base, p, timeout=timeout//len(factors))
                    l.append(lk)
                    a_i += lk * p_i ** k
                    Pprint.gray('\tFound l_{} = {}'.format(k, lk))
                a.append(a_i)
                print('alpha for p_i {} = {}'.format(p_i, a_i))

            # CRT
            x = 0
            for i in range(len(factors)):
                p_i, e_i = factors[i]
                p_e = p_i ** e_i
                product = a[i]
                for j in range(len(factors)):
                    if j == i:
                        continue
                    p_e_j = factors[j][0] ** factors[j][1]
                    product *= p_e_j * PrimeTools.modular_inverse(p_e_j, p_e)
                    product %= (p-1)
                x += product
                x %= (p-1)

            Pprint.green("pohilg_hellman,found x={}".format(x))
            return x
        return run_crt(h, g, p, timeout=timeout)

    def pollard_rho_cosper_circle(self, h, g, p, timeout):
        '''
        this is  a reference code,ill today, give up to write from 0
        '''
        
        return run(h, g, p)


if __name__ == "__main__":
    y, g, p = WeakGamalPubKeyGen().gen(20)
    print(y, g, p)
    print(Attacker().Babystep_Giantstep(y, g, p, 100))
    print(Attacker().pohilg_hellman(y, g, p, 100))
    print(Attacker().pollard_rho_cosper_circle(y, g, p, 100))
