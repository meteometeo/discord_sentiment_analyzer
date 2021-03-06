from nltk.sentiment import SentimentIntensityAnalyzer
import tkinter as tk
import requests, json
from statistics import mean

def discord_sentiment_analyzer():

    sia = SentimentIntensityAnalyzer()
    compound = []
    flat_compound = []
    
    global compound_rate
    compound_rate = ''

    headers = {
        'authorization': str(authorization.get())
    }
    r = requests.get(
        f'https://discord.com/api/v9/channels/{str(channelId.get())}/messages', headers=headers)
    jsonn = json.loads(r.text)

    for value in jsonn:

        print(value['content'], '\n')

        polarity_score = sia.polarity_scores(value['content'])
        compound.append([polarity_score['compound']])

        print([polarity_score['compound']])

    for c in compound:
        for item in c:
            flat_compound.append(item)

    global compound_score
    compound_score = mean(flat_compound)    
        
    print(f'The compound score is: {compound_score}') 

    if compound_score >= 0.5:
        compound_rate = 'Positive'
        print("Overal sentiment is rated as positive")
    elif compound_score <= -0.5:
        compound_rate = 'Negative'
        print("Overal sentiment is rated as negative")    
    else:
        compound_rate = 'Neutral'
        print("Overal sentiment is rated as neutral")    

    btn_click(root)    

def discord_sentiment_analyzer_UI():
    global root
    root = tk.Tk()
    root.resizable(0,0)

    # Variables to initialize the above functions
    global authorization 
    authorization = tk.StringVar()
    global channelId 
    channelId = tk.StringVar()

    # Config of tkinter
    root.title('Dicord Sentiment Analyzer')
    root.geometry("512x384")

    # Intro label
    intro_text = tk.Label(text = 'Discord Sentiment Analyzer', bg = 'skyblue', padx = 150)
    intro_text.pack()
    intro_text.configure(font=("Courier", 16))

    # Authorization input
    authorization_label = tk.Label(text = 'Enter Authorization Token: ')
    authorization_entry =tk.Entry(textvariable = authorization)

    # Channel ID part
    channelId_label = tk.Label(text = 'Enter Discord Channel ID: ')
    channelId_entry = tk.Entry(textvariable = channelId)

    # Initialize the functions
    tk.Button(root,text = 'Enter', font = 'arial 15 bold' ,bg = 'pale violet red', command = discord_sentiment_analyzer).place(x=220 ,y = 160)

    # result_label = tk.Label(text = 'The result', foreground = 'red', font = (" ", 16))
    
    # Config of the labels and inputs
    authorization_label.place(x = 160, y = 50)
    authorization_entry.place(x = 5, y = 75, width = 500)
    channelId_label.place(x = 160, y = 105)
    channelId_entry.place(x = 5, y = 130, width = 500)

    root.mainloop()

def btn_click(root):
    root.destroy()
    
    # back to the first page
    def return_view():
        new_root.destroy()
        discord_sentiment_analyzer_UI()

    new_root = tk.Tk()
    new_root.geometry('512x384')
    new_root.resizable(0,0)
    new_root.title("Discord Sentiment Analyzer")
    
    # intro label
    intro_text = tk.Label(text = 'Discord Sentiment Analyzer', bg = 'skyblue', padx = 150)
    intro_text.pack()
    intro_text.configure(font=("Courier", 16))

    # compound label
    compound_score_label = tk.Label(text = f'The compound score is {compound_score}').place(x = 145, y = 50)

    # sentiment rate label
    sentiment_rate_label = tk.Label(text = f'The sentiment is rated as {compound_rate}').place(x = 145, y = 80)

    # button
    btn_return = tk.Button(new_root, text='Back', command=return_view)
    btn_return.place(x=225, y=110)
    new_root.mainloop()

discord_sentiment_analyzer_UI()
