exec(open('g5_free_fall.py').read().split('print("drift check')[0])
_packet=packet
for wd in [60,150,300]:
    packet=lambda th,width=wd: _packet(th,width)
    acc,v0,dx=run(0.1,2e-6)
    print(f"theta=0.1 width={wd}: ratio={acc/(2e-6*c0**2):.4f}")
