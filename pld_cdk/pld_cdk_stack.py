from constructs import Construct
from aws_cdk import  Stack
from aws_cdk import (
    aws_ec2 as ec2,
)
import yaml

class PldCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, file_path: str,**kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #load vpc configuration from the yaml file
        with open(file_path, "r") as file:
            vpc_configuration = yaml.safe_load(file)

        # Create the VPC 
        vpc = ec2.Vpc(self, vpc_configuration["vpc_name"],
              cidr=vpc_configuration["cidr_principal"],
              nat_gateways=0,
              subnet_configuration=[],
        )
        
        # Create an internet gateway
        igw = ec2.CfnInternetGateway(self, "InternetGateway")

        # Attach the Internet Gateway to the VPC
        ec2.CfnVPCGatewayAttachment(self,"Vpcattachement",
                                    vpc_id=vpc.vpc_id,
                                    internet_gateway_id=igw.ref
                                    )
         
        subnets=[]
        public_subnet_ids = []

        # create subnets and add a route to the internet gateway for each public subnet
        for i,subnet in enumerate(vpc_configuration["subnets"]):
            subnets= ec2.Subnet(
            self,subnet["application"],
            cidr_block=subnet["cidr"],
            vpc_id=vpc.vpc_id,
            availability_zone=subnet["availability_zone"],
            map_public_ip_on_launch=subnet["is_public"]
            )
            if subnet["is_public"]:
                ec2.CfnRoute(
                self,
                f"route-to-igw-{subnet['application']}",
                route_table_id=subnets.route_table.route_table_id,
                destination_cidr_block="0.0.0.0/0",
                gateway_id=igw.ref
        )