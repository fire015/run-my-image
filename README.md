# Kubernetes Auth

Use the token generated to login to the web dashboard:

```
kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep admin-user | awk '{print $1}')
```

Start the runner job to run a custom image:

```
kubectl apply -f runner.yml
```
