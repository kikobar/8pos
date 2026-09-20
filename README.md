**Objective**

These Python scripts allow to extract records from the 8POS API and post them to a Mongo database.

**Requirements**

* Python installed on the machine running this application.
* Credentials for accessing the 8POS API - you need to request to 8POS for your credentials and URLs.
* Credentials for writing to a MongDB database - this database will be used for storing the data extracted from the 8POS API.

**How to run this application**

* Copy the file `config-sample.py` to `config.py`.
* Edit `config.py` with your credentials and defaults.
* To generate a token valid for one year, run `python3 generate_token.py` , then copy the token string and paste it in the corresponding field of your `config.py` file.
* To extract the daily sales report from the 8POS API and post them to the Mongo database, run `python3 extract_daily_sales.py` and follow the instructions of the script.
* To delete daily sales from the Mongo database, run `python3 delete_daily_sales.py` and follow de instructions of the script.
