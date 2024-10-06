from groq import Groq
import os

groq_client = Groq(api_key="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")

def generate_response(user_query, context_response):
    combined_content = f"Context: {context_response}\nUser's query: {user_query}"
    
    chat_completion = groq_client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant for solar system and planets."},
            {"role": "user", "content": combined_content},
        ],
        model="llama3-8b-8192",
        temperature=0.5,
        max_tokens=1024,
    )
    
    return chat_completion.choices[0].message.content