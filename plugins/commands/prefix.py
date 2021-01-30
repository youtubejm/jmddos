# -*- coding: utf-8 -*-
#############################
###*ddOs V.1|*   ###        *
#############################
## daa@xmpp.ru ##
#################

def prefix_show(type, source, parameters):
	if parameters:
	 nawrs = str(parameters)
	if parameters.count(u''):
	 reply(type, source, u' Prefix [ '+Prefix+u' ]')
def prefix_del(type, source, parameters):
        if parameters:
	 nawrs = str(parameters)
	if parameters.count(u''):
	 file1 = 'tools/other/prefix.dll'
	 write_file(file1, u'{\'Prefix\': \'\'}')
	 reply(type, source, u'Cleared!;-)')
         reply(type, source, u'I Will Be Back In 5\8 Sec')
	if parameters:
		reason = parameters
	else:
		reason = ''
	if GROUPCHATS:
		gch=GROUPCHATS.keys()
	if reason:
		for x in gch:
			if popups_check(x):
				msg(x, u'Restarting ...!;-)')
	else:
		for x in gch:
			if popups_check(x):
				msg(x, u'/me Restarting ...!;-)')
	prs=xmpp.Presence(typ='unavailable')
	if reason:
		prs.setStatus('Leaving Due Restart ;-)'+reason)
	else:
		prs.setStatus('Restarted by Bot Master;-)')
	JCON.send(prs)
	time.sleep(1)
	JCON.disconnect()
def prefix_add(type, source, parameters):
        if parameters:
	 nawrs = str(parameters)
	if parameters == Prefix:
	  reply(type, source, u'This Command Prefix :'+Prefix+u'Is Already In My List!!')
	if parameters.count(u'') and not parameters.count('show') and not parameters.count('clear') and not Prefix:
	 file2 = 'tools/other/prefix.dll'
	write_file(file2, u'{\'Prefix\': \''+nawrs+'\'}')
	reply(type, source, u'My New Command Prefix :'+nawrs)
	reply(type, source, u'I Will Be Back In 5\8 Sec')
	if parameters:
		reason = parameters
	else:
		reason = ''
	if GROUPCHATS:
		gch=GROUPCHATS.keys()
	if reason:
		for x in gch:
			if popups_check(x):
				msg(x, u'Restarting ...!;-)')
	else:
		for x in gch:
			if popups_check(x):
				msg(x, u'/me Restarting ...!;-)')
	prs=xmpp.Presence(typ='unavailable')
	if reason:
		prs.setStatus('Leaving Due Restart ;-)'+reason)
	else:
		prs.setStatus('Restarted by Bot Master')
	JCON.send(prs)
	time.sleep(1)
	JCON.disconnect()
	
register(prefix_show, 'prefix', 9)
register(prefix_show, 'prefix-show', 9)
register(prefix_add, 'prefix-add', 9)
register(prefix_del, 'prefix-del', 9)
