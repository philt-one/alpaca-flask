# Llama🦙Gen✨

A Flask-based API for generating text using the Llama C++ library. This API provides a simple interface for generating text with Llama's pre-trained language models. It accepts an input text and returns the generated output in JSON format.

## Features

- Built with Flask, a lightweight and easy-to-use web framework.
- Uses the Llama C++ library for efficient text generation.
- Handles JSON requests and responses for easy integration with other services.
- Configurable model path and default number of tokens.
- Includes error handling, logging, and environment variable support for model paths.

Usage:

1. Install Flask if you haven't already: `pip install flask`
2. Clone this repository and navigate to the project directory.
3. Set the environment variable `LLAMA_MODEL_PATH` to the path of your Llama model, if desired. Otherwise, you can download the [ggml-alpaca-7b-q4.bin](https://huggingface.co/Sosaka/Alpaca-native-4bit-ggml/blob/main/ggml-alpaca-7b-q4.bin)
4. Run the `main.py` file using the command `python main.py`. The API will start running at http://127.0.0.1:5000/.
5. To call the API, send a POST request with JSON data containing an 'input' key with your desired input text to the /generate endpoint.

```json
{
    "input": "What is the capital of France?"
}
```

```bash
curl -X POST \
  http://127.0.0.1:5000/generate \
  -H 'Content-Type: application/json' \
  -d '{"input": "What is the capital of France?"}'
```

The API will process the input and return the generated output in JSON format.

