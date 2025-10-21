import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# -----------------------------
# Streamlit page config
# -----------------------------
st.set_page_config(
    page_title="UMAP SINASC Explorer",
    page_icon="🧬",
    layout="wide"
)

st.title("🌐 UMAP 2D - SINASC Explorer")
st.markdown("Visualizing high-dimensional SINASC data in 2D space using UMAP")

# -----------------------------
# Load precomputed embedding
# -----------------------------
@st.cache_data
def load_embedding(path="models/umap_embedding.pkl"):
    """
    Carrega o embedding UMAP pré-computado a partir de um arquivo pickle.
    """
    df = pd.read_pickle(path)  # <-- corrige leitura de pickle
    return df

# Carrega o embedding
df_plot = load_embedding().reset_index(drop=True)

# -----------------------------
# Features para coloração
# -----------------------------
color_feats = ['APGAR5', 'PESO', 'CONSPRENAT', 'SEMAGESTAC', 'APGAR1', 'TPROBSON', 'KOTELCHUCK']

# Garantir que todas as colunas são numéricas
for feat in color_feats:
    df_plot[feat] = pd.to_numeric(df_plot[feat], errors='coerce')

# -----------------------------
# Construir figura Plotly
# -----------------------------
fig = go.Figure()

for feat in color_feats:
    vals = df_plot[feat].values.astype(float)
    
    trace = go.Scattergl(
        x=df_plot['UMAP_1'],
        y=df_plot['UMAP_2'],
        mode='markers',
        marker=dict(
            size=6,
            opacity=0.7,
            color=vals,
            colorscale='Inferno',
            showscale=True,
            colorbar=dict(title=feat),
            cmin=np.nanmin(vals),
            cmax=np.nanmax(vals)
        ),
        hoverinfo='text',
        hovertext=[
            f"index: {i}<br>UMAP1: {u1:.3f}<br>UMAP2: {u2:.3f}<br>" +
            "<br>".join([
                f"{f}: {df_plot.loc[i,f]}" 
                for f in ['PESO','CONSPRENAT','SEMAGESTAC','APGAR1','TPROBSON','KOTELCHUCK']
            ])
            for i,(u1,u2) in enumerate(zip(df_plot['UMAP_1'], df_plot['UMAP_2']))
        ],
        visible=(feat == 'APGAR5')  # só APGAR5 visível inicialmente
    )
    fig.add_trace(trace)

# -----------------------------
# Dropdown selector
# -----------------------------
updatemenus = [
    dict(
        type="dropdown",
        direction="down",
        x=1.05,
        y=1.15,
        showactive=True,
        active=0,
        buttons=[
            dict(
                label=feat,
                method="update",
                args=[
                    {"visible": [f == feat for f in color_feats]},
                    {"title": f"UMAP 2D — color by {feat}"}
                ],
            ) for feat in color_feats
        ]
    )
]

# -----------------------------
# Layout final da figura
# -----------------------------
fig.update_layout(
    updatemenus=updatemenus,
    title="UMAP 2D SINASC",
    width=1024,
    height=768,
    margin=dict(l=50, r=300, t=80, b=50),
    annotations=[
        dict(
            text="Visualizing high-dimensional SINASC data in 2D space using UMAP",
            xref="paper",
            yref="paper",
            x=0,
            y=1.08,  # posição logo acima do título
            showarrow=False,
            font=dict(size=14)
        )
    ]
)

# -----------------------------
# Exibir no Streamlit
# -----------------------------
st.plotly_chart(fig, use_container_width=True)
