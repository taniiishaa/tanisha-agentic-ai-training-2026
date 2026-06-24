# Streamlit

## What is Streamlit?

Streamlit is an open-source Python framework used to build interactive web applications for Data Science, Machine Learning, Artificial Intelligence, and Data Visualization projects.

It allows developers to create web applications directly using Python without requiring knowledge of HTML, CSS, or JavaScript.

Streamlit automatically converts Python scripts into interactive web applications that can run in a browser.

---

# Why Streamlit?

Traditional web development requires:

* HTML
* CSS
* JavaScript
* Backend Frameworks

With Streamlit, everything can be built using only Python.

Benefits:

* Easy to learn
* Fast development
* Interactive UI components
* Ideal for AI and ML projects
* Real-time updates
* Open source

---

# Features of Streamlit

## 1. Pure Python Development

Applications are created entirely in Python.

Example:

```python
import streamlit as st

st.title("My First Streamlit App")
st.write("Hello World!")
```

---

## 2. Interactive Widgets

Streamlit provides built-in components such as:

* Buttons
* Checkboxes
* Radio buttons
* Sliders
* Select boxes
* Text inputs
* File uploaders
* Date pickers

Example:

```python
name = st.text_input("Enter your name")

if name:
    st.write("Welcome", name)
```

---

## 3. Data Visualization

Supports popular visualization libraries:

* Matplotlib
* Plotly
* Altair
* Seaborn
* Bokeh

Example:

```python
import pandas as pd
import streamlit as st

data = pd.DataFrame({
    "Sales": [10, 20, 30, 40]
})

st.line_chart(data)
```

---

## 4. Machine Learning Integration

Machine learning models can easily be connected to Streamlit applications.

Example:

```python
prediction = model.predict(data)

st.write(prediction)
```

---

## 5. File Upload Support

Users can upload files directly from the interface.

Example:

```python
uploaded_file = st.file_uploader("Choose a file")
```

---

## 6. Real-Time Updates

Whenever code changes, Streamlit automatically refreshes the application.

No manual browser refresh is needed.

---

# Installation

Install Streamlit using pip:

```bash
pip install streamlit
```

Verify installation:

```bash
streamlit --version
```

---

# Creating Your First Streamlit App

Create a file:

```text
app.py
```

Add the following code:

```python
import streamlit as st

st.title("Hello Streamlit")
st.write("My first web application")
```

Run the application:

```bash
streamlit run app.py
```

Output:

```text
Local URL: http://localhost:8501
```

---

# Streamlit Components

## Text Components

### Title

```python
st.title("Main Title")
```

### Header

```python
st.header("Header")
```

### Subheader

```python
st.subheader("Subheader")
```

### Text

```python
st.text("Simple Text")
```

### Write

```python
st.write("General Output")
```

### Markdown

```python
st.markdown("# Markdown Heading")
```

---

# Input Widgets

## Text Input

```python
name = st.text_input("Enter Name")
```

---

## Number Input

```python
age = st.number_input("Enter Age")
```

---

## Button

```python
if st.button("Submit"):
    st.write("Submitted")
```

---

## Checkbox

```python
agree = st.checkbox("I Agree")
```

---

## Radio Button

```python
choice = st.radio(
    "Select Language",
    ["Python", "Java", "C++"]
)
```

---

## Select Box

```python
language = st.selectbox(
    "Choose Language",
    ["Python", "Java", "C++"]
)
```

---

## Slider

```python
marks = st.slider(
    "Marks",
    0,
    100
)
```

---

# Displaying Data

## Table

```python
import pandas as pd

data = pd.DataFrame({
    "Name": ["Tanisha", "Shivani"],
    "Marks": [95, 90]
})

st.table(data)
```

---

## DataFrame

```python
st.dataframe(data)
```

---

# Charts in Streamlit

## Line Chart

```python
st.line_chart(data)
```

---

## Bar Chart

```python
st.bar_chart(data)
```

---

## Area Chart

```python
st.area_chart(data)
```

---

# Displaying Images

```python
from PIL import Image

img = Image.open("photo.jpg")

st.image(img)
```

---

# Displaying Videos

```python
video_file = open("video.mp4", "rb")

st.video(video_file)
```

---

# Displaying Audio

```python
audio_file = open("audio.mp3", "rb")

st.audio(audio_file)
```

---

# Sidebar

The sidebar helps create navigation menus.

Example:

```python
option = st.sidebar.selectbox(
    "Choose Page",
    ["Home", "About", "Contact"]
)
```

---

# Session State

Session State stores values across reruns.

Example:

```python
import streamlit as st

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increase"):
    st.session_state.count += 1

st.write(st.session_state.count)
```

---

# Forms

Forms collect multiple inputs together.

Example:

```python
with st.form("student_form"):

    name = st.text_input("Name")

    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write(name)
```

---

# Advantages of Streamlit

* Easy to learn
* Python-only development
* Fast deployment
* Interactive widgets
* Excellent for ML projects
* Open-source
* Automatic updates
* Built-in visualization support

---

# Limitations of Streamlit

* Limited frontend customization
* Not ideal for large-scale enterprise applications
* Less flexibility than React
* Fewer advanced UI options

---

# Streamlit vs Flask

| Feature           | Streamlit        | Flask                   |
| ----------------- | ---------------- | ----------------------- |
| Purpose           | Interactive Apps | Web Applications & APIs |
| Frontend Required | No               | Yes                     |
| Learning Curve    | Easy             | Moderate                |
| Development Speed | Fast             | Medium                  |
| Customization     | Limited          | High                    |

---

# Streamlit vs FastAPI

| Feature           | Streamlit | FastAPI   |
| ----------------- | --------- | --------- |
| Purpose           | Web Apps  | APIs      |
| Frontend Included | Yes       | No        |
| Performance       | Moderate  | High      |
| AI Dashboards     | Excellent | Good      |
| API Development   | Limited   | Excellent |

---


# Conclusion

Streamlit is one of the most popular frameworks for creating interactive Python-based web applications. It is widely used in Machine Learning, Artificial Intelligence, and Data Science because of its simplicity, speed, and ability to build professional web applications using only Python. It enables developers to focus on solving problems and building models rather than spending time on frontend development.
