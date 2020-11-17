import os

for i in range(366):
	d = str(i) + 'days ago'
	with open('bot.txt','a') as file:
		file.write(d+'\n')

	os.system('git add bot.txt')
	os.system('git commit --date="'+d+'" -m "hack-commit"')

os.system('git push origin master')