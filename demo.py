# from hate.logger import logging
# logging.info("welcome to out Project")

from hate.configuration.gcloud_syncer import GCloudSync
obj = GCloudSync()
obj.sync_folder_from_gcloud("hate-speech-bucket007", "dataset.zip", "data/dataset.zip")