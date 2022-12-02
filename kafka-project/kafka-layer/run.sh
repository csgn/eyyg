

docker network create kafka-tier --driver bridge


docker run -d --name zookeeper-server \
 	--network app-tier \
 	-e ALLOW_ANONYMOUS_LOGIN=yes \
 	bitnami/zookeeper:latest
