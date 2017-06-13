# pyssh
A project to help to manage your ssh hosts

![status](https://travis-ci.org/felipear89/sytssh.svg?branch=master)

## How to install
`pip install sytssh`

## How to configure
Write a yaml file in `~/.sytssh.yaml` 
ex:
```
username: myUser
port: 22
hosts:
  project-name-1:
    test: "hostname-test"
    prod: "hostname-prod-{1-10}" // A pool of machines
  project-name-2:
    test: "hostname-test"
    prod: "hostname-prod-{1-10}:2222" // You can info a specific port
```
## How to use
Run the command line sytssh. 

Simple connect using ssh
`sytssh project-name-1 qa`

Connect using ssh to a specific machine
`sytssh project-name-1 prod -n 1`

Connect using ssh on the first machine
`sytssh project-name-1 prod`

Run again to connect on the second machine
`sytssh project-name-1 prod`


## Enable Auto-complete
### Bash
```
 $ activate-global-python-argcomplete && eval "$(register-python-argcomplete sytssh)"
```
### zsh

```
 $ autoload bashcompinit && bashcompinit && autoload compinit && compinit && eval "$(register-python-argcomplete sytssh)"
```
