def multi_3(context,event):
    event.body['int']=event.body['int']*3
    print(event.body)
    return event.body
