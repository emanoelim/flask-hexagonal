import werkzeug

from item.adapters.outbound.upload_s3_adapter import UploadS3Adapter


file_type = werkzeug.datastructures.FileStorage


class UploadPort:
    def __init__(self, adapter=None):
        self.adapter = adapter or UploadS3Adapter()

    def upload_file(self, file: file_type, file_name: str = None) -> str:
        return self.adapter.upload_file(file, file_name)
