# Simple Azure Function (BLOB Storage Trigger) Excel -> SQL

This Azure Function triggers each time a new .xlsx file gets uploaded to an Azure Storage Container ('excels').
The function reads the data of the blob and appends the data to an Azure SQL Database table (creates the table if it doesn't exist).
The conversion from Excel to SQL is found in the 'data_tosql.py' file, I used Pandas and SQLAlchemy.
The connection string to the database was provided through an Azure Key Vault secret.

The objective of this project was to try out blob storage trigger functions.

Thank you for reading.