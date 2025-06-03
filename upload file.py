import boto3

client = boto3.client("s3")

response = client.put_object(
    Body='filetouploadcar.jpg',
    Bucket='kelvinayisi88',
    Key='objectkeycar.jpg',
    ContentType = "image/jpg"
)

print(response)