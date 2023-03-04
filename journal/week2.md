# Week 2 — Distributed Tracing

## Homework Challenges
This is best week in terms of learning lot of new tools and trying out 
1. Distributing Tracing - 
   - Honeycomb - Spans and ability to capture custom attributes and build a Dashboard for observability
   - X-Ray - Instrumenting with X-Ray and able to create sub-segments with metadata and annotations
2. Error Tracing - 
   - Rollbar - Ability to capture errors occuring in the application.
3. CloudWatch Logs -
   - Logging details of what's happening in the application   


1. **Reduce Docker Image size to 1/3rd**  
I changed the base image in "frontend-react-js" from "FROM node:16.18" -> "FROM node:16.18-alpine" and could reduce the image size to 1/3rd.  
    ```
    FROM node:16.18
    aws-bootcamp-cruddur-2023-frontend-react-js   latest             41b154ba3b97   9 minutes ago    1.23GB  
    ```
    ```
    FROM node:16.18-alpine
    aws-bootcamp-cruddur-2023-frontend-react-js   latest             df45a97a8c0d   52 seconds ago   434MB  
    ```
2. **Run the dockerfile CMD as an external script**  
For this task I created an external python script with commands in CMD with file name "run_commands.py"  
Content of run_commands.py file  
    ```
    #!/usr/bin/env python

    import subprocess

    # Replace these commands with the ones specified in your Dockerfile CMD line
    commands = ["python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]

    # Execute the commands
    for command in commands:
        subprocess.run(command, shell=True)
    ```
    Created a separate Dockerfile as "Dockerfile2" for demo  and updated ONLY the last line to execute the python script  
    ```
    # Set the command to execute the script
    CMD ["python", "run_commands.py"]
    ```
    and build the image using the command  
    ```
    docker build -t backend:v2 -f Dockerfile2 .
    ```
3. **Push and tag a image to DockerHub**  
I already have a account in DockerHub. Tagged and Pushed the backed-flask image into DockerHub

    ```
    docker build -t sameerkm/backend-flask-service:1.0 .
    docker push sameerkm/backend-flask-service:1.0
    ```
    ![Docker Hub](../_docs/assets/week-1/dockerhub-image.png)
4. **Launch an EC2 instance that has dockerinstalled, and pull a container to demonstrate you can run your own docker processes**  
To complete this task, I lauched an EC2 instance (t2.micro), attached a Security Group (with Inbound Rule allowed from source '0.0.0.0/0'). As I wanted Docker pre-installed in the lauched EC2 instance, I added the instructions in the user-data.  
User Data Code - 
    ```
    #! /bin/sh
    yum update -y
    amazon-linux-extras install docker
    service docker start
    usermod -a -G docker ec2-user
    chkconfig docker on
    ```  
    Commands to pull Docker image, Run the Container
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
    Able to access the service from Browser  
    ![Site accessible in browser](../_docs/assets/week-1/docker-ec2-site-browser.png)
5. **Implement a healthcheck in the V3 Docker compose file**  
For this challenge, I updated the docker-compose.yml with 'healthcheck' block
    ```
    healthcheck:
    test: curl --fail http://localhost:4567/api/activities/home || exit 1
    interval: 60s
    retries: 5
    start_period: 60s
    timeout: 10s
    ``` 
    For this to work 'curl' needs to be installed in the 'backed-flash' container which can be installed by adding the following command
    ```
    RUN apt-get update && apt-get install -y curl
    ```