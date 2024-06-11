from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from aws_cdk import (
    Stack,
    SecretValue,
    Environment,
    App
)
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from aws_cdk.aws_codepipeline_actions import GitHubTrigger
from aws_cdk.aws_codedeploy import codedeploy
from my_pipeline.my_pipeline_app_stage import MyPipelineAppStage


class MyPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline = CodePipeline(self, "Pipeline",
                                pipeline_name="MyPipeline",
                                synth=ShellStep("Synth",
                                                input=CodePipelineSource.git_hub(
                                                    "caseywhorton/my-pipeline", "main",
                                                    authentication=SecretValue.secrets_manager(
                                                        "github-token", json_field="token"),
                                                    trigger=GitHubTrigger.WEBHOOK),
                                                commands=["npm install -g aws-cdk",
                                                          "python -m pip install -r requirements.txt",
                                                          "cdk synth"]
                                                )
                                )
        application = codedeploy.LambdaApplication(self, "CodeDeployApplication",
                                                   application_name="MyApplication"
                                                   )
        # pipeline.add_stage(MyPipelineAppStage(self, "test",
        #    env=cdk.Environment(account="536826985609", region="us-east-1")))
