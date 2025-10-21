# 🩺 SINASC APGAR 5 Explorer - Streamlit App

Bem-vindo ao **SINASC APGAR 5 Explorer**, um aplicativo interativo desenvolvido em **Streamlit** para visualização e análise de dados do **SINASC (Sistema de Informações sobre Nascidos Vivos)**, abrangendo os anos de 2015 a 2025.  

Este app permite:

- Prever o **APGAR 5** de um recém-nascido com base em informações clínicas e obstétricas.
- Explorar embeddings UMAP interativos dos dados, permitindo análise visual de padrões e clusters.

---

## ⚡ Recursos Interativos

### 1️⃣ UMAP 2D Explorer
- Visualização **interativa** de dados reduzidos via UMAP.
- Dropdown para **alterar a feature usada na coloração**.
- Hover sobre cada ponto exibe todas as informações relevantes (`PESO`, `CONSPRENAT`, `SEMAGESTAC`, `APGAR1`, `TPROBSON`, `KOTELCHUCK`).

### 2️⃣ Calculadora APGAR 5
- Previsão do escore APGAR 5 com base no modelo **LightGBM** treinado.
- Inputs interativos via sliders e dropdowns.
- Retorna o **valor previsto de APGAR 5** instantaneamente.

---

