import pandas as pd

# tabela de escolas
escolas = pd.read_csv("tabelas_csv/TS_ESCOLA.csv", sep=";", encoding="latin1")
print("tabela escolas:", escolas.shape)

# alunos do 9 ano (arquivo muito grande, pegamos so algumas colunas)
colunas = ["ID_ALUNO", "ID_ESCOLA", "ID_UF", "IN_PUBLICA", "ID_LOCALIZACAO",
           "IN_PREENCHIMENTO_QUESTIONARIO", "INSE_ALUNO", "PROFICIENCIA_MT_SAEB",
           "TX_RESP_Q01", "TX_RESP_Q02", "TX_RESP_Q08", "TX_RESP_Q19",
           "TX_RESP_Q20", "TX_RESP_Q21d"]
alunos = pd.read_csv("tabelas_csv/TS_ALUNO_9EF.csv", sep=";", encoding="latin1", usecols=colunas)
print("tabela alunos 9 ano:", alunos.shape)

print("\nporcentagem de valores vazios:")
print(alunos.isna().mean() * 100)

# Q20 -> "alguma vez voce abandonou a escola?"
# A = nunca, B = uma vez, C = duas ou mais, . = branco, * = nulo
print("\nrespostas da Q20:")
print(alunos["TX_RESP_Q20"].value_counts())

# juntando alunos com escolas
dados = alunos.merge(escolas[["ID_ESCOLA", "NIVEL_SOCIO_ECONOMICO"]], on="ID_ESCOLA", how="left")
print("\nalunos que acharam a escola:", dados["NIVEL_SOCIO_ECONOMICO"].notna().mean() * 100, "%")

dados.to_csv("alunos_9ano.csv", index=False)
print("salvo em alunos_9ano.csv")
