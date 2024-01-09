import streamlit as st
from transformers import pipeline

# 感情分析モデルのロード
classifier = pipeline('sentiment-analysis')

def main():
    st.title("Sentiment Analysis with Transformers and Streamlit")

    # ユーザーからのテキスト入力
    text_input = st.text_area("Enter text for sentiment analysis:", "")
    # st.write(f"{text_input}")

    # テキストの感情分析
    if st.button("Analyze Sentiment"):
        result = classifier(text_input)
        sentiment = result[0]['label']
        confidence = result[0]['score']

    #     # 結果の表示
        st.write(f"Sentiment: {sentiment}")
        st.write(f"Confidence: {confidence}")

        # generator = pipeline("text-generation", model = "rinna/japanese-gpt2-medium")
        # output = generator(text_input)
        # st.write(output)

if __name__ == "__main__":
    main()