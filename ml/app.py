from pyspark.sql import SparkSession

# Spark session & context
spark = SparkSession.builder.master("local").getOrCreate()
sc = spark.sparkContext

# Sum of the first 100 whole numbers
rdd = sc.parallelize(range(100 + 1))
print("rdd1:", rdd.sum())

spark2 = SparkSession.builder.master("spark://master:7077").getOrCreate()
sc2 = spark2.sparkContext

# Sum of the first 100 whole numbers
rdd2 = sc.parallelize(range(100 + 1))
print("rdd2: ", rdd2.sum())
