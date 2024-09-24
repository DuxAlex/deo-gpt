from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a chave da API do OpenAI a partir das variáveis de ambiente
openai_api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Configura a chave da API do OpenAI
openai.api_key = openai_api_key

# Lista para armazenar o histórico de mensagens
lista_mensagens = [
    {"role": "system", "content": "Você é um chatbot projetado para ajudar pessoas com questões relacionadas ao autismo."}
]
@app.route('/enviar', methods=['POST'])
def enviar():
    data = request.get_json()
    mensagem = data.get('message', '')

    if not mensagem:
        return jsonify({"error": "Mensagem não pode ser vazia."}), 400

    resposta = enviar_mensagem(mensagem)

    return jsonify({"message": resposta['content']})

def enviar_mensagem(mensagem):
    lista_mensagens.append({"role": "user", "content": mensagem})

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=lista_mensagens,
    )

    return resposta["choices"][0]["message"]

if __name__ == '__main__':
    app.run(debug=True)
