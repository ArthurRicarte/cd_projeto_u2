# Dicionário de dados

Fonte: microdados do SAEB 2023 (INEP). O dicionário completo do INEP está em `dicionario/Dicionario_Saeb_2023.xlsx`.

## Tabelas

| Tabela | O que é cada linha | Linhas |
|---|---|---|
| TS_ALUNO_5EF / 9EF / 34EM | um aluno (prova + questionário) | ~2,4 mi / 2,5 mi / 2,1 mi |
| TS_ALUNO_2EF | um aluno do 2º ano (só prova) | 37 mil |
| TS_ESCOLA | uma escola pública (médias e indicadores) | 70 mil |
| TS_PROFESSOR | um professor (questionário) | 412 mil |
| TS_DIRETOR | um diretor (questionário) | 107 mil |
| TS_SECRETARIO_MUNICIPAL | um secretário de educação | 5,5 mil |
| TS_ITEM | uma questão da prova | 993 |

As tabelas se ligam pelo `ID_ESCOLA` (aluno ↔ escola ↔ diretor) e pelo `ID_TURMA` (aluno ↔ professor).

## Variáveis que vamos usar (tabela de alunos)

| Variável | Descrição | Valores |
|---|---|---|
| ID_ALUNO | código do aluno | número |
| ID_ESCOLA | código da escola | número |
| ID_UF | estado | código IBGE (ex.: 24 = RN) |
| IN_PUBLICA | rede da escola | 0 = privada, 1 = pública |
| ID_LOCALIZACAO | localização | 1 = urbana, 2 = rural |
| INSE_ALUNO | nível socioeconômico do aluno | número (quanto maior, mais rico) |
| PROFICIENCIA_MT_SAEB | nota em Matemática | escala SAEB (média 250) |
| TX_RESP_Q01 | sexo | A = masculino, B = feminino |
| TX_RESP_Q02 | idade | A a F (B = idade certa para a série) |
| TX_RESP_Q08 | escolaridade da mãe | A (não completou o 5º ano) até E (superior) |
| TX_RESP_Q19 | já foi reprovado? | A = não, B = uma vez, C = duas ou mais |
| **TX_RESP_Q20** | **já abandonou a escola?** | A = nunca, B = uma vez, C = duas ou mais |
| TX_RESP_Q21d | trabalha fora de casa? | A = não, B a D = tempo gasto |

Nas respostas do questionário, `.` significa em branco e `*` significa resposta nula.
