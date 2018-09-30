# 89. 加法構成性によるアナロジー
# 85で得た単語の意味ベクトルを読み込み，vec("Spain") - vec("Madrid") + vec("Athens")を計算し，
# そのベクトルと類似度の高い10語とその類似度を出力せよ．
from chapter9 import ex86, ex88

# 単語文脈行列を読み込む
X_300 = ex86.load_matrix()
index_t = ex86.load_index_t()

vector = X_300[index_t["Spain"]] - X_300[index_t["Madrid"]] + X_300[index_t["Athens"]]
print(ex88.get_similar_words(vector, 10, X_300, index_t))
