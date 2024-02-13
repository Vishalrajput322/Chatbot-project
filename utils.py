import openai

#user query
#user responses
def get_initial_message():
    messages = [
        {"role":"user","content":"Hi, can you help me with some AI questions?"},
        {"role":"assistant","content":"ofcourse! What do you want to know?"}
    ]
    return messages

def get_chatgpt_response(messages,model):
    print("model:",model)
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages
    )
    return response['choices'][0]['message']['content']

def update_chat(messages,role,content):
    messages.append({"role":role,"content":content})
    return messages