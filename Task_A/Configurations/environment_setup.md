---
title: environment_setup
---

---
## Environment Setup
---

### AWS EC2 instance and security group creation
<details - open>
<summary>Configure EC2 instance and security group with SSH and port forwarding</summary>
---
- Use a `t2.xlarge` instance type
- Allocate at least `32GB` of storage
- Allow port range: `4000 - 38888` in the EC2 security group
- Connect to EC2 via SSH:
  ```bash
  ssh -i "D:\path\to\private\key.pem" user@Public_DNS
  ```
  - Example:
    ```bash
    ssh -i "D:\Users\pyerravelly\Desktop\twitter_analysis.pem" ec2-user@ec2-54-203-235-65.us-west-2.compute.amazonaws.com
    ```
- Enable port forwarding:
  ```bash
  ssh -i "D:\path\to\private\key.pem" user@Public_DNS
  ```
  - Example:
    ```bash
    ssh -i "D:\Users\pyerravelly\Desktop\twitter_analysis.pem" ec2-user@ec2-34-208-254-29.us-west-2.compute.amazonaws.com -L 2081:localhost:2041 -L 4888:localhost:4888 -L 2080:localhost:2080 -L 8050:localhost:8050 -L 4141:localhost:4141
    ```
- Copy files from local machine to EC2:
  ```bash
  scp -r -i "D:\Users\pyerravelly\Desktop\twitter_analysis.pem"
  ```
  - Example:
    ```bash
    scp -r -i "D:\Users\pyerravelly\Desktop\twitter_analysis.pem" D:\Users\pyerravelly\Downloads\spark-standalone-cluster-on-docker-master\build\docker\docker-exp ec2-user@ec2-34-208-254-29.us-west-2.compute.amazonaws.com:/home/ec2-user/docker_exp
    ```
---
</details>

### Docker installation and running
<details - open>
<summary>Install Docker and Docker Compose on EC2 instance</summary>
---
- Install Docker:
  ```bash
  sudo yum update -y
  sudo yum install docker
  sudo curl -L "https://github.com/docker/compose/releases/download/1.29.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  sudo chmod +x /usr/local/bin/docker-compose
  sudo gpasswd -a $USER docker
  newgrp docker
  ```
- Start Docker service:
  ```bash
  sudo systemctl start docker
  ```
- Stop Docker service:
  ```bash
  sudo systemctl stop docker
  ```
---
</details>

### Usage of docker-composer and starting all the tools
<details - open>
<summary>Access services locally and run Docker containers</summary>
---
- List running containers:
  ```bash
  docker ps
  ```
- Open CLI inside Docker container:
  ```bash
  docker exec -i -t docker_kafka_1 bash
  ```
- Access services in browser:
  - NiFi: `http://localhost:2080/nifi/`
  - Mongo Express: `http://localhost:4141/`
  - Jupyter Lab: `http://localhost:4888/lab?`
---
</details>
