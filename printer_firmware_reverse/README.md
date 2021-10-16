<!--
 * @Description: Editor's info in the top of the file
 * @Author: p1ay8y3ar
 * @Date: 2021-10-16 17:18:16
 * @LastEditor: p1ay8y3ar
 * @LastEditTime: 2021-10-16 17:45:14
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

```shell
❯ binwalk -M 176BV3020AN.bin                                                                                                              ─╯

Scan Time:     2021-10-16 17:44:34
Target File:   /Users/freedom/Desktop/opensource_code/fls_extract/176BV3020AN.bin
MD5 Checksum:  c2272e15de16a45aa327483ad6263d36
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
3420818       0x343292        Zlib compressed data, default compression
6506754       0x634902        Zlib compressed data, default compression
9472018       0x908812        Zlib compressed data, default compression
22819266      0x15C31C2       Zlib compressed data, default compression
22936386      0x15DFB42       Zlib compressed data, default compression
23774578      0x16AC572       Zlib compressed data, default compression
28858242      0x1B85782       Zlib compressed data, default compression
29180098      0x1BD40C2       Zlib compressed data, default compression
33132274      0x1F98EF2       Zlib compressed data, default compression
36204306      0x2286F12       Zlib compressed data, default compression
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

```shell
❯ binwalk -M  176BV3020AN.out                                                                                                             ─╯

Scan Time:     2021-10-16 17:44:04
Target File:   /Users/freedom/Desktop/opensource_code/fls_extract/176BV3020AN.out
MD5 Checksum:  7a1a7326bf91c29c23095c043c6d5f6d
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
1244878       0x12FECE        MySQL MISAM compressed data file Version 8
2831357       0x2B33FD        Certificate in DER format (x509 v3), header length: 4, sequence length: 27328
3412167       0x3410C7        Certificate in DER format (x509 v3), header length: 4, sequence length: 27075
3446884       0x349864        Certificate in DER format (x509 v3), header length: 4, sequence length: 2827
3490265       0x3541D9        Certificate in DER format (x509 v3), header length: 4, sequence length: 22868
3689712       0x384CF0        XML document, version: "1.0"
3796648       0x39EEA8        XML document, version: "1.0"
3819867       0x3A495B        Certificate in DER format (x509 v3), header length: 4, sequence length: 30449
3953044       0x3C5194        XML document, version: "1.0"
3978138       0x3CB39A        MySQL MISAM index file Version 3
4001286       0x3D0E06        MySQL ISAM index file Version 5
5545743       0x549F0F        Certificate in DER format (x509 v3), header length: 4, sequence length: 32288
5708128       0x571960        Certificate in DER format (x509 v3), header length: 4, sequence length: 5140
5938376       0x5A9CC8        MySQL MISAM compressed data file Version 7
6097090       0x5D08C2        MySQL ISAM index file Version 6
6927072       0x69B2E0        Certificate in DER format (x509 v3), header length: 4, sequence length: 15677
7120726       0x6CA756        MySQL MISAM index file Version 2
7528872       0x72E1A8        MySQL ISAM compressed data file Version 9
7703130       0x758A5A        Certificate in DER format (x509 v3), header length: 4, sequence length: 899
7703134       0x758A5E        Certificate in DER format (x509 v3), header length: 4, sequence length: 899
7703138       0x758A62        Certificate in DER format (x509 v3), header length: 4, sequence length: 899
7733406       0x76009E        Certificate in DER format (x509 v3), header length: 4, sequence length: 28678
7733410       0x7600A2        Certificate in DER format (x509 v3), header length: 4, sequence length: 28678
7933768       0x790F48        MySQL MISAM index file Version 5
8608568       0x835B38        MySQL MISAM compressed data file Version 7
8614222       0x83714E        MySQL ISAM compressed data file Version 2
8663862       0x843336        MySQL MISAM compressed data file Version 1
8723366       0x851BA6        MySQL MISAM compressed data file Version 3
8998952       0x895028        JPEG image data, JFIF standard -40.-1, thumbnail -1x-32
9197538       0x8C57E2        MySQL MISAM compressed data file Version 7
10007873      0x98B541        Copyright string: "Copyright 1999-3.02 2 020 Inc. All  Inc.s reserved."
10065372      0x9995DC        GIF image data 17993 x 16
10148350      0x9AD9FE        HTML document header
10243589      0x9C4E05        HTML document header
10329630      0x9D9E1E        GIF image data, version "89a", 109 x 20
10329656      0x9D9E38        GIF image data 17993 x
10524898      0xA098E2        GIF image data, version "89a", 18220 x 17993
11800145      0xB40E51        MySQL MISAM index file Version 1
11929524      0xB607B4        Certificate in DER format (x509 v3), header length: 4, sequence length: 8461
12130306      0xB91802        Certificate in DER format (x509 v3), header length: 4, sequence length: 4112
12130310      0xB91806        Certificate in DER format (x509 v3), header length: 4, sequence length: 2056
12303456      0xBBBC60        AES S-Box
12307988      0xBBCE14        AES Inverse S-Box
12413669      0xBD6AE5        Motorola S-Record; binary data in text format, record type: data (32-bit)
12455348      0xBE0DB4        AES S-Box
12516724      0xBEFD74        SHA256 hash constants, little endian
12534484      0xBF42D4        AES S-Box
13047949      0xC7188D        Certificate in DER format (x509 v3), header length: 4, sequence length: 8986
13703804      0xD11A7C        MySQL MISAM compressed data file Version 10
13922488      0xD470B8        MySQL MISAM index file Version 3
14056956      0xD67DFC        SHA256 hash constants, little endian
15056988      0xE5C05C        AES Inverse S-Box
15382513      0xEAB7F1        AES S-Box
16564280      0xFCC038        Copyright string: "Copyright 1990-Cop9 Bitstream Inc.  All 9 Bits reserved.s reserved. I BT BTes  BTe  BTe BTeserved. Inc.  BTesmfgpctt-v4.5mfgp Ma"

```

but binwalk can't extrct it:(,you can use `dd` to extract which section you are interested in 