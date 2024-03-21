# Deployment Guide
This guide provides step-by-step instructions for deploying the API, infrastructure, and Streamlit app.

## API Deployment
Docker Containerization
1. Clone the api_generator repository:
```bash
git clone https://github.com/your_username/api_generator.git
```

2. Navigate to the cloned repository:

```bash
cd api_generator
```
3. Build the Docker image:

```bash
docker build -t api-generator .
```
4. Tag the Docker image with your ECR repository URI:

```bash
docker tag api-generator:latest your-ecr-uri/api-generator:latest
```
5. Push the Docker image to your ECR repository:

```bash
docker push your-ecr-uri/api-generator:latest
```
## Infrastructure Deployment

1. Navigate to the infrastructure directory:

```bash
cd infrastructure
```

2. Initialize Terraform:

```bash
terraform init
```

3. Review the Terraform execution plan:

```bash
terraform plan
```

4. Apply the Terraform changes:

```bash
terraform apply
```

## Streamlit App Deployment

Note: It's necessary to access the EC2 instance created previously to execute the following commands.

1. Clone the streamlit_app repository:

```bash
git clone https://github.com/your_username/streamlit_app.git
```

2. Navigate to the streamlit_app directory:

```bash
cd streamlit_app
```
3. Install the required dependencies:

```bash
sudo pip3 install -r requirements.txt
```

4. Run the Streamlit app in the background:

```bash
sudo nohup streamlit run main.py & disown
```