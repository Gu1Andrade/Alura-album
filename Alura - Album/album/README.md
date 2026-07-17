# 🏆 Alura Album - Copa do Mundo Tech

O **Alura Album - Copa do Mundo Tech** é uma aplicação web interativa que simula um álbum de figurinhas virtual colecionável. O projeto homenageia grandes mentes, tecnologias e personalidades do ecossistema de desenvolvimento de software e da tecnologia moderna.

Desenvolvido com foco em alta fidelidade interativa e design premium, o projeto conta com efeitos visuais futuristas, simulação realista de folheamento de páginas e geração dinâmica de efeitos sonoros diretamente no navegador via síntese de áudio, além de uma API integrada para o carregamento dinâmico das figurinhas.

---

## 🎯 Principais Funcionalidades

- **Simulação Realista de Folheamento (`St.PageFlip`):** Permite arrastar e virar as páginas do álbum com animações e sombras realistas tridimensionais, adaptando-se para visualização em páginas duplas (desktop) ou página única (dispositivos móveis).
- **Arraste e Gestos Customizados:** Otimização para gestos de clique e toque na tela, ativando a animação de virada somente após transpor um limiar físico (threshold) de 10 pixels no mouse/touch, evitando disparos involuntários ao interagir com outros elementos.
- **Sintetizador Sonoro (Web Audio API):** Gera dinamicamente o som de papel virando em tempo real através da síntese de ruído branco, envelope de amplitude e filtros de frequência dinâmicos. Não requer download de arquivos de áudio externos!
- **Capa Cibernética Premium:** Animações com efeito glitch 100% CSS, esfera central em 3D brilhante com anéis em órbita rotativa, silhuetas de mini-cards flutuantes e selo brilhante de "Coleção Oficial".
- **Integração Assíncrona com API REST:** Busca a listagem de figurinhas disponíveis em um backend FastAPI e injeta as imagens nos respectivos slots no DOM com efeito suave de fade-in e overlay dinâmico com o nome do personagem.
- **Atualização Inteligente dos Slots:** Quando uma figurinha é carregada da API, o slot remove o texto informativo de fundo e exibe o nome do personagem formatado na base da figurinha.

---

## 💻 Tecnologias Utilizadas

### Frontend
- **HTML5:** Estrutura semântica para acessibilidade e organização do álbum.
- **CSS3 (Vanilla):** Variáveis de ambiente (`:root`), Grid e Flexbox Layout, animações de órbita 3D, efeitos de iluminação neon, técnica de glitch via clip-path e sombras de lombada dinâmicas para profundidade.
- **JavaScript (ES6+):** Controle de estado, manipulação assíncrona do DOM e requisições via Fetch API.
- **Web Audio API:** Síntese de áudio procedural para geração de som em tempo real.
- **[St.PageFlip](https://github.com/Nodonisko/StPageFlip):** Biblioteca JS para simulação de dobras e folheamento de páginas com fidelidade física.

### Backend
- **Python 3.x:** Linguagem base de programação do servidor.
- **FastAPI:** Framework moderno, robusto e de alto desempenho para construção de APIs assíncronas.
- **Uvicorn:** Servidor web ASGI de alta performance para execução da aplicação FastAPI.
- **CORS Middleware:** Configurado para aceitar requisições de qualquer origem (`*`), simplificando a comunicação local com o frontend.
- **Glob / OS:** Módulos integrados do Python para o mapeamento dinâmico de imagens e correspondência de nomes e extensões com base nos IDs.

---

## 📂 Estrutura do Projeto

O projeto é dividido em dois diretórios principais:

```text
├── backend/
│   ├── figurinhas/          # Pasta com as imagens das figurinhas (01-alan-turing.jpg a 30-Gui.jpeg)
│   ├── .venv/               # Ambiente virtual Python
│   ├── main.py              # Servidor API FastAPI (CORS, lista de figurinhas, endpoint de imagens)
│
└── front-end/album/
    ├── index.html           # Estrutura HTML do álbum (capa, páginas temáticas, botões)
    ├── style.css            # Estilos visuais, animações responsivas e efeitos especiais
    ├── app.js               # Lógica de controle, PageFlip, Web Audio e comunicação com a API
    └── README.md            # Documentação oficial do projeto
```

### Detalhamento das Páginas do Álbum
- **Capa:** Título com efeito glitch, esfera 3D central animada com anéis e silhuetas de mini-cards flutuantes.
- **Página 1:** *Pioneiros da Inteligência Artificial* (Figurinhas #01 a #05)
- **Página 2:** *Arquitetos da Simplicidade (Python)* (Figurinhas #06 a #10)
- **Página 3:** *Arquitetos de Bancos de Dados* (Figurinhas #11 a #15)
- **Página 4:** *Arquitetos da Computação Moderna (Sistemas Operacionais)* (Figurinhas #16 a #20)
- **Páginas 5 e 6:** *Celebridades Tech do Brasil* (Figurinhas #21 a #30)
- **Contracapa:** Resumo do álbum e simulação de código de barras.

---

## ⚙️ Instruções de Instalação e Execução

### 1. Configurando e Executando o Backend (FastAPI)

O backend é responsável por servir a lista estruturada das figurinhas e transmitir os respectivos arquivos de imagem dinamicamente.

1. Abra um terminal e navegue para o diretório do backend:
   ```powershell
   cd backend
   ```
2. Crie o ambiente virtual Python (caso ainda não o tenha feito):
   ```powershell
   python -m venv .venv
   ```
3. Ative o ambiente virtual:
   - **No Windows (PowerShell):**
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - **No Windows (CMD):**
     ```cmd
     .\.venv\Scripts\activate.bat
     ```
   - **No Linux / macOS:**
     ```bash
     source .venv/bin/activate
     ```
4. Instale as dependências do projeto:
   ```bash
   pip install fastapi uvicorn
   ```
5. Inicie o servidor FastAPI com live-reload ativo:
   ```bash
   uvicorn main:app --reload
   ```
   *O servidor do backend estará em execução em: `http://localhost:8000`.*

### 2. Executando o Frontend

Para que o frontend envie requisições HTTP (`fetch`) ao backend local e carregue a biblioteca `PageFlip` sem problemas de CORS ou bloqueios de protocolo de arquivo local (`file://`), recomenda-se rodar o frontend por meio de um servidor local.

**Opção A: Utilizando a extensão Live Server (VS Code)**
1. Abra a pasta `front-end/album` no VS Code.
2. Clique com o botão direito no arquivo `index.html` e selecione **"Open with Live Server"**.

**Opção B: Utilizando o Servidor HTTP embutido do Python**
1. Abra um terminal e navegue até a pasta do frontend:
   ```powershell
   cd front-end/album
   ```
2. Inicialize o servidor local:
   ```bash
   python -m http.server 8080
   ```
3. Acesse `http://localhost:8080` em seu navegador.

**Opção C: Utilizando o npx (Node.js)**
1. Abra um terminal e navegue até a pasta do frontend:
   ```powershell
   cd front-end/album
   ```
2. Execute o utilitário `serve`:
   ```bash
   npx serve .
   ```
3. Acesse o endereço informado (normalmente `http://localhost:3000` ou `http://localhost:5000`).

---

## 🎮 Como Utilizar a Aplicação

1. Certifique-se de que o backend FastAPI está rodando em `http://localhost:8000`.
2. Acesse o frontend por meio do servidor local configurado (por exemplo, `http://localhost:8080`).
3. **Virada de Páginas:**
   - **Mouse/Touch:** Clique nos cantos externos das páginas e arraste-as lateralmente.
   - **Teclado:** Utilize as setas direcionais esquerda e direita (`ArrowLeft` e `ArrowRight`).
   - **Navegação UI:** Clique nas setas flutuantes localizadas nas laterais esquerda e direita da tela.
4. **Controle de Efeitos Sonoros:**
   - Por padrão, o áudio sintetizado que simula o barulho das páginas físicas de papel é reproduzido ao folhear.
   - Clique no ícone de alto-falante localizado no canto superior direito para alternar entre os estados mudo e ativado.
5. **Figurinhas Coladas:**
   - Ao abrir e folhear o álbum, os slots serão preenchidos automaticamente com as fotos fornecidas pela API, se estiverem salvas no diretório `backend/figurinhas/`. As figurinhas entram com um efeito de fade-in e exibem o nome do respectivo profissional na parte inferior.

---

## 🛠️ Dependências do Projeto

### Backend
- **FastAPI**
- **Uvicorn**

### Frontend
- **StPageFlip (v2.0.7):** Biblioteca carregada via CDN:
  ```text
  https://cdn.jsdelivr.net/npm/page-flip@2.0.7/dist/js/page-flip.browser.min.js
  ```
- **Google Fonts:** Fontes *Inter* e *Outfit*:
  ```text
  https://fonts.googleapis.com
  ```
