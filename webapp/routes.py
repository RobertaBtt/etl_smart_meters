from bottle import route, view, get, post, request, abort, error, redirect
from boto.dynamodb2.table import Table
import boto.dynamodb2.exceptions

REGION = 'eu-west-1'

conn = boto.dynamodb2.connect_to_region(REGION)
messages_21 = Table('sg_E_21', connection=conn)
messages_30 = Table('sg_E_30', connection=conn)

HEADER_FIELDS = (
	'API_version',
	'measurement_ts',
	'send_ts',
	'msg_id',
	'content_length',
	'CRC'
)

MESSAGES = {
	19: (
		'GET_INFO_DATA_MONOFASE_REQ',
		'',
		tuple()
),
	20: (
		'GET_INFO_DATA_MONOFASE_RSP',
		'16s7f4d',
		('bla','TODO')
	),
	21: (
		'INFO_DATA_MONOFASE',
		'7f4d',
		(
			'potenza_attiva',
			'potenza_reattiva',
			'potenza_apparente',
			'fattore_potenza',
			'tensione_fase',
			'corrente_fase',
			'frequenza_rete',
			'energia_attiva_prelievo',
			'energia_attiva_immisione',
			'energia_reattiva_prelievo',
			'energia_reattiva_immissione'
		)
	),
	30: (
		'ALARMS',
		'19B',
		(
			'sovra_o_sotto_tensione',
			'inversione_fasi',
			'overflow_tensione',
			'bassa_tensione',
			'alta_tensione',
			'alta_tensione_base10min',
			'sovra_frequenza_rete',
			'sotto_frequenza_rete',
			'basso_fattore_potenza',
			'supero_pmax_%',
			'intervento_limitatore',
			'corruzione_registri_energia',
			'manomissione',
			'problemi_rete_2g3g',
			'contatore_non_riconosciuto',
			'switch_user_leds',
			'no_power',
			'usb_removed',
			'supero_pmax_contr_%'
		)
	)
}

@get('/message/<msg_id>/<payload_hash>')
@view('message_detail')
def message_details(msg_id,payload_hash):
	table = messages_21 if msg_id == '21' else messages_30
	msg = table.get_item(payload_hash=payload_hash)
	msg_name = MESSAGES[int(msg_id)][0]
	return {'msg':dict(msg), 'title':'message details for %s' %payload_hash, 'msg_id':msg_id, 'msg_name': msg_name}

@get('/list/<msg_id>')
@view('message_list')
def message_list(msg_id):
	table = messages_21 if msg_id == '21' else messages_30
	fields_list = HEADER_FIELDS + MESSAGES[int(msg_id)][2]
	msg_name = MESSAGES[int(msg_id)][0]
	msg = table.scan()
	return {'fields_list':fields_list, 'msg': msg, 'msg_id':msg_id, 'title': 'message list for %s' % msg_id, 'msg_name':msg_name}

@get('/')
def home():
	redirect('/list/21')