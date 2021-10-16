<!--
 * @Description: Editor's info in the top of the file
 * @Author: p1ay8y3ar
 * @Date: 2021-10-16 17:18:16
 * @LastEditor: p1ay8y3ar
 * @LastEditTime: 2021-10-16 17:40:25
 * @Email: p1ay8y3ar@gmail.com
-->

# cannon printer update firmware decrypt and decompress

## test env 

- macos with m1 chip 


download fimware from [cannon support](http://www.canon.com/support/)

You can confirm the usb vendor id  [here](https://devicehunt.com/view/type/usb/vendor/04A9)


## use case 


### before run the script 

```shell
❯ binwalk -M 1769V1100AN.bin                                                                                                              ─╯

Scan Time:     2021-10-16 17:37:01
Target File:   /Users/freedom/Desktop/opensource_code/fls_extract/1769V1100AN.bin
MD5 Checksum:  f5ada85784021e54668d91e72ffeb198
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
```

### after run the script 

```shell
❯ binwalk -M 1769V1100AN.out                                                                                                              ─╯

Scan Time:     2021-10-16 17:39:11
Target File:   /Users/freedom/Desktop/opensource_code/fls_extract/1769V1100AN.out
MD5 Checksum:  cfc71482513a9a78547c875ef3ac9fe0
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
179636        0x2BDB4         Certificate in DER format (x509 v3), header length: 4, sequence length: 1285
720596        0xAFED4         MPEG transport stream data
1593959       0x185267        MySQL ISAM index file Version 4
2784949       0x2A7EB5        MySQL MISAM index file Version 4
2835233       0x2B4321        Certificate in DER format (x509 v3), header length: 4, sequence length: 27328
3051604       0x2E9054        Certificate in DER format (x509 v3), header length: 4, sequence length: 16448
3545488       0x361990        XML document, version: "1.0"
3709687       0x389AF7        Certificate in DER format (x509 v3), header length: 4, sequence length: 30449
3806376       0x3A14A8        MySQL MISAM index file Version 5
5367099       0x51E53B        Certificate in DER format (x509 v3), header length: 4, sequence length: 32288
5801808       0x588750        MySQL MISAM compressed data file Version 7
6192110       0x5E7BEE        MySQL ISAM compressed data file Version 4
6738132       0x66D0D4        Certificate in DER format (x509 v3), header length: 4, sequence length: 15677
6931786       0x69C54A        MySQL MISAM index file Version 2
7102230       0x6C5F16        Certificate in DER format (x509 v3), header length: 4, sequence length: 6168
7102234       0x6C5F1A        Certificate in DER format (x509 v3), header length: 4, sequence length: 7196
7102238       0x6C5F1E        Certificate in DER format (x509 v3), header length: 4, sequence length: 8224
7102242       0x6C5F22        Certificate in DER format (x509 v3), header length: 4, sequence length: 257
7102246       0x6C5F26        Certificate in DER format (x509 v3), header length: 4, sequence length: 9252
7102250       0x6C5F2A        Certificate in DER format (x509 v3), header length: 4, sequence length: 10280
7102254       0x6C5F2E        Certificate in DER format (x509 v3), header length: 4, sequence length: 11308
7102258       0x6C5F32        Certificate in DER format (x509 v3), header length: 4, sequence length: 12336
7102262       0x6C5F36        Certificate in DER format (x509 v3), header length: 4, sequence length: 514
7102266       0x6C5F3A        Certificate in DER format (x509 v3), header length: 4, sequence length: 771
7102270       0x6C5F3E        Certificate in DER format (x509 v3), header length: 4, sequence length: 1028
7367632       0x706BD0        MySQL ISAM compressed data file Version 9
7541890       0x731482        Certificate in DER format (x509 v3), header length: 4, sequence length: 899
7541894       0x731486        Certificate in DER format (x509 v3), header length: 4, sequence length: 899
7541898       0x73148A        Certificate in DER format (x509 v3), header length: 4, sequence length: 899
7572166       0x738AC6        Certificate in DER format (x509 v3), header length: 4, sequence length: 28678
7572170       0x738ACA        Certificate in DER format (x509 v3), header length: 4, sequence length: 28678
7775304       0x76A448        MySQL MISAM index file Version 5
8450032       0x80EFF0        MySQL MISAM compressed data file Version 7
8455686       0x810606        MySQL ISAM compressed data file Version 2
8505326       0x81C7EE        MySQL MISAM compressed data file Version 1
8564830       0x82B05E        MySQL MISAM compressed data file Version 3
8839640       0x86E1D8        JPEG image data, JFIF standard -40.-1, thumbnail -1x-32
9330045       0x8E5D7D        MySQL ISAM compressed data file Version 10
9330057       0x8E5D89        MySQL ISAM compressed data file Version 10
9330078       0x8E5D9E        MySQL ISAM compressed data file Version 10
9330084       0x8E5DA4        MySQL ISAM compressed data file Version 10
9330093       0x8E5DAD        MySQL ISAM compressed data file Version 10
9330115       0x8E5DC3        MySQL ISAM compressed data file Version 10
9330125       0x8E5DCD        MySQL ISAM compressed data file Version 10
9330133       0x8E5DD5        MySQL ISAM compressed data file Version 10
9330143       0x8E5DDF        MySQL ISAM compressed data file Version 10
9330166       0x8E5DF6        MySQL ISAM compressed data file Version 10
9330170       0x8E5DFA        MySQL ISAM compressed data file Version 10
9421501       0x8FC2BD        Copyright string: "Copyright 1999-1.12 2 100 Inc. All  Inc.s reserved."
9477824       0x909EC0        GIF image data 17993 x 16
9560802       0x91E2E2        HTML document header
9656041       0x9356E9        HTML document header
9742082       0x94A702        GIF image data, version "89a", 109 x 20
9742108       0x94A71C        GIF image data 17993 x
9957321       0x97EFC9        GIF image data, version "89a", 18220 x 17993
11061441      0xA8C8C1        MySQL MISAM index file Version 1
11190828      0xAAC22C        Certificate in DER format (x509 v3), header length: 4, sequence length: 8461
11391610      0xADD27A        Certificate in DER format (x509 v3), header length: 4, sequence length: 4112
11391614      0xADD27E        Certificate in DER format (x509 v3), header length: 4, sequence length: 2056
11564760      0xB076D8        AES S-Box
11569292      0xB0888C        AES Inverse S-Box
11674973      0xB2255D        Motorola S-Record; binary data in text format, record type: data (32-bit)
11716652      0xB2C82C        AES S-Box
11778028      0xB3B7EC        SHA256 hash constants, little endian
11795788      0xB3FD4C        AES S-Box
12309257      0xBBD309        Certificate in DER format (x509 v3), header length: 4, sequence length: 8986
12965108      0xC5D4F4        MySQL MISAM compressed data file Version 10
13183792      0xC92B30        MySQL MISAM index file Version 3
14064160      0xD69A20        AES Inverse S-Box
14389681      0xDB91B1        AES S-Box
15552876      0xED516C        Copyright string: "Copyright 1990-Cop9 Bitstream Inc.  All 9 Bits reserved.s reserved. I BT BTes  BTe  BTe BTeserved. Inc.  BTesmfgpctt-v4.5mfgp Ma"
```

but binwalk can't extrct it:(,you can use `dd` to extract which section you are interested in 