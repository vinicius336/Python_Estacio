import findspark
from pyspark.sql import SparkSession

findspark.init()
spark = SparkSession.builder.master('local[*]').getOrCreate()

dataset = spark.read.csv('/content/sample_data/california_housing_test.csv', inferSchema = True, header = True)

dataset.printSchema()