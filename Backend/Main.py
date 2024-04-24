import sys
import json

# Path where the APIKeys.py file is located
api_keys_path = 'E:\\Projects\\APIKeysPy'
# Add this path to sys.path to make it searchable for importing modules
sys.path.append(api_keys_path)

from Edamam import fetch_recipes
from OpenAI import generate_cooking_steps
from APIKeys import APIKeys

def get_recipe_details(query):
    keys = APIKeys()
    try:
        recipes = fetch_recipes(query, keys.edamam_app_id, keys.edamam_app_key)
        if recipes and 'hits' in recipes and len(recipes['hits']) > 0:
            recipe = recipes['hits'][0]['recipe']
            ingredients = '\n'.join(recipe['ingredientLines'])
            steps = generate_cooking_steps(ingredients, keys.openai_api_key)
            recipe_details = {
                "title": recipe['label'],
                "ingredients": recipe['ingredientLines'],
                "steps": steps.split('\n')
            }
            return recipe_details
        else:
            return {"error": "No recipes found."}
    except Exception as e:
        return {"error": f"Error processing your request: {str(e)}"}
