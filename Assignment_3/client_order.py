from winreg import DisableReflectionKey
from numpy import product
from datetime import datetime
from math import floor
import numpy as np

class ClientOrder:
    
    def __init__(self, order):
        self.order = order # [product, amount]
    
