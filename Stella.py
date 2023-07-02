import time
import sys
import inquirer
import webbrowser
from googlesearch import search
from datetime import date
from datetime import datetime
import os


def main():
    def delay_print(s):
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.1)
    url = "https://openai.com/chatgpt"
    today = date.today()
    now = datetime.now()
    dt = now.strftime("%H:%M:%S")
    # Textual month, day and year	
    d2 = today.strftime("%B %d, %Y")
    

    delay_print("Welcome to chat GPT V2.0")
    questions = [
      inquirer.List('p1',
                    message="Please Choose",
                    choices=["Rate-Us","Visit-Us","Quit", "Search-Something", "What-is-the-datetime"],
                ),
    ]   
    answers = inquirer.prompt(questions)
    delay_print (answers["p1"])


    if answers["p1"] == "Rate-Us":
        rating = input("\nEnter Amount  Of stars in Numbers: \n")
        delay_print("\n........\n")
        delay_print("\nTHANK YOU\n")

    elif answers["p1"] == "Visit-Us":
        webbrowser.open(url)
    
    
    elif answers["p1"] == "Quit":
        sys.exit()
    
    elif answers["p1"] == "Search-Something":
        query = input("\nEnter Some Value: \n")
        for i in search(query, tld="co.in", num=10, stop=10, pause=2):
            print(i)
            
    elif answers["p1"] == "What-is-the-datetime":
        print("\nToday is: \n", d2)
        print(" Time is: ", dt)
    
    else:
        print("ERR 404")
        
if __name__ == "__main__":
    main()
