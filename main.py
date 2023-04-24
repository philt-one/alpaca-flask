import os
from flask import Flask, request, jsonify
from llama_cpp import Llama

# Use an environment variable for the model path or fall back to the default path
DEFAULT_MODEL = os.environ.get("LLAMA_MODEL_PATH", "./models/ggml-alpaca-7b-q4.bin")
DEFAULT_N_TOKENS = 256

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    """Generate text using the Llama library."""
    input_str = request.json.get('input')
    
    if not input_str:
        return jsonify({"error": "Missing 'input' parameter"}), 400

    try:
        output = process_input_and_generate_output(input_str)
        return jsonify(output)
    except Exception as e:
        app.logger.error(f"Error generating text: {e}")
        return jsonify({"error": "An error occurred while generating text"}), 500

def process_input_and_generate_output(input_text):
    """Process the input text and generate output using the Llama library.

    Args:
        input_text (str): The input text for the Llama library.

    Returns:
        str: The generated output text.
    """
    llm = Llama(model_path=DEFAULT_MODEL)
    output = llm(f"Q: {input_text} A: ", max_tokens=DEFAULT_N_TOKENS, stop=["Q:", "\n"], echo=True)

    return output

if __name__ == '__main__':
    app.run(debug=True)
