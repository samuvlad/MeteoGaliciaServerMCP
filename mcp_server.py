from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("Mi Servidor MCP")

STATION_LIST_URL = "https://servizos.meteogalicia.gal/mgrss/observacion/listaEstacionsMeteo.action"
DAILY_DATA_URL = "https://servizos.meteogalicia.gal/mgrss/observacion/datosDiariosEstacionsMeteo.action"

_station_cache: dict[str, str] = {}

def _load_stations():
    if _station_cache:
        return
    response = requests.get(STATION_LIST_URL)
    response.raise_for_status()
    data = response.json()
    for est in data.get("listaEstacionsMeteo", []):
        name = est.get("estacion", "")
        est_id = est.get("idEstacion")
        if name and est_id:
            _station_cache[name.lower()] = str(est_id)

def get_station_id(station_name: str) -> str | None:
    _load_stations()
    return _station_cache.get(station_name.lower())

@mcp.tool()
def get_info(station: str, start_date: str, end_date: str) -> dict:
    station_id = get_station_id(station)
    if not station_id:
        return {"error": f"Station not found: {station}"}

    params = {"idEst": station_id, "dataIni": start_date, "dataFin": end_date}
    response = requests.get(DAILY_DATA_URL, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    mcp.run(transport="stdio")
