#!/bin/bash

# retrieving all logs
curl -si -X GET http://server:8000/logs

# saving new logs
curl -si -X POST http://server:8000/logs -d "logs1"
curl -si -X POST http://server:8000/logs -d "logs2"
curl -si -X POST http://server:8000/logs -d "logs3"

# retrieving all logs
curl -si -X GET http://server:8000/logs

# deleting all logs
# curl -si -X DELETE http://server:8000/logs
