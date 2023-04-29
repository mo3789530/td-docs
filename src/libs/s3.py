import boto3

s3 = boto3.resource('s3')


def get_list_objects(bucket_name):
    bucket = s3.Bucket(bucket_name)
    return [obj.key for obj in bucket.objects.all()]


def get_list_buckets_with_prefix(prefix):
    arry = []
    for bucket in s3.buckets.all():
        if bucket.name.startswith(prefix):
            arry.append(bucket.name)
    return arry


def get_object_by_key(bucket_name, key):
    obj = s3.Object(bucket_name, key)
    return obj.get()['Body'].read().decode('utf-8')
