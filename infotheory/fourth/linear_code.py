'''
Description: Editor's info in the top of the file
Author: p1ay8y3ar
Date: 2021-05-06 15:23:28
LastEditor: p1ay8y3ar
LastEditTime: 2021-05-08 00:40:51
Email: p1ay8y3ar@gmail.com
'''

import math
import numpy as np
import itertools
import random
import json


class CodeError(Exception):
    def __init__(self):
        pass


class CodeGen:
    '''
        整体思路：
        参数：input 
            Rate:R
            n: length to encode
            P: error p
        书写思路：
            首先通过 R=k/n -> k =R*n ,k为信息位
            然后计算 m=n-k 校验位的数量
            随机生成一个生成矩阵G
    '''

    def __init__(self, R, n, P, verbose=False):
        '''
            R: 传输率
            n: 码字的长度
            p: 错误率
        '''
        self.__R = R
        self.__n = n
        self.__P = P
        self.__verbose = verbose

    def _verbose(self, data):
        if self.__verbose:
            print(data)

    def _G(self):
        '''
        生成带有单位矩阵的校验矩阵
            生成 H的策略：
                1：单位矩阵k*k
                2：生成random matrix k*(m-k)
                    i dont know is right to use random to generate a linear relationship?
                3:accroding H to Generate G
        '''
        # # first generate H
        # ident=np.identity(self._m) #校验位 Q
        # info_matrix=np.random.randint(0,2,(self._m,self._k)) # I
        # H=np.append(info_matrix,ident,axis=1)

        # dont need H ,just generate G
        i_m = np.identity(self.__m, dtype=int)
        q_m = np.random.randint(0, 2, (self.__m, self.__k), dtype=int)
        G = np.append(i_m, q_m, axis=1)
        return G.tolist()

    def _matmul(self, original_code: list, G_matrix: list) -> dict:
        '''
        使用码元*G生成码字

        output:
            dict("original":"code")
        '''
        if len(original_code) != len(G_matrix):
            raise CodeError("fail to generate code")

        r = {}
        code_t = 0
        # 先进行乘法 ,每个元素乘每行
        for g in range(len(G_matrix)):
            g_x = np.array(G_matrix[g])
            code = (original_code[g]*g_x) % 2
            code_t += code
        # 然后对结果进行取余
        code_t %= 2
        original_code = [str(i) for i in original_code]
        code_t = [str(i) for i in code_t.tolist()]
        # 返回dict列表
        r["".join(original_code)] = "".join(code_t)  # 值都是字符串，这很不好操作
        return r

    def _dmin(self, code_list) -> str:
        '''
        从列表中找出dmin，并返回这个字符串
        input: code list
        output:str,the min distacne of the e-simple
        '''

        tmp_dict = {}
        for code in code_list:
            tmp_dict[code] = code.count("1")
        return min(tmp_dict, key=tmp_dict.get)

    def _mod2add(self, str1: str, str2: str) -> str:
        '''
        bit mod2 add
        out:a new added string
        '''
        s1 = np.array([int(i) for i in list(str1)])
        s2 = np.array([int(i) for i in list(str2)])
        s = (s1+s2) % 2
        return ''.join([str(i) for i in s.tolist()])

    def _prob_calc(self, code_list):
        '''

        '''
        pass

    def run(self):
        # 求出信息为k
        self.__k = math.ceil(self.__R * self.__n)
        # 求出校验位
        self.__m = self.__n-self.__k

        # G
        self.__G = self._G()

        # generate STANDAND MATRIX

        code_list = []
        # 生成
        for block in itertools.product([0, 1], repeat=self.__k):
            code_dict = self._matmul(list(block), self.__G)
            code_list.append(code_dict)

        # 生成标准阵列
        # 先生成 n的所有组合
        e_simple_list = [''.join([str(i)for i in e])
                         for e in itertools.product([0, 1], repeat=self.__n)]
        alreay_gen_list = [list(r.values())[0] for r in code_list]
        # 剔除已经生成的
        e_simple_list = list(set(e_simple_list)-set(alreay_gen_list))

        standard_matrix = {list(r.keys())[0]: list(
            r.values()) for r in code_list}
        # 原有的code list key value 互换
        new_code_dict = {list(r.values())[0]: list(
            r.keys())[0] for r in code_list}
        # 重新排序用来适合这个序列 使000在前
        # new_code_dict = sorted(new_code_dict.items(),
        #                        key=lambda d: d[0])

        while len(e_simple_list) != 0:
            # 取出dmin，然后加到生成的码上
            min_e = self._dmin(e_simple_list)
            keys = list(new_code_dict.keys())  # 取出原本的列表
            for key in keys:
                new_c = self._mod2add(key, min_e)
                # 添加进st matrix
                standard_matrix[new_code_dict[key]].append(new_c)
                alreay_gen_list.append(new_c)
            e_simple_list = list(set(e_simple_list)-set(alreay_gen_list))
        # 然后就算生成完毕，还需要一个概率 ，应该是编码错误概率

        # 把数据吸入到json中
        code_tmp = {}
        [code_tmp.update(i) for i in code_list]
        json_dict = {}
        json_dict["k"] = self.__k
        json_dict["n"] = self.__n
        json_dict["p"] = self.__P
        json_dict["G"] = self.__G
        json_dict["code_table"] = code_tmp
        json_dict["standard_matrix"] = standard_matrix
        with open("info.json", "w") as f:
            f.write(json.dumps(json_dict))


class Coder:
    def __init__(self, k, n) -> None:
        self.__k = k
        self.__n = n

    def __s2b(self, s):
        def _convert(num):
            tmp="{0:b}".format(num)
            return "0" * (8  - len(tmp)) + tmp
        return ''.join([_convert(ord(c))for c in s])

    def encode(self, code_element, msg, p, standard_matrix):
        # 转换str为二进制形式
        msg_bin = self.__s2b(msg)
        
        # 进行加密
        pa_len = len(msg_bin)//self.__k
        
        encoded = ''
        for i in range(pa_len):
            code_block = msg_bin[i*self.__k:i*self.__k+self.__k]
            code = code_element[code_block]
            # 进行随机选取
            is_choice = random.choices([0, 1], [1-p, p])[0]
            if is_choice:
                code = random.choice(standard_matrix[code_block])
            
            encoded += code
        encoded += msg_bin[pa_len*self.__k:]
        return encoded

    def decode(self, standard_matrix, msg):
        '''
        msg 默认接收的是二进制，像"010101"
        '''
        
        # 根据n的大小进行画块
        pd_len = len(msg)//self.__n
        orginal_bin = ''
        for i in range(pd_len):
            code_block = msg[i*self.__n:i*self.__n+self.__n]
            # 最这个码进行查找
            for k in standard_matrix.keys():
                if code_block in standard_matrix[k]:
                    orginal_bin += k
                    
                    continue
        orginal_bin+=msg[pd_len*self.__n:]
        # 解码为Unicode 8个bit一组，进行分割
        v = ''
        for i in range(len(orginal_bin)//8):
            single_code = orginal_bin[i*8:i*8+8]
            
            single_code = chr(int(single_code, 2))
            v += single_code
        return v


if __name__ == "__main__":
    # a = CodeGen(0.5, 6, 0.1)
    # a.run()
    # 测试 生成和解密
    with open("info.json", "r")as f:
        json_dict = json.load(f)
        print(json_dict)

    # 进行加密
    a = Coder(json_dict["k"], json_dict["n"])
    encod = a.encode(json_dict["code_table"], msg="hello world",
                     p=json_dict["p"], standard_matrix=json_dict["standard_matrix"])
    print("---解密")
    b=a.decode(json_dict["standard_matrix"],encod)
    print(b)