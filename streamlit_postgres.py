import streamlit as st
import requests
import os
from dotenv import load_dotenv
import pandas as pd

# Load environment variables
load_dotenv()

def execute_query(query):
    """
    Execute query via FastAPI endpoint and handle different response types
    """
    try:
        API_URL = os.getenv('POSTGRES_API_URL', 'http://localhost:8000/execute-query/')
        
        response = requests.post(
            API_URL, 
            json={"query": query},
            headers={
                "Content-Type": "application/json",
                "ngrok-skip-browser-warning": "true"
            }
        )
        
        response.raise_for_status()
        result = response.json()
        
        # Check if the query was successful
        if result.get('success', False):
            query_type = result.get('query_type', '').lower()
            
            if query_type == 'select':
                # For SELECT queries, return DataFrame
                return pd.DataFrame(result['data'])
            else:
                # For other queries (INSERT, UPDATE, etc.), return success message
                st.success(f"{result.get('message')} - Rows affected: {result.get('rows_affected', 0)}")
                return None
        else:
            # Handle error case
            st.error(f"Query Error: {result.get('error', 'Unknown error')}")
            return None
            
    except requests.RequestException as e:
        st.error(f"API Request Error: {e}")
        return None
    except Exception as e:
        st.error(f"Unexpected Error: {e}")
        return None
def main():
    st.title("Exploring heart disease risk factors and health conditions")
    
    query = st.text_area("Enter your PostgreSQL Query:", height=150)
    
    if st.button("Execute Query"):
        if query.strip():
            # Remove query type restrictions
            results = execute_query(query)
            
            # Only display DataFrame if we have one (SELECT queries)
            if isinstance(results, pd.DataFrame):
                st.dataframe(results)
        else:
            st.warning("Please enter a query.")

if __name__ == "__main__":
    main()
