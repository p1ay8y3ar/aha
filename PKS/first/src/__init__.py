'''
Description: Editor's info in the top of the file
Author: p1ay8y3ar
Date: 2021-03-31 21:38:57
LastEditor: p1ay8y3ar
LastEditTime: 2021-04-01 19:07:03
Email: p1ay8y3ar@gmail.com
'''

from PyQt5.QtCore import QFile, QFileInfo
from PyQt5.QtWidgets import QMainWindow, QWidget, QMessageBox, QFileDialog
from src import pks_login
from src import pks_text_editor
from src import pks_user
from src import pks_signup
from src import key_verify
from src.db import User, convert_path, xor_allkey
from script import passcoder
from src.key_util import KeyUtil
import hashlib
import os
import base64
import binascii
import datetime


class LoginWindow(QWidget, pks_login.Ui_pks_login):
    """
    登陆界面
    """
    db_user = User  # sqllite3

    def __init__(self):
        QWidget.__init__(self)
        pks_login.Ui_pks_login.__init__(self)
        self.setupUi(self)

        # 设置槽函数
        self.bt_login.clicked.connect(self.login)
        self.bt_signup.clicked.connect(self.signup)
        self.rw = RegisterWin()
        # self.u_i = UserInterface()

    def login(self):
        username = self.le_username.text()
        password = self.le_password.text()
        if len(username) == 0 or len(password) == 0:
            self.showmsg("account or password wrong")
            return
        if self.db_user.select().where(
                self.db_user.username == username).count() == 0:
            self.showmsg("account or password wrong")
            return
        password_md5 = hashlib.md5(password.encode("utf-8")).hexdigest()

        user_db = self.db_user.select().where(
            self.db_user.username == username).get()

        if user_db.pwd != password_md5:
            self.showmsg("account or password wrong")
            return
        # login  success
        self.user_interface(username)
        self.close()

    def signup(self):
        self.rw.show()

    def user_interface(self, username):
        self.u_i = UserInterface(username)
        self.u_i.show()

    def showmsg(self, data):
        QMessageBox.information(self, "Note", data)


class RegisterWin(QWidget, pks_signup.Ui_RegisterUI):
    def __init__(self):
        QWidget.__init__(self)
        pks_signup.Ui_RegisterUI.__init__(self)
        self.setupUi(self)
        self.bt_register.clicked.connect(self.sign)

    def showmsg(self, data):
        QMessageBox.information(self, "Note", data)

    def sign(self):
        username = self.le_username.text()
        password = self.le_pwd.text()
        password2 = self.le_pwd_again.text()
        if len(username) < 8 or len(password) < 8 or len(password2) < 8:
            self.showmsg("length not enough")
            return
        # username = username.replace(" ", "")
        # password = password.replace(" ", "")
        # password2 = password2.replace(" ", "")
        if password != password2:
            self.showmsg("password do not match")
            return
        # 判断库里是不是有重复的

        if User.select().where(User.username == username).count() != 0:
            self.showmsg("username already registered")
            return
        pwd_md5 = hashlib.md5(password.encode("utf-8")).hexdigest()
        pwd2num = passcoder.Utils.str2num(pwd_md5)  # convert string to num

        # 生成rabin公私钥
        rabin = passcoder.PKSRabin()
        rabin_p, rabin_q, rabin_n = rabin.keygen(512)

        # 使用用户的账号的密码进行保护
        rabin_xor_p = rabin_p ^ pwd2num
        rabin_xor_q = rabin_q ^ pwd2num
        # 生成rsa公私钥
        rsa_sign = passcoder.RsaSign()
        sign_p, sign_q, sign_e, sign_d = rsa_sign.k_gen(32)
        sign_xor_p = sign_p ^ pwd2num
        sign_xor_q = sign_q ^ pwd2num
        sign_xor_e = sign_e ^ pwd2num
        sign_xor_d = sign_d ^ pwd2num
        try:
            # create user
            User.create(username=username,
                        pwd=pwd_md5,
                        rabin_p=str(rabin_xor_p),
                        rabin_q=str(rabin_xor_q),
                        rsa_p=str(sign_xor_p),
                        rsa_q=str(sign_xor_q),
                        rsa_e=str(sign_xor_e),
                        rsa_d=str(sign_xor_d))
            self.le_username.setText("")
            self.le_pwd.setText("")
            self.le_pwd_again.setText("")
            self.showmsg("register success,close and return to  login")
        except Exception as e:
            self.showmsg("register failed:{}".format(e))
            return


class KeyVerify(QWidget, key_verify.Ui_Verify):
    def __init__(self):
        QWidget.__init__(self)
        key_verify.Ui_Verify.__init__(self)
        self.setupUi(self)
        self.bt_load_rabin.clicked.connect(self.load_rabin)
        self.bt_load_rsa.clicked.connect(self.load_rsa)
        self.bt_verify.clicked.connect(self.verify)

    def load_rsa(self):
        pub_key_path, _ = QFileDialog.getOpenFileName(self,
                                                      "open public key file",
                                                      r"./", "TXT(*.pub_rsa)")
        self.pub_rsa = pub_key_path

    def load_rabin(self):
        pub_key_path, _ = QFileDialog.getOpenFileName(self,
                                                      "open public key file",
                                                      r"./",
                                                      "TXT(*.pub_rabin)")
        self.pub_rabin = pub_key_path

    def showmsg(self, data):
        QMessageBox.information(self, "Note", data)

    def verify(self):
        if not os.path.exists(self.pub_rabin) or not os.path.exists(
                self.pub_rsa):
            self.showmsg("file not exists")
            return
        # load ras public key file
        rsa_start, rsa_e, rsa_n, rsa_end = KeyUtil.load_rsa_pub(self.pub_rsa)
        if "RSA-PUBLIC-KEY-START" not in rsa_start or "RSA-PUBLIC-KEY-END" not in rsa_end:
            self.showmsg("rsa pubkey file format not match")
            return

        # load rabin public key file
        rabin_start, rabin_n, rabin_sign, rabin_end = KeyUtil.load_rabin_pub(
            self.pub_rabin)
        if "RABIN-PUBLIC-KEY-START" not in rabin_start or "RABIN-PUBLIC-KEY-END" not in rabin_end:
            self.showmsg("rabin pubkey file format not match")
            return
        rabin_n_un = base64.b32decode(rabin_n.encode("utf-8"))

        rsa_e_un = int(base64.b32decode(rsa_e.encode("utf-8")).decode('utf-8'))
        rsa_n_un = int(base64.b32decode(rsa_n.encode("utf-8")).decode('utf-8'))
        crc32_digest = passcoder.RsaSign().unsign(rsa_e_un, rsa_n_un,
                                                  rabin_sign)
        crc32_rabin = binascii.crc32(rabin_n_un)
        if crc32_rabin == crc32_digest:
            self.showmsg("verify success ,signature match")
        else:
            self.showmsg("verify failed ,signature not match")


class UserInterface(QMainWindow, pks_user.Ui_UserInterface):
    """
    用户界面
    """
    u_name: str

    def __init__(self, u_name):
        QMainWindow.__init__(self)
        pks_user.Ui_UserInterface.__init__(self)
        self.setupUi(self)
        # setting username
        self.u_name = u_name
        self.la_showname.setText(self.u_name)
        # 设置槽函数
        self.bt_regen.clicked.connect(self.key_regen)  # 重新生成key，包括rabin好rsa
        self.bt_dl_rabin_pubkey.clicked.connect(
            self.dl_pubkey)  # 下载rabin的pubkey
        self.bt_verify_signature.clicked.connect(self.verify_pubkey)  # 验证签名
        self.bt_encrypt_msg.clicked.connect(self.encrypt_msg)
        self.bt_decrypt_msg.clicked.connect(self.decrypt_msg)

    def decrypt_msg(self):
        file_path, _ = QFileDialog.getOpenFileName(self,
                                                   "open public key file",
                                                   r"./", "TXT(*.txt)")
        if len(file_path) == 0 or not os.path.exists(file_path):
            self.showmsg("please select correct file ")
            return
        # 读取file文件
        with open(file_path, "r") as f:
            msg = f.read()
        # 加载rabin的私钥
        user = User.select().where(User.username == self.u_name).get()
        pwd_md5 = user.pwd
        pwd2num = passcoder.Utils.str2num(pwd_md5)
        rabin = passcoder.PKSRabin()
        rabin_xor_p = int(user.rabin_p) ^ pwd2num
        rabin_xor_q = int(user.rabin_q) ^ pwd2num
        decrypted_msg = rabin.decrypt(rabin_xor_p, rabin_xor_q, msg)
        try:
            new_filename = "{}-decrypted-msg.txt".format(
                datetime.datetime.now())
            with open(new_filename, "w+") as f:
                f.write(decrypted_msg)
            self.showmsg("decrypted success,file:{}".format(new_filename))

        except Exception as e:
            self.showmsg("decrypted failed:{}".format(e))

    def encrypt_msg(self):
        self.text_editor = TextEditor(self.u_name)
        self.text_editor.show()

    def verify_pubkey(self):

        self.ui_verify = KeyVerify()
        self.ui_verify.show()

    def key_regen(self):
        username = self.u_name
        try:
            user = User.select().where(User.username == username).get()
            pwd_md5 = user.pwd
            pwd2num = passcoder.Utils.str2num(pwd_md5)
            # 生成rabin公私钥
            rabin = passcoder.PKSRabin()
            rabin_p, rabin_q, rabin_n = rabin.keygen(512)

            # 使用用户的账号的密码进行保护
            rabin_xor_p = rabin_p ^ pwd2num
            rabin_xor_q = rabin_q ^ pwd2num
            # 生成rsa公私钥
            rsa_sign = passcoder.RsaSign()
            sign_p, sign_q, sign_e, sign_d = rsa_sign.k_gen(32)
            sign_xor_p = sign_p ^ pwd2num
            sign_xor_q = sign_q ^ pwd2num
            sign_xor_e = sign_e ^ pwd2num
            sign_xor_d = sign_d ^ pwd2num

            # save
            user.rabin_p = str(rabin_xor_p)
            user.rabin_q = str(rabin_xor_q)
            user.rsa_p = str(sign_xor_p)
            user.rsa_q = str(sign_xor_q)
            user.rsa_e = str(sign_xor_e)
            user.rsa_d = str(sign_xor_d)
            user.save()
            self.showmsg("key regen success")
        except Exception as e:
            self.showmsg("{}".format(e))

    def dl_pubkey(self):
        '''
        download rabin public key
        '''
        try:
            # 设置publickey

            file_path = QFileDialog.getExistingDirectory(
                self, "choose path to save", r"./")
            filename = file_path + convert_path("/{}.pub_rabin".format(
                self.u_name))
            print("文件{}".format(filename))
            # 下载rabin key
            user = User.user = User.select().where(
                User.username == self.u_name).get()
            rabin_p, rabin_q, rsa_p, rsa_q, rsa_e, rsa_d = xor_allkey(
                user.username)

            rsa_sign = passcoder.RsaSign()

            rabin_n = str(rabin_q * rabin_p)

            signer = rsa_sign.sign(rsa_d, rsa_p, rsa_q, rabin_n)

            if KeyUtil.gen_pub_key(user.username, rabin_n, signer, filename):

                # 产生rsa的公钥
                KeyUtil.gen_rsa_pubkey(
                    user.username, str(rsa_e), str(rsa_p * rsa_q), file_path +
                    convert_path("/{}.pub_rsa".format(self.u_name)))
                self.showmsg(
                    "save success,file name:{}.pub_rabin,{}.pub_rsa".format(
                        self.u_name, self.u_name))
            else:
                self.showmsg("save success,file failed.format")

        except Exception as e:
            print(e)
            self.showmsg(e)

    def showmsg(self, data):
        QMessageBox.information(self, "Note", data)


class TextEditor(QWidget, pks_text_editor.Ui_TextEditor):
    """
    编辑信息的界面
    """
    def __init__(self, username):
        QWidget.__init__(self)
        pks_text_editor.Ui_TextEditor.__init__(self)
        self.setupUi(self)
        self.u_name = username
        self.bt_ok.clicked.connect(self.encrypt)
        self.bt_load_rabin_pubkey.clicked.connect(self.load_rabinkey)
        self.rabin_n = None

    def load_rabinkey(self):
        pub_key_path, _ = QFileDialog.getOpenFileName(self,
                                                      "open public key file",
                                                      r"./",
                                                      "TXT(*.pub_rabin)")

        if not os.path.exists(pub_key_path):
            self.showmsg("pubkey not exists")
            return

        # load rabin public key file
        rabin_start, rabin_n, rabin_sign, rabin_end = KeyUtil.load_rabin_pub(
            pub_key_path)
        if "RABIN-PUBLIC-KEY-START" not in rabin_start or "RABIN-PUBLIC-KEY-END" not in rabin_end:
            self.showmsg("rabin pubkey file format not match")
            return
        rabin_n_un = int(base64.b32decode(rabin_n.encode("utf-8")))
        self.rabin_n = rabin_n_un

    def encrypt(self):
        text = self.textEditor.toPlainText()
        if len(text) == 0:
            self.showmsg("please input some text")
            return
        if not self.rabin_n:
            self.showmsg("please load public key file first")
            return
        filename = "{}-{}-encrypted-msg.txt".format(datetime.datetime.now(),
                                                    self.u_name)
        encrypted_msg = passcoder.RsaSign().encrypt(self.rabin_n, text)

        with open(filename, "w+") as f:
            f.write(encrypted_msg)
        self.showmsg("save success,file:{}".format(filename))
        self.close()

    def showmsg(self, data):
        QMessageBox.information(self, "Note", data)
