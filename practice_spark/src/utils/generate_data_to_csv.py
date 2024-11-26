import pandas as pd
import numpy as np
import random
import string


# 生成随机数据
def generate_random_data(num_rows=100):
    data = {
        'Name': [''.join(random.choice(string.ascii_letters) for _ in range(5)) for _ in range(num_rows)],
        'Age': [random.randint(18, 100) if random.random() > 0.1 else np.nan for _ in range(num_rows)],
        'Salary': [random.uniform(30000, 100000) if random.random() > 0.1 else np.nan for _ in range(num_rows)],
        'City': [random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']) for _ in range(num_rows)],
        'Email': [f"{''.join(random.choice(string.ascii_lowercase) for _ in range(5))}@example.com" for _ in
                  range(num_rows)],
        'Date': [pd.Timestamp(year=random.randint(2000, 2023), month=random.randint(1, 12), day=random.randint(1, 28))
                 for _ in range(num_rows)]
    }
    df = pd.DataFrame(data)
    return df


# 生成数据
df = generate_random_data(100000)

output_path = r'../../data/generated_data.csv'
# 保存为 CSV 文件
df.to_csv(output_path, index=False)

print("Data generated and saved to 'generated_data.csv'")
