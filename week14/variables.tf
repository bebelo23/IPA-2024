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
variable "default_name" {
  default = "itKMITL"
}
locals {
  default_tags = {
    itclass = "IPA24"
    itgroup = "year3"
  }
}

variable "network_address_space" {
  description = "VPC CIDR Block"
  default     = "10.0.0.0/16"
}

variable "availability_zones" {
  type    = list(string)
  default = ["us-east-1a", "us-east-1b"]
}

variable "subnet_count" {
  default = 2
}
