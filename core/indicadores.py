from core.engine import peso_status

def indice_maturidade(itens):
total = 0
realizado = 0
for i in itens:
peso = i['peso']
total += peso
realizado += peso * peso_status(i['status'])
if total == 0:
return 0
return round((realizado / total) * 100, 2)
