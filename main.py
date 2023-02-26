import pandas as pd
import jieba
import re


def load_data():
    """tsv -> csv
    tsv 文件中有很多字段, 选取其中表示文本和类型的字段作为返回值, 同时存入 csv
    """
    data_tsv_df = pd.read_csv(r"data/temp.tsv", sep="\t", header=0, encoding="gbk")
    data_tsv_df_col2 = data_tsv_df.loc[:, ["BUSI_TYPE_CODE", "ACCEPT_CONTENT"]]
    data_tsv_df_col2.to_csv(r"data/temp.csv", index=False)
    return data_tsv_df_col2


def get_all_punctuation(data_df):
    p_list = []
    for index, row in data_df.iterrows():
        rule = re.compile(r"\W")
        row_p = rule.findall(row[1])
        for p in row_p:
            if p not in p_list:
                p_list.append(p)
    with open(r"data/all_punctuation.txt", 'w') as f:
        for p in p_list:
            f.write(p)
            f.write('\n')
    return p_list


def clean_data(data_df):
    """
    - 清洗数据 https://zhuanlan.zhihu.com/p/517220095
    """
    # * 获取标点: 匹配非英文和非数字和非中文
    all_punctuation =  get_all_punctuation(data_df)
    # * 删除多余符号
    clean_data_df = del_
    for index, row in data_df.iterrows():
        re.sub(r'\W{2,}', '', row)
    # * 删除指定符号
    

    print("end")


def build_dataset():
    """
    - 加载数据
    - 清洗数据
    - 中文分词 https://github.com/fxsjy/jieba
    """
    # 加载数据
    data_df = load_data()

    data_clean = clean_data(data_df)

    for index, row in data_df.iterrows():
        seg_obj = jieba.cut(row["ACCEPT_CONTENT"])
        seg_str = " ".join(seg_obj)
        seg_list = seg_str.split(" ")
        print(seg_obj)
        print(seg_str)
        print(seg_list)


def main():
    """
    https://blog.csdn.net/kobeyu652453/article/details/106551131

    - 中文预处理
        - 构建数据集
    """
    build_dataset()


if __name__ == "__main__":
    main()
