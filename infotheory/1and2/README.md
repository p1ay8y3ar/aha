<!--
 * @Description: Editor's info in the top of the file
 * @Author: p1ay8y3ar
 * @Date: 2021-03-28 23:49:30
 * @LastEditor: p1ay8y3ar
 * @LastEditTime: 2021-03-29 00:35:40
 * @Email: p1ay8y3ar@gmail.com
-->

# how to use

## ТИИТК*Задание*Кодирование*стационарных*источников*без*памяти_равномерными

### first topic

```shell
python InfoSrcCoding.py -hw 1 -topic 1
```

here is a sample output

```shell
 selected source :coin_1-{'0': '1/3', '1': '2/3'} 	 H:0.9182958340544896
```

## second topic

```shell
python InfoSrcCoding.py -hw 1 -topic 2 -r 0.6 -eps 0.1 -q 2
```

here is a sample output

```shell
{'seq': [15, 23, 27, 29, 30, 31, 39, 43, 45, 46, 47, 51, 53, 54, 55, 57, 58, 59, 60, 61, 62, 71, 75, 77, 78, 79, 83, 85, 86, 87, 89, 90, 91, 92, 93, 94, 99, 101, 102, 103, 105, 106, 107, 108, 109, 110, 113, 114, 115, 116, 117, 118, 120, 121, 122, 124], 'code': ['000000', '000001', '000010', '000011', '000100', '000101', '000110', '000111', '001000', '001001', '001010', '001011', '001100', '001101', '001110', '001111', '010000', '010001', '010010', '010011', '010100', '010101', '010110', '010111', '011000', '011001', '011010', '011011', '011100', '011101', '011110', '011111', '100000', '100001', '100010', '100011', '100100', '100101', '100110', '100111', '101000', '101001', '101010', '101011', '101100', '101101', '101110', '101111', '110000', '110001', '110010', '110011', '110100', '110101', '110110', '110111']}
```

## ТИИТК*Задание*Моделирование*дискретных*источников

### topic1

```shell
python InfoSrcCoding.py -hw 2 -topic 1 -n 10
```

-n to specify seq size,if you want to gen infinite , without use this arg and use `sudo` to gain root privilege for package `keyboard`

here is a sample output

```shell
0010101001
```

### topic2

```shell
python InfoSrcCoding.py -hw 2 -topic 2 -n 10 -seq 0 1 0 0
```

here is a sample output

```shell
random code seq is:1101001000,'1':0.4,'0':0.6
 probability:0.08639999999999999
```
