from financial_engine import FinancialEngine
from insight_generator import generate_answer

engine = FinancialEngine(
    "data/BCG_GenAI_Financial_Data_Extraction_Example.xlsx"
)


def process_query(query):

    # Convert the entire dataframe to a CSV string to use as context
    data_context = engine.df.to_csv(index=False)
    
    # Send the user's query and the data context to the LLM
    answer = generate_answer(query, data_context)

    return answer