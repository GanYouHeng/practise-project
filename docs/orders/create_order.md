### 创建订单接口

请求地址:

    /api/orders/orders/
    
请求方式:

    POST
    
请求参数:

    token string 标示用户唯一的值
    
响应结果:

    {
        'code': 1010,
        'msg': '购物车中没有下单的商品，请选择再下单',
        'data': {
        
        }
    }
    
    {
        'code': 200,
        'msg': '请求成功',
        'data': {
            'order_id':
        }
    }
    
响应参数:
    
    code int 状态码
    msg string 响应描述
    data 结果
    
