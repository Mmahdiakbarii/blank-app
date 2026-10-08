import streamlit as st
from datetime import datetime

# تنظیم ثابت ظاهر برنامه
st.markdown("""
<style>

/* اجبار حالت روشن */
:root {
    color-scheme: light;
}


/* پس زمینه اصلی */
.stApp {
    background-color: #ffffff !important;
    direction: rtl;
}


/* متن‌های اصلی */
.stMarkdown,
.stMarkdown p,
.stMarkdown span,
.stMarkdown li,
label,
input {
    color: #111827 !important;
}


/* کارت‌ها */
.card,
.question-box {
    background-color: #ffffff !important;
    color: #111827 !important;
}


/* متن سوال‌ها */
.question-box {
    border: 1px solid #e5e7eb;
}


/* عنوان‌ها */
h1,
h2,
h3,
h4 {
    color: #111827 !important;
}


/* گزینه‌های پاسخ */
.stRadio label,
.stRadio span {
    color: #111827 !important;
}


/* ورودی متن */
.stTextInput input {
    background-color: #ffffff !important;
    color: #111827 !important;
}


/* دکمه‌ها */
.stButton button {
    color: white !important;
}


/* پیام‌ها */
.stAlert {
    color: inherit !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- تنظیمات صفحه ----------------

st.set_page_config(
    page_title="ارزیابی اولیه سازگاری زوجین",
    layout="centered"
)


# ---------------- استایل کامل فارسی ----------------

st.markdown("""
<style>

/* فونت */
html, body, [class*="css"] {
    font-family: "B Nazanin", Tahoma, Arial, sans-serif !important;
}


/* راست چین کلی */
.stApp {
    direction: rtl;
}


/* متن‌های عمومی */
.stMarkdown,
.stMarkdown p,
.stMarkdown li,
.stMarkdown span,
p,
li {
    direction: rtl !important;
    text-align: right !important;
}


/* تیترها */
h1, h2, h3, h4 {
    direction: rtl !important;
    text-align: right !important;
    color: #111827 !important;
}


/* عنوان اصلی */
.main-title {

    direction: rtl;

    text-align: center !important;

    font-size: 38px;

    font-weight: bold;

    color:#111827;

}


/* زیر عنوان */

.subtitle {

    direction: rtl;

    text-align:center !important;

    font-size:22px;

    color:#475569;

    margin-bottom:30px;

}



/* کارت‌ها */

.card {

    direction: rtl;

    text-align:right;

    background:#ffffff;

    padding:30px;

    border-radius:20px;

    border:1px solid #e5e7eb;

    box-shadow:
    0 8px 25px rgba(0,0,0,0.08);

}



/* عنوان بخش */

.section-title {

    direction:rtl;

    text-align:right !important;

    font-size:27px;

    font-weight:bold;

    color:#111827;

}



/* کارت سوال */

.question-box {

    direction:rtl;

    text-align:right !important;

    background:#f8fafc;

    color:#111827;

    padding:20px;

    border-radius:16px;

    border:1px solid #e2e8f0;

    margin-bottom:15px;

    font-size:20px;

    line-height:2;

}



/* ورودی متن */

.stTextInput {

    direction:rtl;

}


.stTextInput label {

    direction:rtl !important;

    text-align:right !important;

    color:#111827 !important;

}


.stTextInput input {

    direction:rtl !important;

    text-align:right !important;

}



/* گزینه‌های پاسخ */

.stRadio {

    direction:rtl !important;

}


.stRadio > div {

    direction:rtl !important;

}



/* افقی کردن پاسخ‌ها */

.stRadio [role="radiogroup"] {

    display:flex !important;

    flex-direction:row !important;

    justify-content:flex-start;

    gap:12px;

    direction:rtl;

}


.stRadio label {

    direction:rtl !important;

    text-align:center !important;

}



/* دکمه‌ها */

.stButton button {

    font-family:"B Nazanin",Tahoma,sans-serif;

    font-size:20px;

    border-radius:12px;

}



/* پیام‌ها */

.stAlert {

    direction:rtl !important;

    text-align:right !important;

}



/* نتیجه */

.result-box {

    direction:rtl;

    text-align:center;

    background:#eff6ff;

    padding:30px;

    border-radius:20px;

}



.score {

    font-size:55px;

    font-weight:bold;

    color:#2563eb;

    /* ===== اصلاح رنگ و خوانایی متن‌ها ===== */


/* متن‌های معمولی داخل برنامه */
.stMarkdown,
.stMarkdown p,
.stMarkdown span,
.stMarkdown li {
    color: #111827 !important;
}


/* کارت‌های سفید */
.card,
.card p,
.card li,
.question-box,
.question-box p {
    color: #111827 !important;
}


/* عنوان‌ها */
h1,
h2,
h3,
h4,
.section-title {
    color: #111827 !important;
}


/* زیرعنوان */
.subtitle {
    color: #475569 !important;
}


/* متن سوال‌ها */
.question-box {
    color: #111827 !important;
}


/* گزینه‌های پاسخ */
.stRadio label,
.stRadio span {
    color: #111827 !important;
}


/* نوشته داخل فیلد نام */
.stTextInput label {
    color: #111827 !important;
}


/* نوشته داخل کادر ورودی */
.stTextInput input {
    color: #111827 !important;
    background-color: #ffffff !important;
}


/* عدد درصد نتیجه */
.score {
    color: #2563eb !important;
}


/* دکمه‌ها */
.stButton button {
    color: white !important;
}


/* پیام‌های Streamlit مثل هشدار و اطلاع‌رسانی */
.stAlert,
.stAlert p {
    color: inherit !important;
}




</style>

""", unsafe_allow_html=True)



# ---------------- اطلاعات آزمون ----------------


questions = [

    {
        "topic":"مسائل مالی",
        "text":"در مورد شیوه مدیریت درآمد، هزینه‌ها و پس‌انداز، دیدگاه من با شریک عاطفی‌ام سازگار است."
    },

    {
        "topic":"فرزندآوری",
        "text":"در مورد داشتن یا نداشتن فرزند و نگرش کلی نسبت به فرزندآوری، دیدگاه من با شریک عاطفی‌ام سازگار است."
    },

    {
        "topic":"اهداف زندگی",
        "text":"در مورد اهداف مهم آینده، سبک زندگی و مسیر کلی زندگی، دیدگاه من با شریک عاطفی‌ام سازگار است."
    },

    {
        "topic":"حل اختلاف",
        "text":"در هنگام بروز اختلاف، درباره شیوه مناسب گفت‌وگو، حل مسئله و رسیدن به توافق، دیدگاه من با شریک عاطفی‌ام سازگار است."
    },

    {
        "topic":"نقش خانواده‌ها",
        "text":"در مورد میزان دخالت و نقش خانواده‌های دو طرف در زندگی مشترک، دیدگاه من با شریک عاطفی‌ام سازگار است."
    }

]


options = [
    "کاملاً مخالف",
    "مخالف",
    "ممتنع",
    "موافق",
    "کاملاً موافق"
]



# ---------------- حافظه موقت برنامه ----------------


if "page" not in st.session_state:
    st.session_state.page = 1


if "name1" not in st.session_state:
    st.session_state.name1 = ""


if "name2" not in st.session_state:
    st.session_state.name2 = ""


if "answers1" not in st.session_state:
    st.session_state.answers1 = []


if "answers2" not in st.session_state:
    st.session_state.answers2 = []



# ---------------- توابع ----------------


def persian_number(number):

    return str(number).translate(
        str.maketrans(
            "0123456789",
            "۰۱۲۳۴۵۶۷۸۹"
        )
    )



def calculate_agreement(a,b):

    diff = abs(a-b)

    scores = {
        0:100,
        1:75,
        2:50,
        3:25,
        4:0
    }

    return scores[diff]



def show_progress():

    steps = [
        "معرفی",
        "نفر اول",
        "نفر دوم",
        "نتیجه"
    ]

    current = st.session_state.page

    result=""

    for i,item in enumerate(steps,1):

        if i == current:
            result += f"🔵 {item}   "

        elif i < current:
            result += f"✅ {item}   "

        else:
            result += f"⚪ {item}   "

    st.write(result)



show_progress()
# ---------------- صفحه معرفی ----------------


if st.session_state.page == 1:


    st.markdown(
        '<div class="main-title">ارزیابی اولیه سازگاری زوجین</div>',
        unsafe_allow_html=True
    )


    st.markdown(
        '<div class="subtitle">بررسی اولیه هماهنگی دیدگاه‌های زوجین</div>',
        unsafe_allow_html=True
    )


    st.markdown("""
    <div class="card">


    <div class="section-title">
    هدف ارزیابی
    </div>


    <p>
    این ابزار یک نمونه اولیه آموزشی برای بررسی میزان نزدیکی
    دیدگاه‌های دو نفر درباره موضوعات مهم زندگی مشترک است.
    </p>


    <br>


    <div class="section-title">
    ساختار آزمون
    </div>


    <ul>

    <li>۵ سؤال برای هر نفر</li>

    <li>
    پاسخ‌دهی با مقیاس پنج درجه‌ای
    از کاملاً مخالف تا کاملاً موافق
    </li>

    <li>
    موضوعات:
    مسائل مالی، فرزندآوری، اهداف زندگی،
    حل اختلاف و نقش خانواده‌ها
    </li>

    </ul>


    <div class="section-title">
    نحوه اجرا
    </div>


    <p>
    ابتدا نفر اول پاسخ می‌دهد.
    سپس نفر دوم پاسخ‌های خود را ثبت می‌کند.
    در پایان میزان توافق دو نفر محاسبه می‌شود.
    </p>


    </div>

    """, unsafe_allow_html=True)



    st.info(
        """
        پاسخ‌ها در این نسخه اولیه ذخیره دائمی نمی‌شوند
        و فقط برای محاسبه نتیجه همین اجرا استفاده می‌شوند.
        """
    )



    st.caption(
        """
    
نتایج  شما به صورت محرمانه نزد ما نگه داری می شود         """
    )


    if st.button(
        "شروع ارزیابی",
        use_container_width=True
    ):

        st.session_state.page = 2
        st.rerun()





# ---------------- صفحه نفر اول ----------------


elif st.session_state.page == 2:


    st.markdown(
        '<div class="section-title">پاسخ‌های نفر اول</div>',
        unsafe_allow_html=True
    )


    st.session_state.name1 = st.text_input(
        "نام نفر اول",
        value=st.session_state.name1
    )


    answers=[]


    for i,q in enumerate(questions):


        st.markdown(
            f"""
            <div class="question-box">

            {persian_number(i+1)} -
            {q["text"]}

            </div>
            """,
            unsafe_allow_html=True
        )


        answer = st.radio(
            "انتخاب پاسخ",
            options,
            horizontal=True,
            key=f"p1_{i}"
        )


        answers.append(
            options.index(answer)+1
        )



    if st.button(
        "ادامه به نفر دوم",
        use_container_width=True
    ):


        if not st.session_state.name1:


            st.error(
                "لطفاً نام نفر اول را وارد کنید."
            )


        else:

            st.session_state.answers1 = answers

            st.session_state.page = 3

            st.rerun()





# ---------------- صفحه نفر دوم ----------------


elif st.session_state.page == 3:


    st.markdown(
        '<div class="section-title">پاسخ‌های نفر دوم</div>',
        unsafe_allow_html=True
    )


    st.session_state.name2 = st.text_input(
        "نام نفر دوم",
        value=st.session_state.name2
    )


    answers=[]


    for i,q in enumerate(questions):


        st.markdown(
            f"""
            <div class="question-box">

            {persian_number(i+1)} -
            {q["text"]}

            </div>
            """,
            unsafe_allow_html=True
        )


        answer = st.radio(
            "انتخاب پاسخ",
            options,
            horizontal=True,
            key=f"p2_{i}"
        )


        answers.append(
            options.index(answer)+1
        )



    if st.button(
        "نمایش نتیجه",
        use_container_width=True
    ):


        if not st.session_state.name2:


            st.error(
                "لطفاً نام نفر دوم را وارد کنید."
            )


        else:


            st.session_state.answers2 = answers

            st.session_state.page = 4

            st.rerun()





# ---------------- صفحه نتیجه ----------------


elif st.session_state.page == 4:


    st.markdown(
        '<div class="main-title">نتایج ارزیابی</div>',
        unsafe_allow_html=True
    )


    results=[]


    for i in range(5):

        score = calculate_agreement(
            st.session_state.answers1[i],
            st.session_state.answers2[i]
        )

        results.append(score)



    overall = round(
        sum(results)/len(results)
    )



    st.markdown(
        f"""

        <div class="result-box">

        <div>
        درصد توافق کلی
        </div>


        <div class="score">
        {persian_number(overall)}٪
        </div>


        </div>

        """,
        unsafe_allow_html=True
    )



    st.subheader(
        "نتیجه هر موضوع"
    )



    report = f"""
گزارش ارزیابی اولیه سازگاری زوجین

نفر اول:
{st.session_state.name1}

نفر دوم:
{st.session_state.name2}


"""


    for i,q in enumerate(questions):


        st.markdown(
            f"""
            <div class="question-box">

            <b>
            {q["topic"]}
            </b>

            <br><br>

            میزان توافق:
            {persian_number(results[i])}٪

            </div>
            """,
            unsafe_allow_html=True
        )


        st.progress(
            results[i]/100
        )


        report += (
            f"{q['topic']} : "
            f"{results[i]} درصد\n"
        )



    report += (
        f"\nدرصد توافق کلی: {overall} درصد\n"
    )



    st.download_button(
        "دانلود گزارش نتیجه",
        data=report,
        file_name="couple_report.txt",
        mime="text/plain",
        use_container_width=True
    )



    if st.button(
        "شروع ارزیابی جدید",
        use_container_width=True
    ):


        st.session_state.page = 1

        st.session_state.name1 = ""

        st.session_state.name2 = ""

        st.session_state.answers1 = []

        st.session_state.answers2 = []


        st.rerun()
