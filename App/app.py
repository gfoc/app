from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Function to call OpenAI API and generate response
def generate_response(message):
    prompt = f'User: {message}\nAI:'
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def api():
    if request.method == 'POST':
        data = request.get_json()
        message = data['message']
        response = generate_response(message)
        return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
