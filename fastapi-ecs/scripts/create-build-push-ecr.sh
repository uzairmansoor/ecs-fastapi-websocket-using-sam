#!/bin/bash

# Variables
AWS_REGION="us-east-1"
AWS_PROFILE="nebula-shines"
REPO_NAME="serverless-fastapi-ecs-service-dev"
IMAGE_TAG="latest"
ACCOUNT_ID=$(aws sts get-caller-identity --query "Account" --output text --profile $AWS_PROFILE)
ECR_URI="$ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:$IMAGE_TAG"

# Step 1: Check if repository exists; create it if not
if ! aws ecr describe-repositories --repository-names "$REPO_NAME" --region $AWS_REGION --profile $AWS_PROFILE > /dev/null 2>&1; then
  echo "ECR repository $REPO_NAME does not exist. Creating..."
  aws ecr create-repository --repository-name "$REPO_NAME" --region $AWS_REGION --profile $AWS_PROFILE
  echo "ECR repository $REPO_NAME created successfully."
else
  echo "ECR repository $REPO_NAME already exists."
fi

# Step 2: Log in to ECR
echo "Logging into Amazon ECR..."
aws ecr get-login-password --region $AWS_REGION --profile $AWS_PROFILE | docker login --username AWS --password-stdin "$ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com"

# Step 3: Build the Docker image
echo "Building Docker image..."
docker build -t $REPO_NAME:$IMAGE_TAG .

# Step 4: Tag the Docker image with the full ECR URI
echo "Tagging Docker image..."
docker tag $REPO_NAME:$IMAGE_TAG $ECR_URI

# Step 5: Push the image to ECR
echo "Pushing image to ECR..."
docker push $ECR_URI

# Step 6: Confirm push success
if [ $? -eq 0 ]; then
  echo "Image successfully pushed to ECR: $ECR_URI"
else
  echo "Failed to push the image to ECR."
  exit 1
fi
