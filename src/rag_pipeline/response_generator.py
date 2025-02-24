import openai

class ResponseGenerator:
    def __init__(self, openai_api_key):
        self.api_key = openai_api_key
        openai.api_key = self.api_key

    def generate_response(self, query, documents):
        prompt = f"Given the documents: {documents}, answer the following question: {query}"
        response = openai.Completion.create(
            model="gpt-4",
            prompt=prompt,
            max_tokens=150
        )
        return response['choices'][0]['text']