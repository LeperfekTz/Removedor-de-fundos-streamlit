# 🖼️ Removedor de Fundo de Fotos

Uma aplicação web simples e eficiente para remover o fundo de imagens usando Streamlit e IA.

## 📋 Descrição

Este projeto utiliza a biblioteca `rembg` (Remove Background) para automaticamente remover o fundo de imagens enviadas pelo usuário. A interface é construída com Streamlit, proporcionando uma experiência web intuitiva e responsiva.

## ✨ Funcionalidades

- 🔄 **Remoção automática de fundo** usando modelos de IA pré-treinados
- 📤 **Upload de múltiplos formatos** (JPG, JPEG, PNG, BMP, WEBP)
- 👁️ **Visualização lado a lado** da imagem original e processada
- 💾 **Download direto** da imagem sem fundo em formato PNG
- 🌐 **Interface web responsiva** e fácil de usar

## 🚀 Como usar

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/LeperfekTz/Removedor-de-fundos-streamlit.git
   cd Removedor-de-fundos-streamlit
   ```

2. **Crie um ambiente virtual (recomendado):**
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual:**
   
   **Windows (PowerShell):**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   
   **Windows (Command Prompt):**
   ```cmd
   venv\Scripts\activate
   ```
   
   **Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

### Executando a aplicação

```bash
streamlit run main.py
```

A aplicação será aberta automaticamente no seu navegador em `http://localhost:8501`

## 🛠️ Dependências principais

- **streamlit** - Framework para criação de aplicações web
- **rembg** - Biblioteca para remoção de fundo usando IA
- **pillow** - Manipulação e processamento de imagens
- **onnxruntime** - Runtime para modelos de Machine Learning

## 📖 Como funciona

1. **Upload**: Envie uma imagem através da interface web
2. **Processamento**: A IA analisa a imagem e identifica o objeto principal
3. **Remoção**: O fundo é removido automaticamente
4. **Download**: Baixe a imagem processada em formato PNG com fundo transparente

## 🎯 Casos de uso

- 📸 Preparação de fotos para e-commerce
- 🎨 Criação de materiais gráficos
- 📱 Processamento de fotos de perfil
- 🖼️ Edição rápida de imagens para apresentações

## 🔧 Estrutura do projeto

```
Removedor-de-fundos-streamlit/
│
├── main.py              # Aplicação principal
├── requirements.txt     # Dependências do projeto
├── README.md           # Documentação
└── venv/               # Ambiente virtual (criado após instalação)
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**LeperfekTz**
- GitHub: [@LeperfekTz](https://github.com/LeperfekTz)

## 🙏 Agradecimentos

- [rembg](https://github.com/danielgatis/rembg) - Pela excelente biblioteca de remoção de fundo
- [Streamlit](https://streamlit.io/) - Pelo framework incrível para aplicações web em Python
- Comunidade open source por todas as bibliotecas utilizadas

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!