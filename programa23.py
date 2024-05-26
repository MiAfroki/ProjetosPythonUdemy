import json

log = "-- Log do sistema --\n"
log += "Lendo arquivo\n"

arquivo = open('dados.json', 'r') # r = read = ler
info = arquivo.read()
# print(info)
dados = json.loads(info)

log += "Alterando 'casado' para false\n"
dados['casado'] = False

log += "Gravando novo arquivo\n"
novo_arquivo = open('dados_novo.json', 'w') # w = write = escrever
novos_dados = json.dumps(dados)
novo_arquivo.write(novos_dados)
novo_arquivo.close()

log += "Adicionando ao novo arquivo\n"
novo_arquivo = open('dados_novo.json', 'a') # a = append = incrementar
novo_arquivo.write(', { "teste": "ok" }')
novo_arquivo.close()

arquivo_log = open('log.txt', 'w') 
arquivo_log.write(log)
arquivo_log.close()