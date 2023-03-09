#!/bin/bash

# minikube start

kubectl apply -f database.yaml
kubectl apply -f backend.yaml
kubectl apply -f frontend.yaml

minikube service frontend-service

