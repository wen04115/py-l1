# N的阶乘
# def dg(s):
#     if s==1:
#         return 1
#     else:
#       return s*dg(s-1)
# print(dg(8))

# 电商订单计算器
# 定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额。
# 具体规则如下：
# 优惠券需要商品金额满 5000 才可以使用，且优惠券金额不能超过商品总价。
# 积分抵扣需要商品总金额满 5000 才可以使用，100 积分抵扣 1 元（且抵扣金额不能超过商品总价，积分只能整百抵扣）
def total_goods(*args,coupon,score,express):
    """
       *args    把传入的一批商品信息（商品名、价格、数量）组成元组
       coupon   优惠券
       score    积分抵扣
       express  运费信息
    """
    # 订单的总金额=商品总价-优惠券金额-积分抵扣+运费
    shangpin_price=sum([goods[1]*goods[2] for goods in args])  #把商品原金额生成列表
    if shangpin_price>=5000 and shangpin_price>coupon:  #列表不能和数字做算术运算 所以上一行加sum 不然无法比较
        total_price=shangpin_price-coupon-score//100+express
    else:
        total_price=shangpin_price
    return total_price 

print(total_goods(("苹果",10,20),("手机",6999,1),coupon=100,score=200,express=20))           
