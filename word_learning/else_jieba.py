import pandas # import pandas
from pandas import Series as sr, DataFrame as df
from clooections import Counter as cr   # import Counter to count number
import jieba.posseg as pseg  # import jieba label

path = ''   # file path
data1 = df.read_csv(path, sep= )
l = len(data1)
df1 = df(columns=['word', 'type'])
for i in range(l):
    words = pseg.cut(data1.ix[i][x])
    for t in words:
        df2 = pd.DataFrame([t.word,t.flag], columns=data2.columns)
        df1.append(df2,ignore_index=True)
de3 = df1.groupby(['word','type']).count()
 
