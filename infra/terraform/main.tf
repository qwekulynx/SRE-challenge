terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region                      = var.aws_region
  access_key                  = var.aws_access_key
  secret_key                  = var.aws_secret_key
  skip_credentials_validation = true
  skip_requesting_account_id  = true
  s3_use_path_style           = true

  endpoints {
    s3       = var.aws_endpoint
    dynamodb = var.aws_endpoint
    iam      = var.aws_endpoint
  }
}

# LocalStack-safe S3 bucket (no force_destroy, no ACLs)
resource "aws_s3_bucket" "avatars" {
  bucket = var.s3_bucket_name
}

# DynamoDB table for storing users
resource "aws_dynamodb_table" "users" {
  name         = var.dynamodb_table_name
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "email"

  attribute {
    name = "email"
    type = "S"
  }
}

