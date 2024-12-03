import streamlit as st
import requests
import os
from dotenv import load_dotenv
import pandas as pd

# Load environment variables
load_dotenv()

def execute_query(query):
    """
    Execute query via FastAPI endpoint
    """
    try:
        # Get API URL from environment variable
        API_URL = os.getenv('POSTGRES_API_URL', 'http://localhost:8000/execute-query/')
        
        # Make POST request to API
        response = requests.post(
            API_URL, 
            json={"query": query},
            headers={
                "Content-Type": "application/json",
                "ngrok-skip-browser-warning": "true"  # Optional: helps with ngrok browser warnings
            }
        )
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse response
        result = response.json()
        
        # Convert to pandas DataFrame
        df = pd.DataFrame(result['data'])
        
        return df
    except requests.RequestException as e:
        st.error(f"API Request Error: {e}")
        return None
    except Exception as e:
        st.error(f"Unexpected Error: {e}")
        return None

def main():
    st.title("PostgreSQL Query Interface")
    
    query = st.text_area("Enter your PostgreSQL Query:", height=150)
    
    if st.button("Execute Query"):
        if query.strip():
            # Validate query to prevent potentially harmful operations
            lower_query = query.lower().strip()
            if any(forbidden in lower_query for forbidden in ['drop', 'delete', 'truncate', 'alter']):
                st.error("Potentially destructive query detected. Only SELECT queries are allowed.")
                return
            
            # Execute query
            results = execute_query(query)
            
            if results is not None:
                st.dataframe(results)
        else:
            st.warning("Please enter a query.")

if __name__ == "__main__":
    main()
