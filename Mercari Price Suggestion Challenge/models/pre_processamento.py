import random
import numpy as np
import pandas as pd
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords



   #Função para "separação" de palavras, ex: Can't -> can not, objetivo de facilitar a limpeza, aonde não serão criadas duas palavras para cant/can not.
    # Será feito para diversas palavras com a mesma condição.
def text_preprocess(phrase):

    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    
    phrase = re.sub('https?://\S+| www.\S+', ' ', phrase) #Remoção de qualquer site que possa ter no nosso dataset
    phrase = re.sub("[^a-zA-Z0-9' \n\.]", ' ', phrase)  #excluindo tudo o que não for letra e numero.
    phrase = re.sub(r'([a-z0-9])\1{2,}', " ", phrase) #retirando letras repetidas mais de 2 vezes seguidas ex: "ele vaaai" -> "ele vai"
    phrase = re.sub(r'\s+[0-9]{3,}\s+', " ", phrase)  # removendo numeros muito grandes com 3 digitos ou mais
    phrase = re.sub(r'\s+([a-zA-Z])\1{1,}\s+', " ", phrase) #removendo letras repetidas isoladas ex: ele zz vai -> ele vai
    
    
    phrase = re.sub(' +', ' ', phrase) #exclusão de espaços extras, ex: "eu    vou" -> "eu vou"

    phrase = phrase.lower() #passando para letra minúscula.

   
    return phrase


#Função proposta como adicional ao desafio do bootcamp, para adição de colunas de estoque e data.
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
    
  train['datetime_date'] = pd.to_datetime(train['date'], format = "%d-%m-%Y", errors = 'coerce')
  train.drop('date', axis = 1, inplace=True)
  train['datetime_month'] = train['datetime_date'].dt.month
  train['datetime_year'] = train['datetime_date'].dt.year

  train = train.drop('datetime_date', axis = 1)
  train = train.drop(train[train['price'] == 0].index)

  return train,test


#Função pra juntar as colunas de texto em uma só
def textcolumns_junct(df):

      #Preenchendo valores nulos com espaço em branco.
      df[["name",
          "brand_name",
          "item_description"]] = df[["name",                            
                                     "brand_name",
                                     "item_description"]].fillna(" ")
       

                                     
      df["item_description"] =   df["name"]+" "+df["brand_name"]+" "+ df["item_description"]
                                 
                            
      #Removendo colunas duplicadas
      df = df.drop(["name",
                    "brand_name"] , axis = 1)

   

      return df






#função para stemm dos textos, será inserida dentro da função nlp
def stemming(text):
    porter = PorterStemmer()
    stop_words = stopwords.words('english')
    
    result=[]
    for word in text:
        if word not in stop_words:
            result.append(porter.stem(word))
    return result

