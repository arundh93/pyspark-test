import sys
from pyspark.sql import SparkSession
import yaml
from src.config import load


if __name__ == '__main__':
    spark = SparkSession.builder.getOrCreate()

    df = spark.createDataFrame([[1]], ['a'])
    contents = load.config
    # with open(location, 'r') as file:
    fruits_list = yaml.safe_load(contents)
    print(fruits_list)
    df.show()

