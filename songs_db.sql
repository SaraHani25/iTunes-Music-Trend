-- Step 2.1: Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS songs_db;

-- Step 2.2: Use the database
USE songs_db;

-- Step 2.4: Create the first table (for the first CSV file)
CREATE TABLE songs_date1 (
    Position_of_the_Songs_the_Chart_that_Day INT PRIMARY KEY,
    Title VARCHAR(255),
    Artist VARCHAR(255),
    Position_Change_that_Day VARCHAR(255),
    How_Many_Days_at_Position INT,
    Highest_Position_Reached INT,
    How_Many_Times_at_Position VARCHAR(255),
    Points_Total INT,
    Extra_Points_that_Day INT
);

-- Step 2.5: Create the second table (for the second CSV file)
CREATE TABLE songs_date2 (
    Position_of_the_Songs_the_Chart_that_Day INT PRIMARY KEY,
    Title VARCHAR(500),
    Artist VARCHAR(255),
    Position_Change_that_Day VARCHAR(255),
    How_Many_Days_at_Position INT,
    Highest_Position_Reached INT,
    How_Many_Times_at_Position VARCHAR(255),
    Points_Total INT,
    Extra_Points_that_Day INT,
    FOREIGN KEY (Position_of_the_Songs_the_Chart_that_Day) REFERENCES songs_date1(Position_of_the_Songs_the_Chart_that_Day)
);


select * from songs_date1;
select * from songs_date2;
