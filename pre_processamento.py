import random
import numpy as np
import pandas as pd

def pre_processamento(df_train, df_test):
  train = df_train
  test = df_test

  def data(n, seed):

      datas = []
      
      random.seed(seed)
      for i in range(n):
          dia_maximo = 30
          dia_minimo = 1
          mes_maximo = 12
          mes_minimo = 1
          
          dia = int(round(random.random() * (dia_maximo - dia_minimo) + dia_minimo, 0))
          mes = int(round(random.random() * (mes_maximo - mes_minimo) + mes_minimo, 0))
          
          datas.append(str(dia)+'-'+str(mes)+'-2018')
          
      return datas

  def estoque(n, seed):

      np.random.seed(seed)
      mu, sigma = 1, 20
      s = np.random.normal(mu, sigma, n)
      s[s < 0] = s[s < 0] * -0.5
      s = s.astype(int)
      s[s < 1] = 1
      
      return s

  train['date']  = data(n = train.shape[0], seed = 10)
  train['stock'] = estoque(n = train.shape[0], seed = 10)

  test['date']  = data(n = test.shape[0], seed = 15)
  test['stock'] = estoque(n = test.shape[0], seed = 15)

  train.drop('train_id', axis=1, inplace=True)

  rotulos = [i for i in train['category_name'].fillna('missing/missing/missing').str.split("/")]

  gen_cat = []
  sub1_cat = []
  sub2_cat = []

  for i in range(0,len(rotulos)):
    gen_cat.append(rotulos[i][0])
    sub1_cat.append(rotulos[i][1])
    sub2_cat.append(rotulos[i][2])

  train['gen_cat'] = gen_cat
  train['sub1_cat'] = sub1_cat
  train['sub2_cat'] = sub2_cat

  train = train.drop('category_name' , axis = 1)

  train['datetime_date'] = pd.to_datetime(train['date'], format = "%d-%m-%Y", errors = 'coerce')
  train.drop('date', axis = 1, inplace=True)
  train['datetime_month'] = train['datetime_date'].dt.month
  train['datetime_year'] = train['datetime_date'].dt.year

  train = train.drop('datetime_date', axis = 1)
  train = train.drop(train[train['price'] == 0].index)

  return train,test