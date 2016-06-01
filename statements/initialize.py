# -*- coding: utf-8 -*-

class INITIALIZE(object):
    def __init__(self, ALPHANUMERIC=' ', NUMERIC=0):
        self.alphanumeric = ALPHANUMERIC
        self.numeric = NUMERIC

    def __call__(self, obj):
        self.initialize(obj)

    def initialize(self, obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, dict):
                    self.initialize(obj[k])
                elif isinstance(v, list):
                    for l in v:
                        self.initialize(l)
                elif k.startswith('FILLER'):
                    continue
                elif isinstance(v, str):
                    obj[k] = self.alphanumeric
                elif isinstance(v, int):
                    obj[k] = self.numeric
                elif isinstance(v, float):
                    obj[k] = float(self.numeric)
        elif isinstance(obj, list):
            for l in obj:
                self.initialize(l)

