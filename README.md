# TrendingYouTubeVideos
The objective of this project is to ensure the secure management, streamlined processing, and thorough analysis of structured and semi-structured data from YouTube videos. This will be accomplished by organizing the data based on video categories and trending metrics.

Built an ETL pipeline using Python in AWS - 
1. Built an AWS lambda function to convert all json data to apache parquet and store it in AWS glue catalog database. Added trigger so that the function automatically reads incoming json data in s3 bucket and converts it. 
2. Built an AWS Glue ETL job to convert all csv data to apache parquet and store it in AWS glue catalog database.
3. Built an AWS Glue ETL job for joining data for the analytics layer to combine AWS glue databases and visualize data for reporting layer.

Dataset - https://www.kaggle.com/datasets/datasnaek/youtube-new?resource=download 

Languages- SQL, Python3

Services- AWS S3, AWS Glue, QuickSight, AWS Lambda, AWS Athena, AWS IAM

Some visualizations using QuickSight:

<img width="797" alt="Screenshot 2023-07-31 at 7 31 23 PM" src="https://github.com/harshakalmath/TrendingYouTubeVideos/assets/50831461/50976216-5d05-49b2-8259-fa2f927046ce">


<img width="1138" alt="Screenshot 2023-07-31 at 7 33 45 PM" src="https://github.com/harshakalmath/TrendingYouTubeVideos/assets/50831461/220bcaeb-8429-4c3f-8820-ef1457becc89">


<img width="1135" alt="Screenshot 2023-07-31 at 7 34 05 PM" src="https://github.com/harshakalmath/TrendingYouTubeVideos/assets/50831461/743f3a93-c20c-463f-91ef-2ed2ac3beb3d">
