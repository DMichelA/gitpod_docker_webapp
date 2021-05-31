# gitpod_docker_webapp

docker pull ubuntu:20.04

Carpeta dentro contenedor
docker run -it -p 8080:8080 -v /workspace/gitpod_docker_webapp/volume:/volume --name webpy -h webpy ubuntu:20.04

Iniciar contenedor 
docker start -i contenedor

apt update 
apt install -y python3
apt install -y python3-pip
pip3 install web.py