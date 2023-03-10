#import openai_secret_manager
import streamlit as st
import openai

# Use the openai API key
#openai.api_key = openai_secret_manager.get_secret("openai")["api_key"]

# Create a function that uses GPT-3 to generate text
def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

def write_email():
    api_key = st.text_input("Please enter OpenAI API key", "")
    openai.api_key = api_key

#     reason = st.selectbox("Select the reason for the email", ["Job Application", "Business Proposal", "Complaint", "Inquiry"])
#     recipient = st.text_input("Recipient's Email Address:")
#     st.write("Please provide more details about the email")
#     prompt = (f"Write an email for the reason {reason}")
#     details = st.text_area("Enter your message here")
#     prompt += ' '+ details
#     # Use GPT-3 to generate the email
#     message = generate_text(prompt)
#     st.write("Generated Email:")
#     st.write(message)
#     subject = st.text_input("Please enter email subject:", "")
#     prompt = (f"Write a email with the subject: {subject}")
#     message = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=2048, n =1,stop=None,temperature=0.5)
#     st.write("Email Message:")
#     st.write(message.choices[0].text)
    #api_key = st.text_input("Please enter OpenAI API key", "")
    #openai.api_key = api_key
    if openai.api_key:
        subject = st.text_input("Please enter email subject:", "")
        prompt = (f"Write a email with the subject: {subject}")
        message = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=2048, n =1,stop=None,temperature=0.5)
        st.write("Email Message:")
        st.write(message.choices[0].text)
    else:
        st.warning("API key is missing")
    
if __name__=="__main__":
    st.title("Email Writer using GPT-3")
    write_email()
