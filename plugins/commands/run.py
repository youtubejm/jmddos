# -*- coding: utf-8 -*-
#############################
###*ddOs V.1|*   ###        *
#############################
## daa@xmpp.ru ##
#################

def get_afools_state(gch):
	if not 'afools' in GCHCFGS[gch]:
		GCHCFGS[gch]['afools']=0
		
register_stage1(get_afools_state)
