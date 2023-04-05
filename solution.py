import pandas as pd
import numpy as np


chat_id = 5156861873 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t = 48
    a = (np.mean(x)*2)/t*t
    return a #
