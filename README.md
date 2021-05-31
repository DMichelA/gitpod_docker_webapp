# gitpod_docker_webapp

# Comandos 

## Descargar imagen Ubuntu
docker pull ubuntu:20.04

## Creacion contenedor dentro carpeta volume
docker run -it -p 8080:8080 -v /workspace/gitpod_docker_webapp/volume:/volume --name webpy -h webpy ubuntu:20.04

## Iniciar contenedor 
docker start -i contenedor

apt update 
apt install -y python3
apt install -y python3-pip
pip3 install web.py