import os
from dotenv import load_dotenv
import openai
import pandas as pd
from pandasql import sqldf, PandaSQLException

from prompt import generate_prompt


# Function to get an answer to a question
def get_answer(prompt, deployment_name):
    response = openai.Completion.create(
        engine=deployment_name,
        prompt=prompt
    )
    text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()

    # Find the first index of the "~" character
    start_index = text.find("~")

    # Find the first index of the "~" character after the start index
    end_index = text.find("~", start_index + 1)

    # Extract the text between the first "~" characters
    query = text[start_index + 1:end_index].strip()

    return query


def main():
    # Load the env variables
    load_dotenv()

    # Get the environment variables
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_base = os.getenv("OPENAI_API_BASE")
    openai.api_type = os.getenv("OPENAI_API_TYPE")
    openai.api_version = os.getenv("OPENAI_API_VERSION")
    deployment_name = os.getenv("DEPLOYMENT_NAME")

    # Read the csv file into a df
    df = pd.read_csv('data/ml_project1_data.csv')

    print("Welcome to the CSV Query Chat Bot. Type your question or 'q' to quit.")

    while True:
        user_input = input("Your question: ")
        if user_input.lower() == 'q':
            print("Exiting the CSV Query Chat.")
            break

        prompt = generate_prompt(user_input)
        response = get_answer(prompt, deployment_name)
        globals()['df'] = df

        def pysqldf(query):
            try:
                return sqldf(query, globals())
            except PandaSQLException:
                return "Unfortunately I did not understand, please rephrase the question."

        result_df = pysqldf(response)
        print(result_df)


if __name__ == '__main__':
    main()
