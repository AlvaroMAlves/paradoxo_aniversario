import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def birthday_paradox(n, days_in_year=365):
    """
    Calcula a probabilidade de pelo menos 2 pessoas em um grupo de n pessoas
    compartilharem o mesmo aniversário.
    
    Parâmetros:
    - n: número de pessoas no grupo
    - days_in_year: número de dias no ano (padrão: 365)
    
    Retorna:
    - Probabilidade de coincidência de aniversário
    """
    prob_unique = 1.0
    for i in range(n):
        prob_unique *= (days_in_year - i) / days_in_year
    return 1 - prob_unique

# Configuração da página
st.set_page_config(
    page_title="Paradoxo do Aniversário",
    page_icon="🎂",
    layout="wide"
)

# Título e descrição
st.title("📊 Paradoxo do Aniversário")
st.markdown("""
Este aplicativo demonstra o famoso Paradoxo do Aniversário: a probabilidade surpreendentemente 
alta de que em um grupo pequeno de pessoas, pelo menos duas façam aniversário no mesmo dia.
""")

# Layout com duas colunas
col1, col2 = st.columns([1, 2])

with col1:
    st.header("Parâmetros")
    
    # Parâmetro principal: Número de pessoas na sala
    num_people = st.slider(
        "Número de pessoas na sala", 
        min_value=1, 
        max_value=100, 
        value=23,
        step=1
    )
    
    # Dias no ano (opcional, mas mantido com valor padrão)
    days_in_year = 365
    
    # Calcular a probabilidade para o número escolhido
    probability = birthday_paradox(num_people, days_in_year)
    probability_percent = probability * 100
    
    # Exibição da probabilidade
    st.header("Resultado")
    st.metric(
        label="Probabilidade de coincidência", 
        value=f"{probability_percent:.2f}%"
    )
    
    # Informações adicionais
    st.info(f"""
    Com {num_people} pessoas em uma sala, a probabilidade 
    de pelo menos duas delas compartilharem o mesmo aniversário 
    é de aproximadamente {probability_percent:.2f}%.
    """)
    
    # Mostrar valor específico
    st.subheader("Calcular pessoas para probabilidade")
    target_prob = st.slider(
        "Probabilidade desejada (%)", 
        min_value=0, 
        max_value=100, 
        value=50
    )
    
    # Encontrar número de pessoas para a probabilidade alvo
    target_prob_decimal = target_prob / 100
    people_needed = 0
    for p in range(1, 101):
        if birthday_paradox(p, days_in_year) >= target_prob_decimal:
            people_needed = p
            break
    
    st.success(f"""
    Para obter uma probabilidade de aproximadamente {target_prob}%, 
    você precisa de pelo menos {people_needed} pessoas na sala.
    """)

with col2:
    # Gera os dados para o gráfico
    people = np.arange(1, 101)
    probabilities = [birthday_paradox(n, days_in_year) for n in people]
    
    # Criação do gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plotando a linha principal
    ax.plot(people, probabilities, marker='o', color='#1f77b4', label='Probabilidade')
    
    # Destacando o valor atual
    ax.axhline(probability, color='gray', linestyle='--', label='Probabilidade atual')
    ax.axvline(num_people, color='red', linestyle='--', label=f'{num_people} pessoas')
    
    # Destacando o valor para a probabilidade alvo
    if people_needed > 0:
        ax.axhline(target_prob_decimal, color='green', linestyle='--', 
                   label=f'Probabilidade alvo ({target_prob}%)')
        ax.axvline(people_needed, color='orange', linestyle='--', 
                   label=f'{people_needed} pessoas')
    
    # Configuração do gráfico
    ax.set_title('Paradoxo do Aniversário: Probabilidade de Coincidência')
    ax.set_xlabel('Número de Pessoas na Sala')
    ax.set_ylabel('Probabilidade de pelo menos 2 pessoas\nfazerem aniversário no mesmo dia')
    ax.set_ylim(0, 1)
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    
    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)
    
    # Tabela de valores específicos
    st.subheader("Valores de referência")
    reference_data = {
        "Pessoas": [10, 20, 23, 30, 40, 50, 60, 70],
        "Probabilidade (%)": [11.7, 41.1, 50.7, 70.6, 89.1, 97.0, 99.4, 99.9]
    }
    st.table(reference_data)

# Rodapé
st.markdown("---")
st.markdown("Visualização interativa do Paradoxo do Aniversário | Feito por Alvaro Martins Alves | Desenvolvido com Streamlit") 