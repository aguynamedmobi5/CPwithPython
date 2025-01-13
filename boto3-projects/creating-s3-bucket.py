import boto3, sys, os

bucket_name = sys.argv[1]

s3 = boto3.client('s3')


def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except:
        print("Something else went wrong")


def create_bucket(bucket_name, region=None):

    try:
        if region is None:
            s3.create_bucket(Bucket=bucket_name)
        else:
            location = {'LocationConstraint': region}
            s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    except:
        print("Something else went wrong")



if __name__ == "__main__":
    # create_bucket(bucket_name, 'us-west-1')
    upload_file('hello.txt', 'mobi-21-43-56-iqbal')