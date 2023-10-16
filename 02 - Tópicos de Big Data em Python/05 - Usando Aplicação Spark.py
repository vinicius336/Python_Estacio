from pyspark import SparkContext

sparkContext = SparkContext()
print('####', sparkContext, '####')
print('####', sparkContext.version, '####')

from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()  # Create my_spark
print('####', spark, '####')                # Print  my_spark

dataset = spark.read.csv('/content/sample_data/california_housing_test.csv', inferSchema = True, header = True) # Arquivo exemplo do Google Colab (terá erro)

print()