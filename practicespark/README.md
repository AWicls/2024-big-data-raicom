```
word_count_project/
│
├── data/
│ └── word.csv # 原始数据⽂件
│
├── src/
│ ├── __init__.py # 初始化⽂件
│ ├── data_loader.py # 数据加载模块
│ ├── word_count.py # 词频统计主模块
│ ├── hive_integration.py # Hive 查询与数据整合模块
│ └── hdfs_operations.py # HDFS 读写操作模块
│
├── config/
│ └── config.yaml # 配置⽂件（如 HDFS、Hive、Spark 等相关配
置）
│
├── results/
│ └── word_count_output.csv # 输出结果⽂件（包含每个单词的计数结果）
│
├── logs/
│ └── word_count.log # 运⾏⽇志
│
└── README.md # 项⽬说明⽂档
```
