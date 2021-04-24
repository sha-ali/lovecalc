import time

def fl(k):
	x = ['Freind','Lover','Angry','Marriage','enemy','sister']
	count = 0
	while x:
		for i in range(len(x)):
			count +=1
			if count == k:
				val = x.pop(i)
				count = 0
				break
	return val

def clr(a):
	temp = []
	for i in a:
		if(i>=10):
			x = int(i /10)
			temp.append(x)
			y = int(i%10)
			temp.append(y)
		else:
			temp.append(i)
	a = temp
	a.sort(reverse = True)
	if(len(a)==2):
		too(a)
	else:
		calc(a) 
		
 
def too(a):
	t = a[0]+a[1]
	a = t
	print(fl(a))	

def calc(a):
	n = len(a)
	i = 0
	temp = []
	if(n%2==0):
		mid = int((n/2)-1)
		while(i<=mid):
			t = a[i]+a[n-1-i]
			temp.append(t)
			i +=1
		a = temp
		clr(a)	
	elif(n%2==1):
		mid = int(n/2)
		while(i<=mid):	
			if(i<mid):
				t = a[i]+a[n-1-i]
				temp.append(t)
				i += 1
			else:
				t = a[mid]
				temp.append(t)
				i += 1
		a = temp
		clr(a)
	
def cname(b,g):
	c = b+g
	c = ''.join(c.split())
	c = list(c)
	ce = set(c)
	a = [c.count(x) for x in ce]
	a.sort(reverse = True)
	clr(a)
def heart():
	for i in range(4):
		for j in range(4-i-1):
			print(" ",end="")
		for j in range(i+1):
			print("* ",end="")
		for j in range(2*(4-i-1)):
			print(" ",end="")
		for j in range(i+1):
			print("* ",end="")
		print()
	for i in range(8,0,-1):
		for j in range(8-i):
			print(" ",end="")
		for j in range (i,0,-1):
			print("* ",end="")
		print()

load = "Loading..."
for i in range(len(load)):
    print(load[i], end ="")
    time.sleep(1)
print()
print("fetching Resourse file...")
print("============FLAME CALCULATOR==========")
print("                                   ")
time.sleep(1)
print("   _____   _______  __     __      ")
time.sleep(1)
print("  | ___ \ |___ ___| \ \   / /      ")
time.sleep(1) 
print("  | |__||    | |     \ \ / /       ")
time.sleep(1)
print("  | ___ /    | |      \ v /        ")
time.sleep(1)
print("  | |_| \    | |       | |         ")
time.sleep(1)
print("  |____ /    |_|       |_|         ")
time.sleep(1)
print("                           pvt.ltd ")
time.sleep(1) 
print("---------- Dedicated for those who are in doubt --------")
b = input("\n Enter your name :\n")
g = input("\n Enter your crush name :\n")
print()
print("its take few seconds")
time.sleep(5)
heart()
cname(b,g)
print("")
print("                                                          @copyright BtY     ")


