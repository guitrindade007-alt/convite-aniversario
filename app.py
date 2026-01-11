import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Título
st.set_page_config(page_title="🎉 Aniversário da Débora!")

st.title("🎉 Você está convidado!")
st.subheader("Aniversário da Débora 🎂")

st.write("""
Vai rolar meu aniversário e você é parte importante disso.
Confirme sua presença abaixo para eu me organizar 😊
""")


# Autenticação Google
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_dict(
    st.secrets["google"], scope
)

client = gspread.authorize(creds)

sheet = client.openall()[0].sheet1

# Formulário
with st.form("formulario"):
    nome = st.text_input("Seu nome")
    presenca = st.selectbox("Você vai?", ["Sim", "Não"])
    pessoas = st.number_input("Quantas pessoas?", 0, 10, 1)
    obs = st.text_area("Observações")
    enviar = st.form_submit_button("Enviar")

if enviar:
    if nome.strip() == "":
        st.error("Digite seu nome!")
    else:
        sheet.append_row([
            nome,
            presenca,
            pessoas,
            obs,
            datetime.now().strftime("%d/%m/%Y %H:%M")
        ])

        if presenca == "Sim":
            st.success(f"🎉 Perfeito, {nome}! Te espero lá!")
        else:
            st.info(f"Ok, {nome}! Fica pra próxima 😊")




