# 正常运营执照
# success_data = {'name': '新增企业营业执照-正常测试', 'username': 'haha', 'password': '123456', 'email': '123@qq.com',
#                 'phone': '13776787676', 'Msg': '创建成功'}

success_data = {'name': '新增企业营业执照-正常测试', 'file_path': r"D:\Workbook\test\picture\timg5.jpg", 'Msg': '天津联星传动有限公司'}

# 异常场景
error_data = [
    {'name': '新增企业营业执照-营业执照已经认证', 'file_path': r"D:\Workbook\test\picture\timg5.jpg", 'Msg': '营业执照已经认证'},
    {'name': '新增企业营业执照-上传文件的名称过长，请修改后上传', 'file_path': r"D:\Workbook\test\picture\timg5.jpg", 'Msg': '上传文件的名称过长，请修改后上传'},
    {'name': '新增企业营业执照-营业执照识别失败', 'file_path': r"D:\Workbook\test\picture\timg5.jpg", 'Msg': '营业执照识别失败'},
]
