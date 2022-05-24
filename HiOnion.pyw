# -*- coding: UTF-8 -*-

from tkinter import Tk,Canvas,PhotoImage
import time
import random

with open('settings.txt','r') as fset:
	settings=fset.readlines()
	resolution=settings[2].strip().split('x')

with open('maps.txt') as fmap:
	allmap=fmap.read()
	rawmap=allmap.split('[')
	del(allmap)
	levelmap=[]
	levelname=[]
	for n in range(1,len(rawmap)):
		levelmap.append(rawmap[n].split('\n'))
		levelname.append(levelmap[n-1][0])
	tplist=[]
	locklist=[]
	for n in range(0,len(rawmap)-2):
		tplist.append(levelmap[n][-3].split('/'))
		locklist.append(levelmap[n][-2].split('/'))
	
	for n in range(0,len(rawmap)-2):
		tplist[n]=tplist[n][1].split(';')
		locklist[n]=locklist[n][1].split(';')
	del(rawmap)

root = Tk()
root.resizable(False,False)
root.title('Hi,Onion!')
root.geometry('%sx%s'%(resolution[0],resolution[1]))
root.iconbitmap('./assets/logo.ico')
cv = Canvas(root,bg='midnightblue',width=int(resolution[0]),height=int(resolution[1]))
cv.pack()

with open('./assets/usrdat/000.ini','r') as flevelr:
	cursavedlevel=int(flevelr.readline())
	trophynumber=int(flevelr.readline())
trophy=PhotoImage(file='./assets/trophy.gif')
trophyget=PhotoImage(file='./assets/trophyget.gif')
add=PhotoImage(file='./assets/add.gif')
add1=PhotoImage(file='./assets/add1.gif')
add10=PhotoImage(file='./assets/add10.gif')
minus=PhotoImage(file='./assets/minus.gif')
minus1=PhotoImage(file='./assets/minus1.gif')
minus10=PhotoImage(file='./assets/minus10.gif')

if cursavedlevel<=0:
	curlevel=0
else:
	curlevel=cursavedlevel

air=PhotoImage(file='./assets/air.gif')
wall=[]
for walln in range(1,17):
	wall.append(PhotoImage(file='./assets/wall%d.gif'%walln))
lava=[]
for lavan in range(1,17):
	lava.append(PhotoImage(file='./assets/lava%d.gif'%lavan))
player=PhotoImage(file='./assets/player.gif')
exit=PhotoImage(file='./assets/exit.gif')
wormhole=[]
for wormholen in range(1,9):
	wormhole.append(PhotoImage(file='./assets/wormhole%d.gif'%wormholen))
key=PhotoImage(file='./assets/key.gif')
lock=PhotoImage(file='./assets/lock.gif')
glass=PhotoImage(file='./assets/glass.gif')
slider=PhotoImage(file='./assets/slider.gif')
brokenglass=PhotoImage(file='./assets/brokenglass.gif')
replay=PhotoImage(file='./assets/replay.gif')

images={'0':air,'1':wall[3],'2':lava[0],'3':player,'4':exit,'5':wormhole[2],'6':key,'7':lock,'8':glass,'9':slider,'b':brokenglass}
colors=['red','magenta','ivory','royalblue','darkgreen','springgreen','lightyellow','purple','maroon','darkgray','coral','cyan','lightskyblue','hotpink','forestgreen','gold']

while True:
	cv['bg']='midnightblue'
	with open('./assets/usrdat/000.ini','r') as flevelr:
		cursavedlevel=int(flevelr.readline())
		trophynumber=int(flevelr.readline())

	if cursavedlevel<=0:
		curlevel=0
	else:
		curlevel=cursavedlevel
	def moveup(event):
		global movevec
		movevec=[0,-1]	
	def movedown(event):
		global movevec
		movevec=[0,1]	
	def moveleft(event):
		global movevec
		movevec=[-1,0]	
	def moveright(event):
		global movevec
		movevec=[1,0]	

	def click(event):
		global startlevel,movevec,velocity,curlevel,cursavedlevel
		if int(resolution[0])-320<event.x<int(resolution[0])-272 and 0<event.y<48:
			startlevel=True
			movevec=None
			velocity=None
		elif trophynumber==1:
			if int(resolution[0])-305<event.x<int(resolution[0])-275 and 94<event.y<126:
				startlevel=True
				movevec=None
				velocity=None
				cursavedlevel=-3
				curlevel=0
			elif int(resolution[0])-265<event.x<int(resolution[0])-215 and 94<event.y<126:
				startlevel=True
				movevec=None
				velocity=None
				if cursavedlevel<=7:
					curlevel=0
					cursavedlevel=-3
				elif cursavedlevel<=10:
					curlevel=0
					cursavedlevel-=10
				else:
					cursavedlevel-=10
					curlevel-=10
			elif int(resolution[0])-205<event.x<int(resolution[0])-165 and 94<event.y<126:
				startlevel=True
				movevec=None
				velocity=None
				if -3<cursavedlevel<=0:
					cursavedlevel-=1
				elif cursavedlevel>0:
					cursavedlevel-=1
					curlevel-=1
			elif int(resolution[0])-155<event.x<int(resolution[0])-115 and 94<event.y<126:
				startlevel=True
				movevec=None
				velocity=None
				if cursavedlevel<0:
					cursavedlevel+=1
				else:
					cursavedlevel+=1
					curlevel+=1
			elif int(resolution[0])-105<event.x<int(resolution[0])-55 and 94<event.y<126:
				startlevel=True
				movevec=None
				velocity=None
				if cursavedlevel<0:
					cursavedlevel+=10
					curlevel=cursavedlevel
				elif cursavedlevel+10>len(levelmap)-2:
					cursavedlevel=len(levelmap)-2
					curlevel=len(levelmap)-2
				else:
					cursavedlevel+=10
					curlevel+=10
			elif int(resolution[0])-45<event.x<int(resolution[0])-15 and 94<event.y<126:
				startlevel=True
				movevec=None
				velocity=None
				cursavedlevel=len(levelmap)-2
				curlevel=len(levelmap)-2

	cv.bind_all('<KeyPress-w>',moveup)
	cv.bind_all('<KeyPress-s>',movedown)
	cv.bind_all('<KeyPress-a>',moveleft)
	cv.bind_all('<KeyPress-d>',moveright)
	cv.bind_all('<KeyPress-W>',moveup)
	cv.bind_all('<KeyPress-S>',movedown)
	cv.bind_all('<KeyPress-A>',moveleft)
	cv.bind_all('<KeyPress-D>',moveright)
	cv.bind_all('<KeyPress-Up>',moveup)
	cv.bind_all('<KeyPress-Down>',movedown)
	cv.bind_all('<KeyPress-Left>',moveleft)
	cv.bind_all('<KeyPress-Right>',moveright)
	cv.bind_all('<Button-1>',click)

	while curlevel<=len(levelmap)-2:
		flickerperiod=5*(len(levelmap)-curlevel)
		keyamount=0
		unlock=0
		global startlevel
		startlevel=False
		curmap=[]
		curtplist=[]
		curlocklist=[]
	
		for a in range(1,len(levelmap[curlevel])):
			curmap.append(levelmap[curlevel][a])
		for a in range(0,len(tplist[curlevel])):
			curtplist.append(tplist[curlevel][a])
		for a in range(0,len(locklist[curlevel])):
			curlocklist.append(locklist[curlevel][a])
		for x in range(0,len(curtplist)):
			curtplist[x]=curtplist[x].split(',')
		for x in range(0,len(curlocklist)):
			curlocklist[x]=curlocklist[x].split(',')
	
		if cursavedlevel<=0:
			if cursavedlevel==-2:
				curmap[3]=curmap[3][:14]+'5'+curmap[3][15:]
				curmap[2]=curmap[2][:6]+'5'+curmap[2][7:]
			if cursavedlevel==-1:
				curmap[3]=curmap[3][:14]+'5'+curmap[3][15:]
				curmap[2]=curmap[2][:6]+'5'+curmap[2][7:]
				curmap[8]=curmap[8][:21]+'2'+curmap[8][22:]
				curmap[0]=curmap[0][:16]+'7'+curmap[0][17:]
				curmap[4]=curmap[4][:6]+'6'+curmap[4][7:]
			if cursavedlevel==0:
				curmap[6]=curmap[6][:21]+'8'+curmap[6][22:]
				curmap[4]=curmap[4][:15]+'9'+curmap[4][16:18]+'0'+curmap[4][19:]
	
		mapwidth=len(curmap[1])
		mapheight=len(curmap)-4
		x1st=(int(resolution[0])-320-32*mapwidth)//2+17
		y1st=(int(resolution[1])-32*mapheight)//2
		count=0
		count2=0
			
		velocity=None
		reachexit=False
		global movevec
		movevec=None

		lavastate=0
		while startlevel==False:
			if count==0:
				cv.delete('all')
				lavastate+=1
				lavastate%=16
				cv.create_rectangle(int(resolution[0])-320,0,int(resolution[0]),int(resolution[1]),fill='tan')
				cv.create_text(int(resolution[0])-160,30,text='Level:%d'%curlevel,fill='black',font=('times',40))
				cv.create_text(int(resolution[0])-160,80,text='\"'+levelname[curlevel][:-1]+'\"',fill='dimgray',font=('courier',16))
				cv.create_image(int(resolution[0])-295,25,image=replay)
				if trophynumber==1:
					cv.create_image(int(resolution[0])-17,17,image=trophy)
					cv.create_image(int(resolution[0])-290,110,image=minus)
					cv.create_image(int(resolution[0])-240,110,image=minus10)
					cv.create_image(int(resolution[0])-185,110,image=minus1)
					cv.create_image(int(resolution[0])-135,110,image=add1)
					cv.create_image(int(resolution[0])-80,110,image=add10)
					cv.create_image(int(resolution[0])-30,110,image=add)
	
				cv.create_image(int(resolution[0])-260,150,image=wall[random.randrange(0,16)])
				cv.create_text(int(resolution[0])-140,150,text='wall    ',font=('couried',30))
				cv.create_image(int(resolution[0])-260,200,image=lava[lavastate])
				cv.create_text(int(resolution[0])-140,200,text='lava    ',font=('couried',30))
				cv.create_image(int(resolution[0])-260,250,image=player)
				cv.create_text(int(resolution[0])-140,250,text='player  ',font=('couried',30))
				cv.create_image(int(resolution[0])-260,300,image=exit)
				cv.create_text(int(resolution[0])-140,300,text='exit    ',font=('couried',30))
				cv.create_image(int(resolution[0])-260,350,image=wormhole[random.randrange(0,8)])
				cv.create_text(int(resolution[0])-140,350,text='wormhole',font=('couried',30))
				cv.create_image(int(resolution[0])-260,400,image=key)
				cv.create_text(int(resolution[0])-140,400,text='key     ',font=('couried',30))
				cv.create_text(int(resolution[0])-100,400,text='(%d)'%(keyamount),fill='blueviolet',font=('courier',25))
				cv.create_image(int(resolution[0])-260,450,image=lock)
				cv.create_text(int(resolution[0])-140,450,text='lock    ',font=('couried',30))
				cv.create_image(int(resolution[0])-260,500,image=glass)
				cv.create_text(int(resolution[0])-140,500,text='glass   ',font=('couried',30))
				cv.create_image(int(resolution[0])-260,550,image=slider)
				cv.create_text(int(resolution[0])-140,550,text='slider ',font=('couried',30))
				for y in range(0,mapheight+1):
					for x in range(mapwidth):
						curblock=curmap[y][x]
						curx,cury=x1st+32*x,y1st+32*y
						if curblock=='0':
							cv.create_image(curx,cury,image=air)
						elif curblock=='1':
							cv.create_image(curx,cury,image=wall[random.randrange(0,16)])
						elif curblock=='2':
							cv.create_image(curx,cury,image=lava[lavastate])
						elif curblock=='3':
							playerposition=[x,y]
							cv.create_image(curx,cury,image=player)
						elif curblock=='4':
							cv.create_image(curx,cury,image=exit)
						elif curblock=='5':
							cv.create_image(curx,cury,image=wormhole[random.randrange(0,8)])
						elif curblock=='6':
							cv.create_image(curx,cury,image=key)
						elif curblock=='7':
							cv.create_image(curx,cury,image=lock)
						elif curblock=='8':
							cv.create_image(curx,cury,image=glass)
						elif curblock=='9':
							cv.create_image(curx,cury,image=slider)
						elif curblock=='b':
							cv.create_image(curx,cury,image=brokenglass)
			count+=1
			count%=flickerperiod
			
			if count2==1:
				if movevec:
					if velocity==None:
						velocity=movevec
				if velocity:
					nextpoint=[playerposition[0]+velocity[0],playerposition[1]+velocity[1]]
					nextblock=curmap[nextpoint[1]][nextpoint[0]]
					
					if nextblock=='0':
						cv.create_image(x1st+32*nextpoint[0],y1st+32*nextpoint[1],image=player)
						cv.create_image(x1st+32*playerposition[0],y1st+32*playerposition[1],image=air)
						curmap[playerposition[1]]=curmap[playerposition[1]].replace('3','0')
						curmap[nextpoint[1]]=curmap[nextpoint[1]][:nextpoint[0]]+'3'+curmap[nextpoint[1]][nextpoint[0]+1:]
						playerposition=[nextpoint[0],nextpoint[1]]
					elif nextblock=='1':
						movevec=None
						velocity=None
					elif nextblock=='2':
						cv.create_rectangle(0,int(resolution[1])//2-70,int(resolution[0])-320,int(resolution[1])//2+70,fill='gray')
						cv.create_text(int(resolution[0])//2-160,int(resolution[1])//2-30,text='You failed to',fill='darkred',font=('Courier',50))
						cv.create_text(int(resolution[0])//2-160,int(resolution[1])//2+30,text='swim in lava!',fill='darkred',font=('Courier',50))
						root.update()
						time.sleep(2)
						movevec=None
						velocity=None
						break
					elif nextblock=='3':
						break
					elif nextblock=='4':
						if cursavedlevel<0:
							cursavedlevel+=1
						else:
							cursavedlevel+=1
							curlevel+=1
						with open('./assets/usrdat/000.ini','w') as flevelw:
							flevelw.write(str(cursavedlevel)+'\n'+str(trophynumber))
						reachexit=True
						startlevel=True
						break
					elif nextblock=='5':
						for x in range(0,len(curtplist)-1):
							if nextpoint[0]==int(curtplist[x][0]) and nextpoint[1]==int(curtplist[x][1]):
								nextpoint=[int(curtplist[x][2])+velocity[0],int(curtplist[x][3])+velocity[1]]
							elif nextpoint[0]==int(curtplist[x][2]) and nextpoint[1]==int(curtplist[x][3]):
								nextpoint=[int(curtplist[x][0])+velocity[0],int(curtplist[x][1])+velocity[1]]
						cv.create_image(x1st+32*playerposition[0],y1st+32*playerposition[1],image=air)
						cv.create_image(x1st+32*nextpoint[0],y1st+32*nextpoint[1],image=player)
						curmap[playerposition[1]]=curmap[playerposition[1]].replace('3','0')
						curmap[nextpoint[1]]=curmap[nextpoint[1]][:nextpoint[0]]+'3'+curmap[nextpoint[1]][nextpoint[0]+1:]
						playerposition=[nextpoint[0],nextpoint[1]]
					elif nextblock=='6':
						cv.create_image(x1st+32*nextpoint[0],y1st+32*nextpoint[1],image=player)
						cv.create_image(x1st+32*playerposition[0],y1st+32*playerposition[1],image=air)
						curmap[playerposition[1]]=curmap[playerposition[1]].replace('3','0')
						curmap[nextpoint[1]]=curmap[nextpoint[1]][:nextpoint[0]]+'3'+curmap[nextpoint[1]][nextpoint[0]+1:]
						playerposition=[nextpoint[0],nextpoint[1]]
						keyamount+=1
					elif nextblock=='7':
						movevec=None
						velocity=None
						if keyamount>0:
							keyamount-=1
							for x in range(0,15):
								for n in range(0,len(curlocklist[unlock])//3):
									cv.create_image(x1st+32*int(curlocklist[unlock][3*n+0]),y1st+32*int(curlocklist[unlock][3*n+1]),image=images[curlocklist[unlock][3*n+2]])
								root.update()
								time.sleep(0.05)
								for n in range(0,len(curlocklist[unlock])//3):
									cv.create_image(x1st+32*int(curlocklist[unlock][3*n+0]),y1st+32*int(curlocklist[unlock][3*n+1]),image=images[curmap[int(curlocklist[unlock][3*n+1])][int(curlocklist[unlock][3*n+0])]])
								root.update()
								time.sleep(0.05)
							for n in range(0,len(curlocklist[unlock])//3):
								curmap[int(curlocklist[unlock][3*n+1])]=curmap[int(curlocklist[unlock][3*n+1])][:int(curlocklist[unlock][3*n])]+curlocklist[unlock][3*n+2]+curmap[int(curlocklist[unlock][3*n+1])][int(curlocklist[unlock][3*n])+1:]
								for n in range(0,len(curlocklist[unlock])//3):
									cv.create_image(x1st+32*int(curlocklist[unlock][3*n+0]),y1st+32*int(curlocklist[unlock][3*n+1]),image=images[curmap[int(curlocklist[unlock][3*n+1])][int(curlocklist[unlock][3*n+0])]])
								root.update()
							unlock+=1
						else:
							cv.create_rectangle(0,int(resolution[1])//2-70,int(resolution[0])-320,int(resolution[1])//2+70,tags='nokey',fill='chartreuse')
							cv.create_text(int(resolution[0])//2-160,int(resolution[1])//2-30,tags='nokey',text='You have no key',fill='royalblue',font=('Courier',50))
							cv.create_text(int(resolution[0])//2-160,int(resolution[1])//2+30,tags='nokey',text=' to unlock it.',fill='royalblue',font=('Courier',50))
							root.update()
							time.sleep(1.5)
							cv.delete('nokey')
					elif nextblock=='8':
						curmap[nextpoint[1]]=curmap[nextpoint[1]][:nextpoint[0]]+'b'+curmap[nextpoint[1]][nextpoint[0]+1:]
						cv.create_image(x1st+32*nextpoint[0],y1st+32*nextpoint[1],image=brokenglass)
						movevec=None
						velocity=None
					elif nextblock=='9':
						nextpoint2=[playerposition[0]+2*velocity[0],playerposition[1]+2*velocity[1]]
						nextblock2=curmap[nextpoint2[1]][nextpoint2[0]]
						if nextblock2=='0'or nextblock2=='b':
							cv.create_image(x1st+32*playerposition[0],y1st+32*playerposition[1],image=air)
							cv.create_image(x1st+32*nextpoint[0],y1st+32*nextpoint[1],image=player)
							cv.create_image(x1st+32*nextpoint2[0],y1st+32*nextpoint2[1],image=slider)
							curmap[playerposition[1]]=curmap[playerposition[1]].replace('3','0')
							curmap[nextpoint[1]]=curmap[nextpoint[1]][:nextpoint[0]]+'3'+curmap[nextpoint[1]][nextpoint[0]+1:]
							curmap[nextpoint2[1]]=curmap[nextpoint2[1]][:nextpoint2[0]]+'9'+curmap[nextpoint2[1]][nextpoint2[0]+1:]
							playerposition=[nextpoint[0],nextpoint[1]]
						movevec=None
						velocity=None
					elif nextblock=='b':
						cv.create_image(x1st+32*nextpoint[0],y1st+32*nextpoint[1],image=player)
						cv.create_image(x1st+32*playerposition[0],y1st+32*playerposition[1],image=air)
						curmap[playerposition[1]]=curmap[playerposition[1]].replace('3','0')
						curmap[nextpoint[1]]=curmap[nextpoint[1]][:nextpoint[0]]+'3'+curmap[nextpoint[1]][nextpoint[0]+1:]
						playerposition=[nextpoint[0],nextpoint[1]]
			count2+=1
			count2%=3
			time.sleep(0.01)
			root.update()
		if curlevel<=len(levelmap)-2 and startlevel==True and reachexit==True:
			cv.create_rectangle(0,int(resolution[1])//2-70,int(resolution[0])-320,int(resolution[1])//2+70,fill='floralwhite')
			cv.create_text(int(resolution[0])//2-160,int(resolution[1])//2,text='NEXT LEVEL',fill='royalblue',font=('Courier',50))
			root.update()
			time.sleep(2)
	with open('./assets/usrdat/000.ini','w') as flevelw2:
		flevelw2.write('-3\n'+'1')
	cv.delete('all')
	cv.create_rectangle(0,int(resolution[1])//2-32,int(resolution[0]),int(resolution[1])//2+32,tags='end',fill='red')
	cv.create_image(int(resolution[0])//2,int(resolution[1])//2,tags='end',image=trophyget)
	root.update()
	time.sleep(3)
	cv.delete('end')
	cv['bg']='black'
	cv.create_image(int(resolution[0])-81,33,image=trophyget)
	cv.create_image(25,25,image=replay)
	cv.create_rectangle(0,int(resolution[1])//2-60,int(resolution[0]),int(resolution[1])//2+60,fill='gold')
	lights=[]
	lights.append([random.randrange(0,int(resolution[0])),0,random.randrange(0,15)])
	for x in range(0,int(resolution[1])//10+8):
		lights.append([random.randrange(0,int(resolution[0])),int(resolution[1])+80-10*x,random.randrange(0,15)])
		lights.append([random.randrange(0,int(resolution[0])),int(resolution[1])+80-10*x,random.randrange(0,15)])
		cv.create_line(lights[-1][0],lights[-1][1]-80,lights[-1][0],lights[-1][1],tags='light',fill=colors[lights[-1][2]])
		cv.create_line(lights[-1][0],lights[-1][1]-80,lights[-1][0],lights[-1][1],tags='light',fill=colors[lights[-1][2]])
	restartgame=False
	def reboot(event):
		if 0<event.x<50 and 0<event.y<50:
			global restartgame
			restartgame=True

	cv.bind_all('<Button-1>',reboot)
	while restartgame==False:
		cv.delete('light')
		cv.create_text(int(resolution[0])//2,int(resolution[1])//2,text='VICTORY!',fill=colors[random.randrange(0,14)],font=('Courier',100))
		for n in range(0,len(lights)):
			cv.create_line(lights[n][0],lights[n][1]-80,lights[n][0],lights[n][1],tags='light',fill=colors[lights[n][2]])
			lights[n][1]=lights[n][1]+10
		lights.append([random.randrange(0,int(resolution[0])),0,random.randrange(0,15)])
		cv.create_line(lights[-1][0],lights[-1][1]-80,lights[-1][0],lights[-1][1],tags='light',fill=colors[lights[-1][2]])
		lights.pop(0)
		lights.append([random.randrange(0,int(resolution[0])),0,random.randrange(0,15)])
		cv.create_line(lights[-1][0],lights[-1][1]-80,lights[-1][0],lights[-1][1],tags='light',fill=colors[lights[-1][2]])
		lights.pop(0)
		root.update()
		time.sleep(0.1)
	
root.mainloop()