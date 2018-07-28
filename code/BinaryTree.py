import numpy as np

class TreeNode():
    def __init__(self,value,possibility):
        self.possibility = possibility
        self.left = None
        self.right = None
        self.value = value #叶子节点存储单词本身，非叶子节点存储中间向量
        self.Huffman = "" #存储the Huffman code

class Reigion():
    def __init__(self,poi_list):
        [self.a,self.b,self.c,self.d] = get_vertex(poi_list) #对应左上，右上，左下，右下的定点
        self.size = (self.a-self.b)*(self.a-self.c)
        set = poi_list
class BinaryTree():
    def __init__(self,poi_dict,vec_len=200):
        self.vec_len = vec_len
        self.root = None

        poi_dict_list = list(poi_dict.values())
        node_list = [TreeNode(x['word'],x['possibility']) for x in poi_dict_list]
        self.build_tree(node_list)
        self.generate_huffman_code(self.root,poi_dict)

    def build_tree(self,node_list):
        while(get_size())