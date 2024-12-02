import streamlit as st
import psycopg2
import pandas as pd

def create_connection():
    """
    Create a connection to the PostgreSQL database.
    """
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="heart_data",
            user="postgres",
            password="2410"
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        st.error(f"Error connecting to PostgreSQL database: {error}")
        return None

def execute_query(query):
    """
    Execute the given SQL query and return results as a DataFrame
    """
    conn = create_connection()
    if conn is None:
        return None
    
    try:
        # Use pandas to read SQL directly
        df = pd.read_sql_query(query, conn)
        return df
    except psycopg2.Error as e:
        st.error(f"Error executing query: {e}")
        return None
    finally:
        if conn:
            conn.close()

def main():
    # Initialize session state for results if not already exists
    if 'query_results' not in st.session_state:
        st.session_state.query_results = None

    st.title("PostgreSQL Query Interface")
    
    # Query input text area
    query = st.text_area("Enter your PostgreSQL Query:", height=150)
    
    # Execute query button
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
                # Store results in session state
                st.session_state.query_results = results
                # Display results
                st.dataframe(results)
        else:
            st.warning("Please enter a query.")
    
    # Clear results button
    if st.button("Clear Results"):
        # Set query results to None
        st.session_state.query_results = None
        # Rerun the app to refresh the state
        st.rerun()

if __name__ == "__main__":
    main()