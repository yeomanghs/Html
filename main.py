import streamlit as st
import streamlit.components.v1 as components

AreaList = ['Data Manipulation/Wrangling',
            'Data Scraping',
            'Data Analysis & Visualization',
            'Machine Learning']

AreaToTaskList_Dict = {'Data Manipulation/Wrangling':['PdfToTable', 'Manipulate Excel Data'],
                        'Data Scraping':['Doctor Database', "Durham's website"],
                        'Data Analysis & Visualization':['Firm Performance', 'Spanish Sentiment Analysis'],
                        'Machine Learning':['Classification of Student Enrolment']}

TaskToFile_Dict = {
                    'PdfToTable':
                        {
                        'Title':'Converting PDF to Table',
                        'Filename':"FromPDFtoTable-Html.html"
                        },  
                    'Manipulate Excel Data':
                        {
                        'Title':'Manipulating and analyzing data in Excel',
                        'Filename':"2021-10-03_DataManipulation.html"
                        }, 
                    'Doctor Database':
                        {
                        'Title':'Scraping Data from Doctor Database',
                        'Filename':"Doctor website.html"
                        }, 
                    "Durham's website":
                        {
                        'Title':"Scraping Program from Durham's website",
                        'Filename':"Durham.html"
                        },         
                    'Firm Performance':
                        {
                        'Title':'Analysis of Firm Performance',
                        'Filename':"2021-12-11_DataAnalysisFinancialFirms.html"
                        },
                    'Spanish Sentiment Analysis':
                        {
                        'Title':'Spanish Sentiment Analysis',
                        'Filename':"2022-04-26_SentimentAnalysisSpanish_Html.html"
                        },
                    'Classification of Student Enrolment':
                        {
                        'Title':'Predicting if a student enrols',
                        'Filename':"2021-09-23_ML_Classification.html"
                        }                        
                    }

#sidebar to area
area = st.sidebar.radio("Select an area",
                        AreaList)

#select task 
task = st.selectbox('Select a task',
                        AreaToTaskList_Dict[area])

title = TaskToFile_Dict[task]['Title']
filename = TaskToFile_Dict[task]['Filename']
st.header(f"{title}")
HtmlFile = open(filename, 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height = 30000, width = 1500)