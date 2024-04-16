from openai import OpenAI
import pandas as pd
import ast
from youtube_search import YoutubeSearch

key = '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'
client = OpenAI(api_key=key)

def get_video(formula):
    
    results = YoutubeSearch('how to create ' + formula, max_results=20).to_dict()
    d = {
        'dict': results,
        'formula': formula
    }
    
    completion = client.chat.completions.create(
    model="gpt-4-0125-preview",
    messages=[
        {"role": "system", "content": "Given a dictionary of video fetched from youtube and a chemical formula. You must determine if there is a video in the dict describe the process of synthesizing the chemical formula. If There is, return a single string of the video's url_suffix. If there aren't any, return a single empty string. Do not answer anything differently from the rules."},
        {"role": "user", "content": str(d)}
    ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

