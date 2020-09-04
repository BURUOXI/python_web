from selenium.webdriver.common.by import By


class IndexLocator:
    # 选择账号进入首页
    logout_loc = (By.XPATH, '/html/body/div[7]/div/div[2]/div/div[1]')

    # 进入个人账号
    login_personal = (By.XPATH, '/html/body/div[7]/div/div[2]/div/div[3]/div[2]/div[2]/a/span')

    # 进入企业账号
    login_company = (By.XPATH, '/html/body/div[7]/div/div[2]/div/div[4]/div[2]/div[2]/a/span')

    # 申请加入企业
    apply_company = (By.XPATH, '/html/body/div[7]/div/div[2]/div/div[5]/div[1]/button')

    # 创建新企业
    create_company = (By.XPATH, '/html/body/div[7]/div/div[2]/div/div[5]/div[2]/button')



