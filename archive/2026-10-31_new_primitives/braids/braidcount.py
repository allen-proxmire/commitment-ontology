import itertools, sys
# Artin action of positive generators on free group F_n (faithful). Letters: x_1..x_n as +i, inverses as -i.
def red(w):
    out=[]
    for c in w:
        if out and out[-1]==-c: out.pop()
        else: out.append(c)
    return tuple(out)
def inv(w): return tuple(-c for c in reversed(w))
def act(word,n):
    # images of x_1..x_n under the braid (apply generators left to right)
    img={i:(i,) for i in range(1,n+1)}
    for g in word:   # sigma_g: x_g -> x_g x_{g+1} x_g^-1, x_{g+1} -> x_g
        new=dict(img)
        a,b=img[g],img[g+1]
        new[g]=red(a+b+inv(a)); new[g+1]=a
        img=new
    return tuple(img[i] for i in range(1,n+1))
def perm(word,n):
    p=list(range(n))
    for g in word:
        i=g-1; p[i],p[i+1]=p[i+1],p[i]
    return p
def one_cycle(p):
    n=len(p); seen=0; x=0
    for _ in range(n):
        x=p[x]; seen+=1
        if x==0: break
    return seen==n
def count(n,L):
    if n==1: return 0
    classes=set(); elems={}
    for w in itertools.product(range(1,n),repeat=L):
        if set(w)!=set(range(1,n)): continue           # unsplittable
        if not one_cycle(perm(w,n)): continue           # one piece
        # primitive as a word-cycle: not a power of a shorter word up to rotation
        prim=True
        for d in range(1,L):
            if L%d==0 and w==w[:d]*(L//d): prim=False;break
        if not prim: continue
        key=min(act(w[i:]+w[:i],n) for i in range(L))   # rotation class, identified by braid element
        classes.add(key)
    return len(classes)
if __name__!="__main__": pass
if __name__=='__main__':
    maxB=int(sys.argv[1]) if __name__=="__main__" else 0
    print("B  " + "  ".join(f"n={n}" for n in range(2,7)))
    for B in range(4,maxB+1):
        row=[]
        for n in range(2,7):
            L=B-n
            row.append(count(n,L) if L>=n-1 else 0)
        best=max(range(len(row)),key=lambda i:row[i])
        print(f"{B:2d} "+"  ".join(f"{c:4d}" for c in row)+f"   max at n={best+2}")
    
    def all_classes(n,L):
        s=set()
        for w in itertools.product(range(1,n),repeat=L):
            s.add(min(act(w[i:]+w[:i],n) for i in range(L)))
        return len(s)
    print("post hoc: share of all patterns at that budget that are self-sustaining")
    for B in (7,9,11,13):
        out=[]
        for n in range(3,7):
            L=B-n
            if L<n-1: out.append('   -  '); continue
            c=count(n,L); a=all_classes(n,L); out.append(f"{c:4d}/{a:<5d}={c/a:.2f}")
        print(B, "  ".join(out))
