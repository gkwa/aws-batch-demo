import argparse
import boto3

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--table", help="DynamoDB table",
                    default='TestTable')
parser.add_argument(
    "-r", "--region", help="AWS Region where your DynamoDB table sits",
    default='us-east-1'
)
args = parser.parse_args()

session = boto3.session.Session(region_name=args.region)
dynamodb = session.resource('dynamodb')


table = dynamodb.Table(args.table)

filler = "x" * 1000

i = 0
while (i < 10):
    j = 0
    while (j < 10):
        print(i, j)

        table.put_item(
            Item={
                'pk': i,
                'sk': j,
                'filler': {"S": filler}
            }
        )
        j += 1
    i += 1
