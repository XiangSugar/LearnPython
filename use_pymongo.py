# -*- coding: utf-8 -*-
from myconn import MongoConn

if __name__ == "__main__":
    my_conn = MongoConn()
    datas = [
        {'_id':1, 'data':12},        
        {'_id':2, 'data':22},
        {'_id':3, 'data':'cc'}      
    ]  
    #插入数据，'mytest'是上文中创建的表名
    my_conn.db['mytest'].insert(datas)
    #查询数据，'mytest'是上文中创建的表名
    res=my_conn.db['mytest'].find({})
    for k in res:
        print(k)