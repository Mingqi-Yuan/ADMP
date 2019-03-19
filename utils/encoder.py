"""
Encoding = UTF-8
By Mingqi, Yuan, 2019/3/18
Usage: An encoder for json.dumps()
"""

import numpy as np
import json

class encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(encoder, self).default(obj)