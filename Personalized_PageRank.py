# original by Xinbo Wu
# annotated by Haoyu Huang
# Personalized PageRank
from jieba import xrange

from Utility import *


class P_PageRank(object):

    def __init__(self, net_file_name, name_ID_file_name, c=0.15):
        self.net_adlist = nom_adlist(make_adlist(net_file_name))    # 转移矩阵
        self.c = c                                                  # 随机选择node的概率
        self.name_ID_dict = make_name_ID_dict(name_ID_file_name)
        self.ID_name_dict = make_ID_name_dict(name_ID_file_name)

    def set_preference(self, p_set=[]):                             # personalised，得到self.u的向量，也就是随机选择node的candidates
        self.u = dict()
        for element in p_set:
            key = self.name_ID_dict[element]                        # 取出对应作者的ID
            self.u.update({key: 1})

        self.u = nom_vec(self.u)                                    # 这里其实还是取的平均，由于list里面只有一个作者，所以每次以0.15的概率再次从它出发

    def run(self, num_iter=10):
        self.v = nom_vec(make_vec(self.net_adlist.keys()))          # 把key，也就是所有的node挑出来然后，平均分布
        # print(self.v)
        for i in xrange(num_iter):                                  # 迭代十次
            self.v = constant_vec_multiply(1 - self.c,              # 根据转移矩阵进行选择，概率是1-c
                                           adlist_vec_multiply(     # 将转移矩阵与个性化向量相乘,得到结果向量(n,1)
                                               self.net_adlist, self.v))
            self.v = vec_vec_add(self.v, constant_vec_multiply(     # 任意随机选择一个node，概率是c，并将两种情况得到的向量相加，得到本轮迭代的结果
                self.c, self.u))
            # print(self.v)

        print("finished")

    def find_top_n(self, n):                                        # 找到概率最大的前n个node，也就是最重要的前n个node
        result = dict()
        sorted_keys = sorted(self.v, key=self.v.__getitem__)

        for key in sorted_keys[len(self.v) - n:len(self.v)]:
            result.update({key: self.v[key]})

        return result
