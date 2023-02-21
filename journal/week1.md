# Week 1 — App Containerization

## Homework Challenges
1. **Run the dockerfile CMD as an external script**  
I executed the Dockerfile in backed-flask in my local machine.
```
Sameers-MacBook-Air:backend-flask sameermeher$ docker build -t backend-flask-service .
[+] Building 1.7s (10/10) FINISHED                                                                                                                                                                    
 => [internal] load build definition from Dockerfile                                                                                                                                             0.0s
 => => transferring dockerfile: 37B                                                                                                                                                              0.0s
 => [internal] load .dockerignore                                                                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                                                                  0.0s
 => [internal] load metadata for docker.io/library/python:3.10-slim-buster                                                                                                                       1.4s
 => [1/5] FROM docker.io/library/python:3.10-slim-buster@sha256:6e96825731607f9d49d382e302a78e994d60db2871f3447152f56621069e6114                                                                 0.0s
 => [internal] load build context                                                                                                                                                                0.0s
 => => transferring context: 713B                                                                                                                                                                0.0s
 => CACHED [2/5] WORKDIR /backend-flask                                                                                                                                                          0.0s
 => CACHED [3/5] COPY requirements.txt requirements.txt                                                                                                                                          0.0s
 => CACHED [4/5] RUN pip3 install -r requirements.txt                                                                                                                                            0.0s
 => CACHED [5/5] COPY . .                                                                                                                                                                        0.0s
 => exporting to image                                                                                                                                                                           0.1s
 => => exporting layers                                                                                                                                                                          0.0s
 => => writing image sha256:8124e9bed0235041ddf5b2ce0ff1df136313886a52e4ad32274704ba9e853fb4                                                                                                     0.0s
 => => naming to docker.io/library/backend-flask-service                                                                                                                                         0.0s
```
2. **Push and tag a image to DockerHub**  
I already have a account in DockerHub. Tagged and Pushed the backed-flask image into DockerHub

```
docker build -t sameerkm/backend-flask-service:1.0 .
docker push sameerkm/backend-flask-service:1.0
```
3. **Use multi-stage building for a Dockerfile build**  
For this challenge, I changed the Dockerfile of 'backend-flask' into a Multi stage build.
```
<<TODO>>
```