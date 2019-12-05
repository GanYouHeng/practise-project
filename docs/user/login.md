### 登录接口

请求地址:

    /api/user/auth/login/
    
请求方式:

    POST
    
请求参数:

    u_username string 账号 必填 长度4-10
    u_password string 密码 必填 长度4-32
    
响应结果:
    
    {
        'code': 1006,
        'msg': '登录失败'
        'data': {
        
        }
    }
    
    {
        'code': 200,
        'msg': '请求成功':
        'data': {
            'token': 
        }
    }
    
响应参数:

    code int 状态码
    msg string 响应描述
    data 结果 
    token 标识用户的唯一值