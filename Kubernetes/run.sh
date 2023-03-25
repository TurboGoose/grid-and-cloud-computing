#!/bin/bash

# minikube start

kubectl apply -f secret.yaml
kubectl apply -f config.yaml

kubectl apply -f database.yaml
kubectl apply -f backend.yaml
kubectl apply -f frontend.yaml

minikube service frontend-service

