#Importing Packages

import streamlit as st
import pandas as pd
# Additional Packages
def Lecture11():
    # ***************** Displaying Colored Text/Bootsraps Alert: *****************
    st.success('Successful!')
    st.warning('Warning!!!')
    st.info('Informations: ')
    st.error('Some Error:')
    st.exception(' Some Exceptions: ')

    # ***************** SuperFunction st.write(): *****************

    st.write('Normal Text')
    st.write('## With Header')
    st.write(23+34)

    # ***************** Help Info: *****************
    st.help(range)
    st.help(dir(st))

def Lecture12(): 
    # LEcture 12/105 of https://www.udemy.com/course/learn-streamlit-python/learn

    # Working with and Displaying Text

    st.text("HEllo World from Mateus")
    st.write(dir(st))

    df = pd.read_csv("iris.csv")
    # ***************** Method 1: *****************
    st.dataframe(df)

    # Adding a color style from pandas
    st.dataframe(df.style.highlight_max(axis=0))
    # st.dataframe(df.style.highlight_min(axis=0))

    # ***************** Method 2: Static Table *****************
    # st.table(df)

    # ***************** Method 3: Using superfxn st.write *****************
    st.write(df.head())
   
    # ***************** Display JSON file: *****************
    st.json({
        'data':'name',
        'info' : 'Mateus'
    })

    # ***************** Display Code: *****************
    my_code = """
    def my_code():
        print("Hello from Mateus")
    """
    st.code(my_code, language='python')

def Lecture13():
    # Working with widgets
    # Buttons/Radio/Checkbox/Select


    # ***************** Buttons: *****************
    name = 'Mateus'

    if st.button('Submit'):
        st.write("My name is : {} . ".format(name.upper()))

    if st.button("Submit",key='new01'):
        st.write('{} is also my name.'.format(name.lower()))

    # ***************** RadioButtons: *****************
    status = st.radio("What is your status: ", ("Active" , "Inactive"))
    if status == 'Active':
        st.success('You are active.')
    else:
        st.error('Your are inactive')

    # ***************** CheckBox: *****************
    if st.checkbox("Show/Hide"):
        st.text("Showing smth")

    # ***************** Beta Expander: *****************
    with st.expander('Python'):
        st.success('Hello from Mateus')

def Lecture14():
    # ***************** Select /Multiple select: *****************
    my_lang = ['Python' , 'Portugues' , 'English' , 'Russian']
    choice = st.selectbox('Language' , my_lang)
    st.write('You selected language {} .'.format(choice))

    my_speaking_languages = st.multiselect('Spoken languages: ', my_lang, default='Portugues')

    # ***************** Slider: *****************
    # numbers (Int/Float/Dates):
    age = st.slider('Age' , 1,100,5)

    # Any datatype:

    color = st.select_slider('Choose Color' , options = ['yellow' , 'red' , 'blue' , 'black' , 'white'] , value=('yellow' , 'red'))

def Lecture15():
    # ***************** Media Files(videos/images/audio): *****************
    # Images: 
    from PIL import Image

    img = Image.open('/home/math/LearnStreamlit/Module01/data/image_03.jpg')
    st.image(img)

    # From URL:

    link = 'https://wallpaperaccess.com/full/472038.jpg'
    st.image(link)    

    # ***************** Videos: *****************
    path_to_video_file = '/home/math/LearnStreamlit/Module01/data/secret_of_success.mp4'
    video_file = open(path_to_video_file , 'rb').read()
    st.video(video_file, start_time=300)

    # ***************** Audio: *****************
    path_to_audio = '/home/math/LearnStreamlit/Module01/data/song.mp3'
    audio_file = open(path_to_audio , 'rb').read()
    st.audio(audio_file)

def Lecture16():
    # ***************** Text Input *****************
    fname = st.text_input('Enter Firstname: ')
    st.title(fname)
    # Hide  Password:
    password = st.text_input('Enter Password:',type='password')

    # ***************** Text Area *****************
    message = st.text_area('Enter Message: ')
    st.write(message)

    # ***************** Numbers: *****************
    number = st.number_input('Enter Number:', 1.0 , 25.0)

    # ***************** Date Input: *****************
    my_appointment = st.date_input('Appointment:  ')

    # ***************** Time Input: *****************
    mytime = st.time_input('My time : ')

    # ***************** Color Picker: *****************
    color = st.color_picker('Select Color:')

def Lecture17():
    # ***************** Conf Page: *****************
    st.set_page_config(page_title='My First Page',
    page_icon = '🇧🇷' , 
    layout = 'wide',
    initial_sidebar_state='collapsed')


    # ***************** Method 2 *****************
    # PAGE_CONFIG = {'page_title':'FirstPage' , 'page_icon': ':smiley:' , 'layout':'centered'}
    # st.set_page_config(**PAGE_CONFIG)

    st.title('My First Ever Streamlit Page 🤩✨🤪')
    st.sidebar.success('Menu')

def Lecture19():
    st.title('Plotting In Streamlit with plotly:')
    import pandas as pd
    import numpy as np
    import plotly.express as px


    df = pd.read_csv('./data/prog_languages_data.csv')
    st.dataframe(df)

    fig = px.pie(df , values='Sum' , names = 'lang' , title = 'Pie Chart of Languages')
    st.plotly_chart(fig)

    fig2 = px.bar(df , x = 'lang' , y = 'Sum')
    st.plotly_chart(fig2)

def Lecture20():
    path = '/home/math/LearnStreamlit/file_upload_app'
    pass

def Lecture21():
    path = '/home/math/LearnStreamlit/saveFileupload_app'
    pass

def Lecture22():
    # Working with multiple File Uploads
    pass

def Lecture23():
    # Working with multiple File Uploads
    path = '/home/math/LearnStreamlit/multi_app'
    pass

def Lecture24():
    # Working with multiple File Uploads
    path = '/home/math/LearnStreamlit/File_Downloader_App'
    pass

def Lecture25():
    path = '/home/math/LearnStreamlit/File_Downloader_App'
    pass

def Lecture26():
    st.title('Stremalit Forms & Salary Calculator')
    menu = ['Home' , 'About']
    choice = st.sidebar.selectbox('Menu' , menu)

    if choice == 'Home':
        st.subheader('Forms Tutorial')

        # Salary Calculator
        # Combine forms + Caolumns

        with st.form(key = 'salaryform' , clear_on_submit=True):  # Lecture 27 - clear_on_submit
            col1 , col2 , col3 = st.columns([3,2,1])

            with col1:
                amount = st.number_input('Hourly Rate in R$:')

            with col2:
                hour_per_week = st.number_input('Hours per week: ', 1 , 120)

            with col3:
                st.text('Salary:')
                submit_salary = st.form_submit_button(label = 'Calculate.')

        if submit_salary:
            with st.expander('Results:'):
                result = amount*hour_per_week*4
                st.write('Your salary is: {} . '.format(result))


        
        # Method 1: Context Manager Approach (with)

        with st.form(key = 'form1'):
            firstname = st.text_input('Firstname:')
            lastname = st.text_input('Lastname:')
            dob = st.date_input('Date of Birth:')

            # Important
            submit_button = st.form_submit_button(label= 'SignUp')

        # Results can be either form or outside

        if submit_button:
            st.success('Succesfully applied for name: {}.'.format(firstname))

        # Method 2: 
        form2 = st.form(key='form2')
        username = form2.text_input('Username')
        jobtype = form2.selectbox('Jobs:',['Dev' , 'DS' , 'Data Engineer'])
        submit_button2 = form2.form_submit_button('LogIn')

    else:
        st.subheader('About')



def main():
    """
    All your code goes here
    """
    # !!!!!!!!!!!!!!!!!! 'dir(arg)' built-in function !!!!!!!!!!!!!!!!!! 
    # Else, return an alphabetized list of names comprising (some of) the attributes
    st.title("Hello meus parcios *clap *clap")
    

if __name__ == '__main__':
    # main()
    # Lecture11()
    # Lecture12()
    # Lecture13()
    # Lecture14()
    # Lecture15()
    # Lecture16()
    # Lecture17()
    Lecture19()
    # Lecture20()
    # Lecture21()
    # Lecture22()
    # Lecture23()
    # Lecture24()
    # Lecture25()
    # Lecture26()