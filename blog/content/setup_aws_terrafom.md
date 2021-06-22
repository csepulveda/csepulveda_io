Title: Initial Setup of Terraform and Github Actions
Date: 2021-06-22 08:00
Modified: 2021-06-22 08:00
Category: Terraform
Tags: terraform, aws, github
Slug: Initial-Setup-of-Terraform-and-Github-Actions
Authors: Cesar Sepulveda
Summary: Setup Terraform cloud and Github Acctions to deploy resources on AWS

Here I will go to describe how to get an integration between Terraform Cloud and Github Acctions to deploy resources on AWS.
Some Stuff that we are going to need to realize this setup:

* Have an AWS account with access to create iam users and grant it full admin privileges.
* Have an Terraform Cloud account.
* Have a Github account.

# Base Setup:
First, we have to create a IAM user and grant him Administrator Access.
![iam_account](./images/post1/iam_account.png "Create Account")
![iam_access](./images/post1/iam_access.png "Grant Access")f

