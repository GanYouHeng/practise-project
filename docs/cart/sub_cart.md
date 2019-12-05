### 减少商品接口

请求地址:

    /api/cart/cart/sub_cart/
    
请求方式:

    POST
    
请求参数:
    
    token string 标示用户唯一的值
    
响应结果:

    {
        'code': 200,
        'msg': '请求成功',
        'data': {
            'c_goods_num':
        }
    }
    
响应参数:
    
    code int 状态码
    msg string 响应描述
    data 结果