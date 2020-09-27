import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)
Estados = ['Ensolarado','Chuvoso']

TransicaoEstados = [['EnEn','EnChu'],['ChuChu','ChuEn']]
MatrizTransicao = [[0.80,0.20],[0.25,0.75]]

previsaoTempoLista = list()
NumDias = 365
PrevisaoHoje = Estados[0]

for i in range(1, NumDias):
  if PrevisaoHoje == 'Ensolarado':        
    Condicao = np.random.choice(TransicaoEstados[0],replace=True,p=MatrizTransicao[0])

    if Condicao == 'EnEn':
      pass
    else:
      PrevisaoHoje = 'Chuvoso'

  elif PrevisaoHoje == 'Chuvoso':
    Condicao = np.random.choice(TransicaoEstados[1],replace=True,p=MatrizTransicao[1])

    if Condicao == 'ChuChu':
      pass
    else:
      PrevisaoHoje = 'Ensolarado'
  
  previsaoTempoLista.append(PrevisaoHoje)
  print(PrevisaoHoje)

plt.plot(previsaoTempoLista)
plt.show()
