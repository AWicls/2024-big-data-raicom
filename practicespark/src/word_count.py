# 词频统计主模块
# 实现词频统计核⼼逻辑，将单词进⾏计数并保存结果。

from collections import Counter

import pandas as pd


def count_words(words):
    word_count = Counter(words)
    return word_count


def save_results(word_count, output_file):
    df = pd.DataFrame(word_count.item(), columns=["word", "count"])
    df.to_csv(output_file, index=False)
