# -*- coding: utf-8 -*-
####################
###*ddOs V.1|*   ###        *
#############################
## daa@xmpp.ru ##
#################



def slaefr(type, source, parameters):
	accdesc={
'-9':u'Full Blocked By Bot',
'-1':u'BlockeD By Bot Owner!',
'1':u'None, Limited orders',
'2':u'User','3':u'MUC Member',
'4':u'MUC Moderator/None',
'5':u'MUC Moderator/Member',
'6':u'MUC Moderator/Admin',
'7':u'MUC Moderator/Owner',
'8':u'BOt\'s Admin',
'9':u'Bot\'s Master.'}
	if not parameters:
		level=str(user_level(source[1]+'/'+source[2], source[1]))
		if level in accdesc.keys():
			slaefr=accdesc[level]
		else:
			slaefr=''
		reply(type, source, u'\nacc in: '+level+u' '+slaefr+u'\nOrders: '+u'\niq - prefix -prefix-show - prefix-add - prefix-sel - master - access - go - leave - res - halt - regjid -  ')
	else:
                reply(type, source, u'Who?')
                
        
def help(type, source, parameters):
	reply(type, source, u'\n\nddOs BOT WAR==> commands , war')

def war(type, source, parameters):
        access_level=str(user_level(source[1]+'/'+source[2], source[1]))
	if access_level == '9':
                reply(type, source, u'Your access level:'+access_level+u'\nدوز\nattack\nضرب روم\nzoech\nتبديل اسم بالروم\nspam1\nضرب فلود صيني\nspam2\nضرب رسائل محددة\nspam3\nضرب أيميلات مسجلة\nspam4\n\nاوامر ضرب ايميل\nspam-jid1;stop1==spam-jid2;stop2')





register(war, Prefix+'war', 0)
register(slaefr, Prefix+'commands', 0)
register(help, Prefix+'help', 0)
register(slaefr, 'commands', 0)
register(help, 'help', 0)
register(war, 'war', 0)
register(war, 'war', 0)
                      
