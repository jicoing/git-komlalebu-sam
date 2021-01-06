---
#The below command builds the packaage in SAM CLI.
sam build

#Once the package is built the below command uploads the template file to my S3 bucket cici-jaya-devops
sam package --output-template-file packaged.yaml --s3-bucket cici-jay-devops --region ap-south-1 --profile aws-devops

#The below command deploys the SAM code in AWS. Thus creating the API and Lambda function
sam deploy --template-file packaged.yaml --capabilities CAPABILITY_IAM --stack-name aws-sam-komlalebu --region ap-south-1 --profile aws-devops

