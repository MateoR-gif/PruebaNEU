import pymongo
from test import *
import numpy as np

# Lectura de CSV
arr = np.loadtxt("data_vector.csv")

# Conexión Base de Datos
client = pymongo.MongoClient("mongodb+srv://root:root@neucluster.iyjtix4.mongodb.net/?retryWrites=true&w=majority")
db = client['NEUTest']
collection = db['Sub-Arrays']
# ----------------------------

# Llamado al Método
resultado = BuscarArrays(arr)
print(resultado)
# ----------------------------

# Query Insert
collection.insert_many(resultado)
# ----------------------------