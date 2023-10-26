class Response:
   def __init__(self, success: bool, errorMsg: str,data):
        # Instance attributes
        self.success = success
        self.error = errorMsg
        self.data = data