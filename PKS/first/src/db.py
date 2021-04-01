'''
Description: Editor's info in the top of the file
Author: p1ay8y3ar
Date: 2021-03-31 21:52:24
LastEditor: p1ay8y3ar
LastEditTime: 2021-04-01 18:46:48
Email: p1ay8y3ar@gmail.com
'''
from script import passcoder
from peewee import *
from datetime import datetime
import os
import time


def convert_path(path: str) -> str:
    return path.replace(r'\/'.replace(os.sep, ''), os.sep)


db = SqliteDatabase(os.getcwd() + convert_path("/homework1.sqlite"))


class User(Model):
    username = CharField(verbose_name="username")
    pwd = CharField(verbose_name="username's pasword")
    rabin_p = CharField(max_length=5000, verbose_name="rabin p")
    rabin_q = CharField(max_length=5000, verbose_name="rabin q")
    rsa_p = CharField(max_length=5000, verbose_name="rsa p")
    rsa_q = CharField(max_length=5000, verbose_name="rsa q")
    rsa_e = CharField(max_length=5000, verbose_name="rsa e")
    rsa_d = CharField(max_length=5000, verbose_name="rsa e")

    class Meta:
        database = db


def xor_allkey(username):
    user = User.user = User.select().where(User.username == username).get()
    pwd2num = passcoder.Utils.str2num(user.pwd)
    return (int(user.rabin_p) ^ pwd2num, int(user.rabin_q) ^ pwd2num,
            int(user.rsa_p) ^ pwd2num, int(user.rsa_q) ^ pwd2num,
            int(user.rsa_e) ^ pwd2num, int(user.rsa_d) ^ pwd2num)


db.connect()
db.create_tables([User])
