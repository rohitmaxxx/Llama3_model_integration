
## 0. About

**Llama3 chat apis:** An extendable async API using FastAPI, Pydantic V2, SQLAlchemy 2.0 and PostgreSQL:

- [`FastAPI`](https://fastapi.tiangolo.com): modern Python web framework for building APIs
- [`Pydantic V2`](https://docs.pydantic.dev/2.4/): the most widely used data Python validation library, rewritten in Rust [`(5x-50x faster)`](https://docs.pydantic.dev/latest/blog/pydantic-v2-alpha/)
- [`SQLAlchemy 2.0`](https://docs.sqlalchemy.org/en/20/changelog/whatsnew_20.html): Python SQL toolkit and Object Relational Mapper
- [`PostgreSQL`](https://www.postgresql.org): The World's Most Advanced Open Source Relational Database
- [`Redis`](https://redis.io): Open source, in-memory data store used by millions as a cache, message broker and more.
- [`Docker Compose`](https://docs.docker.com/compose/) With a single command, create and start all the services from your configuration.
- [`NGINX`](https://nginx.org/en/) High-performance low resource consumption web server used for Reverse Proxy and Load Balancing.

## 1. Features

- Fully async
- Pydantic V2 and SQLAlchemy 2.0
- User authentication with JWT
- Cookie based refresh token
- Easy redis caching
- FastAPI docs behind authentication and hidden based on the environment
- Easily extendable
- Flexible
- Easy running with docker compose


## 2. Prerequisites

### 2.0 Start

Clone your created repository (I'm using the base for the example)

```sh
git clone https://github.com/rohitmaxxx/Llama3_model_integration.git
```
### 2.1 Install Ollama and model
Before start first install the ollama and then pull the **Llama3** model


### 2.2 Docker Compose (preferred)

To do it using docker compose, ensure you have docker and docker compose installed, then:
While in the base project directory (Llama3_model_integration here), run:

To run the seperate app for getting result from the llama3 model
```sh
python src/app2/main.py
```
Then run this command to run the main application
```sh
docker compose up
```

You should have a `web` container, `postgres` container, a `worker` container and a `redis` container running.
Then head to `http://127.0.0.1:8000/docs`.
