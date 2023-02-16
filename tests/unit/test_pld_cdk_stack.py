import aws_cdk as core
import aws_cdk.assertions as assertions

from pld_cdk.pld_cdk_stack import PldCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in pld_cdk/pld_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PldCdkStack(app, "pld-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
