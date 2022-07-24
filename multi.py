def multi_3(context,event):
    event['int']=event['int']*3
    print(event)
    return event
