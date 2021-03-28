<!--
 * @Description: Editor's info in the top of the file
 * @Author: p1ay8y3ar
 * @Date: 2021-03-28 23:49:30
 * @LastEditor: p1ay8y3ar
 * @LastEditTime: 2021-03-29 00:04:01
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
python InfoSrcCoding.py -hw 1 -topic 2 -r 0.4 -eps 0.3 -q 2
```

here is a sample output

```shell
selected source :coin_3-{'0': '0.57', '1': '0.43'}
 {'seq': [0, 1, 2, 3, 4, 5, 6, 7], 'code': ['000', '001', '010', '011', '100', '101', '110', '111']}
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
