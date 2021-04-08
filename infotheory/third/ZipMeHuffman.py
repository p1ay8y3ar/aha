'''
Description: a scirpt to compress and decompress using huffman coding
Author: p1ay8y3ar
Date: 2021-04-08 16:17:07
LastEditor: p1ay8y3ar
LastEditTime: 2021-04-08 18:17:57
Email: p1ay8y3ar@gmail.com
'''

import heapq
import os
import math
import argparse


class HmNode:
    def __init__(self, source=None, weight=0) -> None:
        self.s = source
        self.weight = weight

    def __lt__(self, h: object) -> bool:
        """
        rewrite lt for using heapq
        h: isinstance(h,HmNode)
        """
        return self.weight < h.weight

    def __eq__(self, o: object) -> bool:
        '''
        rewrite eq for using heapq
        o: isinstance(h,HmNode)
        '''
        if not isinstance(o, HmNode):
            return False
        return self.weight == o.weight

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, node) -> None:
        self.__right = node

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left) -> None:
        self.__left = left


class Huffman:
    class CodingError(Exception):
        pass

    def __init__(self) -> None:
        self._code_table = {}

    def __weight(self, stream) -> dict:
        '''
            Get weight by counting the number of occurrences of characters
        input:
            stream:bytes stream
        output:
            dict
        '''
        weight_dict = {}
        for i in stream:
            if i not in weight_dict:
                weight_dict[i] = 0
            weight_dict[i] += 1
        return weight_dict

    def __node(self, weight_dict: dict) -> list:
        '''
        make HmNode
        input:weight_dict
        output: binary tree node list
        '''
        binary_tree_list = []
        for k, v in weight_dict.items():
            heapq.heappush(binary_tree_list, HmNode(k, v))
        return binary_tree_list

    def __huffman_tree(self, binary_tree: list) -> list:
        '''
        build huffman tree
        input:
            binary tree:list
        output:
            huffman tree :list
        '''

        while len(binary_tree) > 1:
            smallest = heapq.heappop(binary_tree)
            second_smallest = heapq.heappop(binary_tree)
            node_plus = HmNode(weight=smallest.weight + second_smallest.weight)
            node_plus.left = smallest
            node_plus.right = second_smallest
            heapq.heappush(binary_tree, node_plus)
        return binary_tree

    def __recursive_build(self, node, code):
        '''
        Recursive construction code 
        input:
            node:HmNode
            code:str
        '''
        if node.s != None:
            self._code_table[node.s] = code
            return
        self.__recursive_build(node.left, code + "0")
        self.__recursive_build(node.right, code + "1")

    def __code_maker(self, huffman_tree: list) -> None:
        '''
        Construct non-singular codes By traversing the huffman tree 
        input:huffman tree
        output:None
        '''
        code_string = ""
        self._code_table.clear()
        root = heapq.heappop(huffman_tree)
        self.__recursive_build(root, code_string)

    def __int2bin(self, num: int, width=1) -> str:
        '''
        make num binary length to 8,
        like 4=0b100 return 00000100
        input:
            num:int
            width: binary width
        '''
        tmp = "{0:b}".format(num)
        formated_code = "0" * (8 * width - len(tmp)) + tmp
        return formated_code

    def __unpadding(self, padded_str, padding_len) -> str:
        '''
        unpadding string 
        '''
        return padded_str[:-1 * padding_len]

    def __padding(self, text: str, weight_dict: dict) -> str:
        '''
        write the weight dict to the top of the file
        and padding the text to fit 8 bit
        input :
            test:str
            weight_dict:dict
        output:
            str
        '''
        # because max is 256,2 bytes is enough
        weight_length = self.__int2bin(len(weight_dict), 2)
        max_weight = max(list(weight_dict.values()))
        bit_width = math.ceil(len("{0:08b}".format(max_weight)) / 8)
        bit_width_bin = self.__int2bin(bit_width)
        weight_dict_str = ""
        for k, v in weight_dict.items():
            k_bin = self.__int2bin(k)
            v_bin = self.__int2bin(v, bit_width)
            weight_dict_str += k_bin + v_bin
        bin_str = weight_length + bit_width_bin + weight_dict_str + text

        # padding to fit 8 bit
        padding_len = 8 - len(bin_str) % 8
        padding_bin = self.__int2bin(padding_len)
        return padding_bin + bin_str + "0" * padding_len

    def __str2bytes(self, text: str) -> bytearray:
        '''
        convert string to bytearray
        input:
            text:str
        output:
            bytearray
        '''
        b_l = bytearray()
        for i in range(0, len(text), 8):
            single_byte = text[i:i + 8]
            b_l.append(int(single_byte, 2))

        return b_l

    def __decode(self, encoded_str) -> bytearray:
        '''
        decode text
        input:encoded_str
        output:bytearray ,decoded
        '''
        decoded_text = bytearray()
        code_map = dict(
            zip(self._code_table.values(), self._code_table.keys()))
        code = ""
        for e in encoded_str:
            code += e
            if code in code_map:
                decoded_text.append(code_map[code])
                code = ""
        return decoded_text

    def __encode(self, text) -> str:
        '''
        对数据进行编码
        input:text
        output:str
        '''
        encoded_str = ""
        for b in text:
            encoded_str += self._code_table[b]
        return encoded_str

    def compress(self, path: str) -> bool:
        '''
        compress function
        input:
            file path:str
        output:
            bool : compress success or not
        '''
        if not os.path.exists(path):
            raise self.CodingError("{} does not exists".format(path))
        out_filepath = path + ".zmh"
        with open(path, "rb+") as input, open(out_filepath, "wb+") as output:
            # File size judgment Make sure the file is correct
            input.seek(0, 2)
            if input.tell() == 0:
                raise self.CodingError("file size is zero")
            input.seek(0, 0)

            # read file data
            # i read all of data which i can use cpu for processing to speed up
            stream_data = input.read()

            # Perform weight calculation
            weight_dict = self.__weight(stream_data)
            
            # make node
            binary_tree_list = self.__node(weight_dict)
            
            # then build huffman tree
            huffman_tree = self.__huffman_tree(binary_tree_list)

            # Construct non-singular codes
            self.__code_maker(huffman_tree)
            
            # Encode the data
            encoded_str = self.__encode(stream_data)

            # write wight to the top of hte file and padding the text
            padded_str = self.__padding(encoded_str, weight_dict)

            # convert string to  bytes then write to file
            bytes_array = self.__str2bytes(padded_str)

            try:
                output.write(bytes_array)
                return True
            except Exception as e:
                raise self.CodingError("file write error", e)

    def decompress(self, path: str) -> bool:
        if not os.path.exists(path):
            raise self.CodingError("{} does not exists".format(path))
        filename, extend = os.path.splitext(path)
        if extend != ".zmh":
            raise self.CodingError(
                "{} does not suppoprt this format,only support '.zmh'file ".
                format(extend))
        with open(path, "rb") as input, open(filename, "wb") as output:
            # Restoration weight list
            padding_len = ord(input.read(1))
            weight_len = int.from_bytes(input.read(2),
                                        byteorder="big",
                                        signed=False)
            # read bit write width
            width_len = ord(input.read(1))
            
            # recover weight dict
            weight_dict = {}
            while weight_len:
                k = input.read(1)
                v = input.read(width_len)
                k_real = (int.from_bytes(k, byteorder='big', signed=False))
                v_real = (int.from_bytes(v, byteorder='big', signed=False))
                weight_dict[k_real] = v_real
                weight_len -= 1
            # builf huffman tree and code table
            binary_tree_list = self.__node(weight_dict)
            
            huffman_tree = self.__huffman_tree(binary_tree_list)
            self.__code_maker(huffman_tree)
            
            read_string = ""
            str_read = input.read(1)
            while len(str_read) > 0:
                str_read = ord(str_read)
                bits = bin(str_read)[2:].rjust(8, '0')
                read_string += bits
                str_read = input.read(1)

            # first unpadding
            unpadded_test = self.__unpadding(read_string, padding_len)
            decoded_bytes = self.__decode(unpadded_test)
            try:
                output.write(decoded_bytes)
                return True
            except Exception as e:
                raise self.CodingError("file write error", e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", type=str, help="compress file")
    parser.add_argument("-d", type=str, help='decompress file')
    args = parser.parse_args()
    if args.c:
        H = Huffman()
        status = H.compress(args.c)
        if status:
            print("compress success")
    elif args.d:
        H = Huffman()
        status = H.decompress(args.d)
        if status:
            print("decompress success")
    