# A test of flatness that uses no positions: only the hop lengths a_x, a_y at each place (hop strength = 1/length), in two dimensions.
# Matter's step H = sum_i (1/a_i) sigma_i sin k_i has E^2 = sum_i (k_i/a_i)^2: the hops along x and y are at right angles, so the geometry is
# ds^2 = a_x^2 dx^2 + a_y^2 dy^2 and Gauss's curvature is  K = -(1/(a_x a_y)) [ d_x( d_x a_y / a_x ) + d_y( d_y a_x / a_y ) ],
# taken here with differences between neighbouring places. Flat means K = 0 at every place.
import numpy as np
L=64; x,y=np.meshgrid(np.arange(L)-L/2,np.arange(L)-L/2,indexing='ij'); eps=0.1
def K(ax,ay):
    fx=lambda f:np.roll(f,-1,0)-f; bx=lambda f:f-np.roll(f,1,0); fy=lambda f:np.roll(f,-1,1)-f; by=lambda f:f-np.roll(f,1,1)   # forward, then backward: one hop wide
    mx=lambda f:(f+np.roll(f,-1,0))/2; my=lambda f:(f+np.roll(f,-1,1))/2
    k=-(bx(fx(ay)/mx(ax))+by(fy(ax)/my(ay)))/(ax*ay); return k[4:-4,4:-4]      # edges dropped (the patterns below are not periodic)
z=(x+1j*y)/L
cases={
 "even grid":(np.ones((L,L)),np.ones((L,L))),
 "flat, redrawn by a smooth map (a = |1 + eps z|)":(abs(1+eps*z),abs(1+eps*z)),
 "flat, redrawn as a fan (a_x = 1, a_y = 1 + eps x/L)":(np.ones((L,L)),1+eps*x/L),
 "curved, a bowl (a = 1 + eps (x^2 + y^2)/L^2)":(1+eps*(x**2+y**2)/L**2,)*2,
 "curved, a ripple (a = 1 + eps sin(2 pi x/16) sin(2 pi y/16))":(1+eps*np.sin(2*np.pi*x/16)*np.sin(2*np.pi*y/16),)*2,
}
rng=np.random.default_rng(1); w=1+eps*rng.standard_normal((L,L)); cases["independent from place to place (eps = 0.1)"]=(w,w)
cases["uneven hop to hop but a relabelling (a_x depends on x only, a_y on y only; eps = 0.1)"]=(np.repeat(1+eps*rng.standard_normal((L,1)),L,1),np.repeat(1+eps*rng.standard_normal((1,L)),L,0))
for nm,(ax,ay) in cases.items():
    k=K(ax,ay); print(f"{nm}: variation of the lengths {max(ax.std(),ay.std()):.3f}; curvature rms {np.sqrt((k**2).mean()):.2e}, largest {abs(k).max():.2e} (per hop^2)")
print("count: lengths of the grid's own links alone, with no angles given, are d numbers per place against d coordinates to place it: for small variations, locally, such lengths can be drawn flat.")
print("the angles carry the rest; matter's step sets them at right angles, so its hop strengths are a full (diagonal) geometry and their curvature is fixed.")
