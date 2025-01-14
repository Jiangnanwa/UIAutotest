import pytest
from common.login import login_by_password


# 每个测试py文件执行前执行1次conftest文件中的fixture
@pytest.fixture(scope="module", autouse=True)
def test_loginin(poco):
    print("开始登录账号...")
    login_by_password('slf1994', 'sns654321', 'com.hexin.plat.android', poco)
