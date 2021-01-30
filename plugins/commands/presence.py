# -*- coding: utf-8 -*-
#############################
###*ddOs V.1|*   ###        *
#############################
## daa@xmpp.ru ##
#################

check_pending=[]

def presence_ra_change(prs):
	groupchat = prs.getFrom().getStripped()
	nick = prs.getFrom().getResource()
	jid = get_true_jid(groupchat+'/'+nick)
	item = findPresenceItem(prs)
	if jid in GLOBACCESS:
		return
	else:
		if groupchat in ACCBYCONFFILE and jid in ACCBYCONFFILE[groupchat]:
			pass
		else:
			if groupchat in GROUPCHATS and nick in GROUPCHATS[groupchat]:
				if jid != None:
					role = item['role']
					aff = item['affiliation']
					if role in ROLES:
						accr = ROLES[role]
						if role=='moderator' or user_level(jid,groupchat)>=7:
							GROUPCHATS[groupchat][nick]['ismoder'] = 1
						else:
							GROUPCHATS[groupchat][nick]['ismoder'] = 0
					else:
						accr = 0
					if aff in AFFILIATIONS:
						acca = AFFILIATIONS[aff]
					else:
						acca = 0
					access = accr+acca
					change_access_temp(groupchat, jid, access)


			
def iqkeepalive_and_s2scheck():
	for gch in GROUPCHATS.keys():
		iq=xmpp.Iq()
		iq = xmpp.Iq('get')
		id = 'p'+str(random.randrange(1, 1000))
		globals()['check_pending'].append(id)
		iq.setID(id)
		iq.addChild('ping', {}, [], 'urn:xmpp:ping')
		iq.setTo(gch+'/'+get_gch_info(gch, 'nick'))
		JCON.SendAndCallForResponse(iq, iqkeepalive_and_s2scheck_answ,{})
	threading.Timer(300, iqkeepalive_and_s2scheck).start()

def iqkeepalive_and_s2scheck_answ(coze, res):
	id = res.getID()
	if id in globals()['check_pending']:
		globals()['check_pending'].remove(id)
	else:
		print 'someone is doing wrong...'
		return
	if res:
		gch,error=res.getFrom().getStripped(),res.getErrorCode()
		if error in ['405',None]:
			pass
		else:
			threading.Timer(60, join_groupchat,(gch,get_gch_info(gch, 'nick') if get_gch_info(gch, 'nick') else BotNick)).start()
		


register_presence(presence_ra_change)
register_stage2(iqkeepalive_and_s2scheck)
