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

   - Os dados de movimentação dos produtos são manipulados diretamente no sistema, com atualizações manuais realizadas pelos responsáveis por cada setor.
     
   - Os dados podem ser exportados automaticamente para um arquivo Excel, com informações sobre o produto, setor de origem, destino e horário da movimentação.
   
### 📊 **Visualização e Interatividade**

   - O sistema oferece um layout visual com a exibição de produtos em cada setor, permitindo um acompanhamento visual do fluxo de produção.
     
   - Cada célula do dashboard pode ser clicada para registrar ou atualizar a movimentação do produto.
     
   - O dashboard exibe as métricas de produção, como o total de produtos em andamento e o número de produtos finalizados.

### 💾 **Exportação Automática**

   - O histórico das movimentações é exportado automaticamente para um arquivo Excel, com os seguintes campos:
     
     - Produto, Origem, Destino, DataHora.

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

### ▶️ Rodar o Programa

1. **Tenha o Python instalado**
   
   Recomendado: Python 3.8+

2. **Instale as dependências do projeto:**

   No terminal (ou prompt de comando), execute o comando:

   ```bash
   pip install dash pandas

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
