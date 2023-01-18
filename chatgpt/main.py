import os
import openai


def main():
    # You can sub in your key here!
    openai.api_key = os.getenv("API_KEY")

    query = input("Enter the query: ")
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=query,
            temperature=0.7,
            max_tokens=1000,
    )
    print(response["choices"][0]["text"])


if __name__ == '__main__':
    main()
