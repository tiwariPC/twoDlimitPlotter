from pandas import DataFrame
import pandas as pd
xs = pd.read_csv("cross_section/tanbeta_vs_ma_scan_mA_1200_fixed.csv",delimiter=",")#, names=["mA", "ma", "sintheta", "tanbeta", "xsec"])
ma = xs.ma.unique().tolist()
tb = xs.tanbeta.unique().tolist()
xs["xsec"] = xs.xsec*0.83



#xs[(xs.mA==1200) & (xs.sintheta==0.7) & (xs.tanbeta==35)]

limits = pd.read_csv("limitFiles/limits_bbDM_combined_2017.txt",delimiter=" ", names=["mA","ma","expm2", "expm1", "exp", "expp1", "expp2", "obs"])

limits["tanbeta"] = 35


xs_skim_35 = xs[xs.tanbeta==35]
xs_35=xs_skim_35.set_index(["mA","ma"])

def getlimitdf(tanb=30):
    xs_skim_30 = xs[xs.tanbeta==tanb]
    xs_30=xs_skim_30.set_index(["mA","ma"])
    merged = xs_35.merge(xs_30,left_index=True, right_index=True, how='outer')


    limits_30 = limits
    limits_30["tanbeta"] = tanb
    limits_30["mA"] = 1200
    limits_30 = limits_30.set_index(["mA","ma"])

    final=merged.merge(limits_30, left_index=True, right_index=True, how='outer')
    final_ = final[:-3]
    for ivar in ["expm2","expm1","exp","expp1","expp2","obs"]:
        final_[ivar] = final_[ivar] * final_.xsec_x / final_.xsec_y

    final_ = final_.drop(labels=["sintheta_x" , "tanbeta_x",    "xsec_x",  "sintheta_y",  "tanbeta_y", "xsec_y"], axis=1)
    final_ = final_.reset_index()
    final_= final_.drop(labels=["mA"], axis=1)
    final_ = final_.set_index(["ma","tanbeta"])
    return final_



#df_35 = getlimitdf(35)
#print (df_35)
dfs=[]

for itanb in tb:
    df_tmp = getlimitdf(itanb)
    dfs.append(df_tmp)

df = pd.concat(dfs)

#df_30 = getlimitdf(30)
#print (df_30)
#df= pd.concat([df_35, df_30])

print (df[:5])

df.to_csv("limits_tanb_vs_ma_scan.txt",sep=" ")
