# Controle de Gastos

Aplicação web para registro e visualização de gastos pessoais, construída com Django. Permite cadastrar, editar e excluir gastos, com um painel visual que agrupa os valores por categoria em um gráfico.

## Funcionalidades

- Login/logout com contas criadas pelo admin do Django (cada usuário só visualiza seus próprios dados)
- CRUD completo de gastos (criar, listar, editar, excluir)
- Painel com total gasto e gráfico de distribuição por categoria (Chart.js)
- Interface responsiva com design próprio

## Tecnologias

- Python / Django
- SQLite
- Chart.js
- HTML / CSS

## Como rodar localmente

```bash
git clone https://github.com/Amaralzz/controle-de-gastos-django.git
cd controle-de-gastos-django

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/gastos/` no navegador.

## Decisões técnicas e aprendizados

- **Agregação de dados com o ORM do Django** (`values().annotate(Sum(...))`) para agrupar gastos por categoria — conceito equivalente a um `groupby` do Pandas, aplicado diretamente no banco de dados em vez de em memória.
- **Conversão de tipos para o front-end**: valores monetários são armazenados como `Decimal` (para evitar erros de arredondamento), mas precisam ser convertidos para `float` antes de serem enviados ao Chart.js, já que JavaScript não reconhece o tipo `Decimal` do Python.
- **Isolamento de dados por usuário**: todas as views usam `get_object_or_404(..., usuario=request.user)` em vez de apenas buscar pelo ID, evitando que um usuário logado edite ou exclua gastos de outra pessoa.

## Possíveis melhorias futuras

- Filtro de gastos por período (mês/ano)
- Exportação de relatórios em PDF ou CSV
- Categorias customizáveis por usuário