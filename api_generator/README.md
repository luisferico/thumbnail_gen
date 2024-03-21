# Thumbnail Generator Service

This project provides a simple thumbnail generator service that allows users to analyze images, generate thumbnails 
based on specified dimensions or reduction ratios, and retrieve image metadata. 
The service is implemented using FastAPI and OpenCV, and it can be deployed as a Docker container.

## Features

- **Analize Image:** Analyze images to retrieve size and dimensions.
- **Generate Thumbnail:** Generate thumbnails of images based on specified width and height, or reduction ratio.

## Requirements

- Docker

## Installation and Usage on Local

1. Clone the repository:

```bash
git clone https://github.com/luisferico/thumbnail_gen.git
```

2. Build the Docker image:

```bash
cd api_generator/

docker build -t thumbnail-service .
```

3. Run the Docker container:

```
docker run -d -p 8000:8000 thumbnail-service
```

4. Access the API endpoints using the provided Swagger UI:

```
http://localhost:8000/docs
```
