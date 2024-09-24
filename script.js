const sendButton = document.getElementById('sendButton');
const userInput = document.getElementById('userInput');
const chatbox = document.getElementById('chatbox');

// Função para adicionar mensagens ao chatbox
function addMessageToChatbox(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = sender === 'user' ? 'user-message' : 'bot-message';
    messageDiv.textContent = message;
    chatbox.appendChild(messageDiv);
    chatbox.scrollTop = chatbox.scrollHeight; // Rolar para baixo
}

// Envio da mensagem ao servidor
sendButton.addEventListener('click', () => {
    const userMessage = userInput.value.trim();
    if (userMessage === '') return;

    addMessageToChatbox(userMessage, 'user');
    userInput.value = '';

    fetch('http://127.0.0.1:5000/enviar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        const botMessage = data.message;
        addMessageToChatbox(botMessage, 'bot');
    })
    .catch(error => console.error('Erro:', error));
});
