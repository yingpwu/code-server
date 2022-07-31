# 用户注册
1. 用户提供用户名,密码POST到我们的服务器
2. 服务组织数据
3. 检测用户是否存在
3.1 用户存在
    直接返回error ,500
3.2 用户不存在
    创建用户
    返回OK, 200

# 用户验证
1. 用户提供用户名,密码post我们的服务器
2. 组织数据
3. 检测用户提供的数据是否合法
3.1 用户合法
    3.1.1 生成JWR token
    3.1.2 返回数据给用户
        {
            "success": True,
            "message": "用户验证有效",
            "token": token
        },200
<<<<<<< Updated upstream
3.2 用户非法
    3.2.1 返回调用方
    {
        "success": False,
        "message": "用户非法",
    },401
=======
- 3.2 用户非法
-     3.2.1 返回调用方
- {
  "success": False,
  "message": "用户非法",
  },401
>>>>>>> Stashed changes
