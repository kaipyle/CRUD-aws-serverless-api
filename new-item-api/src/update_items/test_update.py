x = {'resource': '/items/{id}', 'path': '/items/c02c51f6-f032-4c7f-a50a-28a5abfd6b54', 'httpMethod': 'PUT', 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'CloudFront-Forwarded-Proto': 'https', 'CloudFront-Is-Desktop-Viewer': 'true', 'CloudFront-Is-Mobile-Viewer': 'false', 'CloudFront-Is-SmartTV-Viewer': 'false', 'CloudFront-Is-Tablet-Viewer': 'false', 'CloudFront-Viewer-ASN': '18881', 'CloudFront-Viewer-Country': 'BR', 'Content-Type': 'application/json', 'Host': 'woivri11t4.execute-api.sa-east-1.amazonaws.com', 'User-Agent': 'Thunder Client (https://www.thunderclient.com)', 'Via': '1.1 13bdfe51c955b72c24c041717e9e9508.cloudfront.net (CloudFront)', 'X-Amz-Cf-Id': 'l9ekd6HbxVM5I21lvOdEcFJAhN2xRdL-cTy4At7u9gDrqolgJNBqow==', 'x-amz-date': '20230804T174503Z', 'X-Amzn-Trace-Id': 'Root=1-64cd3916-0eda5e08559981a17b378f02', 'X-Forwarded-For': '177.40.231.194, 18.68.11.70', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'}, 'multiValueHeaders': {'Accept': ['*/*'], 'Accept-Encoding': ['gzip, deflate, br'], 'CloudFront-Forwarded-Proto': ['https'], 'CloudFront-Is-Desktop-Viewer': ['true'], 'CloudFront-Is-Mobile-Viewer': ['false'], 'CloudFront-Is-SmartTV-Viewer': ['false'], 'CloudFront-Is-Tablet-Viewer': ['false'], 'CloudFront-Viewer-ASN': ['18881'], 'CloudFront-Viewer-Country': ['BR'], 'Content-Type': ['application/json'], 'Host': ['woivri11t4.execute-api.sa-east-1.amazonaws.com'], 'User-Agent': ['Thunder Client (https://www.thunderclient.com)'], 'Via': ['1.1 13bdfe51c955b72c24c041717e9e9508.cloudfront.net (CloudFront)'], 'X-Amz-Cf-Id': ['l9ekd6HbxVM5I21lvOdEcFJAhN2xRdL-cTy4At7u9gDrqolgJNBqow=='], 'x-amz-date': ['20230804T174503Z'], 'X-Amzn-Trace-Id': ['Root=1-64cd3916-0eda5e08559981a17b378f02'], 'X-Forwarded-For': ['177.40.231.194, 18.68.11.70'], 'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https']}, 'queryStringParameters': None, 'multiValueQueryStringParameters': None, 'pathParameters': {'id': 'c02c51f6-f032-4c7f-a50a-28a5abfd6b54'}, 'stageVariables': None, 'requestContext': {'resourceId': '17pqea', 'resourcePath': '/items/{id}', 'httpMethod': 'PUT', 'extendedRequestId': 'JJXbjGygGjQFSVQ=', 'requestTime': '04/Aug/2023:17:44:54 +0000', 'path': '/Prod/items/c02c51f6-f032-4c7f-a50a-28a5abfd6b54', 'accountId': '696608785670', 'protocol': 'HTTP/1.1', 'stage': 'Prod', 'domainPrefix': 'woivri11t4', 'requestTimeEpoch': 1691171094420, 'requestId': 'e8a5aee7-662c-4f80-a076-b9ee0370e728', 'identity': {'cognitoIdentityPoolId': None, 'accountId': None, 'cognitoIdentityId': None, 'caller': None, 'sourceIp': '177.40.231.194', 'principalOrgId': None, 'accessKey': None, 'cognitoAuthenticationType': None, 'cognitoAuthenticationProvider': None, 'userArn': None, 'userAgent': 'Thunder Client (https://www.thunderclient.com)', 'user': None}, 'domainName': 'woivri11t4.execute-api.sa-east-1.amazonaws.com', 'apiId': 'woivri11t4'}, 'body': '{\n  "itemName" : "Pêra",\n  "description" : "Uma fruta verde e com um formato estranho",\n  "price" : "7.00",\n  "isActive" : "True"\n}', 'isBase64Encoded': False}
from .app import lambda_handler
from unittest import mock



def setup_mockdb(mock: mock.Mock) -> mock.Mock:
    Table = mock.Mock() 
    mock.return_value.Table.return_value = Table
    return Table


@mock.patch("boto3.resource")
def test_api(mocked_db: mock.Mock) -> None:
    Table = setup_mockdb(mocked_db)
    lambda_handler(x, None)    
    Table.update_item.assert_called_once_with(
        Key={'id': 'c02c51f6-f032-4c7f-a50a-28a5abfd6b54'}, 
        UpdateExpression='set itemName = :itemName, description = :description, price = :price, isActive = :isActive', 
        ExpressionAttributeValues={':itemName': 'Pêra', ':description': 'Uma fruta verde e com um formato estranho', ':price': '7.00', ':isActive': 'True'}, 
        ReturnValues='UPDATED_NEW'
    ) 


