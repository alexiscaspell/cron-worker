# CONFIGURACION DE TAREAS

* Una tarea se compone de las siguientes partes:

### ID
* Es el nombre de la tarea, evitar utilizar espacios ya que luego se utilizara en algunos endpoints siendo enviado en la uri

### CRON
* Esta es una expresion de cron que indica cuando se ejecutara la tarea (para armarla se puede visitar https://crontab.guru/)

### ACTIVA
* Es un booleano que habilita o deshabilita la tarea

### RECEPTORES DE ESTADO
* Esta es una lista con los receptores de estado que seran los que reciban las notificaciones del estado de la tarea, estos se componen de lo sig:

- **status**: Este es el estado en que termina la tarea (actualmente solo existe **"ok"** y **"failed"**)
- **destinatarios**: Esta es una lista de los destinatarios del mail.
- **en_copia**: Esta es una lista con los que iran en copia o cc dentro del mail.
- **template**: Es la plantilla que se usara para enviar el mail, leer [configuracion de template](#template)

### TEMPLATE
* Se compone de 4 atributos:
- **encabezado**: Es el titulo que llevara el mail. Este puede contener codigo python asi como utilizar valores que retorno la funcion ejecutada siendo accedidos como **args[indice]**, siendo indice el indice de la posicion que se paso en [actualizar_template](#aclaraciones)
- **cuerpo**: Es el texto que ira en el cuerpo del mail
- **cuerpo_html**: En este campo se adjunta el contenido html en string
- **adjuntos**: Es una lista de strings que representan tuplas donde el primer elemento es el nombre del archivo y el segundo los bytes de este

> Para visualizarlo mejor, suponga que tiene el siguiente codigo:
```
#Asi es siempre toda funcion recibe como primer parametro la tarea
def generar_informe(tarea,tablero_tareas,fecha):
    '''Genera el informe y devuelve sus bytes para el envio del mail'''

    url = GENERAR_REPORTE_URI+"/"+tablero_tareas

    response = requests.get(url)

    if response.status_code>=300 or response.status_code<200:
        try:
            texto_error = response.text
        except Exception as _:
            texto_error = ""

        return False,[bytes(response.status_code),texto_error]

#Siempre retornar una tupla con Booleano y lista de retorno que sera mapeada a args
    return True,[response.content,firma_html_str()]
```

> Entonces un posible template podria ser:
```
    "template": {
        "encabezado": "f'Informe de tareas de fecha {args[0].day:02d}/{args[0].month:02d}/{args[0].year}'",
        "cuerpo": "f'Por la presente se envia las tareas realizadas hasta el dia de la fecha.  \\n\\nSaludos.\\nGracias.'",
        "cuerpo_html": "args[3]",
        "adjuntos": [
            "(f'reporte-tareas-{args[0].month:02d}-{args[0].year}.md',args[2])"
        ]
    },
```


### MODULO EXTERNO
* Esta es la funcion que se ejecutara en la tarea
- **modulo**: Es el path a donde esta el archivo .py que contiene la funcion (si es relativo sera relativo a la carpeta base del proyecto)
- **funcion**: Es el nombre de la funcion a ejecutar
- **argumentos**: Es una lista con argumentos que se le pasaran a la funcion, estos se evaluan como codigo python por ende si se quiere pasar por ej. un string **"soy un string"** se tiene que pasar como **"'soy un string'"**; Ademas se pueden llamar a funciones siempre y cuando esten dentro del archivo de **modulo** o incluidas en sus imports.

## ACLARACIONES
* Cuando se define una funcion nueva que se llamara desde una tarea siempre se tiene que retornar lo siguiente:
```
    ...
    ...
    return True,una_lista_de_elementos

```
* Toda funcion como primer parametro recibira la tarea del tipo **TareaProgramada** , este objeto contiene toda la info anteriormente mencionada.
* Como retorno de la funcion, en args siempre se encontrara como primer elemento la fecha y hora de ejecucion, como segundo parametro el status de la tarea ([revisar **status** de tarea](#RECEPTORES%20DE%20ESTADO)) y luego el resto de los elementos de la lista retornada en la funcion.


