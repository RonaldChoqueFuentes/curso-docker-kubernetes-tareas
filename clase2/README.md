# dokcer files

## Python flask App

1. Review the base image:
![alt text](screenshots/image.png)

1. Comand to create a image 

```bash
 docker build -t python-flask-api:1.0 .
```
-- output of the creation
![alt text](screenshots/image-1.png)
 
2. Docker file

[Dockerfile](./labs/python-flask-cloud-run-main/python-flask-cloud-run-main/Dockerfile)

3. history and inspect

docker history python-flask-api:1.0
```bash
 docker history python-flask-api:1.0
 docker inspect python-flask-api:1.0

```

3. Comand to deploy the image

```bash
 docker run -p 8000:8080 --name my_flask_app python-flask-api:1.0
```
![alt text](screenshots/image-2.png)

4. docker ignore 
[.dockerignore](./labs/python-flask-cloud-run-main/python-flask-cloud-run-main/.dockerignore)


5. Command to get into the container

```bash
 docker run -it -p 8000:8080 --name my_flask_app python-flask-api:1.0 bash
```

