from itertools import permutations, combinations
from recommendations import sim_distance
from recommendations import critics
import pandas as pd
from pandas import Series
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import font_manager as fm

def plot_distance(data):
	comb=combinations(data.keys(), 2)
	all_dist={str(p1)+':'+str(p2):sim_distance(data, p1, p2) for p1, p2 in comb}

	S=Series(all_dist)
	S=S.sort_values(ascending=False)

	x_num=np.arange(len(S))
	
	ax=S.plot()
	ax.set_xticks(x_num)
	ax.set_xticklabels(S.index, rotation=90, ha='center', va='top')
	myfont=fm.FontProperties(fname=r'C:\Windows\Fonts\msyh.ttc')
	ax.set_title('共同爱好程度', fontproperties=myfont)
	ax.set_xlabel('相关度', fontproperties=myfont)
	ax.set_xlabel('人物关系', fontproperties=myfont)
	ax.legend(('皮尔逊相关度',), prop=myfont)
	plt.subplots_adjust(bottom=0.5)
	
	return S

if __name__ == '__main__':
        
        plot_distance(critics)
        plt.show()
