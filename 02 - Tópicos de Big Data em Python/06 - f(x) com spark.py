from pyspark import SparkContext
spark_contexto = SparkContext()

import numpy as np

vetor = np.array([10, 20, 30, 40, 50])

paralelo = spark_contexto.parallelize(vetor)

print('#' * 80)
print(paralelo)
print('#' * 80)

mapa = paralelo.map(lambda x : x ** 2 + x)

print('#' * 80)
mapa.collect()
print('#' * 80)