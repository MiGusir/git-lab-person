# git-lab-person

Учебный проект для практики CI/CD (GitHub Actions).

## Установка

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Тесты

```bash
pytest
```

## Документация

Генерируется автоматически в CI в папку `docs/`.
Локально:

```bash
pdoc -o docs person
```
