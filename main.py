import os
import sys
from src.search import RAGSearch
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    print("Welcome to RAG Learning CLI!")
    print("Initializing RAG system...")
    
    try:
        # Initialize RAG search
        # This will load existing index from 'faiss_store' or build it from 'data'
        rag = RAGSearch(persist_dir="faiss_store")
        
        while True:
            query = input("\nEnter your query (or 'exit' to quit): ").strip()
            if query.lower() in ['exit', 'quit']:
                break
            
            if not query:
                continue
                
            print(f"Searching and summarizing for: '{query}'...")
            summary = rag.search_and_summarize(query, top_k=3)
            
            print("\n" + "="*50)
            print("SUMMARY RESPONSE:")
            print("-" * 50)
            print(summary)
            print("="*50)
            
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
