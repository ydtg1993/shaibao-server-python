import datetime


def get_sequence(prefix, sequence, length=4):
    """
    获取一个依据时间规则生成的流水号，格式为：prefix + yymmdd + lenth 长度流水号
    :param sequence: 需要生成的序列
    :param prefix: 序列号前缀
    :param length: 流水号长度
    :return: 生成的序列号
    """
    pre = prefix + "-" + datetime.datetime.now().strftime("%y%m%d")
    # seq = Sequence.get(pre)
    s = "".join(['0'] * (length - len(str(sequence))))
    no = pre + s + str(sequence)
    return no
