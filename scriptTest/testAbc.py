import pytest
import allure


class Test_ABC:

    # 函数级开始

    def setup(self):
        print("------->setup_method")

    # 函数级结束

    def teardown(self):
        print("------，->teardown_method")


    @allure.step(title='第一个测试')
    def test_a(self):
        allure.attach("这是一个描叙","试一下")

        assert 1

    @allure.issue('http://www.haodf.com/')
    @allure.testcase('http://www.haodf.com/testab')
    @allure.severity('Critical')
    def test_b(self):
        allure.attach("这是一个描叙", "试一下")
        print("------->test_b")


# if __name__ == '__main__':
#     pytest.main('-s  testAbc.py')