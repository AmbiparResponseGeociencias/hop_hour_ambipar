# Difusão de Temperatura - hop_hour_ambipar

Este programa calcula a difusão de temperatura em uma garrafa padrão de cerveja
de 600 mL, considerando a temperatura do líquido e a temperatura do ambiente.

O modelo é baseado na solução numérica da equação difusão de temperatura (Eq. 1), considerando a densidade ($\rho$), a capacidade de calor específica ($c_p$) e a condutividade térmica ($\kappa$) da cerveja, dados por Bhuvaneswari & Anandharamakrishnan (2014).

$\displaystyle \frac{\partial T}{\partial t} = \left(\frac{\kappa}{c_p * \rho} \right) * \left(\frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} \right)$     Eq. 1

O esquema numérico é baseado na resolução numérica das equações diferenciais utilizando
o método de diferenças finitas para as primeiras e segundas derivadas. A malha do modelo é
construída de modo a acompanhar o formato da garrafa.

**Uso**:

1. Editar ./config/simulation_config.jason
  
  {  
  "beer_initial_temperature": 10, # temperatura inicial do líquido em °C  
  "room_temperature": 22,         # temperatura do ambiente em °C  
  "grid_directory": "path",       # caminho do diretório com a malha  
  "dt": 0.00001,                  # passo de tempo do modelo em segundos  
  "final_time":  600,             # tempo total de simulação em segundos  
  "beer_density": 1048,           # densidade do líquido  
  "save_path": "path",            # caminho para salvar os resultados  
  "save_interval": 10             # intervalo de saída dos resultados em segundos  
  }

  2. Executar o programa principal
  >> python main.py

  **Pré-requisitos**:

  * python
  * numpy
  * matplotlib

**Disclaimer**:

Este programa foi concebido de forma exclusiva para a geração de resultados numéricos com o propósito de ensino e informação. Embora a física implementada no modelo seja correta, sua utilização está restrita às finalidades expressas neste README. A Ambipar Response Geociências e seus colaboradores não assumem qualquer responsabilidade por danos decorrentes do uso indevido deste modelo.

**Créditos**:

Leonardo Carvalho de Jesus * 2024  
Ambipar Response Geociências

