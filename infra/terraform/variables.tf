variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "aws_access_key" {
  description = "AWS access key (dummy when using LocalStack)"
  type        = string
  default     = "test"
}

variable "aws_secret_key" {
  description = "AWS secret key (dummy when using LocalStack)"
  type        = string
  default     = "test"
}

variable "aws_endpoint" {
  description = "LocalStack endpoint (set to real AWS if deploying to cloud)"
  type        = string
  default     = "http://localhost:4566"
}

variable "s3_bucket_name" {
  description = "Name of the S3 bucket for avatars"
  type        = string
  default     = "prima-tech-challenge"
}

variable "dynamodb_table_name" {
  description = "Name of the DynamoDB table for users"
  type        = string
  default     = "prima-users"
}

