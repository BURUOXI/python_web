import pytest, sys, os
from TestDatas.CreateData import create_datas as UAD
from Common.plugs.get_log import Log
from Common.plugs.get_config import r_config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
if sys.platform == "win32":
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini').replace('/', '\\')
else:
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini')
log_dir = r_config(conf_dir, "log", "log_path")
logger = Log(log_dir)


@pytest.mark.smoke
def test_create_licence(start_session):
    logger.info(" 执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
    logger.info('正常上传营业执照用例 ')
    start_session[1].create_licence(UAD.success_data['file_path'])
    logger.info("期望值：{0}".format(UAD.success_data['Msg']))
    logger.info("实际值：{0}".format(start_session[1].get_create_result_msg()))
    try:
        assert start_session[1].get_create_result_msg() == UAD.success_data['Msg']
        logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
        start_session[1].save_pictuer("{0}-正常截图".format(UAD.success_data['name']))
    except:
        logger.error(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
        start_session[1].save_pictuer("{0}-异常截图".format(UAD.success_data['name']))
        raise