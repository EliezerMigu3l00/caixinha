# Como usar

1. **Primeiro passo é criar o ambiente virtual**:
   Execute o comando para criar:
   ```bash
   python -m venv .venv
   ```

2. **Agora ative o Ambiente Virtual**:
   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - **Linux / macOS**:
     ```bash
     source .venv/bin/activate
     ```

3. **Instalar as Dependências**:
   Todas as dependencias do projeto estao no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Fazer as Migrações**:
   Execute as migrações para configurar o banco de dados:
   ```bash
   python manage.py migrate
   ```

5. **Rodar o Projeto**:
   Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

6. **Acessar o Programa**:
   Abra o navegador e acesse a aplicação através da porta mostrada no terminal.
