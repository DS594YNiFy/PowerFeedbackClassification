import pandas as pd
import jieba 


def load_data():
    data_tsv_df = pd.read_csv(
        r"data/temp.tsv", sep="\t", header=0, encoding="gbk"
    )
    data_tsv_df_col2 = data_tsv_df.loc[:, ['BUSI_TYPE_CODE', 'ACCEPT_CONTENT']]
    data_tsv_df_col2.to_csv(r"data/temp.csv", index=False)
    return data_tsv_df_col2


def build_dataset():
    """
    - 加载数据
    - 清洗数据
    - 中文分词
    """
    # 加载数据
    data_df = load_data()


def main():
    """
    - 中文预处理
        - 构建数据集
    """
    build_dataset()


if __name__ == "__main__":
    main()
