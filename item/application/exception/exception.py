class ItemAlreadyExists(Exception):
    message = 'Item already exists.'
    status_code = 400

    def __init__(self, message=message, status_code=status_code):
        self.message = message
        self.status_code = status_code


class ItemNotFound(Exception):
    message = 'Item not found.'
    status_code = 404

    def __init__(self, message=message, status_code=status_code):
        self.message = message
        self.status_code = status_code
