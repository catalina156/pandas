import pandas as pd
from data.platos import platosPopulares
from data.crearTabla import crearTabla

tablaPlatos=pd.DataFrame(platosPopulares)
print(tablaPlatos)
crearTabla(tablaPlatos,"tablaplatospopulares")