

# Machine Learning Model Deployment to AWS Lambda using GitHub Actions

This project demonstrates how to develop and deploy a machine learning (ML) model to AWS Lambda using GitHub Actions as the CI/CD pipeline.

## Project Overview

This repository contains an ML model that is trained and then deployed to AWS Lambda using an automated CI/CD pipeline configured through GitHub Actions.

### Key Features
- **Model Training**: Train a machine learning model locally or in a cloud environment.
- **AWS Lambda Deployment**: Automatically deploy the trained model to an AWS Lambda function.
- **CI/CD Pipeline**: GitHub Actions is used to automate testing and deployment processes.
  
## Prerequisites

- Python 3.x
- AWS CLI configured with appropriate permissions
- GitHub account and repository
- AWS Lambda permissions (IAM Role with Lambda execution and S3 access)
- Docker (for creating the Lambda deployment package)
  
### Tools & Technologies
- Python
- AWS Lambda
- GitHub Actions
- AWS CLI

## Project Structure

```bash
|-- .github/
|   |-- workflows/
|       |-- deploy.yml   # GitHub Actions workflow for CI/CD
|-- src/       # ML model code
|   |-- lambda_handler.py # AWS Lambda handler
|-- requirements.txt      # Python dependencies
|-- README.md             # Project documentation
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/gaurav-kandel/CICD_AWS.git
cd CICD_AWS
```

### 2. Install dependencies
Ensure you have Python and pip installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Configure AWS CLI
Make sure your AWS credentials are set up by running:
```bash
aws configure
```


### 4. GitHub Actions Configuration
Ensure the repository secrets for AWS access keys are set up:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

The `deploy.yml` file in `.github/workflows/` contains the configuration for GitHub Actions to automate the process.

### 5. CI/CD Pipeline
Push your changes to the repository, and GitHub Actions will automatically trigger the pipeline:
1. Code is tested
2. Model is trained (if applicable)
3. Model and Lambda function are packaged and deployed to AWS Lambda

You can monitor the progress of the workflow under the "Actions" tab of your GitHub repository.


