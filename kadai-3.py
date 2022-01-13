import matplotlib.pyplot as plt
x = [1452, 1796, 1894, 2584, 2735, 3447]
y = [3231, 3747, 3726, 5853, 8866, 10913]

plt.scatter(x, y)
plt.xlabel("オープンキャンパス参加者数(人)", fontname="MS Gothic")
plt.ylabel("志願者数(人)", fontname="MS Gothic")
plt.show()