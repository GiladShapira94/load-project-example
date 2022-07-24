from mlrun.execution import MLClientCtx
def func(context : MLClientCtx,num:int):
  num+=num
  num=num*4
  print(num)
  context.log_result("num", num)
  return num
