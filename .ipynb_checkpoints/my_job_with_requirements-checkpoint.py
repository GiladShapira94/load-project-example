import pandas as pd
from mlrun import MLClientCtx

def log_df(context:MLClientCtx,df=None):
    if df==None:
        df=.pd.Data
    context.log_dataset(key='df1',df=df,format='csv')