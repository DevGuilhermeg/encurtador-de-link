**README - Encurtador de Links com Flask**

Este é um simples encurtador de links desenvolvido em Python usando o framework Flask e o banco de dados SQLite. O aplicativo permite que os usuários encurtem URLs longas, gerando links curtos e fáceis de lembrar.

### Funcionalidades Principais:

1. **Encurtamento de Links:**
   - O aplicativo permite que os usuários insiram URLs longas e recebam links curtos exclusivos.

2. **Redirecionamento:**
   - Ao acessar um link encurtado, o usuário é redirecionado para a URL original.

### Requisitos de Instalação:

1. Certifique-se de ter o Python instalado. Caso contrário, faça o download e instale a versão mais recente em [python.org](https://www.python.org/).

2. Instale as bibliotecas necessárias executando o seguinte comando no terminal:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```

### Executando o Aplicativo:

1. Clone ou faça o download do repositório.

2. Navegue até o diretório do projeto no terminal:
   ```bash
   cd caminho/do/projeto
   ```

3. Execute o aplicativo com o seguinte comando:
   ```bash
   python app.py
   ```

4. Abra o navegador e acesse `http://localhost:5000` para usar o encurtador de links.

### Estrutura do Código:

- `app.py`: Contém o código principal do aplicativo Flask.
- `templates/`: Diretório que armazena os arquivos HTML usados para renderizar as páginas.

### Personalização:

- Você pode modificar o código para adicionar funcionalidades adicionais ou personalizar a aparência das páginas HTML no diretório `templates/`.

### Observações:

- Certifique-se de ter permissões adequadas para executar o aplicativo no ambiente local.
- O banco de dados SQLite (`banco.db`) é utilizado para armazenar as informações dos links encurtados.

Espero que este README ajude a entender e configurar o seu encurtador de links. Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato!
