# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from graficos import Linha, Scatter
from gera_graficos import GeradorGraficos
import datetime
from findata import DadosMercado


start = datetime.datetime(2022,1,1)
end = datetime.datetime(2022,6,30)
stocks = ['FBOK34.SA', 'GOGL34.SA','AMZO34.SA', 'AAPL34.SA']
dados = DadosMercado(inicio=start,fim=end,stocks=stocks)

df_prices = dados.preco()
linha = Linha(df=df_prices, title='Preços dos Ativos')
grafico_preco = GeradorGraficos(grafico=linha).cria_graficos()

df_retornos = dados.retorno()
linha_ret = Linha(df=df_retornos, title='Retorno dos Ativos')
grafico_retorno = GeradorGraficos(grafico=linha_ret).cria_graficos()

markdown_text = '''
###
O Dashboard abaixo apresenta graficos com preço e taxa de retorno de 
4 empresas do segmento de tecnologia cotadas na BVSP. 

'''

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

colors = {
    'background': '#111111',
    'text': '#ADFF2F'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, 
                    children=[
                        html.H1(
                            children='Graficos Financeiros',
                            style={
                                'textAlign': 'center',
                                'color': colors['text']
                            }
                        ),

    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Markdown(children=markdown_text,
        style={
            'textAlign': 'center', 
            'color': colors['text'],
        }
    ),

    dcc.Graph(
        id='example-graph-1',
        figure=grafico_preco,
        style={'width': '100vh', 'height': '60vh','display': 'inline-block'}
    ),

    dcc.Graph(
        id='example-graph-2',
        figure=grafico_retorno,
        style={'width': '100vh', 'height': '60vh','display': 'inline-block'}
    ),
])

if __name__ == '__main__':
    
    app.run_server(debug=True)
