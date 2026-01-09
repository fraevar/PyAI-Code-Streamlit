# Criando Assistente de Programação Python, para auxiliar os amantes em Python

# Importa módulo para interagir com o sistema operacional
import os

# Importa a biblioteca Streamlit para criar a interface web interativa
import streamlit as st

# Importa a classe Groq para se conectar à API da plataforma Groq e acessar o LLM
from groq import Groq
#from openai import openai

# Configura a página do Streamlit com título, ícone, layout e estado inicial da sidebar
st.set_page_config(
    page_title="PyAI Coder",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título no topo centralizado
st.markdown("""
<div style="text-align: center; margin-top: -2rem; margin-bottom: 2rem;">
    <h1 style="color: #E0E0E0; font-size: 1.8rem; font-weight: 600; margin-bottom: 0.5rem;">
        🐍 PyAI Coder: Seu Tutor de Python com IA
    </h1>
    <p style="color: #B0B0B0; font-size: 0.9rem; margin: 0;">
        Seu caminho direto para dominar Python: ensino por IA, com base sólida e fontes confiáveis.
    </p>
</div>
""", unsafe_allow_html=True)

# Adiciona estrelas suaves e animadas
st.markdown("""
<style>
    .stars {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1000;
    }
    
    .star {
        position: absolute;
        background: white;
        border-radius: 50%;
        box-shadow: 0 0 4px rgba(255, 255, 255, 0.8);
        animation: sparkle 3s infinite ease-in-out, float 12s infinite ease-in-out;
    }
    
    .star-small { width: 2px; height: 2px; }
    .star-medium { width: 3px; height: 3px; }
    .star-large { width: 4px; height: 4px; }
    
    @keyframes sparkle {
        0%, 100% { opacity: 0.4; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.3); }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) translateX(0px); }
        25% { transform: translateY(-10px) translateX(5px); }
        50% { transform: translateY(-5px) translateX(-8px); }
        75% { transform: translateY(-15px) translateX(3px); }
    }
    
    .star:nth-child(1) { left: 8%; top: 15%; animation-delay: 0s, 0s; }
    .star:nth-child(2) { left: 25%; top: 70%; animation-delay: 0.5s, 1s; }
    .star:nth-child(3) { left: 45%; top: 25%; animation-delay: 1s, 2s; }
    .star:nth-child(4) { left: 65%; top: 80%; animation-delay: 1.5s, 3s; }
    .star:nth-child(5) { left: 85%; top: 35%; animation-delay: 0.2s, 4s; }
    .star:nth-child(6) { left: 15%; top: 60%; animation-delay: 0.8s, 5s; }
    .star:nth-child(7) { left: 35%; top: 10%; animation-delay: 1.2s, 6s; }
    .star:nth-child(8) { left: 55%; top: 55%; animation-delay: 1.8s, 7s; }
    .star:nth-child(9) { left: 75%; top: 20%; animation-delay: 0.3s, 8s; }
    .star:nth-child(10) { left: 95%; top: 75%; animation-delay: 0.7s, 9s; }
    .star:nth-child(11) { left: 20%; top: 40%; animation-delay: 1.3s, 10s; }
    .star:nth-child(12) { left: 40%; top: 85%; animation-delay: 1.7s, 11s; }
    .star:nth-child(13) { left: 60%; top: 5%; animation-delay: 0.4s, 0.5s; }
    .star:nth-child(14) { left: 80%; top: 65%; animation-delay: 0.9s, 1.5s; }
    .star:nth-child(15) { left: 10%; top: 90%; animation-delay: 1.4s, 2.5s; }
    .star:nth-child(16) { left: 30%; top: 50%; animation-delay: 0.1s, 3.5s; }
    .star:nth-child(17) { left: 50%; top: 95%; animation-delay: 0.6s, 4.5s; }
    .star:nth-child(18) { left: 70%; top: 45%; animation-delay: 1.1s, 5.5s; }
    .star:nth-child(19) { left: 90%; top: 10%; animation-delay: 1.6s, 6.5s; }
    .star:nth-child(20) { left: 5%; top: 30%; animation-delay: 0.5s, 7.5s; }
    .star:nth-child(21) { left: 12%; top: 25%; animation-delay: 2.1s, 8.5s; }
    .star:nth-child(22) { left: 28%; top: 75%; animation-delay: 2.6s, 9.5s; }
    .star:nth-child(23) { left: 48%; top: 35%; animation-delay: 0.3s, 10.5s; }
    .star:nth-child(24) { left: 68%; top: 15%; animation-delay: 0.8s, 11.5s; }
    .star:nth-child(25) { left: 88%; top: 85%; animation-delay: 1.9s, 0.8s; }
</style>

<div class="stars">
    <div class="star star-medium"></div>
    <div class="star star-large"></div>
    <div class="star star-small"></div>
    <div class="star star-medium"></div>
    <div class="star star-large"></div>
    <div class="star star-small"></div>
    <div class="star star-medium"></div>
    <div class="star star-small"></div>
    <div class="star star-large"></div>
    <div class="star star-medium"></div>
    <div class="star star-small"></div>
    <div class="star star-medium"></div>
    <div class="star star-large"></div>
    <div class="star star-small"></div>
    <div class="star star-medium"></div>
    <div class="star star-large"></div>
    <div class="star star-small"></div>
    <div class="star star-medium"></div>
    <div class="star star-small"></div>
    <div class="star star-large"></div>
    <div class="star star-medium"></div>
    <div class="star star-small"></div>
    <div class="star star-medium"></div>
    <div class="star star-large"></div>
    <div class="star star-small"></div>
</div>
""", unsafe_allow_html=True)

# Define um prompt de comando que descreve as regras e comportamento da LLM
CUSTOM_PROMPT = """
Você é o "PyAI Coder", um assistente de IA especialista em programação, com foco principal em Python. Sua missão é ajudar desenvolvedores iniciantes com dúvidas de programação de forma clara, precisa e útil.

REGRAS DE OPERAÇÃO:
1.  **Foco em Programação**: Responda apenas a perguntas relacionadas a programação, algoritmos, estruturas de dados, bibliotecas e frameworks. Se o usuário perguntar sobre outro assunto, responda educadamente que seu foco é exclusivamente em auxiliar com código.
2.  **Estrutura da Resposta**: Sempre formate suas respostas da seguinte maneira:
    * **Explicação Clara**: Comece com uma explicação conceitual sobre o tópico perguntado. Seja direto e didático.
    * **Exemplo de Código**: Forneça um ou mais blocos de código em Python com a sintaxe correta. O código deve ser bem comentado para explicar as partes importantes.
    * **Detalhes do Código**: Após o bloco de código, descreva em detalhes o que cada parte do código faz, explicando a lógica e as funções utilizadas.
    * **Documentação de Referência**: Ao final, inclua uma seção chamada "📚 Documentação de Referência" com um link direto e relevante para a documentação oficial da Linguagem Python (docs.python.org) ou da biblioteca em questão.
3.  **Clareza e Precisão**: Use uma linguagem clara. Evite jargões desnecessários. Suas respostas devem ser tecnicamente precisas.
"""

# Cria o conteúdo da barra lateral no Streamlit
with st.sidebar:
    
    # Define o título da barra lateral
    st.title("🐍 PyAI Coder")
    
    # Espaçamento para manter o input na mesma posição
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Campo para inserir a chave de API da Groq
    groq_api_key = st.text_input(
        "Insira aqui a sua API Key Groq", 
        type="password",
        help="Obtenha sua chave em https://console.groq.com/keys"
    )

    
    st.markdown("<br>", unsafe_allow_html=True)
    # Adiciona linhas divisórias, para melhorar a organização visual
    st.markdown("---")
    st.markdown("Conheça a Documentação completa de Python:")

    # Link para a documentação Python
    st.markdown("🔗 [Documentação Python](https://docs.python.org/pt-br/3.14/)")
    
    # Botão de link para enviar e-mail
    st.link_button("✉️ E-mail Para Dúvidas", "mailto:evandrorf34@gmail.com")
    
    # Assinatura do desenvolvedor
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #888888; font-size: 0.8rem; margin-top: 1rem;'>"
        "💻 Desenvolvido por<br><strong>Evandro Franco</strong></div>", 
        unsafe_allow_html=True
    )



# Inicializa o histórico de mensagens na sessão, caso ainda não exista
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe todas as mensagens anteriores armazenadas no estado da sessão
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Inicializa a variável do cliente Groq como None
client = None

# Verifica se o usuário forneceu a chave de API da Groq
if groq_api_key:
    
    try:
        
        # Cria cliente Groq com a chave de API fornecida
        client = Groq(api_key = groq_api_key)
    
    except Exception as e:
        
        # Exibe erro caso haja problema ao inicializar cliente
        st.sidebar.error(f"Erro ao inicializar o cliente Groq: {e}")
        st.stop()

# Caso não tenha chave, mas já existam mensagens, mostra aviso
elif st.session_state.messages:
     st.warning("Por favor, insira sua API Key da Groq na barra lateral para continuar.")

# Caso não tenha chave, mas já existam mensagens, mostra aviso
elif st.session_state.messages:
     st.warning("Por favor, insira sua API Key da Groq na barra lateral para continuar.")

# Captura a entrada do usuário no chat
if prompt := st.chat_input("Qual sua dúvida sobre Python?"):
    
    # Se não houver cliente válido, mostra aviso e para a execução
    if not client:
        st.warning("Por favor, insira sua API Key da Groq na barra lateral para começar.")
        st.stop()

    # Armazena a mensagem do usuário no estado da sessão
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Exibe a mensagem do usuário no chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepara mensagens para enviar à API, incluindo prompt de sistema
    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    for msg in st.session_state.messages:
        
        messages_for_api.append(msg)

    # Cria a resposta do assistente no chat
    with st.chat_message("assistant"):
        
        with st.spinner("Analisando sua pergunta..."):
            
            try:
                
                # Chama a API da Groq para gerar a resposta do assistente
                chat_completion = client.chat.completions.create(
                    messages = messages_for_api,
                    model = "openai/gpt-oss-20b", 
                    temperature = 0.7,
                    max_tokens = 2048,
                )
                
                # Extrai a resposta gerada pela API
                dsa_ai_resposta = chat_completion.choices[0].message.content
                
                # Exibe a resposta no Streamlit
                st.markdown(dsa_ai_resposta)
                
                # Armazena resposta do assistente no estado da sessão
                st.session_state.messages.append({"role": "assistant", "content": dsa_ai_resposta})

            # Caso ocorra erro na comunicação com a API, exibe mensagem de erro
            except Exception as e:
                st.error(f"Ocorreu um erro ao se comunicar com a API da Groq: {e}")

# Texto de aviso simples
st.markdown("""
<style>
    .disclaimer-below-input {
        position: fixed;
        bottom: 10px;
        left: 50%;
        transform: translateX(-50%);
        color: #888888;
        font-size: 0.75rem;
        text-align: center;
        z-index: 1001;
        width: 100%;
    }
</style>
<div class="disclaimer-below-input">
    O PyAI pode cometer erros. Por isso, é bom checar as respostas.
</div>
""", unsafe_allow_html=True)




