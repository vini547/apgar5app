import streamlit as st

# -----------------------------
# Configuração da página
# -----------------------------
st.set_page_config(
    page_title="SINASC APGAR Explorer",
    page_icon="🩺",
    layout="wide"
)

# -----------------------------
# Título e descrição
# -----------------------------
st.title("🩺 SINASC APGAR Explorer")
st.markdown("""
Bem-vindo ao **SINASC APGAR Explorer**, uma aplicação interativa para:

- Prever o **APGAR 5** de recém-nascidos com base em dados clínicos.
- Explorar visualmente embeddings **UMAP 2D** dos dados do SINASC (2015-2025).

Este app é voltado para **pesquisadores, médicos e profissionais de saúde**.
""")

# -----------------------------
# Seção de navegação
# -----------------------------
st.markdown("## 🔹 Descrição das Páginas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🌐 UMAP Explorer")
    st.markdown("""
Explore os dados do SINASC em **2 dimensões**, utilizando UMAP.  
Visualize padrões, clusters e distribuições de variáveis como APGAR, peso, semanas de gestação, entre outras.
""")

with col2:
    st.subheader("🧮 Calculadora APGAR 5")
    st.markdown("""
Preveja o **APGAR 5** de um recém-nascido baseado em características clínicas.  
Insira os valores relevantes e veja a previsão do escore instantaneamente.
""")

# -----------------------------
# Rodapé
# -----------------------------
st.markdown("---")
st.markdown("💡 Use o menu lateral para navegar entre as páginas do app.")
st.markdown("📌 Projeto desenvolvido para análise e exploração de dados SINASC (2015-2025).")
