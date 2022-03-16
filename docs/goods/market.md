### 超市接口

请求地址:

    /api/goods/market/
    
请求方式:
    
    POST
    
请求参数:

    typeid int 食品id
    childcid int 食品子分类
    order_rule int 食品排序规则
    
响应参数:

    {
        'code': 200,
        'msg': '请求成功',
        'data': {
            'goods_list': 
            'foodtype_childname_list': 
            'order_rule_list': 
        }
    }
    
响应参数:

    code int 状态码
    msg string 响应描述
    data 结果
    
