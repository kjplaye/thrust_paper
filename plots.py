import pylab
pylab.axes().set_aspect('equal')

sub_u = 'ᵤ'
sub_v = 'ᵥ' 


# Momentum space
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
