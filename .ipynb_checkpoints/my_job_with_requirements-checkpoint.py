import pandas as pd
from mlrun import MLClientCtx

def log_df(context:MLClientCtx,df=None):
    if df==None:
        df=pd.DataFrame({"col1":[1,2,3,4,5]})
    context.log_dataset(key='df1',df=df,format='csv')