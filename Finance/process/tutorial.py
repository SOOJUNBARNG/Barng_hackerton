import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# https://signate.jp/competitions/1337/tutorials/61

train = pd.read_csv('data/train.csv', index_col=0) # 学習用データ
test = pd.read_csv('data/test.csv', index_col=0) # 学習用データ   # 評価用データ
sample_submit = pd.read_csv('data/sample_submission.csv', index_col=0, header=None) # 応募用サンプルファイル


train[['DisbursementGross',  'GrAppv', 'SBA_Appv']]= \
train[['DisbursementGross',  'GrAppv', 'SBA_Appv']].applymap(lambda x: x.strip().replace('$', '').replace(',', ''))
#testデータも同様に変換します
test[['DisbursementGross',  'GrAppv', 'SBA_Appv']]= \
test[['DisbursementGross',  'GrAppv', 'SBA_Appv']].applymap(lambda x: x.strip().replace('$', '').replace(',', ''))
train[['DisbursementGross',  'GrAppv', 'SBA_Appv']].head()

# train[std_columns] の相関行列を求める
corr_matrix = train[numeric_columns].corr()

# 相関行列を図示
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Standardized Columns')
plt.show()


import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

train_numeric = train[numeric_columns]

# データの準備
X = train_numeric.drop('MIS_Status', axis=1)  # 特徴量
y = train_numeric['MIS_Status']               # 目的変数

# データの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# LightGBMモデルの設定
lgbm = lgb.LGBMClassifier()

# モデルの訓練
lgbm.fit(X_train, y_train)

# モデルの評価
y_pred = lgbm.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

# Accuracy: 0.8994327582131884

# このコンペティションの評価指標はMeanF1Score（MacroF1Score）ですので、それでスコアも計算してみます。


mean_f1 = f1_score(y_test, y_pred, average='macro')
print(f'Mean F1 Score: {mean_f1}')

# Mean F1 Score: 0.5698691806941848

# 数値データ以外の特徴量を学習に取り入れる。
# チュートリアルでは比較的計算時間が短くて済むLightGBMを用いましたが、他の手法を試してみるのも良いかもしれません。
# また、ハイパーパラメータも色々変えて精度を向上させましょう。
# 今回調べているのは、いわゆる「貸し倒れ確率」です。日本の個人向け融資では貸し倒れ確率は借りた額や借りる人の収入に主に依存することが知られています。
# この様な傾向が今回考えている米国中小向けのローンで成立するかをもし良かったら確認してみましょう。

