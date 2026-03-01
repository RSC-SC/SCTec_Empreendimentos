# Desafio SCTec - Gestão de Empreendimentos (Santa Catarina)

## 🚀 Sobre o Projeto
Esta é uma API REST desenvolvida para o desafio do SCTec, focada no gerenciamento de empreendimentos no estado de Santa Catarina. O sistema permite o cadastro, listagem, atualização e remoção (CRUD) de empresas, com validações de segmentos e filtros de busca.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.10+
- **Framework:** FastAPI (Moderno, rápido e com documentação automática)
- **Banco de Dados:** SQLite (Persistência em arquivo, facilitando a portabilidade)
- **ORM:** SQLAlchemy (Mapeamento Objeto-Relacional)
- **Validação:** Pydantic v2 (Garantia de integridade dos dados)

## 🏗️ Estrutura do Projeto
- `app/main.py`: Endpoints da API e lógica de rotas.
- `app/models.py`: Definição das tabelas do banco de dados.
- `app/schemas.py`: Esquemas de validação e tipos de dados.
- `app/database.py`: Configuração da conexão com o SQLite.
- `requirements.txt`: Lista de dependências do sistema.

## 🔧 Como Executar
1. **Clone o repositório ou extraia os arquivos.**
2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv