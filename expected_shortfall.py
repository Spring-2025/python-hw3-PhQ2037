# -*- coding: utf-8 -*-
"""Expected Shortfall.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1inJkWjiIiUqTxMFZsoxe-f_Uwj7FYWcN
"""

import numpy as np

def ES(losses, confidence=None, VaR=None, use_PnL=False):
    if VaR is None:

        VaR = np.percentile(losses, 100 * confidence)

    es_value = np.mean(losses[losses > VaR])
    return es_value

u = np.random.uniform(0, 100, 100000)

es_confidence = ES(losses=u, confidence=0.8)
print('ES with confidence:', np.round(es_confidence, 0) == 90)

es_var = ES(losses=u, VaR=80)
print('ES with VaR:', np.round(es_var, 0) == 90)