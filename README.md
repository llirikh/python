# Шаги по тестированию задач

Uv installing
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
```

Создание окружения
```bash
uv venv --python 3.13.7 .venv
```

Environment activation
```bash
source .venv/bin/activate
```

Установка зависимостей из ```pyproject.toml```
```bash
uv sync --active
```

Установка внутренней библиотеки
```bash
uv pip install --upgrade --editable tools/testlib
```

Запуск тестов
```bash
pytest tasks/01_1_python_tools/hello_world/

ruff check tasks/01_1_python_tools/hello_world/

pyrefly check tasks/01_1_python_tools/hello_world/
```