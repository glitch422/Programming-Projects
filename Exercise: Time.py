from time import time

def performancer(func):
  def wrapper(*args, **kwargs):
    t1 = time()
    result = func(*args, **kwargs)
    t2 = time()
    print(f'It took {t2-t1} seconds')
    return result
  return wrapper

@performancer
def long_time():
  for i in range(10000000):
    i*5

long_time()
