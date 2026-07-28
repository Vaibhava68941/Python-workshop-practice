import boto3

s3 = boto3.resource("s3")
def show_buckets(s3):
    
    for bucket in s3.buckets.all():
        print(bucket.name)
        
def create_bucket(s3, bucket_name):
    s3.create_bucket(Bucket="python-s3-bucket-t")
    print(f"Bucket {bucket_name} created successfully.")

def upload_backup(s3_resource, bucket_name, file_path, key_name):
    # 3. Used 'with open' to ensure the file safely closes after uploading
    with open(file_path, "rb") as data:
        s3_resource.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("Backup uploaded successfully to S3 bucket.")


bucket_name = "python-s3-bucket-t"

# 4. Fixed: Pointed directly to the file, not just the folder
file_path = r"C:\Users\USER\Documents\Python-workshop-practice\backups\backup_2026-06-18.zip"

# Call the function
upload_backup(s3, bucket_name, file_path, "my_backup.zip")
#create_bucket(s3, "python-s3-bucket-t")
#show_buckets(s3)