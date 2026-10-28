# Primeiras análises — segurança na escola (SAEB 2023)

**Pergunta:** os alunos se sentem seguros na escola? O que está ligado a isso?

## Por que mudamos a pergunta
A pergunta anterior era sobre evasão escolar ("quais os pontos em comum entre os alunos que evadem a escola?"). O problema: o SAEB só entrevista quem **está** na escola, então não há dado de quem saiu. A ideia de seguir o mesmo aluno em anos anteriores também não funciona. Testamos com o SAEB 2021: nenhum `ID_ALUNO` e nenhum código de escola se repete entre 2021 e 2023, porque o INEP gera códigos novos a cada edição.

Na nova pergunta o resultado está medido diretamente nos dados: o próprio aluno responde se se sente seguro na escola.

## Coleta
- O notebook `coleta.ipynb` baixa os microdados do SAEB 2023 do site do INEP e coloca as tabelas na pasta `tabelas_csv`.
- Usamos 5 tabelas: alunos do 5º ano, do 9º ano e da 3ª série do EM, diretores e professores.
- Os arquivos de alunos passam de 1 GB cada, então lemos só as colunas que interessam.
- Os arquivos vêm separados por `;` e com acentuação em latin1. É preciso informar isso no `read_csv`.

## Viabilidade e qualidade
- São dados oficiais e nacionais, com milhões de alunos. A rede pública é avaliada inteira; a privada, só por amostra (usamos o peso amostral nas porcentagens nacionais e por estado).
- A pergunta de segurança (Q23d) tem cerca de 2 milhões de respostas válidas no 9º ano. Cerca de 20% dos alunos deixaram em branco.
- Os questionários dos diretores (62 mil escolas) e dos professores (292 mil responderam as perguntas de violência) se ligam aos alunos pelo código da escola. Das escolas com pelo menos 10 alunos do 9º ano respondendo, 85% têm o questionário do diretor e 83% têm professores do 9º ano com resposta.
- Cuidado encontrado: na tabela de diretores a mesma escola aparece uma vez por série avaliada. Sem tirar as repetições, as escolas com mais séries contariam em dobro.
- O código da escola é mascarado, então não dá para cruzar com outros dados (Censo Escolar, ocorrências policiais).

## Conclusões e aprendizados até agora
- Cerca de **3 em cada 10** alunos do 9º ano não se sentem seguros na escola (2 em cada 10 no 5º ano).
- Onde diretores e professores relatam mais violência, mais alunos se sentem inseguros, mesmo comparando escolas do mesmo estado, rede e localização.
- Muros, polícia e projetos contra violência quase não aparecem ligados à sensação de segurança. O que mais acompanha é a relação com os professores.
- "Me sinto seguro" e as perguntas sobre os professores são respondidas pelo mesmo aluno, então mostram associação, não causa.
- Resultados completos em `seguranca_escola.md`.
