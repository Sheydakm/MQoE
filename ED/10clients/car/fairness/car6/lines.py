from datetime import datetime,timedelta
import datetime as dt
import time
dict_couple={}
lines = open('DASH_CLIENT_LOG_basic_2020-03-07.20_53_49.log', 'r').read().splitlines()
print("start")
for i, line in enumerate(lines):
	if "BASIC: Downloaded segment" in line:
		temp = lines[i].split(" ")[1]
		#print(temp)
		key = datetime.strptime(temp, '%H:%M:%S,%f').time()
		#print(key)
		value=(lines[i].split("bunny_")[1].split("bps")[0])
		dict_couple[key]=value
		#print(lines[i])
print(dict_couple)

first = list(dict_couple.keys())[0]
#first = datetime.strptime(first_str, '%H:%M:%S,%f').time()
print("first=",first)

last = list(dict_couple.keys())[-1]
#last = datetime.strptime(last_str, '%H:%M:%S,%f').time()
print("last=",last)


wnd=[]
while(first <= last):
	wnd.append(first)
	delta=timedelta(seconds=10)
	#print(delta)
	temp=(dt.datetime.combine(dt.date(1,1,1),first) + delta) .time()
	#print(temp)
	#temp = first + timedelta(minutes=5)
	#temp = first + timedelta(hours=5).time() # days, seconds, then other fields.
	if temp > last:
		break
	first=temp
	print(first)
print(wnd)



wnd_items=[]
for i in range(len(wnd)):
	items=[]
	for (key, value) in dict_couple.items():
		if i+1 >= len(wnd):
			break
		if key >= wnd[i] and  key < wnd[i+1]:
			print(dict_couple[key])
			items.append(dict_couple[key])
		#print(items)
	#temp=items
	wnd_items.append(items)
	print("************************")
	#wnd_items.append(items)
#print("**********************************")
print(wnd_items)



print("QoE1")
for j in wnd_items:
	cnt=0
	for k in range(len(j)):
		if k+1>=len(j):
			break
		if j[k]!=j[k+1]:
			cnt=cnt+1
	print("switching:",cnt)
	m=list(map(int, j))
	if len(j)==0:
		print("ave_bitrate: 0")
	else:
		print("ave_bitrate:",sum(m)/len(j))

print("\n")

print("QoE2")








