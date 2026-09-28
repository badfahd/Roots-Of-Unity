import numpy as np
import matplotlib.pyplot as h
def plot_roots_of_unity(n):
    k=np.arange(n)
    angles = 2*np.pi*k / n
    roots=np.exp(1j*angles)
    x=roots.real
    y=roots.imag
    x_polygon=np.append(x,x[0])
    y_polygon=np.append(y,y[0])
    h.figure(figsize=(7,7))
    circle_angles=np.linspace(0,2*np.pi,200)
    h.plot(np.cos(circle_angles),np.sin(circle_angles),'k--',label='Unit Circle')
    h.plot(x_polygon,y_polygon,'b--',label=f'{n}-gon')
    h.scatter(x,y,color='red',s=50,zorder=5,label='roots')
    for i, (rx, ry, angle) in enumerate(zip(x, y, angles)):
        
            h.plot([0, rx], [0, ry], 'g:', alpha=0.5)
        
        
            offset_x = 0.18 * np.cos(angle)
            offset_y = 0.18 * np.sin(angle)
        
        
            if i == 0:
             label_text = "1"
            else:
                label_text = f"$e^{{i \\frac{{2\\pi({i})}}{{{n}}}}}$"
            
            h.text(rx + offset_x, ry + offset_y, label_text, 
                 fontsize=10, ha='center', va='center', color='darkblue')
        
    
    h.axhline(0, color='gray', linewidth=0.8)
    h.axvline(0, color='gray', linewidth=0.8)
    h.gca().set_aspect('equal')
    h.xlim(-1.5,1.5)
    h.ylim(-1.5,1.5)
    h.title(f"{n}-th Roots Of Unity($z^{{{n}}}=1$)")
    h.xlabel("Re(z)")
    h.ylabel("Im(z)")
    h.grid(True,linestyle=':',alpha=0.6)
    h.legend(loc='upper right')
    h.tight_layout()
    h.show()
    
    
    

plot_roots_of_unity(8)

