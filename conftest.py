import pytest

# 平台的token
@pytest.fixture(scope='function', autouse=False, params=[{'authorization': 'z+PcFes+a0vo3BWD6UJXKuWah5sCy1+zswrqkWX7JGBr5pH4oMP1AviEoT8tIyd3'}])
def platform_token(request):    # request，获取params配置的参数
    return request.param    # 传参数，不然其他方法调用时获取不到参数

# 商家的token
@pytest.fixture(scope='function', autouse=False, params=[{'authorization': 'z+PcFes+a0vo3BWD6UJXKuWah5sCy1+zswrqkWX7JGBr5pH4oMP1AviEoT8tIyd3'}])
def multishop_token(request):    # request，获取params配置的参数
    return request.param    # 传参数，不然其他方法调用时获取不到参数

# 用户的token
@pytest.fixture(scope='function', autouse=False, params=[{'authorization': 'QdNtoxR9/4LyMEJU4DWPq1gy2wAjKyvuD530yZrF/TPCo7ACMn7LlLbPSiWmsBlG'}])
def user_token(request):    # request，获取params配置的参数
    return request.param    # 传参数，不然其他方法调用时获取不到参数