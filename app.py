#!/usr/bin/env python3
import os

import aws_cdk as cdk
import aws_cdk as cdk

from pld_cdk.pld_cdk_stack import PldCdkStack


file_path ="conf/vpc_conf.yaml"

app = cdk.App()
PldCdkStack(app, "PldCdkStack", file_path=file_path)
app.synth()
