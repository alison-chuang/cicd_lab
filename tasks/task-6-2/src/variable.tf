variable "github_token" {
  type      = string
  sensitive = true
}

variable "github_key_name" {
  type    = string
  default = "terraform_key_github"
}

variable "ec2_key_name" {
  type    = string
  default = "terraform_key_ec2"
}
