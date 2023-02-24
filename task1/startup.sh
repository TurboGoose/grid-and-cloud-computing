#!/bin/bash

docker compose up -d
docker attach curl_client

# test (now have to execute it manually)
# curl -i -X GET http://server:8000/logs

# curl -i -X POST http://server:8000/logs -d "logs1"
# curl -i -X POST http://server:8000/logs -d "logs2"
# curl -i -X POST http://server:8000/logs -d "logs3"

# curl -i -X GET http://server:8000/logs

# curl -i -X DELETE http://server:8000/logs

# curl -i -X GET http://server:8000/logs