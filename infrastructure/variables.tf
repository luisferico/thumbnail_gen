variable "aws_region" {
    description = "The AWS region things are created in"
}

variable "ec2_task_execution_role_name" {
    description = "ECS task execution role name"
    default = "myEcsTaskExecutionRole"
}

variable "ecs_auto_scale_role_name" {
    description = "ECS auto scale role name"
    default = "myEcsAutoScaleRole"
}

variable "az_count" {
    description = "Number of AZs to cover in a given region"
    default = "2"
}

variable "app_image" {
    description = "Docker image to run in the ECS cluster"
    default = "533267004883.dkr.ecr.us-east-1.amazonaws.com/thumbnail-generator:latest"
}

variable "app_image_streamlit" {
    description = "Docker image streamlit to run in the ECS cluster"
    default = "533267004883.dkr.ecr.us-east-1.amazonaws.com/streamlit:latest"
}

variable "app_port" {
    description = "Port exposed by the docker image to redirect traffic to"
    default = 8000
}

variable "app_port_streamlit" {
    description = "Port exposed by the docker image streamlit to redirect traffic to"
    default = 8501
}

variable "app_count" {
    description = "Number of docker containers to run"
    default = 3
}

variable "health_check_path" {
  default = "/"
}

variable "fargate_cpu" {
    description = "Fargate instance CPU units to provision (1 vCPU = 1024 CPU units)"
    default = "1024"
}

variable "fargate_memory" {
    description = "Fargate instance memory to provision (in MiB)"
    default = "2048"
}

variable "ami_id" {
    default = "ami-053b0d53c279acc90"
}

variable "instance_type" {
    default = "t2.micro"
}

variable "key_name" {
    default = "streamlit"
}