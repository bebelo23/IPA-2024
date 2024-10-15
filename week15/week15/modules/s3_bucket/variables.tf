variable "aws_access_key" {
  type        = string
  description = "AWS Access Key"
  sensitive   = true
}
variable "aws_secret_key" {
  type        = string
  description = "AWS Secret Key"
  sensitive   = true
}
variable "aws_session_token" {
  type        = string
  description = "AWS Session Token"
  sensitive   = true
}
variable "key_name" {
  type        = string
  description = "Private key path"
  sensitive   = false
}
variable "region" {
  default = "us-east-1"
}

variable "bucket_name" {
  description = "s3-bucket-127"
  type        = string
  default     = "s3-bucket-127"
}

variable "upload_file_source" {
  description = "./my-melody.jpg"
  type        = string
  default = "./my-melody.jpg"
}


variable "upload_file_key" {
  description = "images/my_image.jpg"
  type        = string
  default = "images/my_image.jpg"
}
