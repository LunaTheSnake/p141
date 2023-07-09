import pandas as pd

df1 = pd.read_csv('shared_articles.csv')
df2 = pd.read_csv('users_interactions.csv')

df1.columns = ['timestamp','eventType','contentId','authorPersonId','authorSessionId','authorUserAgent','authorRegion','authorCountry','contentType','url','title','text','lang']
df2= df2.merge(df1,on='timestamp')


df2.head(5)

C = df2['authorSessionId'].mean()
print(C)

m = df2['sessionId'].quantile(0.9)
print(m)

articles = df2.copy().loc[df2['sessionId'] >= m]
print(articles.shape)

def ids(x, m=m, C=C):
   v = x['authorSessionId']
   R = x['sessionId']
   return (v/(v+m) * R) + (m/(m+v) * C)


articles['score'] = articles.apply(ids, axis=1)

articles = articles.sort_values('score', ascending=False)
articles[['title', 'sessionId', 'authorSessionId', 'score']].head(10)

