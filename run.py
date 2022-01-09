# encoding=utf8
import pytest,os,time
import allure
from Config import setting
now = time.strftime("%Y-%m-%d %H_%M_%S")
reportfile = setting.TEST_REPORT + '/' + now + 'result.html'

def main():
    """运行pytest命令启动测试"""
    pytest.main(
        ['-v', '-s',
         '-m', 'test1',
         'TestCases/login_api/',
         'TestCases/ims_api/',

         '--html=%s' % reportfile, '--self-contained-html'])


if __name__ == '__main__':
    main()
