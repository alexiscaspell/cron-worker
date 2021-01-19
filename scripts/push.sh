source ./scripts/ambiente.sh

echo "$DOCKER_HUB_TOKEN" | docker login --username $DOCKER_HUB_USER --password-stdin $DOCKER_HUB_REPO

docker push $DOCKER_HUB_REPO/$DOCKER_HUB_GROUP/$PROYECTO:$VERSION
