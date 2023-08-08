from extrator import ExtratorURL
from consulta_cotacao import CotacaoAtual

url = "bytebank.com/cambio?moedaOrigem=USD&moedaDestino=BRL&valor=100"

extrator_url = ExtratorURL(url)

moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
valor = float(extrator_url.get_valor_parametro('valor'))

cotacao_dolar_real = CotacaoAtual(moeda_origem, moeda_destino)

print(cotacao_dolar_real)
print(f'{valor} {moeda_origem} = {cotacao_dolar_real.get_valor_convertido(valor)} {moeda_destino}')