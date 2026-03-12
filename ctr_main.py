import controle_proprio as ctr_P
import streamlit as st

#---------------------------------------------------------------

st.title("\tMenu de controle financeiro")
opcao = st.sidebar.radio(
    "Menu",
    [
        "Adicionar lucro",
        "Adicionar gasto",
        "Exibir lucros",
        "Exibir gastos",
        "Relatório final"
    ]
)

if opcao=="Adicionar lucro":
    st.header("Adicionar lucro")
    with st.form("luco_form"):
        valor = st.number_input("Valor")
        origem = st.text_input("Origem")
        data = st.date_input("Data")

        enviar = st.form_submit_button("Salvar")

    if enviar:
            ctr_P.recebidos(valor,origem,data)
            st.success("Valor salvo")

elif opcao == "Adicionar gasto":
    st.header("Adicionar gasto")
    with st.form("gasto_form"):
        valor = st.number_input("Valor")
        origem = st.text_input("Origem")
        data = st.date_input("Data")

        enviar = st.form_submit_button("Salvar")

    if enviar:
            ctr_P.gastos(valor,origem,data)
            st.success("Valor salvo")

elif opcao == "Exibir lucros":
        st.header("Exibir lucros")
        lucro=ctr_P.lucro()
        st.dataframe(lucro)
elif opcao =="Exibir gastos":
        st.header("Exibir gastos")
        desconto=ctr_P.descontos()
        st.dataframe(desconto)
elif opcao == "Relatório final":
    st.header("Relatório final")
    total_recebido, total_gastado, saldo_final = ctr_P.relatorio_final()

   
    st.subheader("Relatório final")
    st.write(f"Total recebido: R${total_recebido:.2f}")
    st.write(f"Total gasto: R${total_gastado:.2f}")
    
    if saldo_final >= 0:
        st.success(f"Saldo final positivo: R${saldo_final:.2f}")
    else:
        st.error(f"Saldo final negativo: R${saldo_final:.2f}")


