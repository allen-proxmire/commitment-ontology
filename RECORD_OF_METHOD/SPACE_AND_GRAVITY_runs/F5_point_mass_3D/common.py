import numpy as np
Lx,Ly,Lz=64,128,64; A=0.05; rc=3.0; Bimp=16; Y0=-56; K0=0.5; sig=6; r=0.5
def mi(d,L): return (d+L/2)%L-L/2
def Phi(x,y,z):   # mass at (-Bimp, 0, 0) relative to the lattice centre; packet starts at (0, Y0, 0); minimum-image distances
    return A/np.sqrt(mi(x+Bimp,Lx)**2+mi(y,Ly)**2+mi(z,Lz)**2+rc**2)
def w(k): return np.sqrt(np.sum(np.sin(k)**2)+(r*np.sum(1-np.cos(k)))**2)
h_=1e-6; VY=(w(np.array([0,K0+h_,0]))-w(np.array([0,K0-h_,0])))/(2*h_); T_FLOW=2*abs(Y0)/VY
