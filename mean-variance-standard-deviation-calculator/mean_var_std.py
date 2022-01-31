import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    cal = np.array(list).reshape(3, 3)

    calculations = {
    'mean': [cal.mean(0).tolist(), cal.mean(1).tolist(), cal.mean()],
    'variance': [cal.var(0).tolist(), cal.var(1).tolist(), cal.var()],
    'standard deviation': [cal.std(0).tolist(), cal.std(1).tolist(), cal.std()],
    'max': [cal.max(0).tolist(), cal.max(1).tolist(), cal.max()],
    'min': [cal.min(0).tolist(), cal.min(1).tolist(), cal.min()],
    'sum': [cal.sum(0).tolist(), cal.sum(1).tolist(), cal.sum()]
    }
  return calculations