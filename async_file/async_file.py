class AsyncFile:
    def __init__(self, filename):
        self.filename = filename

    async def __aenter__(self):
        self.file = i=
        return self

    async def readall(self):
        return None

    async def __aexit__(self, ext, ex, tb):
        pass