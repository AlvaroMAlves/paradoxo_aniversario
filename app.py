import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math

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
    st.header("Número de Pessoas")
    
    # Parâmetro principal: Número de pessoas na sala
    num_people = st.slider(
        "Ajuste o número de pessoas na sala", 
        min_value=1, 
        max_value=100, 
        value=23,
        step=1
    )
    
    # Dias no ano (fixo em 365)
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
    
    # Cálculo passo a passo para o número atual
    with st.expander("Ver cálculo detalhado"):
        st.markdown(f"""
        ### Cálculo da probabilidade para {num_people} pessoas:
        
        Vamos calcular a probabilidade de pelo menos 2 pessoas entre {num_people} compartilharem o mesmo aniversário.
        """)
        
        # Preparando os passos intermediários do cálculo
        steps = []
        prob_so_far = 1.0
        for i in range(num_people):
            new_factor = (365 - i) / 365
            prob_so_far *= new_factor
            steps.append({
                "pessoa": i + 1,
                "novo_fator": new_factor,
                "prob_acumulada": prob_so_far
            })
        
        # Mostrando a fórmula aplicada
        st.latex(f"P({num_people}) = 1 - \\prod_{{i=0}}^{{{num_people}-1}} \\frac{{365-i}}{{365}}")
        
        # Mostrando o primeiro e últimos passos do cálculo (para não ficar muito extenso)
        if num_people <= 10:
            # Para poucos passos, mostra todos
            for step in steps:
                st.markdown(f"""
                **Pessoa {step['pessoa']}**: Multiplicamos por $\\frac{{365-{step['pessoa']-1}}}{{365}} = {step['novo_fator']:.6f}$
                
                Probabilidade acumulada: {step['prob_acumulada']:.6f}
                """)
        else:
            # Para muitos passos, mostra apenas alguns
            for step in steps[:3]:
                st.markdown(f"""
                **Pessoa {step['pessoa']}**: Multiplicamos por $\\frac{{365-{step['pessoa']-1}}}{{365}} = {step['novo_fator']:.6f}$
                
                Probabilidade acumulada: {step['prob_acumulada']:.6f}
                """)
            
            st.markdown("...")
            
            for step in steps[-3:]:
                st.markdown(f"""
                **Pessoa {step['pessoa']}**: Multiplicamos por $\\frac{{365-{step['pessoa']-1}}}{{365}} = {step['novo_fator']:.6f}$
                
                Probabilidade acumulada: {step['prob_acumulada']:.6f}
                """)
        
        # Resultado final
        st.markdown(f"""
        **Resultado final**:
        
        Probabilidade de todos terem aniversários diferentes: {steps[-1]['prob_acumulada']:.6f}
        
        Probabilidade de pelo menos uma coincidência: $1 - {steps[-1]['prob_acumulada']:.6f} = {1 - steps[-1]['prob_acumulada']:.6f} = {(1 - steps[-1]['prob_acumulada']) * 100:.2f}\%$
        """)
    
    # Explicações matemáticas
    with st.expander("Ver fórmula matemática"):
        st.markdown(r"""
        ### Fórmula do Paradoxo do Aniversário
        
        A probabilidade $P(n)$ de pelo menos duas pessoas compartilharem o mesmo aniversário em um grupo de $n$ pessoas é:
        
        $$P(n) = 1 - \frac{365!}{(365-n)! \times 365^n}$$
        
        Para valores grandes, usamos a seguinte aproximação:
        
        $$P(n) = 1 - e^{-\frac{n(n-1)}{2 \times 365}}$$
        
        Ou a abordagem da multiplicação de probabilidades:
        
        $$P(n) = 1 - \prod_{i=0}^{n-1} \frac{365-i}{365}$$
        
        Esta última é a que usamos no cálculo.
        """)
    
    # Tabela de valores específicos
    with st.expander("Valores de referência"):
        reference_data = {
            "Pessoas": [10, 20, 23, 30, 40, 50, 60, 70],
            "Probabilidade (%)": [11.7, 41.1, 50.7, 70.6, 89.1, 97.0, 99.4, 99.9]
        }
        st.table(reference_data)

with col2:
    # Gera os dados para o gráfico
    people = np.arange(1, max(num_people * 2, 50))  # Garante que o eixo x seja pelo menos 2x o valor selecionado
    probabilities = [birthday_paradox(n, days_in_year) for n in people]
    
    # Criação do gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plotando a linha principal
    ax.plot(people, probabilities, marker='o', color='#1f77b4', label='Probabilidade')
    
    # Destacando o valor atual
    ax.axhline(probability, color='gray', linestyle='--', 
               label=f'Probabilidade atual: {probability_percent:.1f}%')
    ax.axvline(num_people, color='red', linestyle='--', 
               label=f'{num_people} pessoas')
    
    # Configuração do gráfico
    ax.set_title('Paradoxo do Aniversário: Probabilidade de Coincidência')
    ax.set_xlabel('Número de Pessoas na Sala')
    ax.set_ylabel('Probabilidade de pelo menos 2 pessoas\nfazerem aniversário no mesmo dia')
    ax.set_ylim(0, 1)
    ax.grid(True)
    ax.legend(loc='lower right')
    plt.tight_layout()
    
    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)
    
    # Calculando o número de comparações para o valor atual
    num_comparisons = (num_people * (num_people - 1)) // 2
    
    # Explicação do paradoxo
    st.markdown(r"""
    ### Explicação do Paradoxo
    
    O Paradoxo do Aniversário mostra como nossa intuição sobre probabilidade frequentemente nos engana. 
    
    Enquanto podemos pensar que precisaríamos de muitas pessoas para ter uma chance significativa 
    de aniversários coincidentes (já que há 365 dias no ano), na verdade a probabilidade cresce muito 
    rapidamente conforme aumentamos o número de pessoas.
    
    **Por que isso acontece?**
    
    Em um grupo de pessoas, não estamos comparando cada pessoa com uma data específica, mas cada pessoa 
    com todas as outras pessoas do grupo. O número de comparações possíveis cresce quadraticamente com o 
    tamanho do grupo.
    
    Para um grupo de $n$ pessoas, o número de pares únicos que podemos formar é:
    
    $$C(n,2) = \frac{n(n-1)}{2}$$
    """)
    
    # Aplicando a fórmula ao número atual
    st.markdown(f"""
    **Aplicando a fórmula ao valor selecionado ({num_people} pessoas):**
    """)
    
    # Criando a fórmula com os números específicos
    st.latex(f"C({num_people},2) = \\frac{{{num_people} \\times ({num_people}-1)}}{{2}} = \\frac{{{num_people} \\times {num_people-1}}}{{2}} = \\frac{{{num_people*(num_people-1)}}}{{2}} = {num_comparisons}")
    
    # Parte dinâmica com o número atual de pessoas e comparações
    st.info(f"""
    **Exemplo com o valor atual:**
    
    Com {num_people} pessoas, fazemos {num_comparisons} comparações de pares!
    
    Isso significa que estamos verificando {num_comparisons} possibilidades de coincidência,
    mesmo tendo apenas {num_people} pessoas em um universo de 365 dias possíveis.
    """)

# Rodapé
st.markdown("---")
st.markdown("Visualização interativa do Paradoxo do Aniversário | Feito por Alvaro Martins Alves | Desenvolvido com Streamlit") 