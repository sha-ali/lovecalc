import time
# importing time library

def find_relation(value):
	#checking the relation status
	#if count is 8 relationship length is 6, 6+2 lover will eliminate
	#its continue until last one
	relationships = ['Freind','Lover','Angry','Marriage','enemy','sister']
	count = 0
	while relationships:
		for i in range(len(relationships)):
			count +=1
			if count == value:
				temp_val = relationships.pop(i)
				count = 0
				break
	return temp_val

def dividingtens(letter_count):
	# if count of letter comes 10 or more split its integer into two
	# if number 12 its split in to 1 and 2
	temp = []
	for i in letter_count:
		if(i>=10):
			x = int(i /10)
			temp.append(x)
			y = int(i%10)
			temp.append(y)
		else:
			temp.append(i)
	letter_count = temp
	letter_count.sort(reverse = True)
	if(len(letter_count)==2):
		adding_two_number(letter_count)
	else:
		calculate_letter_count(letter_count) 
		
 
def adding_two_number(letter_count):
	#adding final two number
	total_figure = letter_count[0]+letter_count[1]
	print(find_relation(total_figure))	

def calculate_letter_count(letter_count):
	#adding first and last number in the list
	#second one adding second last
	#adding odd and even length of list
	n = len(letter_count)
	i = 0
	temp = []
	if(n%2==0):
		mid = int((n/2)-1)
		while(i<=mid):
			t = letter_count[i]+letter_count[n-1-i]
			temp.append(t)
			i +=1
		letter_count = temp
		dividingtens(letter_count)	
	elif(n%2==1):
		mid = int(n/2)
		while(i<=mid):	
			if(i<mid):
				t = letter_count[i]+letter_count[n-1-i]
				temp.append(t)
				i += 1
			else:
				t = letter_count[mid]
				temp.append(t)
				i += 1
		letter_count = temp
		dividingtens(letter_count)
	
def calculate_name(boy_name,girl_name):
	full_name = boy_name+girl_name
	#adding string
	full_name = ''.join(full_name.split())
	full_name = list(full_name)
	name_set = set(full_name)
	# grouping same alphapate 
	letter_count = [full_name.count(x) for x in name_set]
	letter_count.sort(reverse = True)
	dividingtens(letter_count)
def heart():
	# in this printung heart pirmid
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

#start from heare
load = "Loading..."
for i in range(len(load)):
    print(load[i], end ="")
    time.sleep(1)

#string "loading..." with time duration
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
boy_name = input("\n Enter your name :\n")
girl_name = input("\n Enter your crush name :\n")

#entering names
print()
print("its take few seconds")
time.sleep(5)
heart()
calculate_name(boy_name,girl_name)
print("")
print("                                                          @copyright BtY     ")


