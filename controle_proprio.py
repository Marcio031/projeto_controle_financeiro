import pandas as pd
from datetime import datetime as dt

#------------------------------------------------------------------------------
try:
    valores_recebidos=pd.read_csv(r"D:\Meu Drive\estudos\controle\valores_recebidos.csv")
except:
    valores_recebidos=pd.DataFrame(columns=["valor","origem","dia"])

#------------------------------------------------------------------------------
try:
    dispesas=pd.read_csv(r"D:\Meu Drive\estudos\controle\dispesas.csv")
except:
    dispesas=pd.DataFrame(columns=["valor gasto","origem","dia"])
#------------------------------------------------------------------------------
def salvar():
    valores_recebidos.to_csv(r"D:\Meu Drive\estudos\controle\valores_recebidos.csv",index=False)
    dispesas.to_csv(r"D:\Meu Drive\estudos\controle\dispesas.csv",index=False)

#meu contro financeiro 
# 1 - adicionar valor recebido
def recebidos(valor,origem,data):
    valores_recebidos.loc[len(valores_recebidos)]={"valor":valor,"origem":origem,"dia":data}
    salvar()

# 2 - adicionar valor gasto 
def gastos(valor,origem,data):
    dispesas.loc[len(dispesas)]={"valor gasto":valor,"origem":origem,"dia":data}
    salvar()
# 3 - exibir valores recebidos 
def lucro():
    return valores_recebidos
# 4 - exibir valores gastos 
def descontos():
    return dispesas
# 5 - relatorio final
def relatorio_final():
    total_recebido = valores_recebidos["valor"].sum()
    total_gastado = dispesas["valor gasto"].sum()
    saldo_final = total_recebido - total_gastado

    # retorna tudo de uma vez
    return total_recebido, total_gastado, saldo_final

