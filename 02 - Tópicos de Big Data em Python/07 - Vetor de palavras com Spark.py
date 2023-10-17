import numpy as np
from operator import add
from pyspark import SparkContext
spark_contexto = SparkContext()

paralelo = spark_contexto.parallelize(['distribuida', 'distribuida', 'spark', 'rdd', 'spark', 'spark'])

funcao_lambda = lambda x : (x, 1)

mapa = paralelo.map(funcao_lambda).reduceByKey(add).collect()

for (w, c) in mapa:
    print(f'{w}: {c}')

spark_contexto.stop()