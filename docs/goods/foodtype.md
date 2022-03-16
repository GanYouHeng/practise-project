### 食品分类接口

请求地址:

    /api/goods/foodtype/
    
请求方式:
        
    GET
    
响应结果:

    {
    "code": 200,
    "msg": "请求成功",
    "data": [
        {
            "id": 1,
            "typeid": 104749,
            "typename": "热销榜",
            "childtypenames": "全部分类:0",
            "typesort": 1
        },
        {
            "id": 2,
            "typeid": 104747,
            "typename": "新品尝鲜",
            "childtypenames": "全部分类:0",
            "typesort": 2
        },
        {
            "id": 3,
            "typeid": 103532,
            "typename": "优选水果",
            "childtypenames": "全部分类:0#进口水果:103534#国产水果:103533",
            "typesort": 3
        },
        {
            "id": 4,
            "typeid": 103581,
            "typename": "卤味熟食",
            "childtypenames": "全部分类:0",
            "typesort": 4
        },
        {
            "id": 5,
            "typeid": 103536,
            "typename": "牛奶面包",
            "childtypenames": "全部分类:0#酸奶乳酸菌:103537#牛奶豆浆:103538#面包蛋糕:103540",
            "typesort": 5
        },
        {
            "id": 6,
            "typeid": 103549,
            "typename": "饮料酒水",
            "childtypenames": "全部分类:0#饮用水:103550#茶饮/咖啡:103554#功能饮料:103553#酒类:103555#果汁饮料:103551#碳酸饮料:103552#整箱购:104503#植物蛋白:104489#进口饮料:103556",
            "typesort": 6
        },
        {
            "id": 7,
            "typeid": 103541,
            "typename": "休闲零食",
            "childtypenames": "全部分类:0#进口零食:103547#饼干糕点:103544#膨化食品:103543#坚果炒货:103542#肉干蜜饯:103546#糖果巧克力:103545",
            "typesort": 7
        },
        {
            "id": 8,
            "typeid": 103557,
            "typename": "方便速食",
            "childtypenames": "全部分类:0#方便面:103558#火腿肠卤蛋:103559#速冻面点:103562#下饭小菜:103560#罐头食品:103561#冲调饮品:103563",
            "typesort": 8
        },
        {
            "id": 9,
            "typeid": 103569,
            "typename": "粮油调味",
            "childtypenames": "全部分类:0#杂粮米面油:103570#厨房调味:103571#调味酱:103572",
            "typesort": 9
        },
        {
            "id": 10,
            "typeid": 103575,
            "typename": "生活用品",
            "childtypenames": "全部分类:0#个人护理:103576#纸品:103578#日常用品:103580#家居清洁:103577",
            "typesort": 10
        },
        {
            "id": 11,
            "typeid": 104958,
            "typename": "冰激凌",
            "childtypenames": "全部分类:0",
            "typesort": 11
        }]
    }
        
响应参数:

    code int 状态码
    msg string 响应描述
    data 结果
    
    id int id值
    typeid 分类id值
    typename 分类名
    childtypenamse 每种分类的子分类
    typesort 不知道
     
