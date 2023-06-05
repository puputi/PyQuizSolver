S=20
infinitesimal=0.00000001

a=S/2

counter=1
while True:
    b=S/a
    delta=a-b
    print(f'这是第{counter}轮,S={S},a={a:.2f},b={b:.2f},delta={delta},是否结束：{delta<infinitesimal}')

    counter=counter+1

    if delta<infinitesimal:
        break
    else:
        a=a=(a+b)/2
