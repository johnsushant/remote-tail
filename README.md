
# remote-tail
Tail functionality using TCP in Python

Instructions :-

1) Run server.py on the server hosting the log files
2) Run ./tail "name-of-file" to tail it.


Deploy Natively :
```
ansible-playbook -i inventory/remote playbooks/deploy.yaml
```

Deploy inside a docker container :
```
ansible-playbook -i inventory/remote playbooks/deploy-docker.yaml
```
