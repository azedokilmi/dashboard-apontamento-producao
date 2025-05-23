# 📊 Dashboard de Apontamento de Produtos

Este projeto tem como objetivo monitorar a movimentação de produtos nas diferentes fases de produção de uma fábrica, proporcionando uma visão clara e detalhada do status de cada item. Através de um dashboard interativo, os responsáveis administrativos podem acompanhar o andamento da produção, identificar gargalos, medir o cumprimento das metas e visualizar o histórico das movimentações de forma dinâmica.

---

## ⚙️ Como Funciona?

### 🧠 Funcionalidades

- Visualização do status de produtos em diferentes setores da fábrica.
  
- Acompanhamento do progresso da produção e cumprimento de metas.
  
- Histórico das movimentações de produtos entre setores, com exportação para Excel.
  
- Interface interativa para movimentação manual dos produtos entre os setores.
  
- Filtros para facilitar a busca e visualização de produtos.
  
- Exibição de métricas como total de produtos em cada setor e percentual de progresso.
  
### 📥 **Entrada de Dados**

   - Os dados inciais de processamento são importados de uma planilha do Excel `.xlsx` (👉 [Clique aqui para visualizar o arquivo](https://github.com/azedokilmi/dashboard-apontamento-producao/blob/main/apontamento_inicial.xlsx)) onde se tem a informação de qual produto esta presente em determinado setor.

   ![Prévia da Planilha de Dados Inicial.xlsx](https://github.com/azedokilmi/dashboard-apontamento-producao/blob/main/previa-inicial.png)
     
   - Os dados de movimentação dos produtos são manipulados diretamente no sistema, com atualizações manuais realizadas pelos responsáveis por cada setor.
   
### 📊 **Visualização e Interatividade**

   - O sistema oferece um layout visual com a exibição de produtos em cada setor, permitindo um acompanhamento visual do fluxo de produção.
     
   - Cada célula do dashboard pode ser clicada para registrar ou atualizar a movimentação do produto.
     
   - O dashboard exibe as métricas de produção, como o total de produtos em andamento e o número de produtos finalizados.

### 💾 **Exportação de Dados**

   - O histórico das movimentações é exportado automaticamente para uma planilha em Excel `.xlsx` (👉 [Clique aqui para visualizar o arquivo](https://github.com/azedokilmi/dashboard-apontamento-producao/blob/main/historico-movimentacoes.xlsx)) com os seguintes campos:
     
     - Produto, Origem, Destino, DataHora.

   - Caso seja necessário atualizar a planilha de dados de importação é possível através da opção "ATUALIZAR" do dashboard baixar outra planilha em Excel `.xlsx` (👉 [Clique aqui para visualizar o arquivo](https://github.com/azedokilmi/dashboard-apontamento-producao/blob/main/apontamento-final.xlsx)) com as informações que foram registradas até o momento, para guardar essas informações e atualizar no dia seguinte a planilha de importação.

   ![Prévia da Planilha de Atualização.xlsx](https://github.com/azedokilmi/dashboard-apontamento-producao/blob/main/previa-final.png)

---

## 🧪 Detalhes Técnicos

- O sistema foi desenvolvido em Python utilizando a biblioteca Dash para a criação de interfaces web interativas.
  
- O dashboard é projetado para ser visual e dinâmico, permitindo que os usuários administrativos possam interagir diretamente com o sistema e registrar as movimentações, podendo atualizar os dados quando quiser salvando em um arquivo Excel pelo botão "ATUALIZAR" e podendo retornar todos os produtos para a primeira etapa da produção pelo botão "REINICIAR".
  
- O projeto inclui um mecanismo de atualização em tempo real, com a possibilidade de integração futura com sistemas ERP (TOTVS, SAP, etc.) para atualizar automaticamente o fluxo de produção.

---

## 🚀 Passo a Passo da Execução

### 📁 Preparar os Arquivos

#### `APONTAMENTO-DE-PRODUTOS.py`

- Script principal do projeto que deve estar localizado em sua máquina.

- Para a sua execucação é necessário fazer upload do arquivo no programa do JupyterLab, VS Code ou outros programas de codagem para ter interatividade com o dashboard.

- Ambos os programas são gratuitos e de fácil acesso, sendo necessário apenas a instalação deles e posteriormente a instalação das bibliotecas em questão.

### ▶️ Rodar o Programa

Para rodar o programa, siga os passos abaixo:

1. **Tenha o Python instalado e Programa de Codagem (Jupyter Lab ou VS Code)**
   
   Recomendado: Python 3.8+

2. **Instale as dependências do projeto** (caso ainda não tenha feito):
   
   Abra o terminal do programa de codagem e execute o seguinte comando para instalar as bibliotecas necessárias:

   ```bash
   pip install dash pandas
   ```

4. **Execute o programa**:
  
   No programa faça o upload do arquivo `.py` (👉 [Clique aqui para visualizar o arquivo](https://github.com/azedokilmi/dashboard-apontamento-producao/blob/main/APONTAMENTO-DE-PRODUTOS.py)) que pode estar em qualquer lugar da máquina (preferencialmente na área de trabalho):
   
   Após a execução do script pelo programa, o dashboard será criado dentro do programa e os arquivos de saída como histórico e dados atualizados serão gerados na área de trabalho.

## 📂 O que será Gerado

Após rodar o programa, teremos então a geração do dashboard.

- 📈 **Dashboard Interativo**
  
  - Um dashboard com opção dinâmica de movimentar os produtos pelos setores a medida que eles forem sendo apontados e seus processos forem sendo finalizados até a etapa final de entrega ao cliente final. Além do informativo sobre o progresso da fabricação diária da fábrica.
 
  ![Prévia do Dashboard](https://github.com/azedokilmi/dashboard-apontamento-producao/blob/main/previa-dashboard.png)

- 📋  **Histórico de Movimentação**
  
  - Um arquivo detalhado de todos os movimentos que foram feitos com o produto, ou seja, todas as suas transições pelos setores e suas respectivas datas e horas de movimentação.
 
  ![Prévia da Planilha de Histórico de Movimentações .xlsx](https://github.com/azedokilmi/dashboard-apontamento-producao/blob/main/previa-historico.png)

### 🛠️ Planos futuros

- ✅ **Controle por setor**: cada setor poderá mover apenas os produtos sob sua responsabilidade.
  
- 🔗 **Integração automática com ERP/APS** (como TOTVS, SAP, Drummer):
  
  - Produtos programados entrarão automaticamente no sistema no início do dia.
    
  - A movimentação entre setores será feita a partir de eventos no sistema ERP.
 
- 📋 **Informações enriquecidas**:
  
  - Nome completo do produto.
    
  - Cliente responsável.
    
  - Horário exato da mudança de setor.
    
  - Outros dados relevantes conforme necessidade.

### 💡 Possíveis melhorias adicionais

- Dashboard de **KPIs por turno/dia/setor**.
  
- **Categorizacão dos produtos** por tipo ou prioridade.
  
- Interface de **usuários com permissões específicas**.
  
- **Notificações por e-mail ou sistema** ao detectar gargalos ou produtos parados por muito tempo.
  
- Integração com **banco de dados SQL/PostgreSQL** para maior escalabilidade.

- Criação de um executável que permita que o dashboard seja aberto de forma atualizada com o banco de dados com apenas um clique, não sendo necessário ser executado o script toda vez que ele for usado e tendo que importar dados de planilha Excel.

---

## ✍️ Autor

Feito com dedicação por Pedro Cicilini de Nadai 💪\
GitHub: [@azedokilmi](https://github.com/azedokilmi)
