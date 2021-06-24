Title: Setting up a Simple EKS cluster Using Terraform/Github
Date: 2021-06-24 10:54
Modified: 2021-06-24 10:54
Category: IaC
Tags: terraform, aws, github, iac, ci/cd, kubernetes
Slug: Setting_up_a_Simple_EKS_cluster_Using_Terraform_Github
Authors: Cesar Sepulveda
Summary: Setting up a Simple EKS with Autoscaling

Amazon Elastic Kubernetes Service (EKS) is a managed Kubernetes service that makes it easy for you to run Kubernetes on AWS and on-premises.

Here I will describe how to extend our [basic setup](/Initial-Setup-of-Terraform-and-GitHub-Actions.html) and setup a simple kubernetes cluster using EKS using the AWS/EKS terraform module and the Helm chart to install the Auto Scaling controller.

## Setup the VPC
The first step will be set up our vpc, for this case i'm going to create a vpc with 3 different subnets
* private_subnets, in this subnet we are going to launch our node instances
* public_subnets, in this subnet we are going to launch our load balancers (will not by used for the moment)
* database_subnets, in this subnet we are going to launch our databases (will not be used for the moment)

The code could be checked [here](https://raw.githubusercontent.com/csepulveda/aws_base_setup/main/vpc.tf):

```
data "aws_availability_zones" "available" {
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "2.66.0"

  name                 = "k8s-vpc"
  cidr                 = "172.16.0.0/16"
  azs                  = data.aws_availability_zones.available.names
  private_subnets      = ["172.16.1.0/24", "172.16.2.0/24", "172.16.3.0/24"]
  public_subnets       = ["172.16.4.0/24", "172.16.5.0/24", "172.16.6.0/24"]
  database_subnets     = ["172.16.7.0/24", "172.16.8.0/24", "172.16.9.0/24"]
  enable_nat_gateway   = true
  single_nat_gateway   = true
  enable_dns_hostnames = true

  tags = {
    "kubernetes.io/cluster/${var.eks_cluster_name}" = "shared"
  }

  public_subnet_tags = {
    "kubernetes.io/cluster/${var.eks_cluster_name}" = "shared"
    "kubernetes.io/role/elb"                        = "1"
  }

  private_subnet_tags = {
    "kubernetes.io/cluster/${var.eks_cluster_name}" = "shared"
    "kubernetes.io/role/internal-elb"               = "1"
  }
}
```

The tags will be used in the future to launch out ALB using the AWS Ingress Controller.

## Setup the EKS Cluster
To setup the cluster we are going to use the AWS/EKS module. its pretty simple and we have to modify some few thing to enable the Auto Scaling controller.