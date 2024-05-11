import os
import logging

class GCloudSync:

    def authenticate_to_gcp(self):
        service_account_key_path = (r"C:\Users\Naruto\Desktop\generative_ai\PROJECTS\text_classification\hazel-aquifer-418013-c02894dad016.json")
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_key_path


    def sync_folder_to_gcloud(self, gcp_bucket_url, filepath, filename):

        command = f"gsutil cp {filepath}/{filename} gs://{gcp_bucket_url}/"
        # command = f"gcloud storage cp {filepath}/{filename} gs://{gcp_bucket_url}/"
        os.system(command)

    def sync_folder_from_gcloud(self, gcp_bucket_url, filename, destination):

        command = f"gsutil cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
        # command = f"gcloud storage cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
        os.system(command)
