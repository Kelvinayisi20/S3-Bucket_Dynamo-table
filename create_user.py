import boto3
from uuid import uuid4

dynamodb = boto3.resource("dynamodb", region_name='eu-west-1' )

table = dynamodb.Table("tech-world")

user = {
   "pk": "admin",
   "sk": str(uuid4()),
   "first_name": "Kelvin",
   "last_name" : "Ayisi",
   "Location": "Ghana",
   "Role": "Cloud Engineer",
   "Gneder": "Male" 
}

user = {
   "pk": "admin",
   "sk": str(uuid4()),
   "first_name": "Femi",
   "last_name" : "Moses",
   "Location": "Nigeria",
   "Role": "Tutor",
   "Gneder": "Male" 
}
response = table.put_item(Item= user)

print(response)