import streamlit as st
import openai

st.set_page_config(page_title="プログラミングサポートAI", layout="wide")

st.title("英語教師を超すAIです")
st.caption("Created by Daiki Ito")
 
st.write('初めての方は右のリンクから「Sign up」をしてAPIキーを取得してください',
         'https://beta.openai.com'
         '/account/api-keys')

# 質問フォーム
with st.form(key='input_form'):
    st.write("こんにちは！英語に関する質問をしてください。")
    st.write("質問は具体的なほうが的確にアドバイスをくれます。")
    st.write("日本語と英語の区別をつけるためにかっこをつけてください。")
    input_prompt = '''あなたは英語学習アシスタントです。ユーザは高校生で、あなたに英語に関する質問を投げかけます。あなたは高校の英語教師の代わりに高校の教員として、英語の日本語訳や文法、論理構造に関する回答をわかりやすく、長文で、可能な限り根拠を示して以下の######内の質問に返してください。'''
    input_apikey = st.text_input("取得したAPIキーを貼り付けてください")
    input_text = st.text_area("質問を入力してください")
    submitted = st.form_submit_button('質問する')

 

if submitted:
    with st.spinner("考え中…"):
        openai.api_key = input_apikey
        response = openai.Completion.create(
            # テスト
            engine="text-davinci-003",
            prompt=input_prompt+"###"+input_text+"###",
            temperature=0,
            max_tokens=2048,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0
        )

 

    st.write("返答:", response['choices'][0]['text'])

 

st.write('差し支えなければアンケートへのご協力をお願いします。→', 'https://forms.gle/ADcoMh1zQUnoZVub7', 'まで')
st.write('© 2022-2023 Daiki Ito. All Rights Reserved.')
