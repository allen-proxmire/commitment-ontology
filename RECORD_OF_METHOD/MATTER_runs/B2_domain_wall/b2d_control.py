import numpy as np
src=open('b2d_run.py').read().split('res={}')[0]
src=src.replace("p[:,L]=np.cos(eps)*a-1j*np.sin(eps)*b; p[:,0]=np.cos(eps)*b-1j*np.sin(eps)*a",
 "M=(sx+sy+sz)/np.sqrt(3); p[:,L]=np.cos(eps)*a-1j*np.sin(eps)*np.einsum('ij,xjd->xid',M,b); p[:,0]=np.cos(eps)*b-1j*np.sin(eps)*np.einsum('ij,xjd->xid',M,a)")
exec(src)
mc,cc=analyse(16,11,True); print(f"corrected control L=16 m={mc} crossings={cc}", 'informative' if (mc or 0)>=0.03 else 'UNINFORMATIVE')
