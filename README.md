# Scalable and Secure Deployment of REST and WebSocket APIs on Amazon ECS

![ecs-fastapis-websocket-serverless](https://github.com/user-attachments/assets/39f568f3-efd9-4c61-9abc-38220fac3956)

## Prerequisites

1. **Setup AWS Profile**
   - Create an AWS CLI profile named `nebula-shines` on your machine.

2. **Install Node.js**
   - Install Node.js version `22.12.0` (npm version `10.9.0`).

3. **Install Serverless Framework**
   - Install Serverless Framework version `3.39.0`.

4. **Install Serverless Plugins**
   - Install the following Serverless plugins:
     - `hybridless/serverless-ecs-plugin`
     - `serverless-scriptable-plugin`

5. **Grant Executable Permissions**
   - Navigate to the `fastapi-ecs` folder and run the following command to grant executable permissions to the script:
     ```bash
     chmod +x scripts/create-build-push-ecr.sh
     ```

6. **Install Docker**
   - Ensure Docker is installed on your machine.

## Setup Complete
Once all prerequisites are installed and configured, the setup is complete.

---

## Application Details

- The `app.py` file contains the latest FastAPI code with multiple routes, including:
  - `health`
  - `api`
  - `connect`
  - `disconnect`
  - `joinroom`
  - `exitroom`

---

## Working with Docker Images

1. **Existing Image**
   - The Docker image has already been built and pushed to ECR.

2. **Making Changes**
   - If you make changes to the FastAPI code, you need to rebuild and push the image to ECR.

3. **Rebuild and Push Image**
   - Run the following script to rebuild and push the image:
     ```bash
     scripts/create-build-push-ecr.sh
     ```
   - This script:
     - Uses the AWS CLI profile `nebula-shines`.
     - Checks if the ECR repository exists (creates it if it doesn’t).
     - Rebuilds the image using the `Dockerfile`.
     - Pushes the image to ECR.

---

## Deploying the Stack

1. **Destroy Current Stack**
   - Before redeploying, you must destroy the current stack from the AWS CloudFormation Console.

2. **Deploy New Stack**
   - Run the following command to deploy the stack:
     ```bash
     serverless deploy --aws-profile nebula-shines
     ```

3. **Enable Two-Way Communication**
   - After redeploying, manually enable two-way communication for each route of the WebSocket API:
     1. Navigate to the API Gateway Console.
     2. Enable two-way communication for every route.
     3. Redeploy the API to the specific stage (`dev` in this case).

> **Note:** This step is currently not automated in the AWS CloudFormation template and must be performed manually.

---

## Updating ECS Fargate Task with New FastAPI Code

1. **Rebuild and Push New Image**
   - Run the following script:
     ```bash
     scripts/create-build-push-ecr.sh
     ```

2. **Force Deployment**
   - Navigate to the ECS Fargate Service:
     1. Update the service.
     2. Click on **Force Deployment**.

   - This ensures the ECS Fargate service uses the latest Docker image pushed to ECR.

---
