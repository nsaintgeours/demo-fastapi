# Demo FastAPI

This project is a simple demo of how to create a basic **REST API** with **Python 3** using:

- [`fastapi`](https://fastapi.tiangolo.com) to serve the REST API
- [`pydantic`](https://docs.pydantic.dev) to manage data schemas
- [`Docker`](https://www.docker.com) for deployment

## Usage (with Docker)

**Prerequisites**

- `Docker` installed on your computer
- `Docker daemon` running

**Steps**

- build a Docker image for the REST API service:

```bash
docker build . -t my-image
```

- start a Docker container from the image:

```bash
docker run -p 80:80 my-image
```

**Usage**

You can now send requests to your REST API at [`http://localhost:80`](http://localhost:80). The
documentation of the REST API is available at  [`http://localhost:80/docs`](http://localhost:80/docs)
. For example, using `curl` command on Windows prompt:

```bash
curl -H "Content-Type: application/json" -d @./data/example.json http://localhost:80/api/v0/run
```

## Usage (development mode)

**Prerequisites**

- `python==3.9` and `pip` are installed on your computer

**Steps**

- open a terminal, and **move to the project's root folder**


- create and activate a virtual environment for the project (commands for Windows only):

```sh
python -m venv myenv
myenv\Scripts\activate
```

- make sure you have the latest versions of `pip` and `setuptools` libraries installed:

```sh
pip install --upgrade pip
pip install --upgrade setuptools
```

- install Python libraries that are required to run the app':

```sh
pip install -r requirements.txt
```

- install the project sources:

```sh
pip install -e .
```

- launch the REST API on local host with:

```bash
uvicorn src.api:app --host 0.0.0.0 --port 80
```

**Usage**

You can now send requests to the REST API at [`http://localhost:80`](http://localhost:80). The
documentation of the REST API is available at  [`http://localhost:80/docs`](http://localhost:80/docs)
. For example, using `curl` command on Windows prompt:

```bash
curl -H "Content-Type: application/json" -d @./data/example.json http://localhost:80/api/v0/run
```

You can also pass additional query parameters to the REST API, for example:

```bash
curl -H "Content-Type: application/json" -d @./data/example.json http://localhost:80/api/v0/run?some_param=0.2
```

## Remote deployment

- publish the Docker image on your Docker Hub registry:

```bash
docker image tag my-image nathaliesaintgeours/my-api:latest
docker push nathaliesaintgeours/my-api:latest

The push refers to repository [docker.io/nathaliesaintgeours/my-api]
3e27173a8d9a: Pushed
(...)
latest: digest: sha256:c0264ad47ef1921aec7d456f496cb8e2b3dab4578f028c79ed1576ea10c7a537 size: 2845
```

That's it! The Docker image of the REST API is now uploaded on [Docker Hub](https://hub.docker.com/).
You can now pull this image from a remote server to deploy the REST API wherever you need it.
