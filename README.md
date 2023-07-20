ETL Smart Meters (smartgrid_hub)
======================================

This is part of the architecture of Enermed and Techus (2014-2018)


- Messages arrive from Smartmeters every15 minutes
- Throughout Mosquito MQTT Broker they are read so they are put into the SQS Queue
- ETL SmartMeters routines extract the payload of the messages and put the into the DynamoDB table.
- ETL SmartMeters routines copy the content into relational MySQL database


![SmartMeters_data_backend.jpg](static%2FSmartMeters_data_backend.jpg)

From SQS Amazon to DynamoDb Tables.

Meter readings were divided into three types of tables:

 - etl 18 for three-phase
 - etl 21 for single-phase
 - etl 30 for messages of control
 
 Fields of the table 18:
 - sender_id 
 - elaboration_ts
 - measurement_ts, processing_tsreceive_ts send_ts
 - potenza_attiva_r,potenza_attiva_s,potenza_attiva_t,potenza_attiva_sum,
 - potenza_reattiva_r,potenza_reattiva_s,potenza_reattiva_t,potenza_reattiva_sum,
 - potenza_apparente_r,potenza_apparente_s,potenza_apparente_t,potenza_apparente_sum
 - fattore_potenza_r,fattore_potenza_s,fattore_potenza_t,fattore_potenza_trifase,
 - tensione_rn, tensione_sn,tensione_tn,tensione_rs,tensione_st,tensione_tr, 
 - corrente_r,corrente_s,corrente_t, frequenza_rete,
 - energia_attiva_prelievo_r,energia_attiva_prelievo_s,energia_attiva_prelievo_t,energia_attiva_prelievo_sum
 - energia_attiva_immisione_r,energia_attiva_immisione_s,energia_attiva_immisione_t,energia_attiva_immisione_sum,
 - energia_reattiva_immissione_r,energia_reattiva_immissione_s,energia_reattiva_immissione_t,energia_reattiva_immissione_sum,
 - energia_reattiva_prelievo_r,energia_reattiva_prelievo_s,energia_reattiva_prelievo_t,energia_reattiva_prelievo_sum
  