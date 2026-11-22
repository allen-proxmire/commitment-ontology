# The flatness test in three dimensions, from hop lengths alone: ds^2 = a_1^2 dx_1^2 + a_2^2 dx_2^2 + a_3^2 dx_3^2 (lines at right angles).
# Flat exactly when six expressions vanish at every place (Lame's equations), for (i,j,k) a turn of (1,2,3):
#   S_k = d_i( d_i a_j / a_i ) + d_j( d_j a_i / a_j ) + (d_k a_i)(d_k a_j)/a_k^2          (the curvature of the i-j sheet)
#   M_i = d_j d_k a_i - (d_j a_k)(d_k a_i)/a_k - (d_k a_j)(d_j a_i)/a_j                    (the mixed part)
# Differences one hop wide. Reported: rms over places of the largest of the six, per hop^2.
import numpy as np
L=32; g=np.arange(L)-L/2; x=np.meshgrid(g,g,g,indexing='ij'); eps=0.1
f=lambda u,i:np.roll(u,-1,i)-u; b=lambda u,i:u-np.roll(u,1,i); c=lambda u,i:(np.roll(u,-1,i)-np.roll(u,1,i))/2; m=lambda u,i:(u+np.roll(u,-1,i))/2
def six(a):
    out=[]
    for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
        out.append(b(f(a[j],i)/m(a[i],i),i)+b(f(a[i],j)/m(a[j],j),j)+c(a[i],k)*c(a[j],k)/a[k]**2)
        out.append(c(c(a[i],j),k)-c(a[k],j)*c(a[i],k)/a[k]-c(a[j],k)*c(a[i],j)/a[j])
    s=np.array(out)[:,4:-4,4:-4,4:-4]; return np.sqrt((s**2).mean(axis=(1,2,3))).max()
one=np.ones((L,L,L)); R0=200.0; r=R0+x[0]; th=np.pi/2+x[1]/R0
cen=np.array([3*L,2.5*L,-2*L]); d2=sum((x[i]-cen[i])**2 for i in range(3)); inv=(d2.mean()/d2)
rng=np.random.default_rng(3)
cases={
 "even grid":[one,one,one],
 "flat: a fan (1, 1 + eps x/L, 1)":[one,1+eps*x[0]/L,one],
 "flat: a ball's own lines (1, r/R, r sin(th)/R), far from the centre":[one,r/R0,r*np.sin(th)/R0],
 "flat: turned inside out about a far point (a = c/|x - x0|^2)":[inv,inv,inv],
 "flat: each line relabelled alone, uneven hop to hop by 0.1":[np.ones((L,L,L))*(1+eps*rng.standard_normal(L))[:,None,None],np.ones((L,L,L))*(1+eps*rng.standard_normal(L))[None,:,None],np.ones((L,L,L))*(1+eps*rng.standard_normal(L))[None,None,:]],
 "curved: a bowl (a = 1 + eps |x|^2/L^2)":[1+eps*(x[0]**2+x[1]**2+x[2]**2)/L**2]*3,
 "curved: a ripple 16 hops long":[1+eps*np.sin(2*np.pi*x[0]/16)*np.sin(2*np.pi*x[1]/16)*np.sin(2*np.pi*x[2]/16)]*3,
 "curved: independent from place to place, 0.1":[1+eps*rng.standard_normal((L,L,L))]*3,
}
for nm,a in cases.items(): print(f"{nm}: variation of the lengths {max(u.std() for u in a):.3f}; largest of the six, rms {six(a):.1e}")
