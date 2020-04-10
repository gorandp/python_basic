# Marcar tarjeta

Este miniprograma lo que hace es una especie de marcado de tarjeta.

Lo creé solo para controlar el tiempo que trabajo. Porque durante un mes estuve controlando mi tiempo en un excel y ya me había cansado de hacerlo. A parte, con este programa descubrí que me había equivocado en una cuenta que había hecho en excel.

Aunque tengo que aclarar que lo hice para salir del paso y más que seguro se puede mejorar. Es decir, funciona, pero hay ciertos bugs que no arreglé. Como por ejemplo que el inicio de un turno se de en un día y termine en otro. Si alguno encuentra más bugs reportenlo como issue así lo dejamos como tarea pendiente para que cada uno lo arregle por su cuenta (solo con el fin de que practiquen).

También, si alguno hizo una versión mejorada de este programa, me encantaría verlo. Puedo dejar un link a su repo donde lo tengan y así los demás ven cómo fue que solucionaron los bugs de mi programa.

## Modo de uso

- Usar `fast_check.py` para marcado rápido de la fecha y hora actual.
- Usar `check_time.py` para marcado manual.
- Usar `summary.py` para hacer un análisis de los turnos marcados, mostrando las horas trabajadas por día y por mes.

## Funcionamiento

Un turno lo llamo al momento donde se marca la tarjeta. El turno puede ser de inicio o fin (`'s'` de start y `'e'` de end, respectivamente). Por lo tanto, los turnos pueden tener como campos:
    - Fecha
    - Hora
    - Tipo de turno (inicio o fin)
Estas son definiciones que yo impuse.

`fast_check.py` lo primero que hace es fijarse en `next_turn` que letra hay (`'s'` o `'e'`), que es un tipo de caché (esto es así para no tener que dejar corriendo un proceso en segundo plano que cuando termine marque la hora de finalización). Luego agarra la fecha y hora actual del sistema y con esos datos agrega una fila en un CSV llamado `'LOG_TIME.csv'` (si no existe, crea el archivo)

Aunque, como se darán cuenta, `fast_check.py` no hace todo solo, sino que usa de `check_time.py`, que es la versión general de `fast_check.py`. En un principio creé `check_time.py` pero rapidamente me di cuenta que era incómodo, ya que la mayoría del tiempo solo quería agarrar la hora y fecha actual y ponerle el estado que debería ir.  Para eso creé `fast_check.py` que lo hace todo automaticamente.

`check_time.py` es la manera manual de cargar los datos, aunque sigue siendo útil, como por ejemplo si te despertas al día siguiente y te das cuenta que te colgaste en finalizar el turno.

`summary.py` es un script aparte, que lo que hace es agarrar `'LOG_TIME.csv'` y lo analiza, creando dos archivos (o sobrescribirlos) `'LOG_SUMMARY.csv'` y `'LOG_ANALYSIS.csv'`. En el primero se guarda las horas totales trabajadas por cada fecha detectada. En el otro se guarda un analisis mensual para todas las fechas dentro de un mes.

Este programa no está purificado del todo, a lo que me refiero es que más que seguro se puede mejorar para evitar errores.

Tampoco fui muy bueno al asignar nombres... pero bueno, anda.

## Nota al margen

No solo se puede usar para controlar el tiempo de trabajo, sino que también de estudio o de alguna actividad que hagan.

## Reto

Fijense que cuando corren `summary.py` les tira un warning:

```bash
summary.py:26: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  errors='coerce')
--- SUMMARY DONE ---
--- ANALYSIS DONE ---
```

Traten de entender primero qué es lo que está pasando y luego solucionarlo.

## Integrar con otras cosas

Se puede seguir mejorandolo, cómo por ejemplo hacer otro script super simple que use una librería tipo jupyter y graficar los datos.

Si se les ocurre algo y quieren que lo ponga como ejemplo acá, creen un issue diciendo la idea para mejorar el programa, o me mandan un mensaje por WhatsApp.
