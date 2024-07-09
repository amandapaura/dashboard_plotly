# dashboard_plotly
## <font color='lime'> Codes to create a Dashboard with Plotly - Stock Price Data </font>

Nesse projeto fiz uma amostra de dashboard usando o *Plotly Dash* com dados financeiros do *Yahoo Finance*.

O projeto contém 4 módulos dos quais:

O módulo *"findata.py"* gera os dados financeiros que iremos exibir nos gráficos. Contém uma classe que busca os dados dos ativos na api do Yahool Finance, com métodos que fazem calculos financeiros e retornam um dataframe.

Os módulos *"graficos.py"* e *"gera_graficos.py"* são uma fábrica abstrata de diferentes tipos de gráficos. O primeiro módulo gera os graficos (inseri nesse trabalho os gráficos de linha e dispersão) e o segundo cria o layout do gráficos prontos para serem exibidos no dash. 

O módulo *"app.py"* é a construção do dash. Devemos inserir os dados financeiros, criar e grar os gráficos, textos e tudo que quisermos, e pelo Dash do Plotly montar o dashboard. A função __main__ gera o gráfico no localhost. 

Para rodar o grafico basta abrir o terminal no diretorio e dar o comando: 
*python app.py*

A ideia é que vocês aproveitem a estrutura para brincar e criar diferentes layouts de dashboards. 

=)
