@echo off
echo Criando ambiente virtual para o projeto Paradoxo do Aniversario...
python -m venv venv

echo Ativando o ambiente virtual...
call venv\Scripts\activate.bat

echo Instalando dependencias...
pip install -r requirements.txt

echo.
echo Configuracao concluida! Para executar o aplicativo:
echo 1. Ative o ambiente virtual: venv\Scripts\activate
echo 2. Execute o aplicativo: streamlit run app.py
echo.
echo Pressione qualquer tecla para sair...
pause > nul 