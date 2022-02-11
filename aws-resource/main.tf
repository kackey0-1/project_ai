locals {
  env = "dev"
  prefix = "project_ai"
  public_key_path = "~/.ssh/id_rsa-20211001.pub"
  private_key_path = "~/.ssh/id_rsa-20211001"
  default_tags = {
    "Environment" = "dev",
    "Project"     = "project_ai",
    "CreatedBy"   = "kakimoto"
  }
}

######################
# VPC
######################
data "aws_availability_zones" "available" {}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.5.0"

  name               = "${local.env}-${local.prefix}-vpc"
  cidr               = "10.0.0.0/16"
  azs                = data.aws_availability_zones.available.names
  enable_dns_hostnames = true
  public_subnets     = ["10.0.1.0/24"]

  tags = merge(
    local.default_tags,
    )
}

######################
# Security Group
######################
resource "aws_security_group" "http" {
  vpc_id = module.vpc.vpc_id
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(
    local.default_tags,
    {"Name" = "${local.env}-${local.prefix}-http-s"}
  )
}


resource "aws_security_group" "ssh" {
  vpc_id = module.vpc.vpc_id
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(
    local.default_tags,
    {"Name" = "${local.env}-${local.prefix}-ssh-sg"}
  )
}

resource "aws_key_pair" "instance_key" {
  key_name   = "${local.env}-${local.prefix}-key"
  public_key = file(local.public_key_path)

  tags = merge(
  local.default_tags,
  {"Name": "${local.env}-${local.prefix}-key"}
  )
}

resource "aws_instance" "project_ai_instance" {
  ami           = "ami-088da9557aae42f39"
  instance_type = "t2.micro"
  key_name      = aws_key_pair.instance_key.key_name
  vpc_security_group_ids = [aws_security_group.http.id, aws_security_group.ssh.id]
  subnet_id = module.vpc.public_subnets[0]

  root_block_device {
    volume_type = "gp2"
    volume_size = 50
  }

  tags = merge(
    local.default_tags,
    {"Name": "${local.env}-${local.prefix}-ec2"}
  )

  lifecycle { create_before_destroy = true }


  provisioner "file" {
    connection {
      user        = "ubuntu"
      host        = aws_instance.project_ai_instance.public_ip
      private_key = file(local.private_key_path)
    }

    source      = "./initializer.sh"
    destination = "/home/ubuntu/initializer.sh"
  }

  provisioner "remote-exec" {
    connection {
      user        = "ubuntu"
      host        = aws_instance.project_ai_instance.public_ip
      private_key = file(local.private_key_path)
    }

    inline = [
      "/bin/bash ~/initializer.sh"
    ]
  }
}

output "ec2_ssh" {
  description = "ec2 ssh"
  value = {
    "ec2_ssh": "ssh -i ${local.private_key_path} ubuntu@${aws_instance.project_ai_instance.public_ip}"
  }
}
