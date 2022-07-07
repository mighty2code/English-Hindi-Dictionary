# English Hindi Dictionary with English definations.
# Date: 28/06/2022		Modified: 03/07/2022

import sqlite3
from os import system

if __name__=='__main__':
	
	title='\tENGLISH HINDI DICTIONARY\n\n'
	conn = sqlite3.connect('dictionary.db')
	conn2 = sqlite3.connect('definations.db')
	c = conn.cursor()
	c2 = conn2.cursor()
	
	chk=''
	while(chk.lower()!='e'):
		system('clear')
		words=input(title+'Enter Word  : ').strip().split()
		meaning=definations=''; wlist=[]
		
		if(not words):
			continue
		
		for i,word in enumerate(words):
			if(word.isalpha()):
				wlist=list(c.execute('SELECT hindi FROM dictionary WHERE english==?',[word.lower()]))
				dlist=list(c2.execute('SELECT defination FROM dictionary WHERE english==?',[word.capitalize()]))
			else:
				wlist=list(c.execute('SELECT english FROM dictionary WHERE hindi==?',[word]))
				dlist=list(c2.execute('SELECT defination FROM dictionary WHERE english==?',[wlist[0][0].capitalize()]))
			
			defination='\n'
			if(len(words)>1):
				defination='\n'+word.capitalize()+':\n'
				if(i>0):
					meaning+=', '
				meaning+=word.capitalize()
			
			for i,line in enumerate(dlist):
				defination+="%d. %s\n"%(i+1,line[0])
			if dlist:
				definations+=defination
			if wlist:
				if(len(words)>1):
					meaning+='('+wlist[0][0].capitalize()+')'
				else:
					meaning+=wlist[0][0].capitalize()
			
		if(meaning or definations):
			if(meaning):
				print('Meaning     :',meaning)
			if(definations):
				print('Definations :',definations)
		else:
			print('Word not Found, check spelling or try another word.')
		
		chk=input("\n\nPress Enter to Continue...\n(Enter 'e' to Exit.) ")	
	conn.close()