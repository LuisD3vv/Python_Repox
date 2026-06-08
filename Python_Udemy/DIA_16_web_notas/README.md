
# Que son los entornos virtuales

 un entorno virtual en python es un directorio aislado que contiene su propia
    instalacion de python y librerias, permitiendo gestionar dependecias
    especifcias para cada proyecto,   sin afectar el sistema global.

## Apectos claves

>permite que el proyecto A use Django 3 mientras que el proyecto B
>use Django 4, en la misma maquina.

## Cuando usarlos

## Como usarlos

>

## Activarlo con libreria virtualenv (hay opcion nativa)

```bash
    virtualenv (nombre)
    source bin/activate

    # instalara la version mas reciente
    pip install <nombre-dependencia>

    # instalara la version especificada
    pip install <nombre-depencia==versionespecifica>
```

## desactivarlos

```bash
    deactivate
```

> lissandro / pss sabina

## usando Django

## configurar usuario de django admin

```bash
    python3 <manager.py> createsuperuser
```
