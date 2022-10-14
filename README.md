# Bootcamp_Blue

Bootcamp - Precificação dinâmica:  
Mercari Price Suggestion Challenge - Kaggle

https://www.kaggle.com/competitions/mercari-price-suggestion-challenge/overview


#   Sobre o projeto:

O projeto será separado em 5 sprints.

Para esse projeto foram adicionadas duas novas colunas, uma para estoque e outra para data.


#   Objetivo:

 O objetivo desse projeto é elaborar uma solução de Machine Learn para ser oferecido a sites de e-commerce, visando a otimização em suas sugestões de preço para o cliente. 

 Para alcançar o objetivo algumas etapas serão necessárias, primeiro, entendimento do negócio, como exemplo:

 -  Como funciona.
 -  Quão preciso é necessário ser.
 -  Quão rápido precisa ser.
 -  Otimização pensando na manutenção.


#   Etapas

- Exploração dos dados.
- Limpeza do dataset.
- Criação ou remoção de features.
- Criação ou removação de linhas.
- Elaboração de baseline.
- Avaliação de modelos.
- Ajuste de hiperparâmetros.



#   Dícionario de dados

- train_id or test_id: id do item no dataset.
- name: Título do item listado.
- item_condition_id: Condição do item listado, variando de 1 até 5.
- category_name: Categoria atribuida ao item listado, composta de 3 categorias, sendo a segunda uma subcategoria da primeira e a terceira da segunda.
- gen_cat: Categoria primária.
- sub1_cat:	Categoria secundária.
- sub2_cat:	Categoria terciária.
- brand_name: Marca do item listado.
- price: Valor do item vendido, o target. O valor está em USD.
- shipping: 1 para frete pago pelo vendedor e 0 para o frete pago pelo comprador.
- item_description: Descrição dos item listado.
- datetime_month: Mês da venda.
- datetime_year: Ano da venda.



# Bibliotecas usadas no modelo:
    
- Python                       3.10.4
- pandas                       1.4.2
- numpy                        1.22.3
- regex                        2022.6.2
- scipy                        1.8.0
- scikit-learn                 1.0.2
- nltk                         3.7
- keras                        2.9.0
