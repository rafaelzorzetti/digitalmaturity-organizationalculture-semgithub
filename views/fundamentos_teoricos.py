import streamlit as st
import os

# Função para ler o conteúdo de um arquivo markdown
def read_markdown_file(markdown_file):
    with open(markdown_file, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# Função para salvar as alterações no arquivo markdown
def save_markdown_file(markdown_file, content):
    with open(markdown_file, 'w', encoding='utf-8') as file:
        file.write(content)

def page_fundamentos_teoricos():
    st.title("Fundamentos Teóricos")

    # Caminho do arquivo markdown que será lido e modificado
    markdown_file = os.path.join('views', 'fundamentos_teoricos.md')

    # Carregar o conteúdo atual do arquivo .md
    content = read_markdown_file(markdown_file)
    
    # Exibir o conteúdo atual do markdown
    st.markdown(content)

    # Exibir caixa de texto para o usuário editar o markdown
    st.write("### Modificar o conteúdo abaixo:")
    updated_content = st.text_area("Editar fundamentos teóricos", content, height=300)

    # Upload de imagem
    uploaded_image = st.file_uploader("Carregar uma imagem", type=["png", "jpg", "jpeg"])

    # Se uma imagem for carregada, mostrar a imagem e adicionar o caminho sugerido no markdown
    if uploaded_image:
        st.image(uploaded_image, caption="Imagem carregada", use_column_width=True)
        image_path = f"![Imagem carregada](uploaded_image)"
        updated_content += f"\n\n{image_path}"
    
    # Botão para salvar as alterações
    if st.button("Salvar Alterações"):
        # Salvar o conteúdo atualizado no arquivo .md
        save_markdown_file(markdown_file, updated_content)
        
        # Recarregar o conteúdo atualizado
        st.success("Alterações salvas com sucesso!")
        
        # Recarregar
        st.rerun()

# Chamar a função na página principal
if __name__ == "__main__":
    page_fundamentos_teoricos()
