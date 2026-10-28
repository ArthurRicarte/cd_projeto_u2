# cd_projeto_u2
Repositório para o trabalho do Projeto U2 da matéria de Ciência de Dados no BTI - IMD - UFRN

Tema: Segurança na escola, com os microdados do SAEB 2023 (INEP).

**Pergunta:** os alunos se sentem seguros na escola? O que está ligado a isso?

## Como rodar
```bash
pip install -r requirements.txt
jupyter notebook coleta.ipynb
```
Também dá para abrir o `coleta.ipynb` no Google Colab.

Na primeira vez, o notebook baixa os microdados do SAEB 2023 do site do INEP (~700 MB) e coloca as tabelas .csv na pasta `tabelas_csv/`. Depois disso, ele só lê as tabelas que já estão lá.

Depois de rodar o `coleta.ipynb`, rode o `seguranca_escola.ipynb` para gerar as figuras e tabelas da análise.

Link dos dados: https://download.inep.gov.br/microdados/microdados_saeb_2023.zip

## Arquivos
- `coleta.ipynb`: baixa os dados e dá uma primeira olhada nas tabelas que usamos (alunos do 9º ano, diretores e professores): respostas em branco, a pergunta de segurança e quantas escolas dá para ligar entre as tabelas
- `seguranca_escola.ipynb`: os alunos se sentem seguros na escola? Cruza a resposta dos alunos com a violência relatada por diretores e professores (SAEB 2023). Rodar depois do `coleta.ipynb`.
- `seguranca_escola.md`: resultados dessa análise (figuras e tabelas em `resultados_seguranca/`)
- `dicionario_de_dados.md`: tabelas e variáveis usadas
- `primeiras_analises.md`: viabilidade, qualidade e primeiras conclusões
- `dicionario_saeb/`: dicionário oficial do INEP
- `documentos_microdados_saeb/`, `escalas_de_proficiencia/`, `matrizes_de_referencia/`: documentos oficiais do INEP que vêm junto com os dados
