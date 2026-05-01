# MeteoGalicia MCP Server

Un servidor MCP (Model Context Protocol) para obter datos meteorolóxicos de Galicia.

## Requisitos

- Python 3.10+
- mcp
- requests

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

```bash
python mcp_server.py
```

## Ferramenta `get_info`

Obtén datos meteorolóxicos dunha estación de Galicia.

**Parámetros:**
- `station`: Nome da estación meteorolóxica
- `start_date`: Data de inicio (formato: YYYY-MM-DD)
- `end_date`: Data de fin (formato: YYYY-MM-DD)
