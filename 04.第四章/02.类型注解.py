# 变量定义 - 未指定类型注解
# a = 596
# score = 98.5
# hobby = "Python"
# flag = True
# pic = None

# names = ["A", "C", "E"]
# phones = {"13309091111", "15209101902", "18809019201"}
# options = {"count": 2, "total":10}
# goods = ("手机", 6999, 1)


# # 变量定义 - 指定类型注解
# a2: int = 596
# score2: float = 98.5
# hobby2: str = "Python"
# flag2: bool = True
# pic2: None = None

# names2: list[str] = ["A", "C", "E"]   #list[str | int]表示里面的类型可以是字符串也可以是整型
# phones2: set[str] = {"13309091111", "15209101902", "18809019201"}
# options2: dict[str, int] = {"count": 2, "total":10}
# goods2: tuple[str, int, int] = ("手机", 6999, 1)

def total_goods(*args: tuple[str, float, int], coupon: int = 0, score: int = 0, express: int = 0):
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