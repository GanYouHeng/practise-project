### 修改商品选择状态接口
 
请求地址：
    
    /api/cart/cart/1/

请求方式:

    PATCH
    
请求参数:

    token string 标示用户唯一的值
    
响应结果:

    {
        'code': 200,
        'msg': '修改商品选择状态成功'，
        'data': {
        
        }
    }
    
响应参数:

    code int 状态码
    msg string 响应描述
    data 结果
