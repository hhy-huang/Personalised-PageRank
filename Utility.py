# original by Xinbo Wu
# annotated by Haoyu Huang
# Utility functions
# random walk

def make_vec(keys):
    result = dict()
    for key in keys:
        result.update({key: 1})

    return result


def make_adlist(file_name):  # 将raw data整理为dict
    result = dict()

    f = open(file_name, 'r')

    for line in f:
        splited = line.rstrip().split('\t')

        if splited[0] in result:
            if splited[1] in result[splited[0]]:
                print("1")
                result[splited[0]][splited[1]] += 1
            else:
                result[splited[0]].update({splited[1]: 1})
        else:
            result.update({splited[0]: {splited[1]: 1}})  # result形式： author idA: {author id: num,...}

        if splited[1] in result:
            if splited[0] in result[splited[1]]:
                print("1")
                result[splited[1]][splited[0]] += 1
            else:
                result[splited[1]].update({splited[0]: 1})
        else:
            result.update({splited[1]: {splited[0]: 1}})  # 双向的

    f.close()

    return result


def file_to_dict(file_name):
    result = dict()

    f = open(file_name, 'r')

    for line in f:
        splited = line.rstrip().split('\t')

        if splited[0] in result:
            result[splited[0]].append(splited[1])
        else:
            result.update({splited[0]: [splited[1]]})

    f.close()

    return result


def nom_adlist(adlist):
    tmp_adlist = adlist.copy()  # 根据APVPA的result，value->key

    for key1 in tmp_adlist.keys():  # 遍历所有的node（5000）
        count = 0
        for key2 in tmp_adlist.keys():  # 再次遍历所有的node, 计算key1的出度count
            if key1 in tmp_adlist[key2]:
                count += 1

        for key2 in tmp_adlist.keys():  # key1->key2，1/key1的出度
            if key1 in tmp_adlist[key2]:
                tmp_adlist[key2][key1] = float(tmp_adlist[key2][key1]) / count

    return tmp_adlist  # 返回的结果是转移矩阵


def nom_vec(vec):  # 平均分布
    tmp_vec = vec.copy()

    dom = sum(tmp_vec.values())

    for key in tmp_vec.keys():
        tmp_vec[key] = float(tmp_vec[key]) / dom  # 除以总数

    return tmp_vec


def adlist_vec_multiply(adlist, vec):  # 矩阵与向量相乘(n,n)·(n,1)=(n,1)
    result = dict()

    for key1 in adlist.keys():
        tmp1 = adlist[key1]  # 是所有指向key1的node
        tmp_sum = 0

        for key2 in vec.keys():  # 遍历向量的每一个元素
            if key2 in tmp1:  # 如果说向量的这个位置所对应的node，在矩阵的这一行中存在，就讲这两个值相乘
                tmp_sum += tmp1[key2] * vec[key2]  # 矩阵这一行的乘积加起来，没有的就是0，得到结果向量的某个位置的值

        result.update({key1: tmp_sum})
    return result


def constant_vec_multiply(constant, vec):  # 常数*向量
    tmp_vec = vec.copy()

    for key in tmp_vec.keys():  # 将向量整体乘0.15或0.85
        tmp_vec[key] = constant * tmp_vec[key]

    return tmp_vec


def vec_vec_add(vec1, vec2):
    tmp_vec1 = vec1.copy()  # 分配0.85的概率
    tmp_vec2 = vec2.copy()  # 分配0.15的概率

    for key in tmp_vec2.keys():
        if key in tmp_vec1:
            tmp_vec1[key] += tmp_vec2[key]  # 把它自己的概率加上
        else:
            tmp_vec1.update({key: tmp_vec2[key]})

    return tmp_vec1


# 这仨显而易见
def find_ID(file_name, name):
    result = ""

    f = open(file_name, 'r')

    for line in f:
        splited = f.split('\t')

        if splited[1] == name:
            result = splited[0]
            break

    f.close()

    return result


def make_ID_name_dict(file_name):
    result = dict()

    f = open(file_name, 'r')

    for line in f:
        splited = line.rstrip().split('\t')

        result.update({splited[0]: splited[1]})

    f.close()
    # print(result)
    return result


def make_name_ID_dict(file_name):
    result = dict()

    f = open(file_name, 'r')

    for line in f:
        splited = line.rstrip().split('\t')

        result.update({splited[1]: splited[0]})

    f.close()
    # print(result)

    return result
