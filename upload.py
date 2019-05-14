from fdfs_client.client import Fdfs_client

fdfs = Fdfs_client("./client.conf")
with open('./1.jpeg', "rb") as f:
    image = f.read()

res = fdfs.upload_by_buffer(image)
print(res)
