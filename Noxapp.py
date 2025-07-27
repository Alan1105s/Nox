import streamlit as st
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Mostrar logo
st.image("logo.png", width=150)
# --- BASE DE DATOS DE PERFUMES ---
catalogo = [
    {"nombre": "Very Good Girl", "sexo": "mujer", "esencia": "floral", "ph": "acido"},
    {"nombre": "Yara", "sexo": "mujer", "esencia": "dulce", "ph": "acido"},
    {"nombre": "La Vie Est Belle", "sexo": "mujer", "esencia": "dulce", "ph": "equilibrado"},
    {"nombre": "Scandal", "sexo": "mujer", "esencia": "especiado", "ph": "equilibrado"},
    {"nombre": "Light Blue", "sexo": "mujer", "esencia": "fresco", "ph": "muy_acido"},
    {"nombre": "Cloud (Ariana Grande)", "sexo": "mujer", "esencia": "dulce", "ph": "acido"},
    {"nombre": "Miss Dior", "sexo": "mujer", "esencia": "floral", "ph": "acido"},
    {"nombre": "Chance", "sexo": "mujer", "esencia": "floral", "ph": "equilibrado"},

    {"nombre": "Bad Boy", "sexo": "hombre", "esencia": "especiado", "ph": "lig_alcalino"},
    {"nombre": "One Million Lucky", "sexo": "hombre", "esencia": "dulce", "ph": "lig_alcalino"},
    {"nombre": "Aqua Di Gio Profondo", "sexo": "hombre", "esencia": "fresco", "ph": "muy_acido"},
    {"nombre": "Eros", "sexo": "hombre", "esencia": "fresco", "ph": "muy_acido"},
    {"nombre": "Le Male Le Parfum", "sexo": "hombre", "esencia": "dulce", "ph": "equilibrado"},
    {"nombre": "Stronger with you", "sexo": "hombre", "esencia": "dulce", "ph": "equilibrado"},
    {"nombre": "Bleu", "sexo": "hombre", "esencia": "amaderado", "ph": "equilibrado"},
    
    {"nombre": "Santal 33", "sexo": "unisex", "esencia": "amaderado", "ph": "alcalino"},
    {"nombre": "Amber Rouge", "sexo": "unisex", "esencia": "dulce", "ph": "alcalino"},
    {"nombre": "Khamrah", "sexo": "unisex", "esencia": "dulce", "ph": "alcalino"},
    {"nombre": "Oud For Glory", "sexo": "unisex", "esencia": "especiado", "ph": "alcalino"},
    {"nombre": "Baccarat Rouge 540", "sexo": "unisex", "esencia": "dulce", "ph": "alcalino"},
    {"nombre": "Asad", "sexo": "unisex", "esencia": "amaderado", "ph": "lig_alcalino"},
]

# --- FUNCIÓN PARA CLASIFICAR EL PH ---
def clasificar_ph(ph_valor):
    if ph_valor < 4.8:
        return "muy_acido"
    elif 4.8 <= ph_valor <= 5.2:
        return "acido"
    elif 5.3 <= ph_valor <= 5.6:
        return "equilibrado"
    elif 5.7 <= ph_valor <= 6.2:
        return "lig_alcalino"
    else:
        return "alcalino"

# --- FUNCIÓN PARA RECOMENDAR ---
def recomendar_perfume(ph_valor, sexo, esencia):
    ph_categoria = clasificar_ph(ph_valor)
    for perfume in catalogo:
        if (
            perfume["ph"] == ph_categoria and
            perfume["sexo"] == sexo and
            perfume["esencia"] == esencia
        ):
            return f"💎 Te recomendamos: **{perfume['nombre']}**"
    return "⚠️ No encontramos una coincidencia exacta. Prueba con otra combinación."

# --- INTERFAZ STREAMLIT ---
st.set_page_config(page_title="Recomendador NOX", page_icon="🧪")

st.title("🔬 Recomendador de Perfumes NOX")
st.write("Descubre el perfume ideal según tu pH, aroma preferido y estilo.")

ph_input = st.slider("📏 ¿Cuál es tu pH de piel?", min_value=4.0, max_value=7.5, step=0.1)
sexo_input = st.selectbox("👤 ¿Buscas una fragancia para?", ["mujer", "hombre", "unisex"])
esencia_input = st.selectbox("🌸 ¿Qué tipo de aroma prefieres?", ["fresco", "floral", "dulce", "amaderado", "especiado"])

if st.button("✨ Obtener recomendación"):
    resultado = recomendar_perfume(ph_input, sexo_input, esencia_input)
    st.success(resultado)

st.markdown("---")
st.markdown("Creado por **NOX Perfumes** · Tu piel, tu esencia.")
