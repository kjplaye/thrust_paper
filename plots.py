from math import sinh, cosh, exp, pi
import pylab
pylab.axes().set_aspect('equal')

sub_u = 'ᵤ'
sub_v = 'ᵥ' 


# Massless shell
"""
pylab.fill([0,1,-1],[0,1,1],color = (0.85,0.85,0.85))
pylab.plot([-1,1],[-1,1],color = 'black')
pylab.plot([-1,1],[1,-1],color = 'black')
pylab.arrow(-1,1,1,-1,color = 'black', linewidth = 5, head_width = 0.1,length_includes_head = True)
pylab.arrow(0,0,1,1,color = 'black', linewidth = 5, head_width = 0.1,length_includes_head = True)
pylab.text(-0.4,-0.7,"Massless",fontsize = "xx-large")
pylab.text(-0.25,-0.85,"Shell",fontsize = "xx-large")
pylab.text(-0.8,0.1, f'p{sub_v} = 0',fontsize = 'xx-large', rotation = -45)
pylab.text(0.3,0.1, f'p{sub_u} = 0',fontsize = 'xx-large', rotation = 45)
pylab.text(-0.4,0.8,f'p{sub_u}, p{sub_v} < 0',fontsize = 'xx-large')
"""

# Rindler wedge W
def plot_xi_contour(xi):
    T = []
    Z = []
    for eta_v in range(-500,500):
        eta = eta_v*0.01
        t = exp(-xi) * sinh(eta)
        z = exp(-xi) * cosh(eta)
        T.append(t)
        Z.append(z)
    pylab.plot(Z,T, color = 'blue')

def plot_eta_contour(eta):
    T = []
    Z = []
    for xi_v in range(-100,2000):
        xi = xi_v*0.01
        t = exp(-xi) * sinh(eta)
        z = exp(-xi) * cosh(eta)
        T.append(t)
        Z.append(z)
    pylab.plot(Z,T, color = 'green')

pylab.axes().set_aspect('equal')
pylab.plot([-1,1],[-1,1],color = 'black')
pylab.plot([-1,1],[1,-1],color = 'black')

for v in range(30):
    xi = v * 0.1 + 2
    plot_xi_contour(xi)

for v in range(30):
    eta = (v-15) * 0.1
    plot_eta_contour(eta)

pylab.ylim([-0.1,0.1])
pylab.xlim([-0.1,0.15])
pylab.text(-0.065,0.05, f'v = 0',fontsize = 30, rotation = -45)
pylab.text(-0.065,-0.055, f'u = 0',fontsize = 30, rotation = 45)


# Contours
"""
pylab.axes().set_aspect('equal')
X = np.array([cos(2*pi*t/4000) for t in range(1000)])
Y = np.array([sin(2*pi*t/4000) for t in range(1000)])
pylab.plot(X,Y,":",color = "black")
pylab.plot(X,-Y,":",color = "black")
pylab.plot(-X,Y,":",color = "white")
pylab.arrow(0,0,0,1,color = 'black', head_width = 0.1, length_includes_head = True)
pylab.arrow(0,0,1,0,color = 'black', head_width = 0.1, length_includes_head = True)
pylab.arrow(0,0,0,-1,color = 'black', head_width = 0.1, length_includes_head = True)
pylab.arrow(1,0.1,0,-0.1,color = 'black', head_width = 0.06, length_includes_head = True)
pylab.arrow(1,-0.1,0,0.1,color = 'black', head_width = 0.06, length_includes_head = True)
pylab.text(0.45,0.05, 's',fontsize = 'xx-large', rotation = 0)
pylab.text(-0.15,0.5, 'L',fontsize = 'xx-large', rotation = 0)
pylab.text(-0.15,-0.5, 'R',fontsize = 'xx-large', rotation = 0)
"""
