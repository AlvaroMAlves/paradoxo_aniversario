# Paradoxo do Aniversário - Aplicativo Streamlit

Este aplicativo interativo demonstra o famoso Paradoxo do Aniversário, permitindo explorar como a probabilidade de pessoas compartilharem a mesma data de aniversário aumenta surpreendentemente rápido com o tamanho do grupo.

## Sobre o Paradoxo do Aniversário

O Paradoxo do Aniversário refere-se ao fato contraintuitivo de que, com apenas 23 pessoas em uma sala, a probabilidade de pelo menos duas compartilharem o mesmo aniversário já é superior a 50%, mesmo havendo 365 dias possíveis no ano.

## Requisitos

Para executar este aplicativo, você precisa ter Python instalado, além das seguintes bibliotecas:

```
streamlit
matplotlib
numpy
```

## Instalação e Execução

1. Instale as dependências:
```bash
pip install streamlit matplotlib numpy
```

2. Execute o aplicativo:
```bash
streamlit run app.py
```

O aplicativo será aberto automaticamente no seu navegador padrão, geralmente em http://localhost:8501.

## Funcionalidades

O aplicativo permite ajustar os seguintes parâmetros:

- **Número de pessoas na sala**: Ajuste o número de pessoas e veja como isso afeta a probabilidade
- **Probabilidade desejada**: Defina uma probabilidade alvo e veja quantas pessoas são necessárias para atingi-la

A visualização inclui:
- Gráfico interativo mostrando a relação entre o número de pessoas e a probabilidade
- Indicadores visuais destacando valores de interesse
- Tabela de referência com valores comuns

## Autor

Desenvolvido por Alvaro Martins Alves 