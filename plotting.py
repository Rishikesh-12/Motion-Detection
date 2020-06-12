from main import df
from bokeh.plotting import  figure, show, output_file

p=figure(x_axis_type='datetime',height=300, width=500,title="Motion Graph")
p.yaxis.minor_tick_line_color=None
# p.ygrid[0].ticker.desired_num_ticks=1


q=p.quad(left=df["Start"],right=df["End"],bottom=0,top=1,color="orange")
output_file=("Log.html")

show(p)