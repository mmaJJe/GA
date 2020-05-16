import csv
import random
import matplotlib.pyplot as plt

def distance(f,l):
    d = ((int(f[1]) - int(l[1]))**2 + (int(f[2])- int(l[2]))**2)**0.5
    return d

# 중복 제거(퍼옴)
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def make_gene():
    dots = []
    f = open('building.csv','r')
    rdr = csv.reader(f)
    pk = 1
    for line in rdr:
        line.insert(0,pk)
        dots.append(line)
        pk += 1
    f.close()
    return dots

def sort_gene(dots):
    li = []
    times = 99
    i_dot = dots[random.randint(0, times-1)]
    d = 0
    while times > 0:
        add = False
        standard = 1
        while add == False:
            for dot in dots:
                if distance(i_dot,dot) > 0 and distance(i_dot,dot) <= standard :
                    # print(distance(i_dot,dot))
                    d += distance(i_dot,dot)
                    li.append(i_dot)
                    index =  dots.index(i_dot)
                    dots.pop(index)
                    i_dot = dot
                    times -= 1
                    add = True
                    # print(standard,times)
                else:
                    pass
            standard += 1
            # print(standard,times)
            if times == 1:
                # print(dots)
                li.append(i_dot)
                # print(i_dot)
                print("유전자 하나 완성")
                times -= 1
                add = True
    print(d)
    li.insert(0, [0,0,0])
    li.append([100,0,0])
    print(len(li))
    return [d,li] 

#road_li 구조 = [[거리,[좌표]],[거리,[좌표]],[거리,[좌표]]]
def evaluate(road_li):
    road_li.sort(key=lambda x: x[0])
    return road_li


# def upgrade(road_li):
    # upgrade_parts = []  
    # base = road_li[0][1]
    # # print(base)
    # for i in range(100):
    #     if distance(base[i],base[i+1]) > road_li[0][0]//100:
    #         upgrade_parts.append(base[i])
    #         upgrade_parts.append(base[i+1])
    #     else:
    #         pass
        
    # where_li = []
    # w_li =[]
    # for part in upgrade_parts:
    #     if len(w_li) == 0:
    #         where = base.index(part)
    #         w_li.append(where)
    #     else:
    #         where = base.index(part)
    #         if base.index(base[where-1]) in w_li:
    #             if base.index(base[where]) in w_li:
    #                 pass
    #             else:
    #                 w_li.append(where)
    #         else:
    #             where_li.append(w_li)
    #             w_li =[]
    #             w_li.append(where)

    
    # # print("upgrade_parts",len(upgrade_parts))
    # # print(upgrade_parts)
    # # print(len(where_li))
    # # print(where_li)
    
    # quarters = []
    # insert_li = []
    # for where in where_li:
    #     quarters.append([base[where[0]]])
    #     if base[where[0]] in upgrade_parts:
    #         insert_li.append(where[0])
    #         upgrade_parts.pop(upgrade_parts.index(base[where[0]]))
    #     else:
    #         pass
    # # print('quarters',quarters)
    # for quarter in quarters:
    #     time = 1
    #     q_in = quarters.index(quarter)
    #     standard = 1
    #     while time < len(where_li[q_in]):
    #         if len(upgrade_parts) == 0:
    #             break
    #         for part in upgrade_parts:
    #             if part in quarter:
    #                 pass
    #             else:
    #                 if distance(quarter[time-1],part) > 0 and distance(quarter[time - 1],part) < standard:
    #                     quarter.append(part)
    #                     # print('part',part)
    #                     upgrade_parts = remove_values_from_list(upgrade_parts,part)
    #                     time += 1
    #                     # print(upgrade_parts)
    #                 else:
    #                     pass 
    #         standard += 1 
    # # print("q",quarters)
    # # print(len(quarters))
    # # print(insert_li)
    # for quarter in quarters:
    #     for i in range(len(insert_li)):
    #         for q in range(len(quarter)):
    #             if quarter[q] in base:
    #                 index = base.index(quarter[q])
    #                 if index >= insert_li[i]:
    #                     base.pop(index)
    #                     base.insert(insert_li[i] ,quarter[q])
    #                 else:
    #                     base.insert(insert_li[i] ,quarter[q])
    #                     base.pop(index)
    #             else:
    #                 pass

    # print(len(base))
    # # print(base)
    # # print(base)
    # return base


low = float("inf")
#첫 유전자 생성
road_li = []
for i in range(2):
    dots = make_gene()
    road_li.append(sort_gene(dots))


time = 0
while True:
    print(time,"세대 ","최단 거리 ",road_li[0][0])
    evaluate(road_li)
    print("평가 끝")
    
    # # 유전자 조합
    # old = road_li[0][1]
    # part = []
    # parts = []
    # last_parts = []
    # new_parts = []
    # new = []
    # print("리스트 준비")
    # for i in range(100):
    #     if distance(old[i], old[i+1]) > road_li[0][0]/100:
    #         if old[i] in part:
    #             part.append(old[i+1])
    #             if old[i+1] in last_parts:
    #                 pass
    #             else:
    #                 last_parts.append(old[i+1])
    #         else:
    #             parts.append(part)
    #             part=[]
    #             new_parts.append([old[i]])
    #             part.append(old[i])
    #             part.append(old[i+1])
    #             last_parts.append(old[i+1])
    #     else:
    #         pass
    # parts.pop(0)
    # last_parts.pop(-1)
    # print("평균이하 색출")
    # print("유전자 조작중...")
    # for n in range(len(new_parts)):
    #     adding_li = new_parts[n]
    #     print("추가할 리스트",adding_li)
    #     add = False
    #     standardot = adding_li[0]
    #     while add == False:
    #         print(len(adding_li),len(parts[n]))
    #         if len(adding_li) == len(parts[n]):
    #             new.append(adding_li)
    #             print("new에 추가",new)
    #             print("parts",parts)
    #             add = True
    #         else:
    #             find = False
    #             standard = 1
    #             while find == False: 
    #                 for lpart in last_parts:
    #                     if distance(standardot,lpart)> 0 and distance(standardot,lpart) <= standard:
    #                         print(lpart)
    #                         adding_li.append(lpart)
    #                         print("뽑힘",last_parts.pop(last_parts.index(lpart)))
    #                         standardot = lpart
    #                         find = True
    #                         break
    #                     else:
    #                         standard += 1
                    
    #             print(standard)
    new = []
    for i in range(101):
        if random.random() < 0.02:
            new.append(road_li[1][1][i])
        else:
            new.append(road_li[0][1][i])


    dis = 0
    for u in range(100):
        d = distance(new[u],new[u+1])
        dis += d
        # print(dis)
    print('up의 길이',dis)
    print("업그레이드?", bool(dis<road_li[0][0]) )
    road_li.append([dis,new])
    dots = make_gene()
    road_li.append(sort_gene(dots))
    order_li = []
    for i in range(101):
        order_li.append(road_li[0][1][i][0])
    print(order_li)
    time += 1
    # ===================================================


    # dots = []
    # f = open('building.csv','r')
    # rdr = csv.reader(f)
    # dots.append((0,0))
    # for line in rdr:
    #     x = int(line[0])
    #     y = int(line[1])
    #     dots.append((x,y))
    # dots.append((0,0))
    # f.close()

    # print(len(order_li))
    # y_li = []
    # x_li = []
    # for order in order_li:
    #     x_li.append(dots[order][0])
    #     y_li.append(dots[order][1])


    # plt.figure() # marker 인자를 같이 적는다.
    # plt.plot(x_li, y_li, marker='o') 
    # plt.show()
    # plt.close()
