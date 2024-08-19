const socket = io();
let messageElements = {};

socket.on('new_message', function(data) {
    console.log("Creating new message element with ID:", data.message_id);

    // Create a new message element
    const messageElement = document.createElement('div');
    messageElement.classList.add('bot');
    messageElement.setAttribute('data-message-id', data.message_id);
    messageElement.id = data.message_id; // Set the ID for the message
    document.getElementById('messages').appendChild(messageElement);

    messageElements[data.message_id] = messageElement;

    scrollToBottom();
});

socket.on('response', function(data) {
    if (data.type === 'bot') {
        const messageDiv = messageElements[data.message_id];
        messageDiv.innerHTML = data.message;
    }
});


function sendMessage() {
    let inputElement = document.getElementById('input');
    let messageElement = document.createElement('div');
    messageElement.textContent = 'You: ' + inputElement.value;
    messageElement.classList.add('user');
    document.getElementById('messages').appendChild(messageElement);

    socket.emit('message', { message: inputElement.value });
    inputElement.value = '';
    scrollToBottom();
}

function scrollToBottom() {
    const messages = document.getElementById('messages');
    messages.scrollTop = messages.scrollHeight;
}
