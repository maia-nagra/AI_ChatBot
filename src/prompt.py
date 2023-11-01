# Dictionary that maps the column headings to their descriptions
column_descriptions = {
    'ID': "The customer IDs",
    'AcceptedCmp1': "1 if customer accepted the offer in the 1st campaign, 0 otherwise",
    'AcceptedCmp2': "1 if customer accepted the offer in the 2nd campaign, 0 otherwise",
    'AcceptedCmp3': "1 if customer accepted the offer in the 3rd campaign, 0 otherwise",
    'AcceptedCmp4': "1 if customer accepted the offer in the 4th campaign, 0 otherwise",
    'AcceptedCmp5': "1 if customer accepted the offer in the 5th campaign, 0 otherwise",
    'Response': "1 if customer accepted the offer in the last campaign, 0 otherwise",
    'Complain': "1 if customer complained in the last 2 years",
    'DtCustomer': "date of customer's enrollment with the company",
    'Education': "customer's level of education",
    'Marital_Status': "customer's marital status",
    'Kidhome': "number of small children in customer's household",
    'Teenhome': "number of teenagers in customer's household",
    'Income': "customer's yearly household income",
    'MntFishProducts': "amount spent on fish products in the last 2 years",
    'MntMeatProducts': "amount spent on meat products in the last 2 years",
    'MntFruits': "amount spent on fruits in the last 2 years",
    'MntSweetProducts': "amount spent on sweet products in the last 2 years",
    'MntWines': "amount spent on wines in the last 2 years",
    'MntGoldProds': "amount spent on gold products in the last 2 years",
    'NumDealsPurchases': "number of purchases made with discount",
    'NumCatalogPurchases': "number of purchases made using a catalog",
    'NumStorePurchases': "number of purchases made directly in stores",
    'NumWebPurchases': "number of purchases made through the company's website",
    'NumWebVisitsMonth': "number of visits to the company's website in the last month",
    'Recency': "number of days since the last purchase",
}


# Function to generate a prompt based on the user's question and the column descriptions
def generate_prompt(question):
    column_info = "\n".join([f'{column} | {description}' for column, description in column_descriptions.items()])
    return f"""
Answer the question based on the context below. 
If the question cannot be answered using the information provided, answer with "I don't know".

Context: We have a df with customer information, which is named df.
Generate a SQL query to answer the following question based on the following schema.
Remove quotations from the queries, return the query in the following format: "~ [query] ~".
The headings are defined below and are in a "heading | description" format.

Headings:
{column_info}

Question: 
\"\"\"
{question}
\"\"\"

Answer: 
"""
