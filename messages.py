MESSAGES = {
	2:  (
		'GET_INFO_SYS_RSP',
		'2Q12sB12s',
		(
			'md5_reference',
			'matricola',
			'modello',
			'info_herholtd'
		)
	),
	4:  (
		'GET_PARAM_SYS_RSP',
		'2Q2H2Bc50s',
		(
			'md5_reference',
			'freq_agg_reg',
			'tempo_ante_spegnimento',
			'durata_registro_num_allarmi',
			'numero_messaggi_max',
			'indicatore_zona',
			'keep_alive',
			'indirizzo_datacenter'
		)
	),
	7:  (
		'GET_PARAMETERS_RSP',
		'2QcBcBcBcBcBH2B4H2B2H3sH',
		(
			'md5_reference',
			'tt',
			'te',
			'tq',
			'tm',
			'ta',
			'potenza_contrattuale',
			'max_potenza_contrattuale',
			'max_potenza_tollerata',
			'sgancio_per_supero_potenza',
			'tempo_min_ante_sgancio',
			'cost_algoritmo_limitatore',
			'tensione_nominale',
			'tensione_massima_ammessa',
			'tensione_minima_ammessa',
			'base_calcolo_tens_quality',
			'freq_nominale',
			'profilo_utenza',
			'base_calcolo_pot_max',
		)
	),
	11: (
		'GET_DEFAULT_PARAMETERS_RSP',
		'2QcBcBcBcBcBH2B4H2B2H3cH6B2f2H2Bc50s56B35B61B',
		(
			'md5_reference',
			'tt_default',
			'te_default',
			'tq_default',
			'tm_default',
			'ta_default',
			'potenza_contrattuale_default',
			'max_potenza_contrattuale_default',
			'max_potenza_tollerata_default',
			'sgancio_per_supero_potenza_default',
			'tempo_min_ante_sgancio_default',
			'cost_algoritmo_limitatore_default',
			'tensione_nominale_default',
			'tensione_massima_ammessa_default',
			'tensione_minima_ammessa_default',
			'base_calcolo_tens_quality',
			'freq_nominale_default',
			'profilo_utenza_d',
			'base_calcolo_pot_max_default',
			'allarme_bassa_tensione_default',
			'allarme_alta_tensione_default',
			'allarme_alta_tensione_10min_default',
			'allarme_alta_frequenza_default',
			'allarme_bassa_frequenza_default',
			'allarme_basso_fattore_potenza_default',
			'allarme_supero_traffico_sim1_default',
			'allarme_supero_traffico_sim2_default',
			'freq_agg_reg_default',
			'tempo_ante_spegnimento_default',
			'durata_registro_num_allarmi_default',
			'numero_messaggi_max_default',
			'indicatore_zona_default',
			'keep_alive_default',
			'indirizzo_data_center_default',
			'tabella_oraria_annuale_default'
		)
	),
	14: (
		'TAB_ORARIA_RSP',
		'2Q56B35B61B',
		(
			'md5_reference',
			'tabella_oraria_annuale'
		)
	),
	17: (
		'GET_INFO_DATA_TRIFASE_RSP',
		'2Q26f16d',
		(
			'md5_reference',
			'potenza_attiva_r',
			'potenza_attiva_s',
			'potenza_attiva_t',
			'potenza_attiva_sum',
			'potenza_reattiva_r',
			'potenza_reattiva_s',
			'potenza_reattiva_t',
			'potenza_reattiva_sum',
			'potenza_apparente_r',
			'potenza_apparente_s',
			'potenza_apparente_t',
			'potenza_apparente_sum',
			'fattore_potenza_r',
			'fattore_potenza_s',
			'fattore_potenza_t',
			'fattore_potenza_trifase',
			'tensione_rn',
			'tensione_sn',
			'tensione_tn',
			'tensione_rs',
			'tensione_st',
			'tensione_tr',
			'corrente_r',
			'corrente_s',
			'corrente_t',
			'frequenza_rete',
			'energia_attiva_prelievo_r',
			'energia_attiva_prelievo_s',
			'energia_attiva_prelievo_t',
			'energia_attiva_prelievo_sum',
			'energia_attiva_immisione_r',
			'energia_attiva_immisione_s',
			'energia_attiva_immisione_t',
			'energia_attiva_immisione_sum',
			'energia_reattiva_prelievo_r',
			'energia_reattiva_prelievo_s',
			'energia_reattiva_prelievo_t',
			'energia_reattiva_prelievo_sum',
			'energia_reattiva_immissione_r',
			'energia_reattiva_immissione_s',
			'energia_reattiva_immissione_t',
			'energia_reattiva_immissione_sum'
		)
	),
	18: (
		'INFO_DATA_TRIFASE',
		'26f16d',
		(
			'potenza_attiva_r',
			'potenza_attiva_s',
			'potenza_attiva_t',
			'potenza_attiva_sum',
			'potenza_reattiva_r',
			'potenza_reattiva_s',
			'potenza_reattiva_t',
			'potenza_reattiva_sum',
			'potenza_apparente_r',
			'potenza_apparente_s',
			'potenza_apparente_t',
			'potenza_apparente_sum',
			'fattore_potenza_r',
			'fattore_potenza_s',
			'fattore_potenza_t',
			'fattore_potenza_trifase',
			'tensione_rn',
			'tensione_sn',
			'tensione_tn',
			'tensione_rs',
			'tensione_st',
			'tensione_tr',
			'corrente_r',
			'corrente_s',
			'corrente_t',
			'frequenza_rete',
			'energia_attiva_prelievo_r',
			'energia_attiva_prelievo_s',
			'energia_attiva_prelievo_t',
			'energia_attiva_prelievo_sum',
			'energia_attiva_immisione_r',
			'energia_attiva_immisione_s',
			'energia_attiva_immisione_t',
			'energia_attiva_immisione_sum',
			'energia_reattiva_prelievo_r',
			'energia_reattiva_prelievo_s',
			'energia_reattiva_prelievo_t',
			'energia_reattiva_prelievo_sum',
			'energia_reattiva_immissione_r',
			'energia_reattiva_immissione_s',
			'energia_reattiva_immissione_t',
			'energia_reattiva_immissione_sum'
		)
	),
	20: (
		'GET_INFO_DATA_MONOFASE_RSP',
		'16s7f4d',
		(
			'md5_reference',
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
	23: (
		'GET_REGISTRO_CONS_36GG_RSP',
		'',
		(
			'md5_reference',
			'registro_en_attiva_prelievo',
			'registro_en_attiva_immissione',
			'registro_en_reattiva_prelievo',
			'registro_en_reattiva_induttiva_prelievo',
			'registro_en_reattiva_immissione',
			'registro_en_reattiva_induttiva_immissione',
			'registro_pmax_per_fascia_oraria'
		)
	),
	25: (
		'GET_REGISTRO_CONS_FASCE_RSP',
		'2Q16d',
		(
			'md5_reference',
			'registro_en_attiva_prelievo_1',
			'registro_en_attiva_prelievo_2',
			'registro_en_attiva_prelievo_3',
			'registro_en_attiva_prelievo_4',
			'registro_en_attiva_immissione_1',
			'registro_en_attiva_immissione_2',
			'registro_en_attiva_immissione_3',
			'registro_en_attiva_immissione_4',
			'registro_en_reattiva_prelievo_1',
			'registro_en_reattiva_prelievo_2',
			'registro_en_reattiva_prelievo_3',
			'registro_en_reattiva_prelievo_4',
			'registro_en_reattiva_immissione_1',
			'registro_en_reattiva_immissione_2',
			'registro_en_reattiva_immissione_3',
			'registro_en_reattiva_immissione_4'
		)
	),
	27: (
		'GET_REGISTRO_ALLARMI_RSP',
		'',
		(
			'md5_reference',
			'registro_allarmi'
		)
	),
	29: (
		'GET_ALARMS_RSP',
		'2Q21B',
		(
			'md5_reference',
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
	),
	30: (
		'ALARMS',
		'21B',
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
			'supero_pmax_contr_%',
			'supero_traffico_sim1',
			'supero_traffico_sim2'
		)
	),
	31: (
		'RESET_ALARMS',
		'21B',
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
			'supero_traffico_sim1',
			'supero_traffico_sim2'
		)
	),
	33: (
		'GET_SOGLIE_RSP',
		'2Q6B2f',
		(
			'md5_reference',
			'allarme_bassa_tensione',
			'allarme_alta_tensione',
			'allarme_alta_tensione_10min',
			'allarme_alta_frequenza',
			'allarme_bassa_frequenza',
			'allarme_basso_fattore_potenza',
			'allarme_supero_traffico_sim1',
			'allarme_supero_traffico_sim2'
		)
	),
	36: (
		'GET_VER_FIRM_RSP',
		'2Q2B',
		(
			'md5_reference',
			'versione_firmware'
		)
	),
	38: (
		'GET_MONITORING_RSP',
		'2Q3B3fB2I',
		(
			'md5_reference',
			'intensita_del_campo_di_ricezione',
			'%%ram_occupata',
			'%%cpu_istantanea',
			'cpu_load_avg',
			'%%disco_occupato_per_ogni_partizione',
			'traffico_trasmesso',
			'traffico_ricevuto'
		)
	),
	39: (
		'MSG_MONITORING',
		'3B3fB2I',
		(
			'intensita_del_campo_di_ricezione',
			'%%ram_occupata',
			'%%cpu_istantanea',
			'cpu_load_avg',
			'%%disco_occupato_per_ogni_partizione',
			'traffico_trasmesso',
			'traffico_ricevuto'
		)
	),
	41: (
		'GET_QUALITY_RSP',
		'2QB2f2H',
		(
			'md5_reference',
			'campioni_intervallo_vmax_min',
			'tensione_minima_settimanale',
			'tensione_massima_settimanale',
			'num_int_tensione_int_vmax_min',
			'num_int_tensione_sotto_vmin'
		)
	),
	42: (
		'MSG_QUALITY',
		'B2I2H',
		(
			'campioni_intervallo_vmax_min',
			'tensione_minima_settimanale',
			'tensione_massima_settimanale',
			'num_int_tensione_int_vmax_min',
			'num_int_tensione_sotto_vmin'
		)
	),
	45: (
		'MSG_METEO',
		'6H',
		(
			'solar_radiation',
			'temperature',
			'pressure',
			'relative_humidity',
			'wind_direction',
			'wind_velocity'
		)
	),	
	
	
	
	47: (
		'BOOT_MSG',
		'19B',
		(
			'boot'
		)
	)
}