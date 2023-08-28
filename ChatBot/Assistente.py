import nltk
import random
from nltk.chat.util import Chat, reflections

# Defina os padrões de entrada e saída para o assistente
patterns = [
    (r'Olá|Oi|Oi!', ['Olá!', 'Oi!', 'Olá, como posso ajudar?']),
    (r'Qual é o seu nome?|Qual seu nome?|Quem você é?', ['Eu sou um assistente virtual.', 'Meu nome é Assistente Virtual 3000.']),
    (r'Como você está?|Como está se sentido?', ['Estou apenas um programa de computador, então não tenho emoções!', 'Estou bem, obrigado por perguntar!']),
    (r'Qual é o sentido da vida?', ['A resposta para essa pergunta é 42, de acordo com o Guia do Mochileiro das Galáxias.']),
    (r'Sair', ['Até logo!', 'Tchau!', 'Obrigado por ter utilizado o assistente virtual 3000!']),
]

# Crie o objeto Chat usando os padrões
chatbot = Chat(patterns, reflections)

# Função para interagir com o assistente
def chat_with_assistant():
    print("Assistente: Olá! Como posso ajudar?")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            print("Assistente: Até logo!")
            break
        response = chatbot.respond(user_input)
        print("Assistente:", response)

# Inicie a interação
if __name__ == "__main__":
    chat_with_assistant()
