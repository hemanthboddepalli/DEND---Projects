# Data Modeling with Postgres
Hi! In this project, I have created a Postgres database with tables to analyze the data on songs and user activity on a new music streaming app from a company called Sparkify.

## High Level Design
This project reads the json files that contains songs and user activity information and inserts into database tables. The purpose is to provide a suitable data base schema for data analytics team.

## Files
Below are the files used to complete this project.

**test.ipynb** - displays the first few rows of each table to let you check your database.

**create_tables.py** - drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.

**etl.ipynb** - reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables. 

**etl. py** - reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.

**sql_queries.py** - contains all your sql queries, and is imported into the last three files above.

## Database Schema
![Database Schema](https://github.com/hemanthboddepalli/DEND---Projects/blob/master/Schema.jpeg)

## DB Schema Description
The DB Schema created based on Star Schema. The songplays table is the fact time and the other tables are dimension tables.
**users** table capture the details of the users using the app.
**songs** table stores all the songs in the app.
**artists** table stores all the artists and their location.
**time** table stores timestamps of records in songplays.
**songplays** table stores the log data associated with song plays.

songplays table is created based on the dimension data present in the users, songs, artists and time tables.

## How to run the project
1. Install Postgres and Python3 in your machine.
2. Download the project which includes all the project files.
3. Run "python create_tables.py" in your terminal to create tables in your Postgres database.
4. Run "python etl.py" to load the data into the tables created in the above step.
