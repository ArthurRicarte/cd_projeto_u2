# cd_projeto_u2
Repositório para o trabalho do Projeto U2 da matéria de Ciência de Dados no BTI - IMD - UFRN

Tema: Evasão escolar, com os microdados do SAEB 2023 (INEP).

## Como rodar
Primeiro, baixe os microdados do SAEB 2023 em https://download.inep.gov.br/microdados/microdados_saeb_2023.zip, descompacte e coloque as tabelas .csv na pasta `tabelas_csv/`.

```bash
pip install -r requirements.txt
python coleta.py
```

## Arquivos
- `coleta.py`: coleta e primeira olhada nos dados
- `dicionario_de_dados.md`: tabelas e variáveis usadas
- `primeiras_analises.md`: viabilidade, qualidade e primeiras conclusões
