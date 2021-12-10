import matplotlib.ticker as tick

#Show graph
def prof(fig, x, pr, p, prm, strx, stry, strt):
    xd = prm.gxd
    yd = 0.5
    xs = prm.hw - prm.hcs
    xe = prm.hw + prm.hcs
    ys = 0
    ye = 1

    ax = fig.add_subplot(p)
    ax.plot(x, pr, linewidth=2.0, color="black")
    ax.xaxis.set_major_locator(tick.MultipleLocator(xd))
    ax.yaxis.set_major_locator(tick.MultipleLocator(yd))
    ax.tick_params(labelsize=11)
    ax.set_xlim([xs,xe])
    ax.set_ylim([ys,ye])
    ax.set_xlabel(strx, fontsize=11)
    ax.set_ylabel(stry, fontsize=11)
    ax.set_title(strt, fontsize=11)

#Show image
def image(fig,im,p,prm,strx,stry,strt):
    xd = prm.gxd
    yd = prm.gyd
    xs = prm.hw-prm.hcs
    xe = prm.hw+prm.hcs
    ys = prm.hh+prm.hcs
    ye = prm.hh-prm.hcs

    ax = fig.add_subplot(p)
    ax.imshow(im, cmap='gray')
    ax.xaxis.set_major_locator(tick.MultipleLocator(xd))
    ax.yaxis.set_major_locator(tick.MultipleLocator(yd))
    ax.tick_params(labelsize=11)
    ax.set_xlim([xs,xe])
    ax.set_ylim([ys,ye])
    ax.set_xlabel(strx, fontsize=11)
    ax.set_ylabel(stry, fontsize=11)
    ax.set_title(strt, fontsize=11)

#Show graph
def graph(fig,x,y,p,prm,strx,stry,strt):
    xd = prm.itr/5
    yd = 0.2
    xs = 0
    xe = prm.itr
    ys = 0
    ye = 1

    ax = fig.add_subplot(p)
    ax.scatter(x,y,marker="o",c="black", s=20)
    ax.xaxis.set_major_locator(tick.MultipleLocator(xd))
    ax.yaxis.set_major_locator(tick.MultipleLocator(yd))
    ax.tick_params(labelsize=11)
    ax.set_xlim([xs,xe])
    ax.set_ylim([ys,ye])
    ax.set_xlabel(strx, fontsize=11)
    ax.set_ylabel(stry, fontsize=11)
    ax.set_title(strt, fontsize=11)

