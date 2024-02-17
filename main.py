import os
from openai import OpenAI
import customtkinter as ctk

#Functionality Part

def generate():
    language = language_dropdown.get()
    difficulty = difficulty_value.get()
    prompt=f"Please generate 10 ideas for {language} programming project and the level of difficulty should be {difficulty}."
    if checkbox1.get():
        prompt += "The project should have database."
    if checkbox2.get():
        prompt += "The project should also include an API."

    client = OpenAI(
        api_key='API_KEY',
    )
    chat_completion = client.completions.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    answer = chat_completion.choices[0].message['content']
    result.insert("0.0", answer)

#GUI Part
root = ctk.CTk()
root.geometry("750x550")
root.title("Project Idea Generator")
ctk.set_appearance_mode("dark")
title_label = ctk.CTkLabel(root, text="Project Idea Generator",
                              font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack (padx=10, pady= (40, 20))
frame = ctk.CTkFrame (root)
frame.pack(fill="x", padx=100)

language_frame = ctk.CTkFrame(frame)
language_frame.pack(padx=100, pady=(20, 5), fill="both")
language_label=ctk.CTkLabel(
    language_frame, text="Programming Language", font=ctk.CTkFont (weight="bold"))
language_label.pack()
language_dropdown = ctk.CTkComboBox(
    language_frame, values=["Python", "Java", "C++", "JavaScript", "PHP"])
language_dropdown.pack(pady=10)

difficulty_frame = ctk.CTkFrame(frame)
difficulty_frame.pack(padx=100, pady=5, fill='both')
difficulty_label = ctk.CTkLabel(
    difficulty_frame, text="Project Difficulty", font=ctk.CTkFont (weight="bold"))
difficulty_label.pack()

difficulty_value = ctk. StringVar(value="Easy")
radiobutton1 = ctk.CTkRadioButton(
    difficulty_frame, text="Easy", variable=difficulty_value, value="Easy")
radiobutton1.pack(side="left", padx=(20, 10), pady=10)
radiobutton2 = ctk.CTkRadioButton(
    difficulty_frame, text="Medium", variable=difficulty_value, value="Medium")
radiobutton2.pack(side="left", padx=10, pady=10)
radiobutton3 = ctk.CTkRadioButton(
    difficulty_frame, text="Hard", variable=difficulty_value, value="Hard")
radiobutton3.pack(side="left", padx=10, pady=10)

features_frame = ctk.CTkFrame(frame)
features_frame.pack(padx=100, pady=5, fill="both")
features_label = ctk.CTkLabel(
    features_frame, text="Features", font=ctk.CTkFont (weight="bold"))
features_label.pack()
checkbox1 = ctk.CTkCheckBox(features_frame, text="Database")
checkbox1.pack(side="left", padx=50, pady=10)
checkbox2 = ctk.CTkCheckBox (features_frame, text="API")
checkbox2.pack(side="left", padx=50, pady=10)

button = ctk.CTkButton (frame, text="Give me Ideas", command=generate)
button.pack(padx=100, fill="x", pady=(5, 20))

result = ctk.CTkTextbox(root, font=ctk.CTkFont(size=15))
result.pack(pady=10, fill="x", padx=100)

root.mainloop()