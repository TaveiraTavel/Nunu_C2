from json import JSONEncoder

class Encoder(JSONEncoder):
        def encode(self, o):
            return o.__dict__

