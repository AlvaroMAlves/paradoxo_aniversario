#!/bin/bash

echo "Criando ambiente virtual para o projeto Paradoxo do Aniversario..."
python3 -m venv venv

echo "Ativando o ambiente virtual..."
source venv/bin/activate

echo "Instalando dependencias..."
pip install -r requirements.txt

echo ""
echo "Configuracao concluida! Para executar o aplicativo:"
echo "1. Ative o ambiente virtual: source venv/bin/activate"
echo "2. Execute o aplicativo: streamlit run app.py" 