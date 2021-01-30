# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#############################
###*ddOs V.1|*   ###        *
#############################
## daa@xmpp.ru ##
#################



def go(type, source, parameters):
	if parameters:
		args = parameters.split()
		if len(args)>1:
			groupchat = args[0]
		else:
			groupchat = parameters
			reason = ''
		get_gch_cfg(groupchat)
		for process in STAGE1_INIT:
			with smph:
				INFO['thr'] += 1
				threading.Thread(None,process,'atjoin_init'+str(INFO['thr']),(groupchat,)).start()
		DBPATH='tools/back/'+groupchat+'/config.cfg'
		write_file(DBPATH, str(GCHCFGS[groupchat]))
		if Prefix:
			add_gch(groupchat, BotNick)
			join_groupchat(groupchat, BotNick)
		else:
			add_gch(groupchat, BotNick)
			join_groupchat(groupchat, BotNick)
		MACROS.load(groupchat)
		reply(type, source, u'Ok!:-)')
		if popups_check(groupchat):
			if reason:
				msg(groupchat, u'HELLO,:-)\n'+reason)
			else:
				msg(groupchat, u'I\'m '+'BOT DDOS '+', Joined , '+source[2]+'')
	else:
		reply(type, source, u':-)not found.')

def esc(type, source, parameters):
	args = parameters.split()
	if len(args)>1:
		level=int(user_level(source[1]+'/'+source[2], source[1]))
		if level<9 and args[0]!=source[1]:
			reply(type, source, u'I\'m NOT In!:-)')
			return
		reason = ' '.join(args[1:]).strip()
		if not GROUPCHATS.has_key(args[0]):
			reply(type, source, u'I\'m NOT In!:-)')
			return
		groupchat = args[0]
	elif len(args)==1:
		level=int(user_level(source[1]+'/'+source[2], source[1]))
		if level<9 and args[0]!=source[1]:
			reply(type, source, u'I Cann\'t Do it.:-)')
			return
		if not GROUPCHATS.has_key(args[0]):
			reply(type, source, u'I\'m NOT In!')
			return
		reason = ''
		groupchat = args[0]
	else:
		groupchat = source[1]
		reason = ''
	if popups_check(groupchat):
		if reason:
			msg(groupchat, u' Leaved\n'+reason)
		else:
			msg(groupchat, u'Leaved\n')
	if reason:
		leave_groupchat(groupchat, u'Leaved Room By Order From '+source[2]+u' |Reason:\n'+reason)
	else:
		leave_groupchat(groupchat,u'I\'m Leaving By Order From '+source[2])
	reply(type, source, u'Leaved!*HI*')


def reboot(type, source, parameters):
	if parameters:
		reason = parameters
	else:
		reason = ''
	if GROUPCHATS:
		gch=GROUPCHATS.keys()
	if reason:
		for x in gch:
			if popups_check(x):
				msg(x, u'Leaving Due Restart For Reason:\n'+reason)
	else:
		for x in gch:
			if popups_check(x):
				msg(x, u'/me I\'m restart now, I\'ll back in 5/10 sec..')
	prs=xmpp.Presence(typ='unavailable')
	if reason:
		prs.setStatus('Leaving Due Restart '+reason)
	else:
		prs.setStatus('Restarted by Bot Master')
	JCON.send(prs)
	time.sleep(1)
	JCON.disconnect()

def game_over(type, source, parameters):
	if parameters:
		reason = parameters
	else:
		reason = ''
	if GROUPCHATS:
		gch=GROUPCHATS.keys()
	if reason:
		for x in gch:
			if popups_check(x):
				msg(x, u'Leaving Due Sleep For Reason:\n'+reason)
	else:
		for x in gch:
			if popups_check(x):
				msg(x, u'I\'m Going 4 Halt NOW.')
	prs=xmpp.Presence(typ='unavailable')
	if reason:
		prs.setStatus('Leaving Due Sleep, For Reason: '+reason)
	else:
		prs.setStatus('Leaving Due Sleep')
	JCON.send(prs)
	time.sleep(2)
	os.abort()
		
def popups_check(gch):
	DBPATH='tools/back/'+gch+'/config.cfg'
	if GCHCFGS[gch].has_key('popups'):
		if GCHCFGS[gch]['popups'] == 1:
			return 1
		else:
			return 0
	else:
		GCHCFGS[gch]['popups']=1
		write_file(DBPATH,str(GCHCFGS[gch]))
		return 1
def get_autoaway_state(gch):
	if not 'autoaway' in GCHCFGS[gch]:
		GCHCFGS[gch]['autoaway']=1
	if GCHCFGS[gch]['autoaway']:
		LAST['gch'][gch]['autoaway']=0
		LAST['gch'][gch]['thr']=None


def set_default_gch_status(gch):
	if isinstance(GCHCFGS[gch].get('status'), str):
		GCHCFGS[gch]['status']={'status': u'', 'show': u'dnd'}
	elif not isinstance(GCHCFGS[gch].get('status'), dict):
		GCHCFGS[gch]['status']={'status': u'', 'show': u'dnd'}	
	

register(go, Prefix+'go', 9)
register(esc, Prefix+'leave', 9)
register(reboot, Prefix+'res', 9)
register(game_over, Prefix+'halt', 9)
register_stage1(set_default_gch_status)
register_stage1(get_autoaway_state)
