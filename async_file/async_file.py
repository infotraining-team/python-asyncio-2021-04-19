class AsyncFile:
    def __init__(self, filename):
        self.filename = filename

    async def __aenter__(self):
        return self

    async def __aexit__(self, ext, ex, tb):
        pass