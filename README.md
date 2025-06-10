# 🚀 Painel de Controle de Estudos com IA

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?style=for-the-badge&logo=flask)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

Um assistente de estudos inteligente que utiliza uma arquitetura de múltiplos agentes de IA (Google Gemini) para criar planos de estudo detalhados, gerar desafios práticos e fornecer dicas técnicas sob demanda.

(![image](https://github.com/user-attachments/assets/de8c3713-7e4a-469e-849a-68eaade5f2ee)

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
  - [A Arquitetura de 3 Agentes de IA](#-a-arquitetura-de-3-agentes-de-ia)
- [✨ Funcionalidades Principais](#-funcionalidades-principais)
- [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [⚙️ Começando](#️-começando)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação Passo a Passo](#instalação-passo-a-passo)
- [🚀 Como Usar](#-como-usar)
- [📂 Estrutura do Projeto](#-estrutura-do-projeto)
- [📄 Licença](#-licença)

---

## 📖 Sobre o Projeto

Este projeto nasceu da necessidade de criar planos de estudo que fossem além de uma simples lista de tópicos. O objetivo é fornecer um ecossistema de ferramentas inteligentes para auxiliar estudantes e autodidatas em sua jornada de aprendizado. Utilizando o poder do Google Gemini, o aplicativo não só planeja, mas também interage, desafia e aconselha.

### 🤖 A Arquitetura de 3 Agentes de IA

O coração deste aplicativo é a sua arquitetura de múltiplos agentes, onde cada agente tem uma especialização, garantindo respostas de alta qualidade e relevância:

1.  **O Agente Arquiteto**: Recebe os objetivos gerais do usuário e projeta o esqueleto do plano de estudos, definindo os grandes módulos e a ordem lógica de aprendizado.
2.  **O Agente Curador (Mentor Sênior)**: Pega cada módulo definido pelo Arquiteto e o transforma em um plano semanal ultra-detalhado, com objetivos, tópicos técnicos, um roteiro diário, um mini-projeto e, crucialmente, uma lista de **recursos específicos e nomeados** (artigos, vídeos, livros).
3.  **O Agente Tutor**: Atua como um tutor sob demanda, gerando desafios práticos com soluções e dicas técnicas avançadas para qualquer tópico solicitado pelo usuário, de forma independente do cronograma.

---

## ✨ Funcionalidades Principais

-   **Gerador de Cronogramas Dinâmico**: Cria planos de estudo semanais detalhados e personalizados com base em seus objetivos, nível e tempo disponível.
-   **Fábrica de Desafios Sob Demanda**: Gere desafios práticos sobre qualquer tópico para testar seus conhecimentos.
-   **Central de Dicas Técnicas**: Obtenha dicas avançadas e "truques" de especialistas sobre a tecnologia que você está estudando.
-   **Persistência de Dados**: Seu último cronograma gerado é salvo no navegador (`localStorage`), para que você não perca seu plano ao atualizar a página.
-   **Exportação para PDF**: Baixe seu cronograma completo em um arquivo PDF limpo e bem formatado com um único clique.
-   **Interface Reativa**: Navegação fluida entre as ferramentas sem a necessidade de recarregar a página, simulando uma experiência de SPA (Single-Page Application).

---

## 🛠️ Tecnologias Utilizadas

-   **Backend**:
    -   [Python](https://www.python.org/)
    -   [Flask](https://flask.palletsprojects.com/)
    -   [Google Gemini API](https://ai.google.dev/gemini-api)
-   **Frontend**:
    -   HTML5
    -   CSS3 (Estilização moderna)
    -   JavaScript (Vanilla JS, Fetch API para comunicação com o backend)
-   **Geração de PDF**:
    -   [html2pdf.js](https://github.com/eKoopmans/html2pdf.js/) (Biblioteca client-side para conversão de HTML para PDF)

---

## ⚙️ Começando

Siga estas instruções para obter uma cópia do projeto e executá-la em sua máquina local para desenvolvimento e testes.

### Pré-requisitos

-   [Python](https://www.python.org/downloads/) (versão 3.9 ou superior)
-   [Git](https://git-scm.com/)

### Instalação Passo a Passo

1.  **Clone o repositório:**
    ```sh
    git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
    cd nome-do-repositorio
    ```

2.  **Crie e ative um ambiente virtual (altamente recomendado):**
    ```sh
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Crie um arquivo `requirements.txt`** com o seguinte conteúdo:
    ```txt
    Flask
    google-generativeai
    ```

4.  **Instale as dependências:**
    ```sh
    pip install -r requirements.txt
    ```

5.  **Configure sua Chave de API do Google Gemini:**

    O método mais seguro é usar variáveis de ambiente.

    -   **No Windows (CMD/PowerShell):**
        ```sh
        set GOOGLE_API_KEY="SUA_CHAVE_DE_API_AQUI"
        ```
    -   **No macOS/Linux:**
        ```sh
        export GOOGLE_API_KEY="SUA_CHAVE_DE_API_AQUI"
        ```

    O arquivo `app.py` precisará ser ajustado para ler esta variável. Substitua a linha `genai.configure(...)` por:
    ```python
    import os
    # ...
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Chave de API não encontrada. Defina a variável de ambiente GOOGLE_API_KEY.")
    genai.configure(api_key=api_key)
    ```
    *(**Nota:** Se preferir manter a chave diretamente no código para testes locais, como fizemos, lembre-se de nunca enviar este arquivo para um repositório público.)*

6.  **Execute o aplicativo:**
    ```sh
    python app.py
    ```

    Abra seu navegador e acesse `http://127.0.0.1:5000`.

---

## 🚀 Como Usar

1.  **Gerador de Cronogramas**: A tela inicial. Preencha seus objetivos, nível e disponibilidade. Clique para gerar um plano de estudos detalhado.
2.  **Fábrica de Desafios**: Navegue para esta seção, insira um tópico (ex: "SQL Joins"), seu nível e clique para receber um problema prático para resolver.
3.  **Central de Dicas**: Similar aos desafios, insira um tópico e seu nível para receber uma dica técnica avançada do Agente Tutor.
4.  **Exportar e Salvar**: Uma vez que o cronograma é gerado, use os botões para baixá-lo como PDF ou simplesmente recarregue a página para acessá-lo novamente mais tarde.

---

## 📂 Estrutura do Projeto

/painel-de-estudos-ia
|-- app.py              # Lógica do backend Flask, rotas e comunicação com a IA
|-- templates/
|   |-- index.html      # O único arquivo HTML, que contém a interface e o JavaScript
|-- requirements.txt    # Lista de dependências Python
`-- README.md           # Este arquivo

