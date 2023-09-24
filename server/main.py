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
import psycopg2.extras
import openai
import requests
import queries
import json

gpt_url = URL = "https://api.openai.com/v1/chat/completions"
API_key = "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";

def generate_memo(parameters = ["customer","product","supply"]): 
    db = database_conn().cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    #retrieve form data from a url
    selection_data = select_based_on_parameters(db = db, list_of_parameters=parameters)
    memo = gpt_request(selection_data);

    print(memo.role)
    f = open("outputs\memo.txt", "w")
    f.write(memo)

    f.close() 
    db.close();
    return memo;

def gpt_request(data):
     payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": f"Write a memo summarizing the results of these supply chain database queries: {data}"}],
    "temperature" : 1.0,
    "top_p":1.0,
    "n" : 1,
    "stream": False,
    "presence_penalty":0,
    "frequency_penalty":0,
    }

     headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_key}"
    }
     response = requests.post(URL, headers=headers, json=payload, stream=False)
     response = json.loads(response.text)
     return response["choices"][0]["message"]


def select_based_on_parameters(db, list_of_parameters):
    selection_data = [];
    #if information on customers is wanted 
    if "customer" in list_of_parameters:
         db.execute(queries.customer_query);
         selection_data.append(db.fetchall());
    #if information on product is wanted
    if "product" in list_of_parameters:
         db.execute(queries.product_query);
         selection_data.append(db.fetchall());
    #if information on supply is wanted
    if "supply" in list_of_parameters:
         db.execute(queries.supply_query);
         selection_data.append(db.fetchall());
    return selection_data;

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

generate_memo()

