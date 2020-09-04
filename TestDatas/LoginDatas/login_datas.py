# 正常场景测试数据
success_data = {'name': '选择账号进入首页', 'username': '13385289600', 'password': '123456Aa'}

# 异常场景测试 - username
error_usernameFormat_data = [
    {'name': '请输入手机号', 'username': '', 'password': '123456Aa', 'errorMsg': '请输入手机号'},
    {'name': '请输入有效的手机号', 'username': '1338528960', 'password': '123456Aa', 'errorMsg': '请输入有效的手机号'},
    {'name': '请输入有效的手机号', 'username': '133852896000', 'password': '123456Aa', 'errorMsg': '请输入有效的手机号'},
]

# 异常场景测试 - password
error_passwordFormat_data = [
    {'name': '登录功能-异常测试-密码为空', 'username': '13385289600', 'password': '', 'errorMsg': '请输入密码'},
    {'name': '登录功能-异常测试-密码最少8位', 'username': '13385289600', 'password': '12345', 'errorMsg': '密码最少8位'},
]

# toast 提示
error_toastFormat_data = [
    {'name': '登录功能-异常测试-用户名不存在', 'username': '13385289601', 'password': '123456Aa', 'errorMsg': '账号或密码错误'},
    {'name': '登录功能-异常测试-密码错误', 'username': '13385289600', 'password': '12345672', 'errorMsg': '账号或密码错误'},
]
