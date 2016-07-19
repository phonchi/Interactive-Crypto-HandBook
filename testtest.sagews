︠f6a26b43-5ee1-4bf6-ba4e-1a24b79643c7s︠
%hide

html('<h3>Elliptic Curves over the Real Numbers</h3>')

@interact
def _(a = slider([-10..3],default=-4), b = (4,(-10..10))):
    if 4*a^3 + 27*b^2 == 0:
        html('The choice of $a$ = %s and $b$ = %s does not define an elliptic curve because this makes $27a^3 + 4b^2 = 0.$'%(a,b))
    else:
        E = EllipticCurve([a,b])
        s = '$E(\mathbb{R}) = \{ (x,y) \in \mathbb{R} \\times \mathbb{R}\ |\ %s \} \cup \{ \mathcal{O} \}$'%(latex(E))
        html('<font size=5>'+s+'</font>')
        show(plot(E,xmax=3),axes_labels=['x','y'])

html('Figure 3.2 Play around with different values for a and b and note how the curve changes. You can choose a between -10 and <br>3, and b between -10 and 10, because this is the range where you can see something happening. Also note that this program <br>only lets you choose integers for a and b, although real numbers are actually allowed for a curve over the real numbers. This <br>is because real numbers for a and b would make the output ugly.') 
︡bf5d329b-0e80-424d-ae81-0760beacc04e︡{"done":true,"error":"maximum time (=30000ms) exceeded - last error true"}︡
︠7babee1b-7ee1-406e-9aa8-636fab831c08︠









