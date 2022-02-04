# original by Xinbo Wu
# annotated by Haoyu Huang
# Personalized PageRank for APVPA

from Utility import *
from Personalized_PageRank import *


def main():
    # use APVPA'
    net_file_name = "data/APVPA.txt"            # author id的有向图，id1 id2, id2->id1
    name_ID_file_name = "data/author.txt"
    name1 = "Christos Faloutsos"
    name2 = "AnHai Doan"

    p_prank = P_PageRank(net_file_name, name_ID_file_name, c=0.15)

    p_prank.set_preference([name1])             # 每次c的概率随机选择node，但是这里只有一个name1，所以就是c*1的概率访问到name1这个node
    # 这里personalised的都是某个author，这样找到的是与该author关联度较大的author
    # Find top 10 similar researchers for Christos Faloutsos using APVPA
    print("Find top 10 similar researchers for ", name1, " using APVPA")
    p_prank.run(num_iter=10)

    key = p_prank.name_ID_dict["Jiawei Han"]    # 找到相应的author id

    print(p_prank.v[key])                       # 给出这个author的重要性，也就是访问到他的概率

    result = p_prank.find_top_n(10)

    sorted_result = sorted(result, key=result.__getitem__)

    for i in xrange(len(sorted_result)):        # 输出
        key = sorted_result[len(sorted_result) - 1 - i]
        print(i + 1, ". ", p_prank.ID_name_dict[key], '%.15f' % result[key])

    p_prank.set_preference([name2])

    # Find top 10 similar researchers for AnHai Doan using APVPA
    print("Find top 10 similar researchers for ", name2, " using APVPA")
    p_prank.run(num_iter=10)

    result = p_prank.find_top_n(10)

    sorted_result = sorted(result, key=result.__getitem__)

    for i in xrange(len(sorted_result)):
        key = sorted_result[len(sorted_result) - 1 - i]
        print(i + 1, ". ", p_prank.ID_name_dict[key], '%.15f' % result[key])


main()
