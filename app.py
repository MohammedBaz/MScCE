Of course. You want a simpler solution: a single Streamlit app that contains the survey questions and collects the answers. This is a much more direct approach.

Here is the complete code for a Streamlit app that does exactly that.

### \#\# How to Use This Solution

1.  **Save the Code:** Save the code below as a Python file (e.g., `survey_app.py`).
2.  **Install Libraries:** If you haven't already, open your terminal and install Streamlit and Pandas:
    ```bash
    pip install streamlit pandas
    ```
3.  **Run the App:** In your terminal, navigate to where you saved the file and run:
    ```bash
    streamlit run survey_app.py
    ```

Your web browser will open with the interactive survey app.

-----

### \#\# Streamlit Survey App Code

```python
# survey_app.py
import streamlit as st
import pandas as pd

# --- Data Preparation ---
# 1. Store all your questions and sections in a structured way (a list of dictionaries)
survey_data = [
    {"Section": "أولاً: تنظيم المقرر وتخطيطه", "Statement": "تم عرض خطة المقرر بالتفصيل في بداية الفصل الدراسي."},
    {"Section": "أولاً: تنظيم المقرر وتخطيطه", "Statement": "تم عرض الدروس بأشكال وأساليب مختلفة بالتعلم الإلكتروني."},
    {"Section": "أولاً: تنظيم المقرر وتخطيطه", "Statement": "وضح عضو هيئة التدريس آلية تصحيح الاختبارات والأنشطة والتكليفات."},
    {"Section": "أولاً: تنظيم المقرر وتخطيطه", "Statement": "أتيح لي كيفية الحصول على الخدمات الأكاديمية في المقرر مثل الإرشاد الأكاديمي، ورفع الغياب."},
    {"Section": "ثانياً: التواصل والتفاعل", "Statement": "أتاح التعلم الإلكتروني لنا فرص متكافئة في المشاركة أثناء المحاضرة."},
    {"Section": "ثانياً: التواصل والتفاعل", "Statement": "أتاح لي التعلم الإلكتروني التواصل مع عضو هيئة التدريس."},
    {"Section": "ثانياً: التواصل والتفاعل", "Statement": "تتوفر اكثر من وسيلة للتواصل مع عضو هيئة التدريس."},
    {"Section": "ثانياً: التواصل والتفاعل", "Statement": "يتاح لي في التعلم الإلكتروني مناقشة زملائي فيما يرتبط بالمقرر وأنشطته."},
    {"Section": "ثانياً: التواصل والتفاعل", "Statement": "يتوفر لنا الدعم الفني في التعلم الإلكتروني."},
    {"Section": "ثانياً: التواصل والتفاعل", "Statement": "تلقيت تغذية راجعة عن أدائي في بعض المهام من قبل عضو هيئة التدريس."},
    {"Section": "ثانياً: التواصل والتفاعل", "Statement": "اشعر بالمتعة في الدراسة من خلال التعلم الإلكتروني."},
    {"Section": "ثالثاً: عناصر تصميم المقرر ووسائطه المتعددة", "Statement": "تنوعت الوسائط التعليمية التي تم عرض المقرر بها."},
    {"Section": "ثالثاً: عناصر تصميم المقرر ووسائطه المتعددة", "Statement": "تم تنفيذ وعرض المقرر بأسلوب شيق بالتعلم الإلكتروني."},
    {"Section": "ثالثاً: عناصر تصميم المقرر ووسائطه المتعددة", "Statement": "تثقيف التدريب والإرشاد عن كيفية الاستفادة القصوى من التعلم الإلكتروني."},
    {"Section": "ثالثاً: عناصر تصميم المقرر ووسائطه المتعددة", "Statement": "أتاحت لي الأنشطة التعليمية وأدوات المقرر فرصة للتفاعل مع المحتوى."},
    {"Section": "ثالثاً: عناصر تصميم المقرر ووسائطه المتعددة", "Statement": "تمكنت من متابعة ما تغيبت عنه من الدروس من خلال التعلم الإلكتروني."},
    {"Section": "ثالثاً: عناصر تصميم المقرر ووسائطه المتعددة", "Statement": "شجعني التعلم الإلكتروني على التعلم المستمر."},
    {"Section": "ثالثاً: عناصر تصميم المقرر ووسائطه المتعددة", "Statement": "تحسنت مهارتي في استخدام التكنولوجيا والاتصالت من خلال التعلم الإلكتروني."},
    {"Section": "رابعاً: المواد التعليمية والتقييمات", "Statement": "ارتبطت أهداف الوحدات الدراسية بالأهداف العامة للمقرر."},
    {"Section": "رابعاً: المواد التعليمية والتقييمات", "Statement": "الأنشطة والتكليفات التي تم تنفيذها بالتعلم الإلكتروني مرتبطة بالمقرر."},
    {"Section": "رابعاً: المواد التعليمية والتقييمات", "Statement": "يتم من خلال التعلم الإلكتروني تقديم تغذية راجعة فورية بعد الاختبار."},
    {"Section": "رابعاً: المواد التعليمية والتقييمات", "Statement": "يوفر التعلم الإلكتروني وقت الطالب."},
    {"Section": "خامساً: الرضا العام عن المقرر وعضو هيئة التدريس", "Statement": "شعر بالرضا عن شرح عضو هيئة التدريس في المقرر من خلال التعلم الإلكتروني."},
    {"Section": "خامساً: الرضا العام عن المقرر وعضو هيئة التدريس", "Statement": "بشكل عام أنا راضٍ عن هذا المقرر."},
]

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(survey_data)

# 2. Define the answer choices for the Likert scale
answer_options = [
    "لا أوافق بشدة",  # Strongly Disagree
    "لا أوافق",      # Disagree
    "أوافق الى حد ما", # Neutral / Agree to some extent
    "أوافق",        # Agree
    "أوافق بشدة"     # Strongly Agree
]

# --- Streamlit App UI ---
st.set_page_config(layout="wide")

st.title("📝 تقييم تجربة التعلم الإلكتروني")
st.markdown("---")

# Use a form to group all the radio buttons. This ensures all answers are collected at once on submit.
with st.form(key='survey_form'):
    
    responses = {}
    current_section = ""

    # Loop through each question in the DataFrame
    for index, row in df.iterrows():
        # Display a new section header if the section changes
        if row['Section'] != current_section:
            current_section = row['Section']
            st.header(current_section)
        
        # Display the question and the radio buttons for the answers
        # The unique key is essential for Streamlit to track each question's answer
        question_key = f"q_{index}"
        responses[question_key] = st.radio(
            label=row['Statement'],
            options=answer_options,
            horizontal=True,
            key=question_key
        )
    
    # Add a submit button to the form
    submit_button = st.form_submit_button(label='إرسال الإجابات (Submit Survey)')

# --- After Submission Logic ---
if submit_button:
    st.markdown("---")
    st.header("شكراً لك! تم تسجيل إجاباتك.")
    st.balloons()
    
    # Prepare the data for display and download
    results_data = []
    for index, row in df.iterrows():
        question_key = f"q_{index}"
        results_data.append({
            "Section": row['Section'],
            "Statement": row['Statement'],
            "Response": responses[question_key]
        })
    
    results_df = pd.DataFrame(results_data)
    
    # Display the results in a table
    st.dataframe(results_df)

    # Function to convert DataFrame to CSV for downloading
    @st.cache_data
    def convert_df_to_csv(df_to_convert):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df_to_convert.to_csv(index=False).encode('utf-8-sig') # Use utf-8-sig for Arabic compatibility

    csv = convert_df_to_csv(results_df)

    # Add a download button for the results
    st.download_button(
        label="📥 تحميل الإجابات كملف CSV (Download Responses as CSV)",
        data=csv,
        file_name='survey_responses.csv',
        mime='text/csv',
    )
```
