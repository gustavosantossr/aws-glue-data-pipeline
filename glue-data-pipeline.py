import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node s3-raw-file
s3rawfile_node1720597940032 = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": "\"", 
        "withHeader": True, 
        "separator": ";", 
        "optimizePerformance": False
        }, 
    connection_type="s3", 
    format="csv", 
    connection_options={
        "paths": ["s3://devspace-aws-s3-bucket/aluguel.csv"], 
        "recurse": True
        }, 
    transformation_ctx="s3rawfile_node1720597940032"
    )


job.commit()