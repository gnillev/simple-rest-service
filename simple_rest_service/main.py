from random import randrange
from time import sleep
from typing import Optional

from fastapi import FastAPI

from simple_rest_service.echo import echo


app = FastAPI()


@app.get("/echo/{echo_string}")
def echo_string(echo_string: str, q: Optional[str] = None):
    print(f"echo_string called with echo string {echo_string} and query params {q}")
    return echo(echo_string)


@app.get("/wait/{echo_string}")
def wait_and_echo(echo_string: str, q: Optional[str] = None):
    print(f"wait_and_echo called with echo string {echo_string} and query params {q}")
    wait_for = randrange(5)
    print(f"Waiting for {wait_for} seconds")
    sleep(wait_for)
    return echo(echo_string, prefix=f"waited {wait_for}, then echoed: ")
