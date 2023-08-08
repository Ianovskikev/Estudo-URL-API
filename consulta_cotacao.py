import requests

class CotacaoAtual:
    def __init__(self, moedaOrigem, moedaDestino):
        self._moeda_origem = moedaOrigem
        self._moeda_destino = moedaDestino

    def requisicao_api(self):
        resposta = requests.get(
            f'https://economia.awesomeapi.com.br/json/last/{self._moeda_origem}-{self._moeda_destino}')
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def get_valor_cotacao(self):
        dados_cotacao = self.requisicao_api()
        if type(dados_cotacao) is not int:
            cotacao = float(
                dados_cotacao[f'{self._moeda_origem}{self._moeda_destino}']['low'])
            return cotacao
        else:
            return dados_cotacao

    def get_valor_convertido(self, valor):
        dados_cotacao = self.requisicao_api()
        if type(dados_cotacao) is not int:
            cotacao = float(
                dados_cotacao[f'{self._moeda_origem}{self._moeda_destino}']['low'])
            valor_convertido = valor * cotacao
            return valor_convertido
        else:
            return dados_cotacao

    def __str__(self):
        return f'A Cotação atual é 1 {self._moeda_origem} = {self.get_valor_cotacao()} {self._moeda_destino}'
