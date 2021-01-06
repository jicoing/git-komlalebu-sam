
I am setting up my #Cloudresume backend CI/CD Backend with the help of the below action.
The SAM application gets packaged and deployed on any changes to my python code in `komlal_function`
directory or `template.yml`. Please visit [website](https://www.komlalebu.com) for more information.

# Action
This action is forked from  falnyr
[falnyr/aws-sam-deploy-action@v1.2.1](https://github.com/falnyr/aws-sam-deploy-action)
`'Jan Alfred Richter <falnyr@gmail.com>'`


# Purpose
This action is enabling the deployment of my cloudresume CI/CD backend infrastructure using the  sam template I prepared.
Infrastructure consisting of : 1. Lambda Function - komlalebuFunction
                                2. API - komlalebuAPI
                                3. DynamoDB Tabe - komlalebuTable

The below command builds the packaage in SAM CLI.
`sam build`

Once the package is built the below command uploads the template file to my S3 bucket cici-jaya-devops
`sam package --output-template-file packaged.yaml --s3-bucket cici-jay-devops --region ap-south-1 --profile aws-devops`

The below command deploys the SAM code in AWS. Thus creating the API and Lambda function
`sam deploy --template-file packaged.yaml --capabilities CAPABILITY_IAM --stack-name aws-sam-komlalebu --region ap-south-1 --profile aws-devops`

