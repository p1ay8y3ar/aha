'''
Description: cannon rfu firmware decrypt script
Author: p1ay8y3ar
Date: 2021-10-15 19:24:45
LastEditor: p1ay8y3ar
LastEditTime: 2021-10-16 17:41:17
Email: p1ay8y3ar@gmail.com
'''
from io import BufferedReader
import os
import ctypes
import sys
from pathlib import PurePath
import time
KEYBUFSIZE = 32


def get_key(fh: BufferedReader) -> list:
    """get encrypt key

    Args:
        fh (BufferedReader): rfu file handle

    Returns:
        list: key list ,list(int)
    """
    guess_1 = ["S", "F", "0", "9", "0", "0"]
    guess_2 = [0x0D, 0x0A, 'S', 'F', '0', '5', '0', '0', '0', '0']
    key = []

    try:

        original = fh.read(KEYBUFSIZE)
        for idx, s in enumerate(guess_1):
            key.append(original[idx] ^ ord(s))

        for idx, s in enumerate(guess_2):
            s = ord(s) if isinstance(s, str) else s
            key.append(original[idx + 6 + 0x10] ^ s)
        return key
    except Exception:
        return key


def decrypt_rfu(infh: BufferedReader, outfh: BufferedReader, key: list):
    """decrypt all rfu firmware file

    Args:
        infh (BufferedReader): rfu file handle
        outfh (BufferedReader): saved file handle
        key (list): decrypt key file
    """
    print("decrypting ...")
    infh.seek(0)
    outbuf = bytearray()
    while True:
        orginal_buf = infh.read(32768)
        buf_len = len(orginal_buf)
        if buf_len == 0: break
        for i in range(buf_len):
            outbuf.append(orginal_buf[i] ^ key[i % 16])

        outfh.write(outbuf)
        outbuf.clear()


def get_offset(inpath: str):
    # print(inpath)
    infh = open(inpath, "rb")
    sig = b"\x70\xb5\x05\x4c\x05\x48\x06\x49\x45\x1a\x0e\x46\x2a\x46\x31\x46\x20\x46\xff"
    buf = infh.read()
    sig_offset = buf.find(sig)
    if sig_offset == -1:
        print("sig not match")
        return
    offset = sig_offset + 24
    infh.seek(offset)
    offset = infh.read(4)
    end = infh.read(4)
    start = infh.read(4)
    data_offset = int.from_bytes(offset, byteorder="little")
    end_offset = int.from_bytes(end, byteorder="little")
    start_offset = int.from_bytes(start, byteorder="little")

    size = end_offset - start_offset

    offset = data_offset & 0xFFFFFF
    infh.close()

    return size, offset


def decomporess(infh: BufferedReader, outfh: BufferedReader):
    sig = b"\x70\xb5\x05\x4c\x05\x48\x06\x49\x45\x1a\x0e\x46\x2a\x46\x31\x46\x20\x46\xff"

    infh.seek(0, os.SEEK_SET)
    buf = infh.read()
    sig_offset = buf.find(sig)
    if sig_offset == -1:
        print("sig not match")
        return

    offset = sig_offset + 24

    infh.seek(offset)

    offset = infh.read(4)
    end = infh.read(4)
    start = infh.read(4)

    data_offset = int.from_bytes(offset, byteorder="little")
    end_offset = int.from_bytes(end, byteorder="little")
    start_offset = int.from_bytes(start, byteorder="little")

    size = end_offset - start_offset

    offset = data_offset & 0xFFFFFF
    infh.seek(offset)

    outfh.seek(0, os.SEEK_SET)

    while outfh.tell() < size:
        char1 = infh.read(1)
        char1 = int.from_bytes(char1, byteorder="little")
        charl = char1 & 3
        if charl == 0:
            charl = infh.read(1)
            charl = int.from_bytes(charl, byteorder="little")

        chard = char1 >> 4
        if chard == 0:
            chard = infh.read(1)
            chard = int.from_bytes(chard, byteorder="little")
        tmpbuf = infh.read(charl - 1)
        outfh.write(tmpbuf)

        if chard != 0:
            chare = infh.read(1)
            chare = int.from_bytes(chare, byteorder="little")
            fi1 = ctypes.c_uint(char1 << 28).value
            fi2 = ctypes.c_uint(fi1 >> 30).value
            outfh.write(tmpbuf[:chard + 2])


if __name__ == "__main__":
    bin_file = PurePath(sys.argv[1])
    tbin_path = bin_file.parent.joinpath(
        bin_file.name.replace(bin_file.suffix, ".tt"))
    xbin_path = bin_file.parent.joinpath(
        bin_file.name.replace(bin_file.suffix, ".tbin"))
    firm_pth = bin_file.parent.joinpath(
        bin_file.name.replace(bin_file.suffix, ".out"))

    try:
        # 1 decrypt file
        bin_fh = open(bin_file, "rb")
        tbin_fh = open(tbin_path, "wb")
        key_list = get_key(bin_fh)
        print("key found", [hex(i) for i in key_list])
        decrypt_rfu(bin_fh, tbin_fh, key_list)
        tbin_fh.close()
        # 2 decompose file
        cmd = "grep -v -e '^SF' {} | srec_cat -o {} -binary".format(
            tbin_path, xbin_path)
        os.popen(cmd=cmd)
        time.sleep(3)
        # decompress
        # use c api
        print("decompressing...")
        mylib = ctypes.CDLL("libdecom.lib")
        inpath = ctypes.c_char_p(bytes(str(xbin_path), "utf-8"))
        
        outpath = ctypes.c_char_p(bytes(str(firm_pth), "utf-8"))
        size, offset = get_offset(xbin_path)

        mylib.decompress_fp(inpath, outpath, size, offset)

        print('DONE,decrypted and decompressed firmware : {}'.format(firm_pth))

    except Exception as e:
        print(e)
