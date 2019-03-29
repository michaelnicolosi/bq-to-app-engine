import requests 
from google.cloud import bigquery

client = bigquery.Client()

# Send data to the Google Analytics servers 
GA_ENDPOINT = "https://www.google-analytics.com/collect" 

query = (
    "SELECT * FROM `analytics-sandbox-jf.weather_data.daily` "
)
query_job = client.query(
    query,
    # Location must match that of the dataset(s) referenced in the query.
    location="US",
)  # API request - starts the query

for row in query_job:  # API request - fetches results
    data = {
            'v':'1', 
            't':'event', 
            'tid':'UA-134072717-1', 
            'cid':"27878783.7386767",
            'ec':row.hour,
            'ea':'app_engine_lead_data',
            'el':"test",
            'ni': 1
            } 
        
    # Make the reqesut to the GA servers
    r = requests.post(url = GA_ENDPOINT, data = data) 

