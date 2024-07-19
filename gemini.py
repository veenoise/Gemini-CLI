import sys
from dotenv import load_dotenv
from os import getenv
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')
try:
    response = model.generate_content(sys.argv[1])
    print(f"\n-----End of Warning Messages-----\n\n{response.text}")
except IndexError:
    print("Pass in the query after the command!!!")
