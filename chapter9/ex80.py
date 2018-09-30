# 80. コーパスの整形
# 文を単語列に変換する最も単純な方法は，空白文字で単語に区切ることである．
# ただ，この方法では文末のピリオドや括弧などの記号が単語に含まれてしまう．
# そこで，コーパスの各行のテキストを空白文字でトークンのリストに分割した後，各トークンに以下の処理を施し，単語から記号を除去せよ．
#
# ・トークンの先頭と末尾に出現する次の文字を削除: .,!?;:()[]'"
# ・空文字列となったトークンは削除
#
# 以上の処理を適用した後，トークンをスペースで連結してファイルに保存せよ．
import bz2

input_file_name = "enwiki-20150112-400-r100-10576.txt.bz2"
output_file_name = "corpus_raw.txt"
enc = "utf-8"

tokens = []
with bz2.open(input_file_name, "rt", encoding=enc) as in_f:
    for line in in_f:
        # コーパスの各行のテキストを空白文字でトークン候補のリストに分割し、各トークンに以下の処理を施す
        for t in line.split(" "):
            # ・トークンの先頭と末尾に出現する次の文字を削除: .,!?;:()[]'"
            # 全角の‘’、“”も含まれているようなのでそれも追加
            t = t.strip().strip(".,!?;:()[]'\"‘’“”")
            # ・空文字列となったトークンは削除
            if t != "":
                # out_f.write(t + " ")  # この方法だと最後にスペースが入ってしまい、読み込み時に考慮する必要がある。
                tokens += [t]

# ファイルに出力する
with open(output_file_name, "w", encoding=enc) as out_f:
    print(*tokens, sep=" ", end="", file=out_f)