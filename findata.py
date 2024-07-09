import yfinance as yf

class DadosMercado:
    def __init__(self, inicio, fim, stocks):
        self.inicio = inicio
        self.fim = fim
        self.stocks = stocks

    def _get_adjclose(self):
        price = yf.download(self.stocks, start= self.inicio, end= self.fim)
        return price['Adj Close']

    def preco(self):
        price = self._get_adjclose()
        return price.reset_index()
    
    def retorno(self):
        price = self._get_adjclose()
        df_retornos = price/price.shift(1)
        return df_retornos.reset_index()
