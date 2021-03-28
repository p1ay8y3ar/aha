'''
Description: first and second homework of InfoTheory
             Due time is  4/4
Author: p1ay8y3ar
Date: 2021-03-28 15:27:36
LastEditor: p1ay8y3ar
LastEditTime: 2021-03-28 23:56:31
Email: p1ay8y3ar@gmail.com
'''

from math import log2 as Lb
from math import log, ceil
from fractions import Fraction as Fr
from functools import reduce
import operator
import random, time, sys, json, os
import keyboard
SyC = random.choices  #symbol choice according probability
import argparse


class ProbError(Exception):
    pass


class ErrorPrint(Exception):
    pass


class Entropy:
    def __init__(self, problist) -> None:
        self.__pl = problist

    def __probcheck(self, infomodel) -> bool:
        """
            Normalization detection
            input:infomodel- src of info
            output: bool
                True:sum=1
                False:other reason
        """
        num = 0
        value_list = infomodel
        if isinstance(infomodel, dict):
            value_list = list(infomodel.values())

        for v in value_list:
            num += float(Fr(v))
        if not num or num != 1.0:
            return False
        return True

    def calc(self):
        '''
            calc entropy of seq
            return H
        '''
        if not self.__probcheck(self.__pl):
            raise ProbError("sum of prob !=1")
        if isinstance(self.__pl, list):
            return sum([-(Fr(i) * Lb(Fr(i))) for i in self.__pl])
        elif isinstance(self.__pl, dict):
            return sum(
                [-(Fr(i) * Lb(Fr(i))) for i in list(self.__pl.values())])


class Utils:
    @staticmethod
    def DecToHexString(num: int) -> str:
        '''
            convert decimal to  hex string
            like int(8) to "1000"
            input: number in decimal
            output: string
        '''
        return "{0:b}".format(num)

    @staticmethod
    def prod(factors: list) -> float:
        '''
        multiplication
        '''
        return reduce(operator.mul, factors, 1)

    @staticmethod
    def flush_print(data):
        print("\r{0}".format(data), end="")

    @staticmethod
    def gray(data):
        return ("\033[37m {} \033[0m".format(data))

    @staticmethod
    def red(data):
        return ("\033[31m {} \033[0m".format(data))

    @staticmethod
    def kb_listener(x):

        if x.name == "q":

            os._exit(0)


class Practice2:
    c_ent: Entropy = None  # inner class target of Entropy

    def __bruteforce_seq(self, R: float, eps: float, InfoModel: dict) -> list:
        '''
            how elegant to find N-th extend seq really is a problem
            return list
        '''
        N_th = 1
        while N_th:
            r = []
            for i in range(2**N_th):
                itoHexSting = Utils.DecToHexString(i)
                # maybe is a fixed source without considered time
                if abs(-Lb(
                        Fr(InfoModel["1"])**itoHexSting.count("1") *
                        Fr(InfoModel["0"])**(N_th - itoHexSting.count("1"))) /
                       N_th - self.c_ent.calc()) < eps:
                    r.append(i)
            t = [Utils.DecToHexString(i) for i in r]
            prob = []
            for i in range(len(t)):
                prob.append(Utils.prod([Fr(InfoModel[x]) for x in t[i]]))
            if sum(prob) > 1 - (R - self.c_ent.calc()):

                return r
            else:
                N_th += 1

    def __codelen(self, q: int, len: int) -> int:
        '''
            find code length and gen encoded code
            q**l<N
            input:
                q: q-ary
                len:len of seq
            output:
                code length :l
        '''
        return ceil(log(len, q))

    def __generator(self, seqlen: int, q: int, codelen: int) -> list:
        '''
            Non-singular encoding with code length in q-ary
            input:
                seqlen:
                    len of seq
                q:
                    q-ary
                codelen:
                    code length
            output: list, new code
        '''
        r = []
        for i in range(seqlen):
            tmp = i
            s = ''
            for _ in range(codelen):
                s = str(tmp % q) + s
                tmp //= q
            r.append(s)
        return r

    def AutoFixedLCodeGen(self, R: float, eps: float, q: int,
                          infomodel: dict) -> dict:
        '''
            according esp to  bruteforce the epslion typical seqs
            then  covert to q-ary encoding
            input:
                R  : info coding rate
                esp:
                q:  q-ary
            return:
                typical seq and new encods
        '''
        self.c_ent = Entropy(infomodel)
        seq = self.__bruteforce_seq(R, eps, infomodel)
        codelen = self.__codelen(q, len(seq))
        code = self.__generator(len(seq), q, codelen)
        return {'seq': seq, 'code': code}


class CodeGen:
    def __init__(self, d: dict) -> None:
        self._json_dict = d

    def gen(self, N=None, model=True):
        '''
        code generator

        '''
        source = self._json_dict["source"]
        if False in [x in self._json_dict["switches"] for x in source]:
            raise ErrorPrint("please check your json file")
        count = 0
        if N:
            s = ''
        while N if N else True:
            switcher = source[count % len(source)]
            switch = self._json_dict["switches"][switcher]
            coin_number = SyC(list(switch.keys()),
                              weights=[Fr(x) for x in list(switch.values())],
                              k=1)
            code = SyC(list(self._json_dict["models"][coin_number[0]].keys()),
                       weights=[
                           Fr(x) for x in list(self._json_dict["models"][
                               coin_number[0]].values())
                       ],
                       k=1)
            if model:
                print(code[0], end='')
                sys.stdout.flush()
            count += 1
            if N:
                s += code[0]
                N -= 1
                if N == 0: break

            time.sleep(0.2)
        return s


def main():
    '''
    arg parser
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-hw", type=int, help="which homework")
    parser.add_argument("-topic", type=int, help='which topic')
    parser.add_argument("-r", type=float, help="coding rate")
    parser.add_argument("-eps", type=float)
    parser.add_argument("-q", type=int, help="q-ary")
    parser.add_argument("-n", type=int, help="number of seq")
    parser.add_argument("-seq", nargs="+")
    args = parser.parse_args()

    def json_data():
        with open("sample.json") as f:
            return json.load(f)

    if not args.hw:
        raise ErrorPrint("must select which homework")
    jd = json_data()

    if args.hw == 1:
        l = random.choice(list(jd['models'].keys()))
        if args.topic == 1:
            print(Utils.gray("selected source :{}-{}".format(
                l, jd['models'][l])),
                  end="\t")
            print(Utils.red("H:{}".format(Entropy(jd['models'][l]).calc())))
        elif args.topic == 2:
            R = args.r
            eps = args.eps
            q = args.q
            if not R or not eps or not q:
                raise ErrorPrint("use -r -eps -q to make all args are entered")
            print(
                Utils.gray("selected source :{}-{}".format(l,
                                                           jd['models'][l])))

            r = Practice2().AutoFixedLCodeGen(R, eps, q, jd['models'][l])
            print(Utils.red("{}".format(r)))
        else:
            raise ErrorPrint("Unknow topic number")
    elif args.hw == 2:
        if args.topic == 1:
            N = args.n
            if not N:
                keyboard.hook(Utils.kb_listener)
                # keyboard.wait()
            if N and N < 0: raise ErrorPrint("N should >0")
            CodeGen(jd).gen(N)
        elif args.topic == 2:
            seq = args.seq
            if len(seq) == 0: raise ErrorPrint("seq should not less than 1")
            seq = "".join(seq)

            N = args.n
            if not N or N < 0:
                raise ErrorPrint("need input N,use '-n' ")
            s = CodeGen(jd).gen(N, False)
            tmp_p = s.count("1") / N
            print(Utils.gray("random code seq is:{},'1':{},'0':{}".format(s,tmp_p,(1-tmp_p))))
            print(
                Utils.red("probability:{}".format(tmp_p**seq.count('1') *
                                                  (1 - tmp_p)**seq.count('0'))))
        else:
            raise ErrorPrint("Unknow topic number")
    else:
        raise ErrorPrint("number overflow")


if __name__ == "__main__":
    main()
