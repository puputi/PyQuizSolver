# 递归求和(1-10)

def get_sum(num):
    if num>=1:
        res=num+get_sum(num-1)
    else:
        res=0
    
    return res
res=get_sum(10)
print(res)
