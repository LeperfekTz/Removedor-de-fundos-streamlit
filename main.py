

import streamlit as st
from rembg import remove
from PIL import Image
import io
import os

def remover_fundo_streamlit(imagem):
    """
    Remove o fundo de uma imagem enviada pelo usuário
    """
    try:
        # Remove o fundo
        img_data = io.BytesIO()
        imagem.save(img_data, format=imagem.format)
        img_data = img_data.getvalue()
        output_data = remove(img_data)
        
        # Retorna a imagem sem fundo
        img_output = Image.open(io.BytesIO(output_data))
        return img_output
    except Exception as e:
        st.error(f"Erro ao processar imagem: {e}")
        return None

# Configuração da página
st.set_page_config(page_title="Removedor de Fundo", layout="centered")

# Título do app
st.title("🖼️ Removedor de Fundo de Fotos")

# Upload de imagem
uploaded_file = st.file_uploader("Envie uma imagem", type=["jpg", "jpeg", "png", "bmp", "webp"])

if uploaded_file is not None:
    # Exibe a imagem original
    st.subheader("Imagem Original")
    imagem = Image.open(uploaded_file)
    st.image(imagem, caption="Imagem enviada", use_container_width=True)
    
    # Botão para remover fundo
    if st.button("Remover Fundo"):
        with st.spinner("Processando..."):
            imagem_sem_fundo = remover_fundo_streamlit(imagem)
            if imagem_sem_fundo:
                st.subheader("Imagem Sem Fundo")
                st.image(imagem_sem_fundo, caption="Imagem sem fundo", use_container_width=True)
                
                # Botão para download
                buf = io.BytesIO()
                imagem_sem_fundo.save(buf, format="PNG")
                byte_imagem = buf.getvalue()
                st.download_button(
                    label="Baixar Imagem Sem Fundo",
                    data=byte_imagem,
                    file_name="imagem_sem_fundo.png",
                    mime="image/png"
                )
