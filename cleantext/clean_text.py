import json

def handler(event, context):
    # Retrieve the text from the event object
    input_text = event.get("input_0")
    
     # Validate presence of input to ensure there's a text for processing.
    if not input_text:
        return {"error": "No text provided"}

    # Replace hyphenated line-breaks with nothing to fix split words
    cleaned_text = input_text.replace('-\n', '')

    # Remove all remaining newline characters
    cleaned_text = cleaned_text.replace('\n', '')

    # Remove all form feed characters
    cleaned_text = cleaned_text.replace('\f', '')

    # Return the cleaned text as JSON
    return json.dumps({"input_0": cleaned_text})