# -*- coding: utf-8 -*-

#############################
###*ddOs V.1|*   ###        *
#############################
## daa@xmpp.ru ##
#################


import calendar

def space2number(number):
	if number <= 9:
		number = ' %s ' % (number)
	else:
		number = '%s ' % (number)
	return number

def month_cal(type, sourse, body):
	text = body.split()
	try:
		month = int(text[0])
	except:
		month = tuple(time.gmtime())[1]
	try:
		year = int(text[1])
	except:
		year = tuple(time.gmtime())[0]
	try:
		smbl = text[2]
	except:
		smbl = '_'
	repl = u'\nMo Tu We Th Fr Sa Su\n'
	try:
		for x in calendar.monthcalendar(year, month):
			for y in x:
				if y:
					repl += space2number(y)
				else:
					repl += '   '
			repl = repl[:-1]+'\n'
		repl = u'\n ;-)by Slaefr: %s%s' % (time.strftime(' %d.%m.%Y (%H:%M:%S )', time.localtime()), repl[:-1].replace(' ', smbl))
	except:
		repl = u'khatai rokh dad!'
	reply(type, sourse, repl)

register(month_cal, Prefix+'time', 0)
