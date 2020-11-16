from datetime import datetime,timedelta
import datetime as dt
import time
import statistics
import pandas as pd
import glob, os
from fnmatch import fnmatch
import itertools
import matplotlib.pyplot as plt
import numpy


x=[]
for i in range(20):
	x.append(i+1)


throughput1= [420940.677708/(1000*1000), 425660.448205/(1000*1000), 508929.894984/(1000*1000), 533078.050551/(1000*1000), 528812.54339/(1000*1000), 499278.928951/(1000*1000), 514013.999972/(1000*1000), 522733.128841/(1000*1000), 526656.819967/(1000*1000), 535324.441186/(1000*1000), 557786.078995/(1000*1000), 566237.782517/(1000*1000), 583521.432623/(1000*1000), 556471.839505/(1000*1000), 533869.780376/(1000*1000), 579509.913992/(1000*1000), 539409.999087/(1000*1000)]
throughput2= [881527.844932/(1000*1000), 852473.53383/(1000*1000), 879955.792845/(1000*1000), 867979.247792/(1000*1000), 747393.342739/(1000*1000), 728688.234674/(1000*1000), 695087.600967/(1000*1000), 690383.661105/(1000*1000), 670154.041237/(1000*1000), 590398.750474/(1000*1000), 585994.397002/(1000*1000), 580237.619814/(1000*1000), 602244.520204/(1000*1000), 585637.131085/(1000*1000)]
throughput3= [661134.183962/(1000*1000), 689491.153056/(1000*1000), 638198.686829/(1000*1000), 566538.760562/(1000*1000), 471116.346952/(1000*1000), 466294.428765/(1000*1000), 473107.120936/(1000*1000), 473856.078579/(1000*1000), 450202.561638/(1000*1000), 447202.161985/(1000*1000), 438283.495805/(1000*1000), 427217.418153/(1000*1000), 443442.544593/(1000*1000), 465430.089205/(1000*1000)]
throughput4= [700967.267447/(1000*1000), 645357.014442/(1000*1000), 571416.46314/(1000*1000), 570473.457216/(1000*1000), 529198.846563/(1000*1000), 516449.521394/(1000*1000), 513663.536392/(1000*1000), 499055.801254/(1000*1000), 489701.065519/(1000*1000), 446721.63256/(1000*1000), 454064.341671/(1000*1000), 551523.270547/(1000*1000), 640680.009531/(1000*1000), 625465.288699/(1000*1000), 634147.198867/(1000*1000)]
throughput5= [708210.167686/(1000*1000), 677706.593439/(1000*1000), 630396.00877/(1000*1000), 543045.270261/(1000*1000), 528517.266341/(1000*1000), 505113.809285/(1000*1000), 499072.359154/(1000*1000), 488269.199307/(1000*1000), 470353.920345/(1000*1000), 455663.499519/(1000*1000), 457756.02044/(1000*1000), 467538.051987/(1000*1000), 470395.491235/(1000*1000)]


print("ave:", statistics.mean(throughput1), "median:",statistics.median(throughput1),"std:",statistics.stdev(throughput1), "max:",max(throughput1), "min:",min(throughput1))
print("ave:", statistics.mean(throughput2), "median:",statistics.median(throughput2), "std:",statistics.stdev(throughput2),"max:",max(throughput2), "min:",min(throughput2))
print("ave:", statistics.mean(throughput3), "median:",statistics.median(throughput3), "std:",statistics.stdev(throughput3), "max:",max(throughput3), "min:",min(throughput3))
print("ave:", statistics.mean(throughput4), "median:",statistics.median(throughput4), "std:",statistics.stdev(throughput4),"max:",max(throughput4), "min:",min(throughput4))
print("ave:", statistics.mean(throughput5), "median:",statistics.median(throughput5), "std:",statistics.stdev(throughput5),"max:",max(throughput5), "min:",min(throughput5))

plt.plot(throughput1,color='pink', linestyle=':',linewidth=8)
plt.plot(throughput2,color='lime', linestyle=':',linewidth=8)
plt.plot(throughput3,color='orange',linewidth=4)
plt.plot(throughput4,color='red',linewidth=4)
plt.plot(throughput5,color='yellow',linestyle='--',linewidth=4)
#plt.plot(x,model45,color='orange',linestyle='--',linewidth=2)
#plt.plot(x,model5,color='pink',linewidth=4)
#plt.title('Client and Cache bitrates (5Mbps No Background Traffic)')
plt.ylabel('Throughputs Mbps')
plt.xlabel('8th window')
plt.legend(['Client#1','Client#2','Client#3','Client#4','client#5','Client#5'],prop={'size':8})
plt.savefig('/home/sheyda/Desktop/QoE/5clients/train/throughputs.eps', format='eps', dpi=1000)
plt.show()
