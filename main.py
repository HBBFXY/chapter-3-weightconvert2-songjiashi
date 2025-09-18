# 在# 设定初始体重（单位：kg，可根据实际情况修改）
initial_weight = 60  

print("年份\t地球体重(kg)\t月球体重(kg)")
for year in range(1, 11):
    # 计算地球上当年的体重
    earth_weight = initial_weight + year * 0.5  
    # 计算月球上当年的体重（月球体重是地球的16.5%）
    moon_weight = earth_weight * 0.165  
    print(f"{year}\t{earth_weight:.2f}\t\t{moon_weight:.2f}")这个文件里编写代码
