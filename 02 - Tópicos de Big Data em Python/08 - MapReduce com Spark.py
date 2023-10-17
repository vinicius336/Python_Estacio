from pyspark import SparkContext
spark_Contexto = SparkContext()

lista = [1, 2, 3, 4, 5, 3]
lista_rdd = spark_Contexto.parallelize(lista)

lista_rdd.count()

par_ordenado = lambda numero: (numero, numero * 10)
lista_rdd.flatMap(par_ordenado).collect()

lista_rdd.map(par_ordenado).collect()

spark_Contexto.stop()