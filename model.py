import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

def calc_times(timeString):
  """ Find time length encoded in time string """
  timeList = re.findall("[0-9]:[0-6][0-9]", timeString)
  timeList = list(map(lambda s : int(s[2:]) + (60 * int(s[0])), timeList))
  return(timeList[1] - timeList[0])
