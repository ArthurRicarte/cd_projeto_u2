# Primeiras análises — evasão escolar (SAEB 2023)

**Pergunta:** Quais os principais pontos em comum entre os alunos que evadem a escola?

## Coleta
- O notebook `coleta.ipynb` baixa os microdados do SAEB 2023 do site do INEP e coloca as tabelas na pasta `tabelas_csv`.
- São 9 tabelas em CSV, com uns 3 GB no total. Os arquivos de alunos passam de 1 GB cada, então lemos só as colunas que interessam.
- Os arquivos vêm separados por `;` e com acentuação em latin1. É preciso informar isso no `read_csv`.

## Viabilidade e qualidade
- São dados oficiais e nacionais, com milhões de alunos. A rede pública é avaliada inteira; a privada, só por amostra.
- O questionário do aluno tem uma pergunta direta sobre abandono (Q20) e várias sobre possíveis causas (reprovação, idade, trabalho, família, nível socioeconômico).
- No 9º ano, cerca de 20% deixaram a Q20 em branco. Ainda assim sobram quase 2 milhões de respostas válidas.

## Conclusões e aprendizados até agora
- Os dados servem para o nosso tema, desde que a Q20 seja tratada como "risco de evasão".
- No 9º ano, cerca de 6% dos alunos que responderam dizem que já abandonaram a escola alguma vez.
- Pela quantidade de registros e de colunas ser muito elevada, é muito importante que a gente realize um filtro das informações de maneira que não acabe manipulando os dados de maneira que não gere dados equivocados.
