import openai
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
api_key = os.getenv('API_KEY')

client = openai.OpenAI(api_key=api_key)

def generate_blog(topic, tone="neutral"):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Write a paragraph about '{topic}' in a {tone} tone."}
            ],
            max_tokens=400,
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating content: {str(e)}"

def save_paragraph(topic, content):
    if not os.path.exists("blog_posts"):
        os.makedirs("blog_posts")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"blog_posts/{timestamp}_{topic.replace(' ', '_')[:30]}.txt"
    
    with open(filename, "w") as file:
        file.write(f"Topic: {topic}\n")
        file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        file.write(content)
    
    return filename

print("This tool helps you generate paragraphs using AI.")

session_paragraphs = []

keep_writing = True

while keep_writing:
    print("\n" + "-" * 50)
    answer = input('Write a paragraph? (Y for yes, anything else to quit): ')
    
    if answer.upper() == 'Y':
        topic = input('What should this paragraph be about? ')
        
        # Add tone selection feature
        print("\nChoose a tone:")
        print("1. Professional")
        print("2. Casual")
        print("3. Enthusiastic")
        print("4. Informative")
        tone_choice = input("Enter your choice (1-4) or press Enter for neutral: ")
        
        tone = "neutral"
        if tone_choice == "1":
            tone = "professional"
        elif tone_choice == "2":
            tone = "casual"
        elif tone_choice == "3":
            tone = "enthusiastic"
        elif tone_choice == "4":
            tone = "informative"
        
        print(f"\nGenerating {tone} paragraph about '{topic}'...\n")
        paragraph = generate_blog(topic, tone)
        
        print("=" * 50)
        print(paragraph)
        print("=" * 50)
        
        session_paragraphs.append({"topic": topic, "tone": tone, "content": paragraph})
        
        save_option = input("\nSave this paragraph to a file? (Y/N): ")
        if save_option.upper() == 'Y':
            filename = save_paragraph(topic, paragraph)
            print(f"Saved to: {filename}")
    else:
        keep_writing = False

if session_paragraphs:
    print("\n" + "=" * 50)
    print(f"Session Summary: Generated {len(session_paragraphs)} paragraphs")
    for i, para in enumerate(session_paragraphs, 1):
        print(f"{i}. '{para['topic']}' ({para['tone']} tone)")

print("\nThanks for using the Enhanced Blog Generator. Goodbye!")
