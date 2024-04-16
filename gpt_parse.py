from openai import OpenAI
import pandas as pd
import ast
from youtube_search import YoutubeSearch

key = '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'
client = OpenAI(api_key='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')

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
    #print(completion.choices[0].message.content)
    return completion.choices[0].message.content

df = pd.read_csv('parse_elements_2.csv')
df['formula_links'] = [[] for _ in range(len(df))]
for index, row in df.iterrows():
    #try:
    for item in ast.literal_eval(row['formulas']):
        try:
            row['formula_links'].append(str(get_video(str(item))))
        except:
            print('error')
            row['formula_links'].append('')
    #break

df.to_csv('parse_elements_3.csv',index=False)

