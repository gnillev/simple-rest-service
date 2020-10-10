
from fastapi import FastAPI

from simple_rest_service.echo import echo


app = FastAPI()


@app.get("/echo/{echo_string}")
def echo(echo_string: str, q: Optional[str] = None):
    print(f"echo_string called with query params {q}")
    return echo(echo_string)
