
# CI/CD Backend
I am setting up my #Cloudresume CI/CD backend with the help of the below action.
The SAM application stack is deployed on any changes to my lambda handler code in `komla_function`
directory or `template.yml`. Please visit my [website](https://www.komlalebu.com) for more information.
Stack consists of API, Lambda Function and DynamoDB Table.

# Action
The action has two jobs `test` and `deploy`.
 `test` - check the integrity of my lambda function.
 `deploy` - deploys the entire SAM stack in AWS and needs `test` to be successful as a dependency.

                jobs:
                  test:
                  delpoy:
                        needs:test


# Purpose
This action is enabling the deployment of my cloudresume CI/CD backend infrastructure using the  sam template I prepared.
Infrastructure consisting of : 1. Lambda Function - komlalebuFunction.
                               2. API - komlalebuAPI.
                               3. DynamoDB Tabe - komlalebuTable.

The below command builds the packaage in SAM CLI.
`sam build`

Once the package is built the below command uploads the output-template-file to my S3 bucket.
`sam package --output-template-file serverless-output.yaml --s3-bucket [YOUR BUCKET NAME] --region ap-south-1 --profile aws-devops`

The below command deploys the SAM code in AWS. Thus creating the API and Lambda function in AWS.
`sam deploy --template-file packaged.yaml --capabilities CAPABILITY_IAM --stack-name aws-sam-komlalebu --region ap-south-1 --profile aws-devops`

The below environment parameters have been passed as secrets for security purposes.
        AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY,
        AWS_DEPLOY_BUCKET

# Usage - ci.yml
                name: "Deploy SAM Stack to Production"
                on: 
                        push:
                        branches:
                        - master

                jobs:
                  test:
                        runs-on: ubuntu-latest
                        steps:
                        - uses: actions/checkout@v2
                        - name: Install Python 3
                        uses: actions/setup-python@v1
                        with:
                                python-version: 3.6
                        - name: Install dependencies
                        run: |
                                python -m pip install --upgrade pip
                                pip install -r requirements.txt
                        - name: Run tests with pytest
                        run: pytest

                deploy:
                        needs: test
                        runs-on: ubuntu-latest
                        steps:
                        - uses: actions/checkout@v1
                        - uses: falnyr/aws-sam-deploy-action@v1.2.1
                        env:
                                TEMPLATE: 'template.yaml'
                                AWS_STACK_NAME: aws-sam-komlalebu
                                AWS_REGION: 'ap-south-1'
                                AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
                                AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
                                AWS_DEPLOY_BUCKET: ${{ secrets.AWS_DEPLOY_BUCKET }}
