"""
Who? Companies that want quick, comprehensible analytics about their supply chain and orders 
What? A small script that will write a memo to a txt file containing information about a supply chain 
Where? The information will be stored on a postgreSQL database on elephantSQL 
Why? To automate something as simple as gathering data and running analysis
how?
    1. Ask user for what information should be included in the memo
    2. Query the database to gather all relevant data 
    3. Compare the information to previous queries to generate analytics 
    4. Send the analysis to a trained LLM that will produce a memo
    5. Write the memo to a txt file
    6. Return the file to the user 
"""
import urllib.parse as up
import psycopg2
import requests

db = None;

def generate_memo(parameters): 
    db = database_conn().cursor()AZD
    #retrieve formdata from a url
    select_based_on_parameters(parameters)
    #generate sql database ew
    memo = 0;


    db.close();
    return memo;

def write_memo_to_file():
    pass

def select_based_on_parameters(list_of_parameters = None):
    pass

def database_conn():
        #parsing URL into sections and setting up the relevant parameters for a connection
        up.uses_netloc.append("postgres")
        url = up.urlparse('postgres://wetzpnnr:I8Ikltc1JA_CcbFCG_54H1Qendr5ILta@lallah.db.elephantsql.com/wetzpnnr')
        #establish the interface for the connection
        conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
        )
        return conn;  



