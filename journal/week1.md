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
4. **Launch an EC2 instance that has docker installed, and pull a container to demonstrate you can run your own docker processes**  
To complete this task, I lauched an EC2 instance (t2.micro), attached a Security Group (with Inbound Rule allowed from source '0.0.0.0/0'). As I wanted the Docker already installed in the lauched EC2 instance, I added the user-data.  
User Data Code - 
    ```
    #! /bin/sh
    yum update -y
    amazon-linux-extras install docker
    service docker start
    usermod -a -G docker ec2-user
    chkconfig docker on
    ```  
    Commands to pull Docker image, Run the Container and Test from Browser  
    ```
    [ec2-user@ip-172-31-55-147 ~]$ docker pull httpd
    Using default tag: latest
    latest: Pulling from library/httpd
    bb263680fed1: Pull complete 
    9e8776e4b876: Pull complete 
    f506d7aab652: Pull complete 
    05289ee4f284: Pull complete 
    b7f64f2f8747: Pull complete 
    Digest: sha256:db2d897cae2ad67b33435c1a5b0d6b6465137661ea7c01a5e95155f0159e1bcf
    Status: Downloaded newer image for httpd:latest
    docker.io/library/httpd:latest
    [ec2-user@ip-172-31-55-147 ~]$ docker images
    REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
    httpd        latest    3a4ea134cf8e   12 days ago   145MB
    [ec2-user@ip-172-31-55-147 ~]$ docker run -d -p 80:80 --name httpd-container httpd
    5b75e76c9d15924ec58d42287b7f232c7d1b477fc5fffc199aa65be48978bffc
    [ec2-user@ip-172-31-55-147 ~]$ curl http://localhost:80
    <html><body><h1>It works!</h1></body></html>
    [ec2-user@ip-172-31-55-147 ~]$ 
    ```
    ![Site accessible in browser](../_docs/assets/week-1/docker-ec2-site-browser.png)