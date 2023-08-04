import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1689808521129 = glueContext.create_dynamic_frame.from_catalog(
    database="db_youtube_cleansed",
    table_name="raw_statistics",
    transformation_ctx="AWSGlueDataCatalog_node1689808521129",
)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1689808490322 = glueContext.create_dynamic_frame.from_catalog(
    database="db_youtube_cleansed",
    table_name="cleansed_statistics_reference_data",
    transformation_ctx="AWSGlueDataCatalog_node1689808490322",
)

# Script generated for node Join
Join_node1689808555176 = Join.apply(
    frame1=AWSGlueDataCatalog_node1689808521129,
    frame2=AWSGlueDataCatalog_node1689808490322,
    keys1=["category_id"],
    keys2=["id"],
    transformation_ctx="Join_node1689808555176",
)

# Script generated for node Amazon S3
AmazonS3_node1689808717012 = glueContext.getSink(
    path="s3://big-data-on-youtube-analytics-useast2-14317621-dev/youtube/rpt_youtube_statistics_categories/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["region", "id"],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1689808717012",
)
AmazonS3_node1689808717012.setCatalogInfo(
    catalogDatabase="db_youtube_analytics",
    catalogTableName="rpt_youtube_statistics_categories",
)
AmazonS3_node1689808717012.setFormat("glueparquet")
AmazonS3_node1689808717012.writeFrame(Join_node1689808555176)
job.commit()
