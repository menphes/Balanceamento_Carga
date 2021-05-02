arqEntrada = open('input.txt', 'r')
arqSaida = open('output.txt', 'w')
tick = 0
arr = []
listaServidores = {}
totalUsersServ = 0
numServidor = 1
counter = 0
qtdServidoresInativos = 0
custoTotal = 0
concluido = False

for cnt, line in enumerate(arqEntrada):
    if cnt == 0:
        ttask = int(line)
		if ttask >= 1 and ttask <= 10:
			continue
		else:
			print('Erro: Valor de ttask fora dos limites!')
			exit()
    elif cnt == 1:
        umax = int(line)
        if umax >= 1 and ttask <= 10:
			continue
		else:
			print('Erro: Valor de umax fora dos limites!')
			exit()
    else:
        arr.append(int(line))

while concluido == False:
    try:
        line = arr[counter]
    except:
        line = 0
    tick += 1

    if tick > ttask:
        try:
            pos = arr[tick-ttask-1]
        except:
            pos = 0
        for n in range(pos):
            for servidor in listaServidores:
                if listaServidores[servidor]['NumUser'] > 0:
                    listaServidores[servidor]['NumUser'] = int(listaServidores[servidor]['NumUser']) - 1
                    if listaServidores[servidor]['NumUser'] == 0:
                        listaServidores[servidor]['Status'] = 'Inativo'
                    break
                else:
                    listaServidores[servidor]['Status'] = 'Inativo'
        #counter += 1

    for i in range(line):
        totalUsersServ += 1
        if totalUsersServ <= umax:
            try:
                listaServidores['Servidor'+str(numServidor)]['NumUser'] = totalUsersServ
            except:
                listaServidores['Servidor'+str(numServidor)] = {'NumUser': totalUsersServ, 'Status': 'Ativo'}
        else:
            totalUsersServ = 1
            numServidor += 1
            listaServidores['Servidor'+str(numServidor)] = {'NumUser': totalUsersServ, 'Status': 'Ativo'}

    output = ''
    for j, servidor in enumerate(listaServidores):
        if listaServidores[servidor]['Status'] == 'Inativo':
            qtdServidoresInativos += 1
        else:
            try:
                listaServidores[servidor]['Tick'] += 1
            except:
                listaServidores[servidor]['Tick'] = 1
            output = output + str(listaServidores[servidor]['NumUser']) + ','
            qtdServidoresInativos = 0
    if output == '':
        #print('0')
        arqSaida.write('0\n')
    else:
        #print(output[:-1])
        arqSaida.write(output[:-1]+'\n')

    if arr[0] != 0:
        if qtdServidoresInativos == len(listaServidores):
            concluido = True

    counter += 1
    #print(listaServidores)

for servidor in listaServidores:
    custoTotal = custoTotal + (listaServidores[servidor]['Tick'] * 1)

#print(custoTotal)
arqSaida.write(str(custoTotal)+'\n')
arqEntrada.close()
arqSaida.close()
print('Processamento Concluido com Sucesso!')