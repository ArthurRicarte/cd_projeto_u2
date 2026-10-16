# Primeiras análises — evasão escolar (SAEB 2023)

**Pergunta:** o que os alunos que abandonam a escola têm em comum?

## Coleta
- O notebook `coleta.ipynb` baixa os microdados do SAEB 2023 do site do INEP e coloca as tabelas na pasta `tabelas_csv`.
- São 9 tabelas em CSV, com uns 3 GB no total. Os arquivos de alunos passam de 1 GB cada, então lemos só as colunas que interessam.
- Os arquivos vêm separados por `;` e com acentuação em latin1. É preciso informar isso no `read_csv`.

## Viabilidade e qualidade
- São dados oficiais e nacionais, com milhões de alunos. A rede pública é avaliada inteira; a privada, só por amostra.
- O questionário do aluno tem uma pergunta direta sobre abandono (Q20) e várias sobre possíveis causas (reprovação, idade, trabalho, família, nível socioeconômico).
- No 9º ano, cerca de 20% deixaram a Q20 em branco. Ainda assim sobram quase 2 milhões de respostas válidas.
- Também faltam o nível socioeconômico de ~20% dos alunos e a nota de ~17%.
- A tabela de escolas só tem escolas públicas, então os alunos de escola privada não se ligam a ela.
- Limitação importante: só responde quem ainda está na escola. A Q20 mostra quem já abandonou e voltou, não quem saiu de vez.

## Conclusões e aprendizados até agora
- Os dados servem para o nosso tema, desde que a Q20 seja tratada como "risco de evasão".
- No 9º ano, cerca de 6% dos alunos que responderam dizem que já abandonaram a escola alguma vez.
- Ler o dicionário do INEP foi essencial para entender os códigos (A, B, C, `.` e `*`).
- Pela quantidade de dados, faz diferença carregar só as colunas necessárias.
