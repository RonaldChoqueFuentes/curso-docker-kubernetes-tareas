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

6.  endpoints

![alt text](screenshots/image-3.png)

![alt text](screenshots/image-4.png)

![alt text](screenshots/image-5.png)

7. verify logs

```bash
  docker logs dd8176b10013
```
![alt text](screenshots/image-6.png)

8. size of the images v2 latest

![alt text](screenshots/image-7.png)

9. docker login

![alt text](screenshots/image-8.png)

10. 

```bash
  docker tag python-flask-api:1.0  docker-practices
  docker push ronaldchoque/docker-practices
```

![alt text](screenshots/image-9.png)

-- web

![alt text](screenshots/image-10.png)

10. notes

-  Revisar el manejo de seguridad.  me genero errores
- no pude desplegar con unicord