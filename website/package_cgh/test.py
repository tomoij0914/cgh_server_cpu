import csv

def func():
	# ファイルのパスを指定
	file = './parameter2.csv'

	#####################################
	#ファイルをオープン(3)
	f = open(file,'r')
	# 行数の取得
	count = 0
	for line in f:
		count += 1

	#####################################
	# 2次元リストの定義
	buf = [[] for i in range(count)]

	#############################
	# ファイルをオープン
	f = open(file,'r')
	# ファイルからデータを読み込み
	rows = csv.reader(f)
	j = 0
	# for文で行を1つずつ取り出す
	for row in rows:
		buf[j] = row
		j += 1

	#############################
	print(buf[0])
	# 開いたファイルをクローズ
	f.close()

if __name__ == "__main__":
    func()