#!/bin/bash

# build the image

docker build -t random-quote-api .

# run the container with proper port mapping

docker run -p 5500:5500 random-quote-api
