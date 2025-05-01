# Paradoxo do Aniversário - Aplicativo Streamlit

Este aplicativo interativo demonstra o famoso Paradoxo do Aniversário, permitindo explorar como a probabilidade de pessoas compartilharem a mesma data de aniversário aumenta surpreendentemente rápido com o tamanho do grupo.

## Requisitos

Para executar este aplicativo, você precisa ter Python instalado, além das seguintes bibliotecas:

```
streamlit
matplotlib
numpy
```

## Instalação

### Configuração rápida (com ambiente virtual)

#### Windows
1. Execute o script `setup.bat` para criar o ambiente virtual e instalar as dependências:
```
setup.bat
```

#### Linux/macOS
1. Torne o script de configuração executável:
```bash
chmod +x setup.sh
```

2. Execute o script:
```bash
./setup.sh
```

### Instalação manual
1. Clone este repositório ou baixe os arquivos
2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando o aplicativo

Para iniciar o aplicativo, execute o seguinte comando no terminal:

```bash
# Certifique-se que o ambiente virtual está ativado, se você o criou
streamlit run app.py
```

O aplicativo será aberto automaticamente no seu navegador padrão.

## Funcionalidades

O aplicativo permite ajustar diversos parâmetros:

- Número máximo de pessoas a considerar
- Número de dias no ano (padrão: 365)
- Probabilidade de destaque (linha horizontal)
- Opções de visualização (grade, marcadores, cores)
- Visualização de tabela com dados numéricos

## Sobre o Paradoxo do Aniversário

O Paradoxo do Aniversário refere-se ao fato contraintuitivo de que, com apenas 23 pessoas em uma sala, a probabilidade de pelo menos duas compartilharem o mesmo aniversário já é superior a 50%, mesmo havendo 365 dias possíveis no ano. 