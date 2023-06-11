import pandas as pd
import matplotlib.pyplot as plt

#ファイル名の入力
filename = input("ファイル名を入力してください: ")

# CSVファイルを読み込む
data = pd.read_csv(filename)

# "Date"列を日付型に変換
data['Date'] = pd.to_datetime(data['Date'])

# 株価の折れ線グラフを作成
plt.plot(data['Date'], data['Close'])

# グラフのタイトルと軸ラベルを設定
plt.title('Stock Price')
plt.xlabel('Date')
plt.ylabel('Close Price')

# x軸のラベルを斜めに表示
plt.xticks(rotation=45)

# グラフを表示
plt.show()