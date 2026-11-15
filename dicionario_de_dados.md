# Dicionário de dados

Fonte: microdados do SAEB 2023 (INEP). O dicionário completo do INEP está em `dicionario_saeb/Dicionario_Saeb_2023.xlsx`.

## Tabelas

| Tabela | O que é cada linha | Linhas |
|---|---|---|
| TS_ALUNO_5EF / 9EF / 34EM | um aluno (prova + questionário) | ~2,4 mi / 2,5 mi / 2,1 mi |
| TS_ALUNO_2EF | um aluno do 2º ano (só prova) | 37 mil |
| TS_ESCOLA | uma escola pública (médias e indicadores) | 70 mil |
| TS_PROFESSOR | um professor de uma série (questionário) | 412 mil |
| TS_DIRETOR | um diretor, repetido para cada série avaliada na escola (questionário) | 107 mil (62 mil escolas) |
| TS_SECRETARIO_MUNICIPAL | um secretário de educação | 5,5 mil |
| TS_ITEM | uma questão da prova | 993 |

Usamos as tabelas de **alunos** (5º ano, 9º ano e 3ª série do EM), de **diretores** e de **professores**. Elas se ligam pelo `ID_ESCOLA`. Esse código é mascarado (fictício, por causa da LGPD), mas é o mesmo em todas as tabelas de 2023.

## Alunos (TS_ALUNO_5EF, TS_ALUNO_9EF, TS_ALUNO_34EM)

| Variável | Descrição | Valores |
|---|---|---|
| ID_ESCOLA | código (mascarado) da escola | número |
| ID_UF | estado | código IBGE (ex.: 24 = RN) |
| IN_PUBLICA | rede da escola | 0 = privada, 1 = pública |
| ID_LOCALIZACAO | localização da escola | 1 = urbana, 2 = rural |
| IN_SITUACAO_CENSO | aluno declarado no Censo Escolar? | 0 = não, 1 = sim (usamos só 1) |
| PESO_ALUNO_MT | peso amostral do aluno | número (usado nas porcentagens nacionais e por estado) |
| **TX_RESP_Q23d** | **"Eu me sinto seguro(a) quando estou na escola"** | A = concordo totalmente, B = concordo, C = discordo, D = discordo totalmente |
| TX_RESP_Q22f | quantos professores da turma abordam bullying e outras formas de violência | A = todos, B = a maior parte, C = poucos, D = nenhum |
| TX_RESP_Q23c | "Há espaço para diferentes opiniões na minha sala de aula" | A a D (como a Q23d) |
| TX_RESP_Q23e | "Eu me sinto à vontade para discordar dos meus professores" | A a D |
| TX_RESP_Q23h | "Meus professores acreditam que eu sou capaz de aprender" | A a D |

Outras variáveis usadas só no 9º ano (análise descritiva):

| Variável | Descrição | Valores |
|---|---|---|
| ID_REGIAO | região | 1 = Norte, 2 = Nordeste, 3 = Sudeste, 4 = Sul, 5 = Centro-Oeste |
| ID_AREA | capital ou interior | 1 = capital, 2 = interior |
| TX_RESP_Q14 | tempo para chegar à escola | A = menos de 30 min, B = 30 min a 1 hora, C = mais de 1 hora |
| TX_RESP_Q16 | como chega à escola | A = a pé, B = bicicleta, C = van, D = ônibus, E = metrô/trem, F = carro, G = barco, H = moto, I = outro |
| TX_RESP_Q19 | já foi reprovado | A = não, B = uma vez, C = duas ou mais |
| TX_RESP_Q20 | já abandonou a escola | A = nunca, B = uma vez, C = duas ou mais |
| TX_RESP_Q24 | o que pretende depois do fundamental | A = só estudar, B = só trabalhar, C = estudar e trabalhar, D = não sabe |
| TX_RESP_Q22a–h | quantos professores: contam o que será ensinado (a), perguntam o que já sabemos (b), trazem temas do cotidiano (c), desigualdade racial (d), de gênero (e), bullying (f), trabalhos em grupo (g), futuro profissional (h) | A = todos, B = a maior parte, C = poucos, D = nenhum |
| TX_RESP_Q23a–i | concorda que: se interessa pelo que foi ensinado (a), se sente motivado a usar (b), há espaço para opiniões (c), à vontade para discordar (e), consegue argumentar (f), as avaliações mostram o que aprendeu (g), professores acreditam nele (h), professores motivam a continuar estudando (i) | A = concordo totalmente ... D = discordo totalmente |

Da tabela **TS_ESCOLA** usamos `NU_MATRICULADOS_CENSO_9EF` (matriculados no 9º ano) para o tamanho da escola.

O **resultado** da análise é a Q23d: o aluno que responde C ou D é contado como "não se sente seguro".

## Diretores (TS_DIRETOR)

| Variável | Descrição | Valores |
|---|---|---|
| ID_ESCOLA | código (mascarado) da escola | número |
| IN_PREENCHIMENTO_QUESTIONARIO | respondeu o questionário? | 0 = não, 1 = sim (usamos só 1) |
| TX_Q093 a TX_Q102 | frequência, neste ano, de: roubo ou furto (093), tráfico de drogas (094), pessoas sob efeito de álcool (095) e de drogas (096), porte de arma (097), assédio sexual (098), discriminação (099), bullying (100), invasão da escola (101), vandalismo (102) | A = nunca, B = poucas vezes, C = muitas vezes, D = sempre |
| TX_Q082 | as aulas foram interrompidas por vários dias por episódios de violência? | A = não, B = sim |
| TX_Q104 | condições de segurança na entrada e saída da escola | A = muito inadequado, B = inadequado, C = adequado, D = muito adequado |
| TX_Q105 | muros e/ou grades que isolam a escola | A a D (como a Q104) |
| TX_Q123 | a escola trabalha regularmente com segurança pública (polícia, guarda municipal)? | A = não, B = sim |
| TX_Q196 | a escola tem projeto de combate à violência? | A = não, B = sim |

A mesma escola aparece em uma linha para cada série avaliada (com as mesmas respostas), então deixamos **uma linha por escola**.

## Professores (TS_PROFESSOR)

| Variável | Descrição | Valores |
|---|---|---|
| ID_ESCOLA | código (mascarado) da escola | número |
| ID_SERIE | série em que o professor dá aula | 2, 5, 9, 12, 13 (usamos 9) |
| TX_Q135 a TX_Q147 | frequência, nesta escola e neste ano, de: atentado à vida (135), lesão corporal (136), roubo ou furto (137), tráfico (138), álcool (139), drogas (140), porte de arma (141), assédio sexual (142), discriminação (143), bullying (144), invasão (145), vandalismo (146), tiroteio ou bala perdida (147) | A = nunca, B = poucas vezes, C = muitas vezes, D = sempre |

Nas respostas dos questionários, `.` significa em branco e `*` significa resposta nula.

## PeNSE 2024 (IBGE) — dados externos para validar

Tabelas prontas do tema Segurança (`Tema_09_Seguranca`), https://ftp.ibge.gov.br/pense/2024/xlsx/. Cada linha é um local (Brasil, região, estado ou capital), com o percentual de escolares de 13 a 17 anos, total e por rede (pública/privada).

| Tabela | Indicador |
|---|---|
| 9.7 | deixou de ir à escola por falta de segurança no caminho (últimos 30 dias) |
| 9.8 | deixou de ir à escola por falta de segurança na escola (últimos 30 dias) |
| 9.9 | envolveu-se em briga com luta física (últimos 30 dias) |
| 9.10 | envolveu-se em briga em que alguém usou arma de fogo (últimos 30 dias) |
| 9.17 | foi agredido fisicamente por alguém fora da família (últimos 12 meses) |

Ligamos ao SAEB pelo nome do estado (convertido para a sigla) e comparamos também rede, faixa de idade e região.
