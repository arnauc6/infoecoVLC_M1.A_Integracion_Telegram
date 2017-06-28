#!/usr/bin/python
# -*- coding: utf-8 -*-

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Librerias
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
from apiai import *
from comunicacionWebhook import *

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Variables
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
respuesta = ''
resErrorRespApiai = 'El servicio esta caído ahora mismo, vuelve a intentarlo más tarde'

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Funciónes
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------

def obtenerRespuesta(texto,chat_id, idioma, nombreUsuario):

    respApiai = sendQuery(texto,chat_id, idioma, nombreUsuario)

    # Si la respuesta es correcta
    if respApiai.status_code==200:
        respApiai = respApiai.json() # Convertimos a dic
        print respApiai

        if respApiai['result']['metadata']['webhookUsed'] == 'true':
            # Se conecta al WebHook
            respWH = buscarRespuestaWH(respApiai)

            if respWH.status_code==200:
                # Si la respuesta es correcta
                respWH = respWH.json() # Convertimos a dic
                respuesta = respWH['displayText']
            else:
                # Si no tomamos la respuesta por defecto
                respuesta = respApiai['result']['speech']

        else:
            # No tiene que conectarse al WebHook
            respuesta = respApiai['result']['speech']
    else:
        respuesta = resErrorRespApiai

    return respuesta
