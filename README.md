# 🚀 Painel de Controle de Estudos com IA

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?style=for-the-badge&logo=flask)

Um assistente de estudos inteligente que utiliza uma arquitetura de múltiplos agentes de IA (Google Gemini) para criar planos de estudo detalhados, gerar desafios práticos e fornecer dicas técnicas sob demanda.

![image](https://github.com/user-attachments/assets/de8c3713-7e4a-469e-849a-68eaade5f2ee)

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

Siga estas instruções para obter uma cópia do projeto e executá-la em sua máquina local.

### Pré-requisitos

-   [Python](https://www.python.org/downloads/) (versão 3.9 ou superior)
-   [Git](https://git-scm.com/)

### Instalação Passo a Passo

1.  **Clone o repositório:**
    Abra seu terminal ou Git Bash e execute o comando:
    ```sh
    git clone https://github.com/LuizaMunis/Cronograma-de-Estudos-IA.git
    cd Cronograma-de-Estudos-IA
    ```

2.  **Instale as dependências:**
    Este projeto precisa de algumas bibliotecas Python para funcionar. Instale todas de uma vez com o seguinte comando completo no seu terminal:
    ```sh
    pip install Flask google-generativeai python-dotenv
    ```

3.  **Configure sua Chave de API:**
    Para proteger sua chave, não a deixe no código.
    -   Crie um arquivo chamado `.env` na pasta principal do projeto.
    -   Dentro do arquivo `.env`, adicione a linha:
        ```
        GOOGLE_API_KEY="SUA_CHAVE_DE_API_AQUI"
        ```
    -   Certifique-se que o seu arquivo `app.py` está configurado para ler esta chave (como fizemos na nossa versão final).
    -   **Importante:** Crie também um arquivo `.gitignore` e adicione `.env` a ele para que sua chave nunca seja enviada para o GitHub.

4.  **Execute o aplicativo:**
    Com tudo instalado e configurado, execute o seguinte comando no seu terminal:
    ```sh
    python app.py
    ```
    O aplicativo será iniciado e uma aba no seu navegador deve abrir automaticamente no endereço `http://127.0.0.1:5000`.

---

## 🚀 Como Usar

1.  **Gerador de Cronogramas**: A tela inicial. Preencha seus objetivos, nível e disponibilidade. Clique para gerar um plano de estudos detalhado.
2.  **Fábrica de Desafios**: Navegue para esta seção, insira um tópico (ex: "SQL Joins"), seu nível e clique para receber um problema prático para resolver.
3.  **Central de Dicas**: Similar aos desafios, insira um tópico e seu nível para receber uma dica técnica avançada do Agente Tutor.
4.  **Exportar e Salvar**: Uma vez que o cronograma é gerado, use os botões para baixá-lo como PDF ou simplesmente recarregue a página para acessá-lo novamente mais tarde.

---

## 📂 Estrutura do Projeto

```text
/painel-de-estudos-ia
|-- app.py              # Lógica do backend Flask, rotas e comunicação com a IA
|-- templates/
|   |-- index.html      # O único arquivo HTML, que contém a interface e o JavaScript
`-- README.md           # Este arquivo
