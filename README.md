# cd_projeto_u2
Repositório para o trabalho do Projeto U2 da matéria de Ciência de Dados no BTI - IMD - UFRN

Tema: Evasão escolar, com os microdados do SAEB 2023 (INEP).

## Como rodar
```bash
pip install -r requirements.txt
jupyter notebook coleta.ipynb
```
Também dá para abrir o `coleta.ipynb` no Google Colab.

Na primeira vez, o notebook baixa os microdados do SAEB 2023 do site do INEP (~700 MB) e coloca as tabelas .csv na pasta `tabelas_csv/`. Depois disso, ele só lê as tabelas que já estão lá.

Link dos dados: https://download.inep.gov.br/microdados/microdados_saeb_2023.zip

## Arquivos
- `coleta.ipynb`: baixa os dados, dá uma primeira olhada e salva `alunos_9ano.csv`
- `dicionario_de_dados.md`: tabelas e variáveis usadas
- `primeiras_analises.md`: viabilidade, qualidade e primeiras conclusões
- `dicionario_saeb/`: dicionário oficial do INEP
- `documentos_microdados_saeb/`, `escalas_de_proficiencia/`, `matrizes_de_referencia/`: documentos oficiais do INEP que vêm junto com os dados
