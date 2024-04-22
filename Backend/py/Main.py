import sys
# Path where the APIKeys.py file is located
api_keys_path = 'E:\\Projects\\APIKeysPy'
# Add this path to sys.path to make it searchable for importing modules
sys.path.append(api_keys_path)

import json

from Edamam import fetch_recipes
from OpenAI import generate_cooking_steps
from APIKeys import APIKeys  # Importing after updating sys.path

def main():
    keys = APIKeys()
    query = 'chicken'
    try:
        recipes = fetch_recipes(query, keys.edamam_app_id, keys.edamam_app_key)
        if recipes and 'hits' in recipes and len(recipes['hits']) > 0:
            recipe = recipes['hits'][0]['recipe']  # Select the first recipe only
            ingredients = '\n'.join(recipe['ingredientLines'])
            print(f"Recipe: {recipe['label']}")
            print("Ingredients:")
            print(ingredients)

            try:
                steps = generate_cooking_steps(ingredients, keys.openai_api_key)
                recipe_details = {
                    "title": recipe['label'],
                    "ingredients": recipe['ingredientLines'],
                    "steps": steps.split('\n')  # Splitting steps into a list for better JSON structure
                }
                recipe_json = json.dumps(recipe_details, indent=4)
                print("Recipe Details in JSON Format:")
                print(recipe_json)
                return recipe_json  # This can be used by a web/app frontend
            except Exception as e:
                print(f"Error generating steps: {e}")
        else:
            print("No recipes found.")
    except Exception as e:
        print(f"Error fetching recipes: {e}")

if __name__ == "__main__":
    main()
