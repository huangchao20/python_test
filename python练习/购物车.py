goods = [["1.iphone X",7399],["2.vivo X21",3598],["3.利用Python进行数据分析",72],["4.迪士尼滑板车", 179],["5.索尼无线蓝牙耳机", 1999]]
havabuys = []

salarytem = input("请输入你带多少钱来购物:")
if not salarytem.isdigit():
    exit()

your = int(salarytem)

print("购物车中的商品有:")
for i in goods:
    print(i)

goodsindex = ""

# print("需要购买的商品序号，'q'退出")
while True:
    goodsindex = input("需要购买的商品序号，'q'退出:")
    if goodsindex == "q" or goodsindex == "Q":
        if not havabuys:
            print("你个搓比，啥都没有买!gun~~~")
        else:
            print("您所购买的商品有:")
            for i in havabuys:
                print(i)
            print("您所剩余额:", your )
        exit()
    elif goodsindex.isdigit():
        buys = int(goodsindex)
        if buys < 0 or buys > len(goods):
            print("您选择的物品不存在")
            exit()
        price = int(goods[buys-1][1])

        # print(type(your))
        # print(type(price))

        if your >= price:
            havabuys.append(goods[buys-1][0])
            your = your -price
            print("购买成功，购买商品为：\n" + goods[buys - 1][0])
        else:
            print("\033你个穷B，剩余：%.2f \033，还差:%.2f \033,买不起就滚..." % (your, price-your))
