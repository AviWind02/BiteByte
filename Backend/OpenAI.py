from openai import OpenAI

def generate_cooking_steps(ingredients, api_key):
    """Generate cooking steps using OpenAI's GPT based on the given ingredients."""
    client = OpenAI(api_key=api_key)  # Instantiate the client with the API key
    prompt = f"List the detailed cooking steps for preparing a dish with the following ingredients:\n{ingredients}\n"
    
    try:
        # Correct method usage as per the latest SDK documentation
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",  # Ensure the model name is correct as per your subscription or plan
            prompt=prompt,
            max_tokens=300,
            temperature=0.5
        )
        return response.choices[0].text.strip()  # Correctly access the text from the choices
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
