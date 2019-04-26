#!/usr/bin/env bash

for j in $(kubectl get jobs -l='app=rmi' -o custom-columns=:.metadata.name)
do
    kubectl delete job $j
done