import streamlit as st
import sqlite3
import pandas as pd
import os

# --- 1. CONFIGURAÇÃO E DESIGN RIGOROSO ---
st.set_page_config(page_title="Blog do Chef João P. Roth", layout="wide")

st.markdown("""
    <style>
    /* Fundo TOTALMENTE BRANCO (Fundo principal, Menu Lateral e Barra do Topo) */
    .stApp, section[data-testid="stSidebar"], header[data-testid="stHeader"] { 
        background-color: #ffffff !important; 
    }
    
    /* Textos PRETOS por padrão */
    .stApp p, .stApp span, .stApp div, .stApp label, .stApp li, .stApp h1, .stApp h2, .stApp h3, .stApp h4 { 
        color: #000000 !important; 
    }
    
    /* SETINHA DO MENU EM VERMELHO FORTE */
    [data-testid="collapsedControl"] { color: #e60000 !important; }
    [data-testid="collapsedControl"] svg { fill: #e60000 !important; color: #e60000 !important; }
    
    /* Expansor (Clique aqui para escrever...) */
    [data-testid="stExpander"] details summary { background-color: #262730 !important; border-radius: 5px; }
    [data-testid="stExpander"] details summary p, [data-testid="stExpander"] details summary span, [data-testid="stExpander"] svg { color: #ffffff !important; font-weight: bold !important; }
    
    /* TODOS OS BOTÕES VERMELHOS COM LETRA BRANCA (Inclui Botões de Foto/Upload) */
    div.stButton > button, 
    [data-testid="stFormSubmitButton"] > button,
    [data-testid="stCameraInput"] button,
    [data-testid="stFileUploadDropzone"] button { 
        background-color: #e60000 !important; 
        border: none !important; 
    }
    div.stButton > button p, 
    [data-testid="stFormSubmitButton"] > button p,
    [data-testid="stCameraInput"] button p,
    [data-testid="stFileUploadDropzone"] button p,
    [data-testid="stCameraInput"] button span,
    [data-testid="stFileUploadDropzone"] button span { 
        color: #ffffff !important; 
        font-weight: bold !important; 
    }
    div.stButton > button:hover, 
    [data-testid="stFormSubmitButton"] > button:hover,
    [data-testid="stCameraInput"] button:hover,
    [data-testid="stFileUploadDropzone"] button:hover { 
        background-color: #cc0000 !important; 
    }

    /* Caixas de texto e seletores */
    div[data-baseweb="input"] > div, div[data-baseweb="textarea"] > div, div[data-baseweb="select"] > div { background-color: #ffffff !important; border: 1px solid #cccccc !important; }
    div[data-baseweb="input"] input, div[data-baseweb="textarea"] textarea, div[data-baseweb="select"] div, div[data-baseweb="select"] span { color: #000000 !important; }
    ul[data-baseweb="menu"] { background-color: #ffffff !important; }
    ul[data-baseweb="menu"] li { color: #000000 !important; }
    
    /* Detalhes visuais */
    section[data-testid="stSidebar"] { border-right: 2px solid #e60000 !important; }
    h1 { border-bottom: 3px solid #e60000 !important; padding-bottom: 10px !important; }
    blockquote { border-left: 5px solid #e60000 !important; background-color: #f9f9f9 !important; padding: 15px !important; margin: 10px 0 !important; color: #000000 !important; font-style: italic !important; }
    </style>
""", unsafe_allow_html=True)

if not os.path.exists("fotos_pratos"):
    os.makedirs("fotos_pratos")

# --- 2. BANCO DE DADOS ---
def inicializar_banco():
    conn = sqlite3.connect('culinaria_v5.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS avaliacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            comida TEXT, 
            restaurante TEXT, 
            preco REAL,
            tamanho TEXT,
            nota INTEGER, 
            comentario TEXT, 
            caminho_foto TEXT
        )
    ''')
    conn.commit()
    return conn

conn = inicializar_banco()

# --- 3. AS PÁGINAS ---

def pagina_quem_somos():
    st.title("Quem Somos")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("chef_joao.jpg"):
            st.image("chef_joao.jpg", use_container_width=True)
        else:
            st.error("A foto 'chef_joao.jpg' não foi encontrada.")
            
    with col2:
        st.subheader("João P. Roth")
        st.markdown("**Autor do blog Nº1 & Food Critic Elected by Time Magazine**")
        st.markdown("> \"Com análises tecnicamente perfeitas e um nível de exigência inegociável, João P. Roth consolidou-se definitivamente como a voz mais influente da alta gastronomia mundial.\" — **Time Magazine**")
        st.markdown("> \"Durante meus oito anos na Casa Branca, lidei com crises globais de todas as naturezas. Mas afirmo com tranquilidade: nada gera mais tensão em um salão do que João P. Roth erguendo uma taça de vinho para analisá-la contra a luz. Seu paladar deveria ser tombado como patrimônio mundial.\" — **Barack Obama**")
        st.markdown("> \"A diplomacia exige resiliência, mas a crítica de Roth é um ataque fulminante e sem concessões à mediocridade. Sua exigência na mesa de jantar é, de longe, mais implacável e temida que qualquer negociação de Estado que já presenciei.\" — **Benjamin Netanyahu**")
        st.markdown("> \"Eu achei que fosse o maior terror das cozinhas, até o dia em que João devolveu o meu melhor Beef Wellington dizendo que a carne 'carecia de propósito'. O homem é um gênio insensível, e eu nunca mais dormi direito desde então.\" — **Gordon Ramsay**")
        st.markdown("> \"Eu enfrentei grupos extremistas e lutei pelo direito global à educação sem hesitar, mas confesso que o arrepio é real quando vejo João P. Roth em silêncio após a primeira garfada. Sua caneta corta mais que qualquer espada, e seu paladar é uma força da natureza.\" — **Malala Yousafzai**")
        st.markdown("> \"O Barack pode até ficar nervoso com a avaliação rigorosa dele sobre os cardápios dos nossos jantares oficiais, mas vou te contar um segredo: toda vez que ele passa pela porta, eu só consigo pensar em como, além de ser o crítico mais temido do mundo, esse homem é um baita de um gatinho.\" — **Michelle Obama**")

    st.write("---")
    
    col3, col4 = st.columns([1, 2])
    with col3:
        if os.path.exists("socio.jpg"):
            st.image("socio.jpg", use_container_width=True)
        else:
            st.error("A foto 'socio.jpg' não foi encontrada.")
            
    with col4:
        st.subheader("Estudante de arquitetura e amigo do João P. Roth")
        st.write("**Nome/ apelido:** Artur Fauth")
        st.write("**Cidade natal:** Santa Maria")
        st.write("**Filmes favoritos:** Corra!, O pianista e Monstros S.A. De série sou muito fã de Game of Thrones!")
        st.write("**Hobbies:** Esportes, videogame, assistir filmes")
        st.write("**Artista favorito:** Bruno Mars e muitos outros")
        st.write("**Música favorita:** Best Friend - 50 Cent, Wake up in the Sky")
        st.write("**Por que escolheu aqr&urb?** Desde pequeno gostava de desenhar prédios, jogos de construir cidades e ler revistas de arquitetura")
        st.write("**Qual outro curso faria?** Relações Internacionais")

def pagina_feed():
    st.title("Feed de Críticas")
    
    with st.expander("Clique aqui para escrever uma nova avaliação"):
        with st.form("form_nova", clear_on_submit=True):
            comida = st.text_input("Comida")
            restaurante = st.text_input("Nome do Restaurante")
            
            col_preco, col_tamanho = st.columns(2)
            with col_preco:
                preco = st.number_input("Preço (R$)", min_value=0.0, step=1.00, format="%.2f")
            with col_tamanho:
                tamanho = st.selectbox("Tamanho do prato", ["1 - Passa vontade", "2 - Dava pra ter um pouco mais", "3 - Satisfeito"])
                
            nota = st.slider("Nota (0 a 10)", 0, 10, 5)
            comentario = st.text_area("Descrição da sua experiência")
            
            st.write("---")
            st.markdown("**Adicionar foto da comida**")
            
            aba_galeria, aba_camera = st.tabs(["Subir arquivo da galeria", "Tirar foto na hora"])
            with aba_galeria:
                foto_galeria = st.file_uploader("Escolha uma foto do seu celular/PC", type=['png', 'jpg', 'jpeg'])
            with aba_camera:
                foto_camera = st.camera_input("Tire a foto agora")
            
            submeteu = st.form_submit_button("Publicar Avaliação")
            
            if submeteu:
                if comida and restaurante:
                    foto_final = foto_galeria if foto_galeria is not None else foto_camera
                    
                    caminho_foto = ""
                    if foto_final is not None:
                        caminho_foto = os.path.join("fotos_pratos", foto_final.name)
                        with open(caminho_foto, "wb") as f:
                            f.write(foto_final.getbuffer())
                            
                    cursor = conn.cursor()
                    cursor.execute('''INSERT INTO avaliacoes (comida, restaurante, preco, tamanho, nota, comentario, caminho_foto) 
                                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (comida, restaurante, preco, tamanho, nota, comentario, caminho_foto))
                    conn.commit()
                    st.success("Avaliação salva com sucesso!")
                else:
                    st.error("Por favor, preencha pelo menos a comida e o restaurante.")

    st.write("---") 
    
    df = pd.read_sql_query("SELECT * FROM avaliacoes ORDER BY id DESC", conn)
    
    if not df.empty:
        for index, linha in df.iterrows():
            col_foto, col_texto = st.columns([1, 2]) 
            with col_foto:
                if linha['caminho_foto'] and os.path.exists(linha['caminho_foto']):
                    st.image(linha['caminho_foto'], use_container_width=True)
                else:
                    st.write("Sem foto")
            with col_texto:
                st.subheader(f"{linha['comida']}")
                st.markdown(f"**Restaurante:** {linha['restaurante']}")
                st.markdown(f"**Preço:** R$ {linha['preco']:.2f} | **Nota:** {linha['nota']}/10")
                st.markdown(f"**Tamanho do prato:** {linha['tamanho']}")
                st.write(linha['comentario'])
                
                if st.button("Apagar Avaliação", key=f"delete_{linha['id']}"):
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM avaliacoes WHERE id = ?", (linha['id'],))
                    conn.commit()
                    if linha['caminho_foto'] and os.path.exists(linha['caminho_foto']):
                        try: os.remove(linha['caminho_foto'])
                        except: pass 
                    st.rerun()
            st.write("---") 
    else:
        st.info("Nenhuma avaliação ainda. Seja o primeiro a publicar!")

# --- 4. O MENU LATERAL ---
st.sidebar.title("Menu")
pagina_escolhida = st.sidebar.radio("Navegação:", ["Página Principal", "Quem Somos"])

if pagina_escolhida == "Página Principal": pagina_feed()
elif pagina_escolhida == "Quem Somos": pagina_quem_somos()