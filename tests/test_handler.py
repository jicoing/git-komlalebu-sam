import json
import boto3
import pytest

from komla_function.app import lambda_handler


def test_lambda_handler():
    out = lambda_handler('','')
    assert out ==  {'statusCode': 200}