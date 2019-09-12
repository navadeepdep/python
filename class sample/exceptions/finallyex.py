try:
  raise KeyboardInterrupt
except KeyboardInterrupt as e:
  print("Intentionally keyboard exception is raised !!")
finally:
  print('Goodbye, world!')


try:
  raise Exception('Navadeep Wants to raise a exception !! ')
except Exception as e:
  print(e)
finally:
  print('Goodbye!')