import math
from dataclasses import dataclass
from typing import List

import streamlit as st
from fpdf import FPDF

PITCH_CONSUMPTION = {
    "P1.8": 550,  # W/m²
    "P2.5": 450,
    "P3": 400,
}

CONTROLADORAS = [
    ("TB30", 1920, 1080),
    ("VX600", 3840, 2160),
    ("NovaStar MRV-366", 7680, 4320),
]

@dataclass
class ProjectData:
    cliente: str
    largura: float
    altura: float
    pitch: str
    uso: str
    estrutura: str
    gabinete: str
    tensao: int
    valor_m2: float

    @property
    def area(self) -> float:
        return self.largura * self.altura

    @property
    def consumo_medio(self) -> float:
        consumo = PITCH_CONSUMPTION.get(self.pitch, 400)
        return consumo * self.area

    @property
    def potencia(self) -> float:
        return self.consumo_medio

    @property
    def corrente(self) -> float:
        return self.potencia / self.tensao

    @property
    def valor_total(self) -> float:
        return self.area * self.valor_m2

    @property
    def quadros_sugeridos(self) -> int:
        return max(1, math.ceil(self.potencia / 1000))

    @property
    def controladora(self) -> str:
        for nome, w, h in CONTROLADORAS:
            if self.largura <= w and self.altura <= h:
                return nome
        return CONTROLADORAS[-1][0]

def gerar_pdf(dados: ProjectData) -> bytes:
    pdf = FPDF()
    pdf.add_page()
    try:
        pdf.image("assets/gabinete.png", w=60)
    except Exception:
        pass
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Orçamento - {dados.cliente}", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Dimensões: {dados.largura}m x {dados.altura}m", ln=True)
    pdf.cell(0, 10, f"Pitch: {dados.pitch} - Uso: {dados.uso}", ln=True)
    pdf.cell(0, 10, f"Estrutura: {dados.estrutura}", ln=True)
    pdf.cell(0, 10, f"Gabinete: {dados.gabinete}", ln=True)
    pdf.cell(0, 10, f"Tensão: {dados.tensao}V", ln=True)
    pdf.cell(0, 10, f"Área: {dados.area:.2f} m²", ln=True)
    pdf.cell(0, 10, f"Potência estimada: {dados.potencia:.1f} W", ln=True)
    pdf.cell(0, 10, f"Quadros recomendados: {dados.quadros_sugeridos}", ln=True)
    pdf.cell(0, 10, f"Controladora: {dados.controladora}", ln=True)
    pdf.cell(0, 10, f"Valor total: R$ {dados.valor_total:,.2f}", ln=True)
    pdf.cell(0, 20, "LED XP", ln=True, align="R")
    return pdf.output(dest="S").encode("latin1")

def main():
    st.title("Orçamento de Painel de LED")

    with st.form("dados_painel"):
        cliente = st.text_input("Nome do cliente")
        largura = st.number_input("Largura (m)", min_value=0.0, step=0.1)
        altura = st.number_input("Altura (m)", min_value=0.0, step=0.1)
        pitch = st.selectbox("Pixel pitch", list(PITCH_CONSUMPTION.keys()))
        uso = st.selectbox("Tipo de uso", ["indoor", "outdoor"])
        estrutura = st.text_input("Tipo de estrutura")
        gabinete = st.text_input("Tipo de gabinete")
        tensao = st.selectbox("Tensão", [110, 220])
        valor_m2 = st.number_input("Valor por m²", min_value=0.0, value=4500.0, step=100.0)
        submitted = st.form_submit_button("Calcular")

    if submitted:
        dados = ProjectData(
            cliente=cliente,
            largura=largura,
            altura=altura,
            pitch=pitch,
            uso=uso,
            estrutura=estrutura,
            gabinete=gabinete,
            tensao=tensao,
            valor_m2=valor_m2,
        )

        st.header("Resultados")
        st.write(f"Área: {dados.area:.2f} m²")
        st.write(f"Valor total: R$ {dados.valor_total:,.2f}")
        st.write(f"Consumo médio: {dados.consumo_medio:.1f} W")
        st.write(f"Potência: {dados.potencia:.1f} W")
        st.write(f"Corrente: {dados.corrente:.2f} A")
        st.write(f"Quadros de energia: {dados.quadros_sugeridos}")
        st.write(f"Controladora sugerida: {dados.controladora}")

        pdf_bytes = gerar_pdf(dados)
        st.download_button(
            label="Exportar PDF",
            data=pdf_bytes,
            file_name="orcamento.pdf",
            mime="application/pdf",
        )

if __name__ == "__main__":
    main()
