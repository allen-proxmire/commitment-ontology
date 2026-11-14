# Scale 4: run past the outer shells' horizon crossings; each shell q crosses its own horizon r = q r_s.
exec(open('g17b.py').read().split("for scale in")[0])
exec(open('g17.py').read().split('if __name__')[0].replace("L=1400;","L=5600;"))
th=0.5; R=2000; edge=80; rs=600.0; tc=(2/3)*R**1.5/np.sqrt(c0**2*rs); T=int(0.93*tc); qs=[0.5,0.7,0.9,0.97]
out=runb(th,R,edge,rs,T,qs); t=np.arange(T+1)
for j,q in enumerate(qs):
    pred=np.maximum(out[0,j]**1.5-1.5*np.sqrt(c0**2*rs*q)*t,0)**(2/3); hz=q*rs
    cm=np.argmax(out[:,j]<hz) if (out[:,j]<hz).any() else None; cp=np.argmax(pred<hz) if (pred<hz).any() else None
    print(f"q={q}: r at t=T ({T}): {out[-1,j]:.0f} (pred {pred[-1]:.0f}); crosses its horizon r={hz:.0f} at t={cm} (pred {cp})")
