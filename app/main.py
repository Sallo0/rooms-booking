import uvicorn

from app.admin.admin import admin  # noqa
from app.api import app  # noqa

# TODO: sql mapping
# TODO: add tests
# TODO: logging and monitoring
# TODO: prometheus grafana

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
