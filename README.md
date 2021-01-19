# CRON-WORKER

> Proyecto de ejecucion de tareas asincronas


![alt text](img/python.png)

## REQUERIMIENTOS

* **Python 3.8**
* **Docker**

## CONFIGURACION
* Para configurar las tareas editar el archivo config_tareas.json o invocar el sig. endpoint:

```
curl --location --request POST '{{cron-worker-host}}/api/v1/tareas' \
--header 'Content-Type: application/json' \
--data-raw '  {
        "cron": "* * * * *",
        "receptores_estado": [
            {
                "activo":false,
                "destinatarios": [
                    "alexis.taberna@moorea.io"
                ],
                "en_copia": [],
                "status": "ok",
                "template": {
                    "encabezado": "f'\''Proceso automatizado {args[0].month:02d} ({args[1]})'\''",
                    "cuerpo": "f'\''Se ejecutaron correctamente los registros {args[2]} del mes {args[0].month:02d}'\''"
                }
            },
            {
                "activo":false,
                "destinatarios": [
                    "alexis.taberna@moorea.io"
                ],
                "en_copia": [],
                "status": "failed",
                "template": {
                    "encabezado": "f'\''Error en proceso automatizado'\''",
                    "cuerpo": "f'\''Fallo de proceso debido a los \"siguientes registros fallidos: {args[2]}\"'\''"
                }
            }
        ],
        "id": "tarea_inservible",
        "modulo_externo": {
            "funcion": "tarea_de_prueba",
            "modulo": "apps/services/funciones_service.py",
            "argumentos": [
                "[f'\''{conf.get(Vars.VARIABLE_CONFIGURADA)}/{date.today().year}-{date.today().month:02d}-{i:02d}.csv'\'' for i in range(1, 16)]"
            ]
        }
    }'
```

## EJECUCION

### PYTHON

* Crear un virtualenv normalmente para python
* Con el virtualenv activado ejecutar `python app.py`

### DOCKER

* Pararse en la ruta raiz del proyecto con docker instalado y funcionando
* Pararse `./scripts/build.sh`
* Ejecutar `docker run -it -p 5000:5000 cron-worker:latest`

## PAGINAS

[Docker python 3.7 apine](https://hub.docker.com/_/python)
