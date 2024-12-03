import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

activities = {
    "阅读": 50,
    "练习": 30,
    "视频学习": 40,
    "测验": 20,
    "项目实践": 60
}

plt.pie(activities.values(), labels=activities.keys())
plt.show()
