#!/usr/bin/env python3
import aws_cdk as cdk
from my_pipeline.my_pipeline_stack import MyPipelineStack

app = cdk.App()
MyPipelineStack(app, "MyPipelineStack",
                env=cdk.Environment(account="536826985609", region="us-east-1")
                )

app.synth()
