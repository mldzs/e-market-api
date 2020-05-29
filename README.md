# E-Market

## Getting started
___
### Set environment variable
Create a file called `.env` at the root of the project and assign the following variables:
```shell script
POSTGRES_DB = emarket
POSTGRES_USER = emarketuser
POSTGRES_PASSWORD = emarketpassword
POSTGRES_HOST = db

DEBUG = true
SECRET_KEY = 3oq%3nhm_o)7z#r#*f66h_r-yijb5)#c1c8t9)7%lfiw3zbms7` 
```

All values set above are standard values for development. If it goes up to production, it needs to be changed
____
### Docker
```shell script
$ cd docker/
$ docker-compose up --build
```
___
### Common errors:

##### PostgreSQL
> ERROR: for db  Cannot start service db: driver failed programming external connectivity on endpoint db 

This error is caused because there is already a database instance running on port `"5432"`. If you use a system other than linux, find out `how to stop the Postgresql service` or `change the port on docker-compose.yml`. If you use linux, you can solve the problem as follows:
```shell script
$ sudo service postgresql stop
```
___
##### Host Permission
> ...starting container process caused "exec: \"/app/docker/entrypoint.sh\": permission denied": unknown

This error is caused because the `user is not allowed to execute the "entrypoint.sh"` file. If you use a system other than linux, search `how to change file execution permission`. If you use linux, you can resolve it by running this command in your shell:
```shell script
$ chmod 777 entrypoint.sh
```
