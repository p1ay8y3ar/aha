'''
Description: Editor's info in the top of the file
Author: p1ay8y3ar
Date: 2021-04-01 14:47:38
LastEditor: p1ay8y3ar
LastEditTime: 2021-04-01 16:55:20
Email: p1ay8y3ar@gmail.com
'''

import base64
import os


class KeyUtil:
    @staticmethod
    def key_title(username, t="RABIN") -> str:
        return "---{}-{}-PUBLIC-KEY-START---".format(username, t)

    @staticmethod
    def key_end(username, t="RABIN") -> str:
        return "---{}-{}-PUBLIC-KEY-END---".format(username, t)

    @staticmethod
    def load_rabin_pub(filepath) -> tuple:
        try:
            with open(filepath, "r") as f:
                start = f.readline()
                n = f.readline()
                sign = f.readline()
                end = f.readline()
                return (start, n.replace("\n", ""), sign.replace("\n",
                                                                 ""), end)
        except Exception as e:
            print("error:{}".format(e))

    @staticmethod
    def load_rsa_pub(filepath) -> tuple:
        try:

            with open(filepath, "r") as f:
                start = f.readline()
                e = f.readline()
                n = f.readline()
                end = f.readline()
                return (start, e.replace("\n", ""), n.replace("\n", ""), end)
        except Exception as e:
            print("error:{}".format(e))

    @staticmethod
    def gen_rsa_pubkey(username, e: str, n: str, path: str) -> bool:
        try:
            with open(path, "w+") as f:
                f.write(KeyUtil.key_title(username, t="RSA"))
                f.write("\n{}".format(
                    base64.b32encode(e.encode("utf-8")).decode("utf-8")))
                f.write("\n{}".format(
                    base64.b32encode(n.encode("utf-8")).decode("utf-8")))
                f.write("\n{}".format(KeyUtil.key_end(username, t="RSA")))
                return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def gen_pub_key(username: str, n: str, sign: str, path: str) -> bool:
        '''
        generate pubkey file
        input:
            username: app user
            n:rabin public key
            sign:rabin key signed
            path: saved path
        output:
            bool: True ,False
        '''
        try:
            # if not os.path.exists(path):
            #     os.makedirs(path)
            with open(path, "w+") as f:
                f.write(KeyUtil.key_title(username))

                f.write("\n{}".format(
                    base64.b32encode(n.encode("utf-8")).decode("utf-8")))
                f.write("\n{}".format(sign))
                f.write("\n{}".format(KeyUtil.key_end(username)))
                return True
        except Exception as e:
            print("文件错误", e)
            return False
