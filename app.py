#!/usr/bin/env python3
import os

from aws_cdk import core as cdk
from config import config
from amazon_cdk.amazon_cdk_stack import AmazonCdkStack


app = cdk.App()
AmazonCdkStack(app, "AmazonCdkStack", env=cdk.Environment(account=config.ACCOUNT_ID, region=config.REGION))

app.synth()
