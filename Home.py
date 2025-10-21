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
# Menu lateral de navegação moderno
# -----------------------------
page = st.sidebar.radio("Navegação", ["Home", "UMAP Explorer", "Calculadora APGAR 5"])

# -----------------------------
# Página Home
# -----------------------------
if page == "Home":
    st.title("🩺 SINASC APGAR Explorer")
    st.markdown("""
    Bem-vindo ao **SINASC APGAR Explorer**, uma aplicação interativa para:

    - Prever o **APGAR 5** de recém-nascidos com base em dados clínicos.
    - Explorar visualmente embeddings **UMAP 2D** dos dados do SINASC (2015-2025).

    Este app é voltado para **pesquisadores, médicos e profissionais de saúde**.
    """)

    st.markdown("## 🔹 Navegação Rápida")
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

    st.markdown("---")
    st.markdown("💡 Use o menu lateral para navegar entre as páginas do app.")
    st.markdown("📌 Projeto desenvolvido para análise e exploração de dados SINASC (2015-2025).")

# -----------------------------
# Página UMAP Explorer
# -----------------------------
elif page == "UMAP Explorer":
    from pages.UMAP_Visualizer import run_umap_page
    run_umap_page()

# -----------------------------
# Página Calculadora APGAR5
# -----------------------------
elif page == "Calculadora APGAR 5":
    from pages.APGAR5_Calculator import run_apgar_page
    run_apgar_page()
