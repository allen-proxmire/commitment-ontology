"""Tight count of faces. A loose nucleon has two free sides (top, bottom) and two
flank notches. A closed ring shows four notches and no free side. A weak join is a
side set into a notch; a stacked join (full or weak) uses one side of each.
Search: is there an assignment of joins such that no split crosses a single weak join only?"""
from itertools import combinations, product
def best(pieces):
    n=len(pieces); L=[i for i in range(n) if pieces[i]!='R']
    # options per unordered pair: none, stack (loose-loose), notch a->b, notch b->a
    pairs=list(combinations(range(n),2)); opts=[]
    for i,j in pairs:
        o=['-']
        if pieces[i]!='R' and pieces[j]!='R': o+=['S']
        if pieces[i]!='R': o+=['i>j']
        if pieces[j]!='R': o+=['j>i']
        opts.append(o)
    for ch in product(*opts):
        sides=[0]*n; notch=[0]*n; J={}
        for (i,j),c in zip(pairs,ch):
            if c=='-': continue
            if c=='S':
                sides[i]+=1; sides[j]+=1
                a,b=pieces[i],pieces[j]
                J[(i,j)]='F' if a[0]!=b[0] and a[1]==b[1] else 'W'
            else:
                g,r=(i,j) if c=='i>j' else (j,i)
                sides[g]+=1; notch[r]+=1; J[(i,j)]='W'
        if any(sides[i]>2 for i in L): continue
        if any(notch[i]>(4 if pieces[i]=='R' else 2) for i in range(n)): continue
        ok=True
        for k in range(1,n//2+1):
            for part in combinations(range(n),k):
                cr=[v for (i,j),v in J.items() if (i in part)!=(j in part)]
                if 'F' not in cr and len(cr)<2: ok=False;break
            if not ok: break
        if ok: return True
    return False
P=lambda s:('p',s); N=lambda s:('n',s)
cases={"H-2":[P(1),N(1)],"p-n opposed":[P(1),N(-1)],"2n":[N(1),N(-1)],"He-3":[P(1),P(-1),N(1)],
"He-5":['R',N(1)],"He-6":['R',N(1),N(-1)],"Li-6":['R',P(1),N(1)],"Li-7":['R',P(1),N(1),N(-1)],
"Be-8":['R','R'],"Be-9":['R','R',N(1)],"Be-10":['R','R',N(1),N(-1)],"B-10":['R','R',P(1),N(1)],
"B-11":['R','R',P(1),N(1),N(-1)],"C-12":['R','R','R'],"C-13":['R','R','R',N(1)]}
obs={"H-2":1,"p-n opposed":0,"2n":0,"He-3":1,"He-5":0,"He-6":1,"Li-6":1,"Li-7":1,"Be-8":0,"Be-9":1,"Be-10":1,"B-10":1,"B-11":1,"C-12":1,"C-13":1}
for k,v in cases.items():
    h=best(v); print(f"{k:12} holds {str(h):5} observed {bool(obs[k])!s:5}{'' if h==bool(obs[k]) else '  <-- miss'}")
