def peso_status(status):
mapa = {
"Concluído": 1,
"Em andamento": 0.5,
"Atrasado": 0.2,
"Não iniciado": 0,
"Não se aplica": 1
}
return mapa.get(status, 0)
