import streamlit as st
import pandas as pd
import os

# Função para carregar o CSV
def load_questions(file):
    file_path = os.path.join(os.path.dirname(__file__), file)
    df = pd.read_csv(file_path, sep=';')
    return df

# Função para calcular o índice de maturidade
def calculate_maturity(responses):
    # Garantir que apenas inteiros sejam usados
    responses = [int(r) for r in responses]
    total_score = sum(responses)
    max_score = len(responses) * 6
    
    # Calcular o índice de maturidade diretamente como uma média dos valores
    average_score = total_score / len(responses)
    
    # Arredondar para garantir um valor de 1 a 6
    maturity_index = round(average_score)
    
    # Garantir que o índice fique dentro dos limites de 1 a 6
    maturity_index = max(1, min(maturity_index, 6))
    
    return maturity_index

# Função para salvar as respostas em um arquivo CSV
def save_responses(company_name, responses, maturity_index):
    # Preparar os dados para salvar no CSV
    data = {'Empresa': company_name, 'Respostas': responses, 'Indice_Maturidade': maturity_index}
    df = pd.DataFrame([data])
    
    if os.path.exists("respostas_questionario.csv"):
        df.to_csv("respostas_questionario.csv", mode='a', header=False, index=False)
    else:
        df.to_csv("respostas_questionario.csv", mode='w', header=True, index=False)

# Página do questionário
def page_questionnaire():
    st.title("Avaliação da Maturidade da Cultura Organizacional")
    
    # Campo para o usuário inserir o nome da empresa
    company_name = st.text_input("Digite o nome da empresa:")

    # Carregar o CSV com as perguntas
    df = load_questions("questionario_cultura_organizacional.csv")

    # Lista para armazenar as respostas numéricas
    responses = []

    st.header("Por favor, responda às seguintes questões:")

    # Apresentar as perguntas e alternativas
    for index, row in df.iterrows():
        st.subheader(row['Pergunta'].strip())
        response = st.radio(
            f"Selecione sua resposta para a pergunta {index+1}:",
            options=[
                (1, row['Alternativa 1']),
                (2, row['Alternativa 2']),
                (3, row['Alternativa 3']),
                (4, row['Alternativa 4']),
                (5, row['Alternativa 5']),
                (6, row['Alternativa 6'])
            ],
            format_func=lambda x: x[1]
        )
        
        # Armazenar o valor numérico da resposta
        responses.append(response[0])

    # Botão para calcular a maturidade e salvar os dados
    if st.button("Enviar Dados"):
        if company_name:
            maturity_index = calculate_maturity(responses)
            save_responses(company_name, responses, maturity_index)
            st.success("Dados enviados com sucesso!")
            st.write(f"O índice de maturidade da {company_name} é {maturity_index}")
        else:
            st.error("Por favor, insira o nome da empresa antes de enviar.")

# Chamar a função na página principal
if __name__ == "__main__":
    page_questionnaire()
