#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
import pandas as pd
import os

# Paths to your CSV files
csv_file_date1 = r"D:\Final\Worldwide iTunes Song Chart_1_8.csv"
csv_file_date2 = r"D:\Final\Worldwide iTunes Song Chart_2_8.csv"

# Function to load and clean data, and then insert into the specified table
def insert_data_into_table(csv_file, table_name, conn):
    if not os.path.exists(csv_file):
        print(f"Error: The CSV file {csv_file} does not exist.")
        return
    
    # Load the data
    data = pd.read_csv(csv_file)
    
    # Strip any leading/trailing whitespace characters from the column names
    data.columns = data.columns.str.strip()
    
    # Drop the Tpts column if it exists
    if 'Tpts' in data.columns:
        data = data.drop(columns=['Tpts'])
    
    # Replace NaN values with None (which will translate to NULL in MySQL)
    data = data.where(pd.notnull(data), None)
    
    # Truncate values to fit the column size (255 characters)
    if 'Artist' in data.columns:
        data['Artist'] = data['Artist'].apply(lambda x: str(x)[:255] if x is not None else None)
    if 'Title' in data.columns:
        data['Title'] = data['Title'].apply(lambda x: str(x)[:255] if x is not None else None)

    cursor = conn.cursor()

    # Insert data into MySQL
    for index, row in data.iterrows():
        sql = f"""
        INSERT INTO {table_name} 
        (Position_of_the_Songs_the_Chart_that_Day, Title, Artist, Position_Change_that_Day, How_Many_Days_at_Position, Highest_Position_Reached, How_Many_Times_at_Position, Points_Total, Extra_Points_that_Day) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (
            row['Position_of_the_Songs_the_Chart_that_Day'],
            row['Title'],
            row['Artist'],
            row['Position_Change_that_Day'],
            row['How_Many_Days_at_Position'],
            row['Highest_Position_Reached'],
            row['How_Many_Times_at_Position'],
            row['Points_Total'],
            row['Extra_Points_that_Day']
        ))

    # Commit the transaction
    conn.commit()
    print(f"Data inserted successfully into {table_name}.")
    cursor.close()

# Initialize MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cra$ymaddex2349",
    database="songs_db"
)

# Insert data into both tables
insert_data_into_table(csv_file_date1, "songs_date1", conn)
insert_data_into_table(csv_file_date2, "songs_date2", conn)

# Close the connection
conn.close()

print("Script completed.")


# In[ ]:




