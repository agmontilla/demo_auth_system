from libs.aws.auth import AWSCognito


def get_aws_cognito() -> AWSCognito:
    """Get an instance of AWSCognito"""
    return AWSCognito()
