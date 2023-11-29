class NoApiTokenError(Exception):
    def __init__(self, message="No Telegram API token was provided"):
        self.message = message
        super().__init__(self.message)
