def func(num:int):
  context = mlrun.get_or_create_ctx(name='context')
  num+=num
  num=num*4
  print(num)
  context.log_result("num", num)
  return num
