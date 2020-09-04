from selenium.webdriver.common.by import By


class LoginLocator:
    # username_loc = (By.XPATH, '//*[@id="app"]/div/form/div[1]/div/div/input')
    # password_loc = (By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div/input')
    # login_btn_loc = (By.XPATH, '//*[@type="button"]')
    # error_msg_loc = (By.CLASS_NAME, 'el-message__content')

    user_locator = (By.XPATH, './/input[@placeholder="请输入手机号"]')
    pwd_locator = (By.XPATH, './/input[@placeholder="请输入密码"]')
    btn_locator = (By.XPATH, './/button[@class="el-button lhb-mt-34 el-button--primary"]')

    # 获取输入手机号提示语
    prompt_user = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[2]/div/div/form/div[1]/div/div[2]')

    # 获取请输入密码提示语
    prompt_pwd = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]')

    # 登录成功-选择账号
    login_success = (By.XPATH, '/html/body/div[7]/div/div[2]/div/div[1]')
    # error_info_locator = (By.XPATH, ".//button[@class="el-button lhb-mt-34 el-button--primary"]")

    # 获取错误提示的toast
    invalid_info_toast = (By.XPATH, '/html/body/div[6]/p')