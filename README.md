# 🚀 Projeto de Automação Web com Selenium

Este projeto consiste em três scripts Python que utilizam a biblioteca Selenium para automatizar interações com uma aplicação web específica. Os scripts realizam diferentes tarefas, como preenchimento de formulários, envio de dados a partir de arquivos CSV e navegação entre páginas.

## 📂 Estrutura dos Scripts

### 1. Script 1: `Projeto1.py`
Este script automatiza o preenchimento e envio de formulários para a criação de cursos em uma plataforma web.

- **Funcionalidades:**
  - 🔑 Realiza login na plataforma.
  - 🌐 Navega para as páginas de criação de curso.
  - 📝 Preenche dados do curso como data de início, data de término, e regras específicas.
  - 📄 Lê dados de um arquivo CSV para preencher informações adicionais do curso.
  - ✅ Submete o formulário e repete o processo para outros cursos listados.

### 2. Script 2: `Projeto2.py`
Este script é utilizado para criar quizzes em uma plataforma online.

- **Funcionalidades:**
  - 🔑 Realiza login na plataforma.
  - 🌐 Navega para as páginas de criação de quizzes.
  - 📄 Lê dados de um arquivo CSV para preencher as informações do quiz, como nome, datas de início e término.
  - ⏰ Preenche automaticamente as datas e horários de abertura e fechamento do quiz.
  - ✅ Submete o formulário e repete o processo para outros quizzes listados.

### 3. Script 3: `Projeto3.py`
Este script automatiza o preenchimento de formulários com base em dados de arquivos CSV e faz upload desses dados em várias páginas da plataforma.

- **Funcionalidades:**
  - 🔑 Realiza login na plataforma.
  - 🌐 Carrega e navega em múltiplas páginas onde os dados devem ser inseridos.
  - 📄 Lê arquivos CSV para extrair e inserir dados nos campos de formulário.
  - 🔁 Itera através de várias páginas e arquivos para completar as tarefas automatizadas.

## 🛠️ Requisitos

- **Python 3.x**
- **Selenium** (`pip install selenium`)
- **webdriver_manager** (`pip install webdriver_manager`)

## 💻 Como Usar

1. **⚙️ Configuração do ambiente:**
   - Certifique-se de ter o Python 3.x instalado.
   - Instale as dependências necessárias usando pip:
     ```bash
     pip install selenium webdriver_manager
     ```

2. **▶️ Execução dos Scripts:**
   - Cada script pode ser executado individualmente.
   - Assegure-se de que os arquivos CSV mencionados nos scripts estejam presentes nos caminhos especificados.
   - Execute o script desejado usando o comando:
     ```bash
     python Projeto1.py
     ```
     ou
     ```bash
     python Projeto2.py
     ```
     ou
     ```bash
     python Projeto3.py
     ```

3. **🔧 Personalização:**
   - Edite os scripts para modificar os caminhos dos arquivos, URLs, e outras informações necessárias para a automação funcionar corretamente em seu ambiente.

## ⚠️ Observações

- As áreas com informações sensíveis foram omitidas ou substituídas por "-----" por questões de segurança.
- Certifique-se de atualizar os detalhes como credenciais de login, URLs, e caminhos de arquivos antes de executar os scripts.
