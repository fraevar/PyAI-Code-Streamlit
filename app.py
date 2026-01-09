# Criando Assistente de Programação Python, para auxiliar os amantes em Python

# Importa módulo para interagir com o sistema operacional
import os

# Importa a biblioteca Streamlit para criar a interface web interativa
import streamlit as st

# Importa a classe Groq para se conectar à API da plataforma Groq e acessar o LLM
from groq import Groq


from dotenv import load_dotenv
# Configura a página do Streamlit com título, ícone, layout e estado inicial da sidebar
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

st.set_page_config(
    page_title="ExPy Coder",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título no topo centralizado
st.markdown("""
<div style="text-align: center; margin-top: -2rem; margin-bottom: 2rem;">
    <h1 style="color: #E0E0E0; font-size: 1.8rem; font-weight: 600; margin-bottom: 0.5rem;">
        📊🐍 ExPy Coder: Domine Python, Excel e VBA com IA
    </h1>
    <p style="color: #B0B0B0; font-size: 0.9rem; margin: 0;">
        Seu caminho direto para dominar Python, Excel e VBA com IA.
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
Você é o "ExPy Coder", um assistente de IA especialista em programação e automação, com foco em Python, Excel e Excel VBA.  
Sua missão é ajudar desenvolvedores iniciantes e usuários de Excel a resolver problemas de programação, automação e análise de dados de forma clara, precisa e didática.

REGRAS DE OPERAÇÃO:

1. **Foco em Programação e Automação**  
   Responda exclusivamente a perguntas relacionadas a:
   - Python (lógica, scripts, automação, análise de dados, bibliotecas)
   - Excel (fórmulas, funções, tabelas, Power Query, boas práticas)
   - Excel VBA (macros, automação, manipulação de planilhas, formulários, eventos)
   - Integração entre Python e Excel (quando aplicável)

   Caso o usuário pergunte sobre assuntos fora desse escopo, responda educadamente que seu foco é exclusivamente programação, automação e uso técnico do Excel.

2. **Idioma e Localidade do Excel (REGRA OBRIGATÓRIA)**  
   - **Todas as fórmulas do Excel DEVEM ser escritas em Português do Brasil (pt-BR)**.
   - Utilize **nomes de funções em português** (ex: `SE`, `PROCV`, `SOMASE`, `ÍNDICE`, `CORRESP`).
   - Utilize **ponto e vírgula (`;`) como separador de argumentos**, nunca vírgula.
   - Caso exista diferença entre funções do Excel em inglês e português, **priorize sempre a versão em português**.
   - Se for relevante, pode mencionar entre parênteses o nome da função em inglês, **apenas como referência**, nunca como fórmula principal.

3. **Estrutura Obrigatória da Resposta**  
   Sempre formate suas respostas seguindo exatamente esta estrutura:

   **Explicação Clara**  
   - Inicie com uma explicação conceitual e objetiva sobre o problema ou tema.
   - Adapte o nível da explicação para iniciantes, evitando jargões desnecessários.

   **Exemplo de Código**  
   - Forneça exemplos práticos conforme o contexto da pergunta:
     - Python → código Python
     - Excel → fórmulas do Excel em **Português (pt-BR)**
     - Excel VBA → código VBA
   - Todo código deve estar corretamente formatado e **comentado linha a linha** quando possível.

   **Detalhes do Código**  
   - Explique detalhadamente o que cada parte do código, fórmula ou macro faz.
   - Destaque a lógica, boas práticas e possíveis variações ou cuidados.

   **Documentação de Referência**  
   Ao final, inclua uma seção chamada:
   📚 Documentação de Referência

   Utilize sempre links oficiais e relevantes, como:
   - Python: https://docs.python.org
   - Excel (Microsoft): https://support.microsoft.com/excel
   - Excel VBA: https://learn.microsoft.com/office/vba

4. **Clareza, Didática e Precisão**  
   - Use linguagem simples, direta e técnica.
   - Priorize exemplos práticos e aplicáveis ao dia a dia.
   - Nunca forneça respostas vagas ou genéricas.
   - Sempre revise a resposta para garantir precisão técnica e clareza.
"""

# Cria o conteúdo da barra lateral no Streamlit
with st.sidebar:
    
    # Define o título da barra lateral
    st.title("📊🐍 ExPy Coder")
    
    # Espaçamento para manter o input na mesma posição
    #st.markdown("<br>", unsafe_allow_html=True)

    # Campo para inserir a chave de API da Groq

    groq_api_key_input = st.text_input(
        "Insira aqui a sua API Key Groq", 
        type="password",
        help="Obtenha sua chave em https://console.groq.com/keys"
    )

    
    
    # Adiciona linhas divisórias, para melhorar a organização visual
    st.markdown("---")
    st.markdown("Conheça as Documentações: Python, Excel e VBA")

    # Link para a documentação Python
    st.markdown("🔗 [Documentação Python](https://docs.python.org/pt-br/3.14/)")
    st.markdown("🔗 [Documentação Excel](https://support.microsoft.com/excel)")
    st.markdown("🔗 [Documentação VBA](https://learn.microsoft.com/office/vba)")

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

# Decide qual API Key usar:
# 1️ variável de ambiente (.env)
# 2️ input do usuário
api_key = GROQ_API_KEY or groq_api_key_input

# Se nenhuma chave foi informada, interrompe a aplicação
if not api_key:
    st.warning("Informe sua API Key da Groq para continuar.")
    st.stop()

# Inicializa o cliente Groq
try:
    client = Groq(api_key=api_key)
except Exception as e:
    st.error(f"Erro ao inicializar o cliente Groq: {e}")
    st.stop()

if not st.session_state.get("api_warning_shown", False):
    st.markdown("""
    <style>
    div[data-testid="toast"] {
        background-color: #ff6b35 !important;
    }
    div[data-testid="toast"] > div {
        background-color: #ff6b35 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.toast(
        "ℹ️ Você está utilizando a API gratuita da Groq, que possui limites de uso. "
        "Para maior estabilidade e continuidade, utilize sua própria API Key.",
        icon="🤖"
    )

    st.session_state.api_warning_shown = True


# Captura a entrada do usuário no chat
if prompt := st.chat_input("Qual sua dúvida sobre Python, Excel ou VBA?"):
   
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
    O ExPy pode cometer erros. Por isso, é bom checar as respostas.
</div>
""", unsafe_allow_html=True)