from aws_cdk import (core, aws_ec2 as ec2, aws_ecs as ecs,
                     aws_ecs_patterns as ecs_patterns)

class FargateStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, 'FargateFlaskVPC', cidr='10.0.0.0/16')

        # ECS cluster
        cluster = ecs.Cluster(self, 'Cluster', vpc=vpc)

        task_definition = ecs.FargateTaskDefinition( self, "flask-app", 
                cpu=512, memory_limit_mib=2048)

        image = ecs.ContainerImage.from_asset("flask-docker-app")
        container = task_definition.add_container( "flask-container", image=image)

        port_mapping = ecs.PortMapping(container_port=5000, host_port=5000)
        container.add_port_mappings(port_mapping)

        ecs_patterns.ApplicationLoadBalancedFargateService(self, "FargateService",
            cluster=cluster,
            task_definition=task_definition,
            desired_count=2,
            cpu=512,
            memory_limit_mib=2048,
            public_load_balancer=True)
