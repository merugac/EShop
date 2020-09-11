# EShop

Build the Docker Image

docker build . -t eshop:1.0.0


# Check image

docker image ls



# Run Docker Images

docker run -ti -d -p 8000:8000 eshop:1.0.0
