from selenium.webdriver.common.by import By


class CreatCompany:
    """申请公司页面元素"""
    # 上传营业执照
    upload_licence = (By.XPATH, '//*[@id="__layout"]/div/div/div[4]/div[3]/div/form/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div')
    # 请上传营业执照
    upload_licence_mgs = (By.XPATH, '')

    # 营业执照名称
    licence_name = (By.XPATH, '//*[@id="__layout"]/div/div/div[4]/div[3]/div/form/div[2]/div/div/div/input')
    # 请填写营业执照全称
    licence_name_mgs = (By.XPATH, '')

    # 公司地址
    company_address = (By.XPATH, '')
    # 请选择公司地址，省市区缺一不可
    company_address_mgs = (By.XPATH, '')

    # 详细地址
    detaile_address = (By.XPATH, '')
    # 请填写详细地址
    detaile_address_mgs = (By.XPATH, '')

    # 联系电话
    create_number = (By.XPATH, '')

    # 授权书
    power_attorney = (By.XPATH, '')
    # 品牌授权书
    brand_authorization = (By.XPATH, '')
    # 经营许可证
    business_license = (By.XPATH, '')
    # 管理员姓名
    administrator_name = (By.XPATH, '')
    # 请填写管理员姓名
    administrator_name_mgs = (By.XPATH, '')

    # 身份证
    administrator_card = (By.XPATH, '')
    # 请上传完整且有效的身份证正反面
    administrator_card_mgs = (By.XPATH, '')