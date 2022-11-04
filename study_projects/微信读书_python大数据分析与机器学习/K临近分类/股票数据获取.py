from cmath import exp
import tushare as ts
ts.set_token('2e406f12355008a8ced831007308c18fe94c7464b156ad086e7359fd')#设置token，只需设置一次
pro = ts.pro_api()

df = ts.get_hist_data('000002', start='2018-01-01', end='2019-01-31')
print(df)
import talib
a = 0.6931
print((exp(-a))/(exp(-a)+exp(a)+exp(-a)+exp(a)+exp(-a)))
