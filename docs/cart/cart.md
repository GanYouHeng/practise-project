### 购物车接口

请求地址:

    /api/cart/cart/
    
请求方式:

    POST
   
请求参数:
    
    token string 标示用户唯一的值
    
响应结果：

    {
        'code': 1009,
        'msg': '用户没有登录，没有操作权限',
        'data': {
        
        }
    }
    
    {
        'code': 200,
        'msg': '请求成功',
        'data': {
            'carts': 
            'total_price':
        }
    }
    
响应结果:

    code int 状态码
    msg string 响应描述
    data 结果
            