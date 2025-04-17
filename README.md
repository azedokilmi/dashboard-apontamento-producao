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

   - Os dados inciais de processamento são importados de uma planilha do Excel `.xlsx` (👉 [Clique aqui para visualizar o arquivo]()) onde se tem a informação de qual produto esta presente em determinado setor.

   ![Prévia da Planilha .xlsx]()
     
   - Os dados de movimentação dos produtos são manipulados diretamente no sistema, com atualizações manuais realizadas pelos responsáveis por cada setor.
   
### 📊 **Visualização e Interatividade**

   - O sistema oferece um layout visual com a exibição de produtos em cada setor, permitindo um acompanhamento visual do fluxo de produção.
     
   - Cada célula do dashboard pode ser clicada para registrar ou atualizar a movimentação do produto.
     
   - O dashboard exibe as métricas de produção, como o total de produtos em andamento e o número de produtos finalizados.

### 💾 **Exportação Automática**

   - O histórico das movimentações é exportado automaticamente para uma planilha em Excel `.xlsx` (👉 [Clique aqui para visualizar o arquivo]()), com os seguintes campos:
     
     - Produto, Origem, Destino, DataHora.

     ![Prévia da Planilha .xlsx]()

---

## 🧪 Detalhes Técnicos

- O sistema foi desenvolvido em Python utilizando a biblioteca Dash para a criação de interfaces web interativas.
  
- O dashboard é projetado para ser visual e dinâmico, permitindo que os usuários administrativos possam interagir diretamente com o sistema e registrar as movimentações.
  
- O projeto inclui um mecanismo de atualização em tempo real, com a possibilidade de integração futura com sistemas ERP (TOTVS, SAP, etc.) para atualizar automaticamente o fluxo de produção.

---

## 🚀 Passo a Passo da Execução

### 📁 Preparar os Arquivos

#### `dashboard-apontamento-produtos.py`

- Script principal do projeto que deve estar localizado em sua máquina.

- Para a sua execucação é necessário fazer upload do arquivo no programa do JupyterLab ou VS Code, para ter interatividade com o dashboard.

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

3. **Execute o programa**:
  
   No programa faça o upload do arquivo `.py` (👉 [Clique aqui para visualizar o arquivo]()) que pode estar em qualquer lugar da máquina (preferência para área de trabalho):
   
   Após a execução do script, os arquivos de saída serão gerados na mesma pasta onde o programa foi executado.

   ```bash
   python APONTAMENTO-DE-PRODUTOS.py
   ```

## 📂 O que será Gerado

Após rodar o programa, os seguintes arquivos serão gerados:

- 📄 **Histórico de Movimentação**
  
  Histórico mostrando toda a movimentação de um produto pelos setores e seu horário de alteração. (👉 [Clique aqui para a planilha]()).
  
  ![Prévia do Histórico]()

- 📈 **Dashboard Interativo**
  
  Um dashboard com opção dinâmica de movimentar os produtos pelos setores e informativo sobre o progresso da fabricação diária da fábrica (👉 [Clique aqui para visualizar o dashboard]()).
  
  ![Prévia do Dashboard]()

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

---

## ✍️ Autor

Feito com dedicação por Pedro Cicilini de Nadai 💪\
GitHub: [@azedokilmi](https://github.com/azedokilmi)
