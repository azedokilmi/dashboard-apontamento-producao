import dash
from dash import html, Output, Input, State, ctx, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import datetime
import os

# Define os nomes dos setores
sectors = [
    "SETOR MONTAGEM DE BASE",
    "SETOR DE PINTURA",
    "SETOR ACABAMENTO FINAL",
    "SETOR DE EXPEDIÇÃO",
    "PRODUTO LIBERADO"
]

# Caminho para o histórico
CAMINHO_HISTORICO = r"C:\Users\pcicilini.CORP\Desktop\historico_movimentacoes.xlsx"

# Função para carregar planilha no formato: setores em linhas, produtos em colunas
def carregar_planilha_por_setor(caminho_arquivo):
    df = pd.read_excel(caminho_arquivo, header=None)
    setores_lidos = df[0].tolist()
    produtos_por_setor = []

    for setor_padrao in sectors:
        if setor_padrao in setores_lidos:
            idx = setores_lidos.index(setor_padrao)
            produtos = df.iloc[idx, 1:].dropna().astype(str).tolist()
            produtos_por_setor.append(produtos)
        else:
            produtos_por_setor.append([])

    return produtos_por_setor

# Função para salvar o histórico de movimentações em Excel
def salvar_historico(produto, origem, destino):
    df = pd.DataFrame([{
        "Produto": produto,
        "Origem": origem,
        "Destino": destino,
        "DataHora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }])
    
    if os.path.exists(CAMINHO_HISTORICO):
        df_existente = pd.read_excel(CAMINHO_HISTORICO)
        df = pd.concat([df_existente, df], ignore_index=True)
    
    df.to_excel(CAMINHO_HISTORICO, index=False)

def salvar_planilha_por_setor(state, caminho_saida=r"C:\Users\pcicilini.CORP\Desktop\apontamento_final.xlsx"):    
    max_len = max(len(linha) for linha in state)
    data = []

    for i, setor in enumerate(sectors):
        linha = [setor] + state[i] + [""] * (max_len - len(state[i]))
        data.append(linha)

    df = pd.DataFrame(data)
    df.to_excel(caminho_saida, index=False, header=False)

# Carrega o estado inicial da planilha
initial_state = carregar_planilha_por_setor(r"C:\Users\pcicilini.CORP\Desktop\apontamento_inicial.xlsx")

# Função para calcular as métricas
def calcular_metricas(state):
    try:
        total = sum(len(row) for row in state)
        finalizados = len(state[-1]) if state else 0
        andamento = total - finalizados
        progresso = f"{(finalizados / total * 100):.1f}%" if total else "0%"
    except Exception as e:
        total = andamento = finalizados = 0
        progresso = "0%"

    return total, andamento, finalizados, progresso

# Geração da grid visual com botões por setor
def generate_grid(state):
    grid = []
    for row_idx, row in enumerate(state):
        grid.append(html.H5(sectors[row_idx], className="mt-3"))
        grid.append(
            html.Div([
                html.Div([
                    html.Button(prod, id={"type": "product-button", "index": f"{row_idx}-{prod}"},
                                n_clicks=0, 
                                className=f"btn m-1 {'btn-success' if row_idx == len(sectors) - 1 else 'btn-outline-primary'}")
                    for prod in row
                ], className="d-flex flex-wrap")
            ])
        )
    return grid

# Layout principal
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"])

# Layout inicial com as métricas já calculadas
initial_total, initial_andamento, initial_finalizados, initial_progresso = calcular_metricas(initial_state)

app.layout = html.Div([
    dcc.Store(id="products-state", data=initial_state),
    html.H1("APONTAMENTO DE PRODUTOS", className="text-center my-4"),

    html.Div([
        dcc.Input(id="input-search", type="text", placeholder="Buscar produto...", className="form-control mb-4")
    ], className="container"),

    html.Div(id="grid", children=generate_grid(initial_state)),

    html.Div(id="dashboard", className="d-flex justify-content-around mt-4 mb-4", children=[
        dbc.Card([
            dbc.CardHeader("EM ANDAMENTO"),
            dbc.CardBody(html.H4(initial_andamento, className="card-title text-white"))
        ], color="warning", inverse=True, style={"width": "18%"}),

        dbc.Card([
            dbc.CardHeader("FINALIZADOS"),
            dbc.CardBody(html.H4(initial_finalizados, className="card-title text-white"))
        ], color="success", inverse=True, style={"width": "18%"}),

        dbc.Card([
            dbc.CardHeader("TOTAL"),
            dbc.CardBody(html.H4(initial_total, className="card-title text-white"))
        ], color="info", inverse=True, style={"width": "18%"}),

        dbc.Card([
            dbc.CardHeader("PROGRESSO"),
            dbc.CardBody(html.H4(initial_progresso, className="card-title text-white"))
        ], color="primary", inverse=True, style={"width": "18%"})
    ]),

    html.Div([
        html.Button([html.I(className="fa fa-refresh"), " ATUALIZAR"], id="btn-atualizar", className="btn btn-warning mt-4"),
        html.Button([html.I(className="fa fa-repeat"), " REINICIAR"], id="btn-reiniciar", className="btn btn-danger mt-4"),
        html.Div(id="atualizar-feedback", className="mt-2 text-success")
    ], className="text-center")
])

# Callback de movimentação, reinício e atualização
@app.callback(
    [Output("grid", "children"),
     Output("products-state", "data"),
     Output("atualizar-feedback", "children"),
     Output("dashboard", "children")],
    [Input({"type": "product-button", "index": dash.ALL}, "n_clicks"),
     Input("btn-reiniciar", "n_clicks"),
     Input("btn-atualizar", "n_clicks"),
     Input("input-search", "n_submit")],  # Adicionando a interação de "Enter"
    [State("products-state", "data"),
     State("input-search", "value")],
    prevent_initial_call=True
)
def update_grid(n_clicks, btn_reiniciar, btn_atualizar, input_search_submit, state, search):
    triggered_id = ctx.triggered_id
    updated_state = [list(row) for row in state]
    feedback = dash.no_update

    if triggered_id == "btn-reiniciar":
        updated_state = carregar_planilha_por_setor(r"C:\Users\pcicilini.CORP\Desktop\apontamento_inicial.xlsx")
    elif isinstance(triggered_id, dict) and "-" in triggered_id.get("index"):
        row_idx, prod = triggered_id["index"].split("-")
        row_idx = int(row_idx)
        if prod in updated_state[row_idx] and row_idx < len(updated_state) - 1:
            updated_state[row_idx].remove(prod)
            updated_state[row_idx + 1].append(prod)
            salvar_historico(prod, sectors[row_idx], sectors[row_idx + 1])
    elif triggered_id == "btn-atualizar":
        salvar_planilha_por_setor(updated_state)
        feedback = "Planilha exportada com sucesso!"
    
    # Se pressionar Enter no campo de busca, faz a filtragem
    if input_search_submit or search:
        search = search.lower().strip()
        filtered_state = []
        for row in updated_state:
            filtered_row = [prod for prod in row if search in prod.lower()]
            filtered_state.append(filtered_row)
        # Exibe os produtos filtrados de todos os setores
        display_state = filtered_state
    else:
        display_state = updated_state

    # Calcular as métricas
    total, andamento, finalizados, progresso = calcular_metricas(updated_state)

    # Cards de métricas
    dashboard = [
        dbc.Card([
            dbc.CardHeader("EM ANDAMENTO"),
            dbc.CardBody(html.H4(andamento, className="card-title text-warning"))
        ], color="warning", inverse=True, style={"width": "18%"}),

        dbc.Card([
            dbc.CardHeader("FINALIZADOS"),
            dbc.CardBody(html.H4(finalizados, className="card-title text-success"))
        ], color="success", inverse=True, style={"width": "18%"}),

        dbc.Card([
            dbc.CardHeader("TOTAL"),
            dbc.CardBody(html.H4(total, className="card-title text-info"))
        ], color="info", inverse=True, style={"width": "18%"}),

        dbc.Card([
            dbc.CardHeader("PROGRESSO"),
            dbc.CardBody(html.H4(progresso, className="card-title text-primary"))
        ], color="primary", inverse=True, style={"width": "18%"})
    ]

    return generate_grid(display_state), updated_state, feedback, dashboard

if __name__ == "__main__":
    app.run(debug=True)
