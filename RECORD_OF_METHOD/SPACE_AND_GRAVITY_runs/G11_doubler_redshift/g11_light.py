# Control: the same births acting on ordinary light (a packet at k = 0.2).
exec(open('g11_redshift.py').read().split('print("1D band')[0])
exec(open('g11_redshift.py').read().split('print("1D band')[1].split('def grow')[0].split('\n',1)[1])
src=open('g11_redshift.py').read(); g=src[src.index('def grow'):src.index('for rule in')].replace("np.pi-0.2","0.2")
exec(g)
for rule in ["empty","mean"]:
    print(rule,"births, light at k=0.2: (a, mean|k|/pi, weight in |k|<pi/2):",grow(rule))
print("pure stretch: mean|k|/pi =",round(0.2/np.pi,3),"-> /a")
