class Writer:
    path = ''

    def __init__(self, path: str):
        self.path = path

    def writing(self, data: str):
        open(self.path, 'w').write(data)

    def reading(self):
        return open(self.path, 'r').read()
