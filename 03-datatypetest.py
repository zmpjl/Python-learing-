#定义变量
name="传智播客"#公司名称
stock_price=19.99#当前股价
stock_code="003032"#股票代码
stock_price_daily_grown_factor=1.2#股票每日增长系数
grown_days=7#增长天数
final_price=stock_price*stock_price_daily_grown_factor**grown_days#股票最终股价
print(f"{name}，股票代码{stock_code},当前股价：{stock_price}")
print(f"每日增长系数是：{stock_price_daily_grown_factor},经过{grown_days}天的增长后，股价达到了：%.2f" %final_price)