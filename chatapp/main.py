from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from chatapp.config import initialize_openai_client
from chatapp.guard import guard_check, is_question_within_topic_fuzzy
from chatapp.chatbot import chatbot
from chatapp.speech import speak_text
import uuid
import mistune
app = Flask(__name__)
socketio = SocketIO(app)

# Initialize OpenAI client
client = initialize_openai_client()


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('message')
def handle_message(data):
    user_input = data['message']
    message_id = str(uuid.uuid4())
    emit('new_message', {'message_id': message_id, 'type': 'bot'})
    # Step 1: Check for safety
    if not guard_check(user_input, client):
        emit('response', {'message': 'Not safe for our ChatBot!', 'message_id': message_id, 'type': 'bot'})
        speak_text('Not safe for our ChatBot!')
        return

    # Step 2: Check if the topic is within allowed topics
    if not is_question_within_topic_fuzzy(user_input):
        emit('response', {'message': 'Not in the topic for the day', 'message_id': message_id, 'type': 'bot'})
        speak_text('Not in the topic for the day')
        return

    # Step 3: Generate and send response in chunks using the chatbot function

    response = chatbot(user_input)

    # Emit the new message event with the message_id

    for chunk in response:
        emit_chunk(chunk, message_id)


accumulated_markdown = {}


def emit_chunk(chunk, message_id):
    global accumulated_markdown
    if hasattr(chunk, 'choices') and len(chunk.choices) > 0:
        delta = chunk.choices[0].delta
        if hasattr(delta, 'content'):
            text = delta.content
            if text:
                if message_id not in accumulated_markdown:
                    accumulated_markdown[message_id] = ""
                accumulated_markdown[message_id] += text
                markdown = mistune.create_markdown()
                html_text = markdown(accumulated_markdown[message_id])
                emit('response', {'message': html_text, 'message_id': message_id, 'type': 'bot'})


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
