# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 00:03:15 2019

@author: aleal
"""
#from sklearn import datasets  
#import pandas as pd
#iris = datasets.load_iris()
#x = pd.DataFrame(iris['data'],columns=iris['feature_names'])
#print(x)
import pickle
import numpy as np
np.set_printoptions(threshold=np.inf)
#with open("C:\\Users\\aleal\\OneDrive\\桌面\\MLGame-master\\MLGame-master\\games\\arkanoid\\log\\2019-09-26_00-42-06.pickle", 'rb") as f1:
 #   data_list1 = pickle.load(f1)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-07_19-58-24.pickle", "rb") as f1:
    data_list1 = pickle.load(f1)
    #print(data_list1[0])
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-07_19-57-39.pickle", "rb") as f2:
    data_list2 = pickle.load(f2)
   # print(data_list2[0])

with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-07_19-56-45.pickle", "rb") as f3:
    data_list3 = pickle.load(f3)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-07_19-52-41.pickle", "rb") as f4:
    data_list4 = pickle.load(f4)  
    
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-07_19-51-49.pickle", "rb") as f5:
    data_list5 = pickle.load(f5)
    #print(data_list1[0])
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-07_19-50-57.pickle", "rb") as f6:
    data_list6 = pickle.load(f6)
   # print(data_list2[0])
   
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-07_19-38-46.pickle", "rb") as f7:
    data_list7 = pickle.load(f7)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-07_19-37-54.pickle", "rb") as f8:
    data_list8 = pickle.load(f8)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-07_19-37-02.pickle", "rb") as f9:
    data_list9 = pickle.load(f9)

with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-07_19-35-56.pickle", "rb") as f10:
    data_list10 = pickle.load(f10)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-07_19-35-13.pickle", "rb") as f11:
    data_list11 = pickle.load(f11)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-07_19-34-22.pickle", "rb") as f12:
    data_list12 = pickle.load(f12)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-07_19-29-34.pickle", "rb") as f13:
    data_list13 = pickle.load(f13)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-07_19-28-50.pickle", "rb") as f14:
    data_list14 = pickle.load(f14)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-07_19-27-56.pickle", "rb") as f15:
    data_list15 = pickle.load(f15)

with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-07_19-26-55.pickle", "rb") as f16:
    data_list16 = pickle.load(f16)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-07_19-26-01.pickle", "rb") as f17:
    data_list17 = pickle.load(f17)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-07_19-25-10.pickle", "rb") as f18:
    data_list18 = pickle.load(f18)

with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-08_00-12-38.pickle", "rb") as f19:
    data_list19 = pickle.load(f19)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-06_22-46-43.pickle", "rb") as f20:
    data_list20 = pickle.load(f20)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-06_22-47-34.pickle", "rb") as f21:
    data_list21 = pickle.load(f21)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_10-38-46.pickle", "rb") as f22:
    data_list22 = pickle.load(f22)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_10-35-20.pickle", "rb") as f23:
    data_list23 = pickle.load(f23)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_10-34-23.pickle", "rb") as f24:
    data_list24 = pickle.load(f24)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_10-33-26.pickle", "rb") as f25:
    data_list25 = pickle.load(f25)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_10-32-20.pickle", "rb") as f26:
    data_list26 = pickle.load(f26)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_10-31-34.pickle", "rb") as f27:
    data_list27 = pickle.load(f27)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_10-42-19.pickle", "rb") as f28:
    data_list28 = pickle.load(f28)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_10-41-50.pickle", "rb") as f29:
    data_list29 = pickle.load(f29)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_10-42-19.pickle", "rb") as f30:
    data_list30 = pickle.load(f30)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_10-48-07.pickle", "rb") as f31:
    data_list31 = pickle.load(f31)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_10-57-26.pickle", "rb") as f32:
    data_list32 = pickle.load(f32)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_10-58-22.pickle", "rb") as f33:
    data_list33 = pickle.load(f33)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_10-59-19.pickle", "rb") as f34:
    data_list34 = pickle.load(f34)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_11-00-25.pickle", "rb") as f35:
    data_list35 = pickle.load(f35)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_11-01-21.pickle", "rb") as f36:
    data_list36 = pickle.load(f36)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_11-02-15.pickle", "rb") as f37:
    data_list37 = pickle.load(f37)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_11-07-49.pickle", "rb") as f38:
    data_list38 = pickle.load(f38)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_11-08-46.pickle", "rb") as f39:
    data_list39 = pickle.load(f39)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_11-09-43.pickle", "rb") as f40:
    data_list40 = pickle.load(f40)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_11-12-02.pickle", "rb") as f41:
    data_list41 = pickle.load(f41)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_11-12-49.pickle", "rb") as f42:
    data_list42 = pickle.load(f42)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_11-13-46.pickle", "rb") as f43:
    data_list43 = pickle.load(f43)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_11-23-39.pickle", "rb") as f44:
    data_list44 = pickle.load(f44)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_11-37-15.pickle", "rb") as f45:
    data_list45 = pickle.load(f45)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_11-41-36.pickle", "rb") as f46:
    data_list46 = pickle.load(f46)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_11-40-39.pickle", "rb") as f47:
    data_list47 = pickle.load(f47)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_11-58-23.pickle", "rb") as f48:
    data_list48 = pickle.load(f48)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_11-57-26.pickle", "rb") as f49:
    data_list49 = pickle.load(f49)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_11-56-30.pickle", "rb") as f50:
    data_list50 = pickle.load(f50)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_12-06-44.pickle", "rb") as f51:
    data_list51 = pickle.load(f51)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_12-05-40.pickle", "rb") as f52:
    data_list52 = pickle.load(f52)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_15-06-13.pickle", "rb") as f53:
    data_list53 = pickle.load(f53)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_15-07-03.pickle", "rb") as f54:
    data_list54 = pickle.load(f54)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_15-07-45.pickle", "rb") as f55:
    data_list55 = pickle.load(f55)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_15-08-49.pickle", "rb") as f56:
    data_list56 = pickle.load(f56)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_15-09-39.pickle", "rb") as f57:
    data_list57 = pickle.load(f57)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_15-10-29.pickle", "rb") as f58:
    data_list58 = pickle.load(f58)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_15-08-49.pickle", "rb") as f59:
    data_list59 = pickle.load(f59)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_15-09-39.pickle", "rb") as f60:
    data_list60 = pickle.load(f60)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_15-10-29.pickle", "rb") as f61:
    data_list61 = pickle.load(f61)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_15-36-06.pickle", "rb") as f62:
    data_list62 = pickle.load(f62)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_15-36-56.pickle", "rb") as f63:
    data_list63 = pickle.load(f63)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_15-37-46.pickle", "rb") as f64:
    data_list64 = pickle.load(f64)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_15-36-06.pickle", "rb") as f65:
    data_list65 = pickle.load(f65)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_15-36-56.pickle", "rb") as f66:
    data_list66 = pickle.load(f66)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_15-37-46.pickle", "rb") as f67:
    data_list67 = pickle.load(f67)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_15-36-06.pickle", "rb") as f68:
    data_list68 = pickle.load(f68)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_15-36-56.pickle", "rb") as f69:
    data_list69 = pickle.load(f69)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_15-37-46.pickle", "rb") as f70:
    data_list70 = pickle.load(f70)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_17-04-54.pickle", "rb") as f71:
    data_list71 = pickle.load(f71)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_17-09-26.pickle", "rb") as f72:
    data_list72 = pickle.load(f72)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_17-11-17.pickle", "rb") as f73:
    data_list73 = pickle.load(f73)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_17-22-50.pickle", "rb") as f74:
    data_list74 = pickle.load(f74)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_17-22-00.pickle", "rb") as f75:
    data_list75 = pickle.load(f75)
with open("C:\\Users\\uers\\Desktop\\MLGame-master\\games\\pingpong\\log\\2019-12-09_17-21-10.pickle", "rb") as f76:
    data_list76 = pickle.load(f76)
Frame=[]
Status=[]
Ballposition=[]
PlatformPosition=[]
#Bricks=[]
for ai in range(0 , 3):
    for i in range(0 , len(data_list1)):
        Frame.append(data_list1[i].frame)
        Status.append(data_list1[i].status)
        Ballposition.append(data_list1[i].ball)
        PlatformPosition.append(data_list1[i].platform_1P)
    for i in range(0 , len(data_list2)):
        Frame.append(data_list2[i].frame)
        Status.append(data_list2[i].status)
        Ballposition.append(data_list2[i].ball)
        PlatformPosition.append(data_list2[i].platform_1P)
        
    for i in range(0 , len(data_list3)):
        Frame.append(data_list3[i].frame)
        Status.append(data_list3[i].status)
        Ballposition.append(data_list3[i].ball)
        PlatformPosition.append(data_list3[i].platform_1P)

    for i in range(0 , len(data_list4)):
        Frame.append(data_list4[i].frame)
        Status.append(data_list4[i].status)
        Ballposition.append(data_list4[i].ball)
        PlatformPosition.append(data_list4[i].platform_1P)        
    for i in range(0 , len(data_list5)):
        Frame.append(data_list5[i].frame)
        Status.append(data_list5[i].status)
        Ballposition.append(data_list5[i].ball)
        PlatformPosition.append(data_list5[i].platform_1P)
        
    for i in range(0 , len(data_list6)):
        Frame.append(data_list6[i].frame)
        Status.append(data_list6[i].status)
        Ballposition.append(data_list6[i].ball)
        PlatformPosition.append(data_list6[i].platform_1P)
    
    for i in range(0 , len(data_list7)):
        Frame.append(data_list7[i].frame)
        Status.append(data_list7[i].status)
        Ballposition.append(data_list7[i].ball)
        PlatformPosition.append(data_list7[i].platform_1P)
    for i in range(0 , len(data_list8)):
        Frame.append(data_list8[i].frame)
        Status.append(data_list8[i].status)
        Ballposition.append(data_list8[i].ball)
        PlatformPosition.append(data_list8[i].platform_1P)
    for i in range(0 , len(data_list9)):
        Frame.append(data_list9[i].frame)
        Status.append(data_list9[i].status)
        Ballposition.append(data_list9[i].ball)
        PlatformPosition.append(data_list9[i].platform_1P)
    for i in range(0 , len(data_list10)):
        Frame.append(data_list10[i].frame)
        Status.append(data_list10[i].status)
        Ballposition.append(data_list10[i].ball)
        PlatformPosition.append(data_list10[i].platform_1P)
    for i in range(0 , len(data_list11)):
        Frame.append(data_list11[i].frame)
        Status.append(data_list11[i].status)
        Ballposition.append(data_list11[i].ball)
        PlatformPosition.append(data_list11[i].platform_1P)
    for i in range(0 , len(data_list12)):
        Frame.append(data_list12[i].frame)
        Status.append(data_list12[i].status)
        Ballposition.append(data_list12[i].ball)
        PlatformPosition.append(data_list12[i].platform_1P)
    for i in range(0 , len(data_list13)):
        Frame.append(data_list13[i].frame)
        Status.append(data_list13[i].status)
        Ballposition.append(data_list13[i].ball)
        PlatformPosition.append(data_list13[i].platform_1P)
    for i in range(0 , len(data_list14)):
        Frame.append(data_list14[i].frame)
        Status.append(data_list14[i].status)
        Ballposition.append(data_list14[i].ball)
        PlatformPosition.append(data_list14[i].platform_1P)
    for i in range(0 , len(data_list15)):
        Frame.append(data_list15[i].frame)
        Status.append(data_list15[i].status)
        Ballposition.append(data_list15[i].ball)
        PlatformPosition.append(data_list15[i].platform_1P)

    for i in range(0 , len(data_list16)):
        Frame.append(data_list16[i].frame)
        Status.append(data_list16[i].status)
        Ballposition.append(data_list16[i].ball)
        PlatformPosition.append(data_list16[i].platform_1P)
    for i in range(0 , len(data_list17)):
        Frame.append(data_list17[i].frame)
        Status.append(data_list17[i].status)
        Ballposition.append(data_list17[i].ball)
        PlatformPosition.append(data_list17[i].platform_1P)
    for i in range(0 , len(data_list18)):
        Frame.append(data_list18[i].frame)
        Status.append(data_list18[i].status)
        Ballposition.append(data_list18[i].ball)
        PlatformPosition.append(data_list18[i].platform_1P)

    for i in range(0 , len(data_list19)):
        Frame.append(data_list19[i].frame)
        Status.append(data_list19[i].status)
        Ballposition.append(data_list19[i].ball)
        PlatformPosition.append(data_list19[i].platform_1P)
    for i in range(0 , len(data_list20)):
        Frame.append(data_list20[i].frame)
        Status.append(data_list20[i].status)
        Ballposition.append(data_list20[i].ball)
        PlatformPosition.append(data_list20[i].platform_1P)
    for i in range(0 , len(data_list21)):
        Frame.append(data_list21[i].frame)
        Status.append(data_list21[i].status)
        Ballposition.append(data_list21[i].ball)
        PlatformPosition.append(data_list21[i].platform_1P)
    for i in range(0 , len(data_list22)):
        Frame.append(data_list22[i].frame)
        Status.append(data_list22[i].status)
        Ballposition.append(data_list22[i].ball)
        PlatformPosition.append(data_list22[i].platform_1P)
    for i in range(0 , len(data_list23)):
        Frame.append(data_list23[i].frame)
        Status.append(data_list23[i].status)
        Ballposition.append(data_list23[i].ball)
        PlatformPosition.append(data_list23[i].platform_1P)
    for i in range(0 , len(data_list24)):
        Frame.append(data_list24[i].frame)
        Status.append(data_list24[i].status)
        Ballposition.append(data_list24[i].ball)
        PlatformPosition.append(data_list24[i].platform_1P)
    for i in range(0 , len(data_list25)):
        Frame.append(data_list25[i].frame)
        Status.append(data_list25[i].status)
        Ballposition.append(data_list25[i].ball)
        PlatformPosition.append(data_list25[i].platform_1P)
    for i in range(0 , len(data_list26)):
        Frame.append(data_list26[i].frame)
        Status.append(data_list26[i].status)
        Ballposition.append(data_list26[i].ball)
        PlatformPosition.append(data_list26[i].platform_1P)
    for i in range(0 , len(data_list27)):
        Frame.append(data_list27[i].frame)
        Status.append(data_list27[i].status)
        Ballposition.append(data_list27[i].ball)
        PlatformPosition.append(data_list27[i].platform_1P)
    for i in range(0 , len(data_list28)): 
        Frame.append(data_list28[i].frame)
        Status.append(data_list28[i].status)
        Ballposition.append(data_list28[i].ball)
        PlatformPosition.append(data_list28[i].platform_1P)

    for i in range(0 , len(data_list29)):
        Frame.append(data_list29[i].frame)
        Status.append(data_list29[i].status)
        Ballposition.append(data_list29[i].ball)
        PlatformPosition.append(data_list29[i].platform_1P)
    for i in range(0 , len(data_list30)):
        Frame.append(data_list30[i].frame)
        Status.append(data_list30[i].status)
        Ballposition.append(data_list30[i].ball)
        PlatformPosition.append(data_list30[i].platform_1P)
    for i in range(0 , len(data_list31)):
        Frame.append(data_list31[i].frame)
        Status.append(data_list31[i].status)
        Ballposition.append(data_list31[i].ball)
        PlatformPosition.append(data_list31[i].platform_1P)
    for i in range(0 , len(data_list32)):
        Frame.append(data_list32[i].frame)
        Status.append(data_list32[i].status)
        Ballposition.append(data_list32[i].ball)
        PlatformPosition.append(data_list32[i].platform_1P)
    for i in range(0 , len(data_list33)):
        Frame.append(data_list33[i].frame)
        Status.append(data_list33[i].status)
        Ballposition.append(data_list33[i].ball)
        PlatformPosition.append(data_list33[i].platform_1P)
    for i in range(0 , len(data_list34)):
        Frame.append(data_list34[i].frame)
        Status.append(data_list34[i].status)
        Ballposition.append(data_list34[i].ball)
        PlatformPosition.append(data_list34[i].platform_1P)
    for i in range(0 , len(data_list35)):
        Frame.append(data_list35[i].frame)
        Status.append(data_list35[i].status)
        Ballposition.append(data_list35[i].ball)
        PlatformPosition.append(data_list35[i].platform_1P)
    for i in range(0 , len(data_list36)):
        Frame.append(data_list36[i].frame)
        Status.append(data_list36[i].status)
        Ballposition.append(data_list36[i].ball)
        PlatformPosition.append(data_list36[i].platform_1P)
    for i in range(0 , len(data_list37)):
        Frame.append(data_list37[i].frame)
        Status.append(data_list37[i].status)
        Ballposition.append(data_list37[i].ball)
        PlatformPosition.append(data_list37[i].platform_1P)
    for i in range(0 , len(data_list38)):
        Frame.append(data_list38[i].frame)
        Status.append(data_list38[i].status)
        Ballposition.append(data_list38[i].ball)
        PlatformPosition.append(data_list38[i].platform_1P)
    for i in range(0 , len(data_list39)):
        Frame.append(data_list39[i].frame)
        Status.append(data_list39[i].status)
        Ballposition.append(data_list39[i].ball)
        PlatformPosition.append(data_list39[i].platform_1P)
    for i in range(0 , len(data_list40)):
        Frame.append(data_list40[i].frame)
        Status.append(data_list40[i].status)
        Ballposition.append(data_list40[i].ball)
        PlatformPosition.append(data_list40[i].platform_1P)
 9 +99   +
    for i in range(0 , len(data_list41)):
        Frame.append(data_list41[i].frame)
        Status.append(data_list41[i].status)
        Ballposition.append(data_list41[i].ball)
        PlatformPosition.append(data_list41[i].platform_1P)
    for i in range(0 , len(data_list42)):
        Frame.append(data_list42[i].frame)
        Status.append(data_list42[i].status)
        Ballposition.append(data_list42[i].ball)
        PlatformPosition.append(data_list42[i].platform_1P)
    for i in range(0 , len(data_list43)):
        Frame.append(data_list43[i].frame)
        Status.append(data_list43[i].status)
        Ballposition.append(data_list43[i].ball)
        PlatformPosition.append(data_list44[i].platform_1P)
    for i in range(0 , len(data_list60)):
        Frame.append(data_list60[i].frame)
        Status.append(data_list60[i].status)   
        Ballposition.append(data_list60[i].ball)
        PlatformPosition.append(data_list60[i].platform_1P)
    for i in range(0 , len(data_list61)):
        Frame.append(data_list61[i].frame)
        Status.append(data_list61[i].status)   
        Ballposition.append(data_list61[i].ball)
        PlatformPosition.append(data_list61[i].platform_1P)
    for i in range(0 , len(data_list63)):
        Frame.append(data_list63[i].frame)
        Status.append(data_list63[i].status)   
        Ballposition.append(data_list63[i].ball)
        PlatformPosition.append(data_list63[i].platform_1P)
    for i in range(0 , len(data_list64)):
        Frame.append(data_list64[i].frame)
        Status.append(data_list64[i].status)   
        Ballposition.append(data_list64[i].ball)
        PlatformPosition.append(data_list64[i].platform_1P)
    for i in range(0 , len(data_list65)):
        Frame.append(data_list65[i].frame)
        Status.append(data_list65[i].status)   
        Ballposition.append(data_list65[i].ball)
        PlatformPosition.append(data_list65[i].platform_1P)
    for i in range(0 , len(data_list66)):
        Frame.append(data_list66[i].frame)
        Status.append(data_list66[i].status)   
        Ballposition.append(data_list66[i].ball)
        PlatformPosition.append(data_list66[i].platform_1P)
    for i in range(0 , len(data_list67)):
        Frame.append(data_list67[i].frame)
        Status.append(data_list67[i].status)   
        Ballposition.append(data_list67[i].ball)
        PlatformPosition.append(data_list67[i].platform_1P)
    for i in range(0 , len(data_list68)):
        Frame.append(data_list68[i].frame)
        Status.append(data_list68[i].status)   
        Ballposition.append(data_list68[i].ball)
        PlatformPosition.append(data_list68[i].platform_1P)
    for i in range(0 , len(data_list69)):
        Frame.append(data_list69[i].frame)
        Status.append(data_list69[i].status)   
        Ballposition.append(data_list69[i].ball)
        PlatformPosition.append(data_list69[i].platform_1P)
    for i in range(0 , len(data_list70)):
        Frame.append(data_list70[i].frame)
        Status.append(data_list70[i].status)   
        Ballposition.append(data_list70[i].ball)
        PlatformPosition.append(data_list70[i].platform_1P)
    for i in range(0 , len(data_list44)):
        Frame.append(data_list44[i].frame)
        Status.append(data_list44[i].status)   
        Ballposition.append(data_list44[i].ball)
        PlatformPosition.append(data_list44[i].platform_1P)
    for i in range(0 , len(data_list45)):
        Frame.append(data_list45[i].frame)
        Status.append(data_list45[i].status)   
        Ballposition.append(data_list45[i].ball)
        PlatformPosition.append(data_list45[i].platform_1P)
    for i in range(0 , len(data_list46)):
        Frame.append(data_list46[i].frame)
        Status.append(data_list46[i].status)   
        Ballposition.append(data_list46[i].ball)
        PlatformPosition.append(data_list46[i].platform_1P)
    for i in range(0 , len(data_list47)):
        Frame.append(data_list47[i].frame)
        Status.append(data_list47[i].status)   
        Ballposition.append(data_list47[i].ball)
        PlatformPosition.append(data_list47[i].platform_1P)
    for i in range(0 , len(data_list48)):
        Frame.append(data_list48[i].frame)
        Status.append(data_list48[i].status)   
        Ballposition.append(data_list48[i].ball)
        PlatformPosition.append(data_list48[i].platform_1P)
    for i in range(0 , len(data_list49)):
        Frame.append(data_list49[i].frame)
        Status.append(data_list49[i].status)   
        Ballposition.append(data_list49[i].ball)
        PlatformPosition.append(data_list49[i].platform_1P)

    for i in range(0 , len(data_list50)):
        Frame.append(data_list50[i].frame)
        Status.append(data_list50[i].status)   
        Ballposition.append(data_list50[i].ball)
        PlatformPosition.append(data_list50[i].platform_1P)
    for i in range(0 , len(data_list51)):
        Frame.append(data_list51[i].frame)
        Status.append(data_list51[i].status)   
        Ballposition.append(data_list51[i].ball)
        PlatformPosition.append(data_list51[i].platform_1P)
    for i in range(0 , len(data_list53)):
        Frame.append(data_list53[i].frame)
        Status.append(data_list53[i].status)   
        Ballposition.append(data_list53[i].ball)
        PlatformPosition.append(data_list53[i].platform_1P)
    for i in range(0 , len(data_list54)):
        Frame.append(data_list54[i].frame)
        Status.append(data_list54[i].status)   
        Ballposition.append(data_list54[i].ball)
        PlatformPosition.append(data_list54[i].platform_1P)

    for i in range(0 , len(data_list55)):
        Frame.append(data_list55[i].frame)
        Status.append(data_list55[i].status)   
        Ballposition.append(data_list55[i].ball)
        PlatformPosition.append(data_list55[i].platform_1P)
    for i in range(0 , len(data_list56)):
        Frame.append(data_list56[i].frame)
        Status.append(data_list56[i].status)   
        Ballposition.append(data_list56[i].ball)
        PlatformPosition.append(data_list56[i].platform_1P)
    for i in range(0 , len(data_list57)):
        Frame.append(data_list57[i].frame)
        Status.append(data_list57[i].status)   
        Ballposition.append(data_list57[i].ball)
        PlatformPosition.append(data_list57[i].platform_1P)
    for i in range(0 , len(data_list58)):
        Frame.append(data_list58[i].frame)
        Status.append(data_list58[i].status)   
        Ballposition.append(data_list58[i].ball)
        PlatformPosition.append(data_list58[i].platform_1P)
    for i in range(0 , len(data_list52)):
        Frame.append(data_list52[i].frame)
        Status.append(data_list52[i].status)   
        Ballposition.append(data_list52[i].ball)
        PlatformPosition.append(data_list52[i].platform_1P)
    for i in range(0 , len(data_list62)):
        Frame.append(data_list62[i].frame)
        Status.append(data_list62[i].status)   
        Ballposition.append(data_list62[i].ball)
        PlatformPosition.append(data_list62[i].platform_1P)
    for i in range(0 , len(data_list59)):
        Frame.append(data_list59[i].frame)
        Status.append(data_list59[i].status)   
        Ballposition.append(data_list59[i].ball)
        PlatformPosition.append(data_list59[i].platform_1P)
    for i in range(0 , len(data_list71)):
        Frame.append(data_list71[i].frame)
        Status.append(data_list71[i].status)   
        Ballposition.append(data_list71[i].ball)
        PlatformPosition.append(data_list71[i].platform_1P)
    for i in range(0 , len(data_list72)):
        Frame.append(data_list72[i].frame)
        Status.append(data_list72[i].status)   
        Ballposition.append(data_list72[i].ball)
        PlatformPosition.append(data_list72[i].platform_1P)
    for i in range(0 , len(data_list73)):
        Frame.append(data_list73[i].frame)
        Status.append(data_list73[i].status)   
        Ballposition.append(data_list73[i].ball)
        PlatformPosition.append(data_list73[i].platform_1P)
    for i in range(0 , len(data_list73)):
        Frame.append(data_list74[i].frame)
        Status.append(data_list74[i].status)   
        Ballposition.append(data_list74[i].ball)
        PlatformPosition.append(data_list74[i].platform_1P)
    for i in range(0 , len(data_list75)):
        Frame.append(data_list75[i].frame)
        Status.append(data_list75[i].status)   
        Ballposition.append(data_list75[i].ball)
        PlatformPosition.append(data_list75[i].platform_1P)
    for i in range(0 , len(data_list76)):
        Frame.append(data_list76[i].frame)
        Status.append(data_list76[i].status)   
        Ballposition.append(data_list76[i].ball)
        PlatformPosition.append(data_list76[i].platform_1P)

import numpy as np
#/5 每次移動5 [:0]只取x
PlatX=np.array(PlatformPosition)[:,0][:,np.newaxis]
#print(PlatX)
PlatX_next=PlatX[1:,:]
#print(PlatX_next)
PlatY=np.array(PlatformPosition)[:,0][:,np.newaxis]

instruct=(PlatX_next-PlatX[0:len(PlatX_next),0][:,np.newaxis])/5
#print(instruct)

BallX=np.array(Ballposition)[:,0][:,np.newaxis]
#print(PlatX)
BallX_next=BallX[1:,:]
print(len(BallX))
VX=(BallX_next-BallX[0:len(BallX_next),0][:,np.newaxis])

BallY=np.array(Ballposition)[:,1][:,np.newaxis]
#print(PlatX)
BallY_next=BallY[1:,:]
print(len(BallX))
VY=(BallY_next-BallY[0:len(BallY_next),0][:,np.newaxis])

#不取最後一個
Ballarray=np.array(Ballposition)[:-1]
print(len(Ballarray))
#特徵X
#x=np.hstack((Ballarray, PlatX[0:-1,0][:,np.newaxis],PlatY[0:-1,0][:,np.newaxis],VX,VY))
#特徵球x、y 平板x 球vx vy
x=np.hstack((Ballarray, PlatX[0:-1,0][:,np.newaxis],VX,VY))
print(len(PlatX[0:-1,0][:,np.newaxis])) 
print(x)
y=instruct

 
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.7, random_state=999)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)

yknn_bef_scaler=knn.predict(x_test) 
acc_knn_bef_scaler=accuracy_score(yknn_bef_scaler,y_test)
print(acc_knn_bef_scaler)
#print(acc_knn_bef_scaler)

#from sklearn.preprocessing import StandardScaler
#scaler=StandardScaler()
#scaler.fit(x_train)
#x_train_stdnorm=scaler.transform(x_train)
#knn.fit(x_train_stdnorm,y_train)
#x_test_standorm=scaler.transform(x_test)
#yknn_aft_scaler=svm.predict(x_test_standorm)
#acc_knn_aft_scaler=accuracy_score(yknn_aft_scaler, y_test)

filename ="C:/Users/uers/Desktop/MLGame-master/knn_ex1.sav"
pickle.dump(knn,open(filename, 'wb'))










