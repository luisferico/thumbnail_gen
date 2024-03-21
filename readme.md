# Strengths and Weaknesses

The proposed architecture offers some strengths. Leveraging cloud services like AWS and Docker facilitates scalability, enabling vertical or horizontal scaling as needed. 
Additionally, tools like Terraform simplify deployment and management, ensuring quickly and repeatable configuration across different environments. The architecture's separation of concerns into distinct components such as the API, Infrastructure, Raw Data Storage and Streamlit application offer easier maintenance and independent evolution of each part. 
Furthermore, the flexibility afforded by Docker containers and cloud services allows for the adoption of diverse technologies and tools, catering to the team's specific needs and preferences.

Some Weaknesses in this approach:

**Potential Infrastructure Overhead:** 
Deploying the Streamlit application on EC2 instances may lead to potential infrastructure overhead, particularly during periods of high demand. If the resources allocated to the EC2 instances are not appropriately sized to handle the incoming traffic, it could result in increased costs due to underutilized resources or performance degradation due to resource constraints. Additionally, scaling EC2 instances manually to accommodate fluctuations in demand may introduce operational complexities and delays in response time, potentially impacting the overall user experience. Therefore, careful monitoring and optimization of EC2 instances are crucial to mitigate the risk of infrastructure overhead and ensure optimal performance of the Streamlit application.

**Lack of Essential Feature:** 
The proposed infrastructure lacks an essential feature - storing calculated metadata in a database. Currently, the application analyzes images and calculates metrics such as Structural Similarity Index (SSI) and Peak Signal-to-Noise Ratio (PSNR), but does not persist this valuable information. Storing metadata in a database enables long-term data retention, facilitates data analysis, and supports features such as historical trend analysis and user-specific metrics. Without this capability, the application may miss out on valuable insights and limit its potential for advanced functionality and data-driven decision-making. Therefore, integrating a database component into the architecture is essential for enhancing the application's capabilities and providing a more comprehensive solution.

# Deployment Guide
This guide provides step-by-step instructions for deploying the API, infrastructure, and Streamlit app.

## API Deployment
Docker Containerization
1. Clone the api_generator repository:
```bash
git clone https://github.com/luisferico/thumbnail_gen.git
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
git clone https://github.com/luisferico/thumbnail_gen.git
```

2. Navigate to the streamlit_app directory:

```bash
cd thumbnail_gen/streamlit_app
```
3. Install the required dependencies:

```bash
sudo pip3 install -r requirements.txt
```

4. Run the Streamlit app in the background:

```bash
sudo nohup streamlit run main.py & disown
```