import nltk
from flask import Flask, render_template, redirect, session, request, flash
from werkzeug.utils import secure_filename
from nltk.stem import WordNetLemmatizer
from flask_mail import Mail, Message
from keras.models import load_model
from langdetect import detect
import mysql.connector
from gtts import gTTS
import numpy as np
import pygame
import random
import pickle
import string
import time
import json
import ast
import os

#IMPORT ALL REQUIRED FILES
model = load_model('./training/model.h5')
intents = json.loads(open('./training/data.json', 'r', encoding='utf-8').read())
words = pickle.load(open('./training/texts.pkl','rb'))
classes = pickle.load(open('./training/labels.pkl','rb'))

# LIBRARY FUNCTION
nltk.download('popular')
lemmatizer = WordNetLemmatizer()

# CLEAN UP SENTENCES - TOKENIZE, LEMMATIZE USER REQUEST
def clean_up_sentence(sentence):
    # TOKENIZE USER REQUEST
    sentence_words = nltk.word_tokenize(sentence)

    # LEMMATIZE TOKEN - GETTING THE ROOT FORM OF THE WORD
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

#BOW - INDEXING USER REQUEST
def bow(sentence, words, show_details=True):
    # TOKENIZING USER REQUEST
    sentence_words = clean_up_sentence(sentence)

    # BAG OF WORDS - MATRIX OF N WORDS, VOCABULARY MATRIX - INDEXING
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                # ASSIGN 1 IF CURRENT WORD IS IN THE VOCABULARY POSITION
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

#PREDICT CLASS FROM MODEL DATA
def predict_class(sentence, model):
    # FILTER OUT PREDICTIONS BELOW A THRESHOLD - HANDLING USER REQUEST
    p = bow(sentence, words,show_details=False)
    print(p)
    # PREDICT CLASS FRO MODEL
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]

    # SORT BY STRENGTH OF PROBABILITY
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

# DETECT ENGLISH LANGUAGE
def is_english(CHATBOT_RESPONSE):
    if detect(CHATBOT_RESPONSE)=="en":
        return True
    english_letters = set(string.ascii_letters)
    for char in CHATBOT_RESPONSE:
        if char==" ":
            continue
        if char not in english_letters:
            return False
    return True

def is_bangla(CHATBOT_RESPONSE):
    if detect(CHATBOT_RESPONSE)=="bn":
        return True
    else:
        return False

#REMOVE MP3 FILE
def remove_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)    

def bangla_voice(text):
        #MAKING THE AUDIO
    global filepath
    tts = gTTS(text=text, lang='bn')
    filename='voice_response_'+str(random.randint(0, 9))+'.mp3'
    filepath = os.path.join('static', 'audio', filename).replace('\\', '/')
    remove_file(filepath)
    tts.save(filepath)

    # Initialize Pygame
    pygame.display.init()
    pygame.mixer.init()

    # Play audio file
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()
    endevent = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(endevent)
    while True:
        for event in pygame.event.get():
            if event.type == endevent:
                pygame.mixer.music.stop()
                pygame.display.quit()
                return
        pygame.time.Clock().tick(10)

    remove_file(filepath)

def english_voice(text):
    # MAKING THE AUDIO
    global filepath
    tts = gTTS(text=text, lang='en')
    filename = 'voice_response_' + str(random.randint(0, 9)) + '.mp3'
    filepath = os.path.join('static', 'audio', filename).replace('\\', '/')
    remove_file(filepath)
    tts.save(filepath)

    # Initialize Pygame
    pygame.display.init()
    pygame.mixer.init()

    # Play audio file
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()
    endevent = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(endevent)
    while True:
        for event in pygame.event.get():
            if event.type == endevent:
                pygame.mixer.music.stop()
                pygame.display.quit()
                return
        pygame.time.Clock().tick(10)

    remove_file(filepath)


def voice_response(CHATBOT_RESPONSE):
    if is_bangla(CHATBOT_RESPONSE):
        return bangla_voice(CHATBOT_RESPONSE)
    elif is_english(CHATBOT_RESPONSE):
        return english_voice(CHATBOT_RESPONSE)

#GETTING CHATBOT RESPONSE
def getResponse(ints, intents_json, msg):
    # print("Loading")
    # print(str(is_english(msg)))
    # print(str(is_bangla(msg)))
    # print(ints)
    # print(ints[0])
    print(float(ints[0]["probability"]))
    if len(ints)!=0 and float(ints[0]["probability"])>.5:
        tag = ints[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if(i['tag']== tag):
                result = random.choice(i['responses'])
                break
    else:
        if(is_english(msg)):
            result="Please ask relevant questions. And give us feedback for future improvement"
        elif(is_bangla(msg)):
            result="অনুগ্রহ করে প্রাসঙ্গিক প্রশ্ন জিজ্ঞাসা করুন. এবং ভবিষ্যতের উন্নতির জন্য আমাদের মতামত দিন"
    return result

# CHATBOT REQUEST & RESPONSE
def chatbot_response(msg):
    # print(msg)
    # CHATBOT REQUEST
    ints = predict_class(msg, model)
    # print(ints)
    # CHATBOT RESPONSE
    res = getResponse(ints, intents, msg)
    # print(res)
    return res

#=============================================FLASK SETUP=============================================#
app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nstuchatbot@gmail.com'
app.config['MAIL_PASSWORD'] = "dmrnhnfpexkkgdpj"
app.config['MAIL_USE_SSL'] = True 

mail = Mail(app)

#=============================================MY SQL CONNECTION=============================================#
conn = mysql.connector.connect(host="localhost", user="root", password="", database="chatbot_application")
cursor = conn.cursor()

#=============================================HANDLING BOT RESPONSE=============================================#
@app.route("/get")
def get_bot_response():
    # GETTING USER TEXT
    global USER_TEXT, CHATBOT_RESPONSE
    USER_TEXT = request.args.get('msg')

    if is_bangla(USER_TEXT) or is_english(USER_TEXT):
        # GETTING BOT RESPONSE, ACCORDING TO USER REQUEST
        CHATBOT_RESPONSE = chatbot_response(USER_TEXT)
        voice_response(CHATBOT_RESPONSE)

        if 'user_id' in session:
            user=session["user_id"]
        elif 'admin_id' in session:
            user=session['admin_id']
        elif 'student_id' in session:
            user=session['student_id']
        elif 'teacher_id' in session:
            user=session['teacher_id']

        # INSERTING USER REQUEST & BOT RESPONSE
        cursor.execute("INSERT INTO queries(user_id, user_text, chatbot_response) VALUES (%s,%s,%s)",(user, USER_TEXT, CHATBOT_RESPONSE))
        conn.commit()
    else:
        CHATBOT_RESPONSE="Invalid Language"

    return CHATBOT_RESPONSE
#=============================================USER FEEDBACK=============================================#
@app.route('/user_feedback', methods=['POST'])
def user_feedback():
    #GETTING DATA
    feed_back_type = request.form.get('feed_back_type')
    feed_back_msg = request.form.get('feed_back_msg')

    #INSERTING INTO DATABASE
    cursor.execute("INSERT INTO feed_back(feed_back_msg,feed_back_type,user_text,bot_response) VALUES (%s,%s,%s,%s)",(feed_back_msg,feed_back_type,USER_TEXT,CHATBOT_RESPONSE))
    conn.commit()

    #SUCCESSFULL SUBMISSION
    flash("Feedback Submitted")
    return redirect('/')

@app.route('/')
def index():
    cursor.execute("SELECT * FROM about_nstu ORDER BY id DESC LIMIT 1")
    last_row = cursor.fetchone()[1]
    words = last_row.split()
    about_info = " ".join(words[:60])

    cursor.execute("SELECT * FROM vc_corner ORDER BY id DESC LIMIT 1")
    last_row = cursor.fetchone()
    name = last_row[1]
    image = last_row[3]
    words = last_row[2].split()
    speech = " ".join(words[:30])

    cursor.execute("SELECT * FROM news ORDER BY time DESC")
    news = cursor.fetchall()

    cursor.execute("SELECT * FROM notices ORDER BY upload_time DESC")
    notices = cursor.fetchall()

    cursor.execute("SELECT * FROM events ORDER BY event_date DESC")
    events = cursor.fetchall()

    return render_template('index.html', about_info= about_info, vc_name=name, vc_image= image, vc_speech=speech, news=news, events=events, notices=notices)

@app.route('/home')
def home():
    cursor.execute("SELECT * FROM about_nstu ORDER BY id DESC LIMIT 1")
    last_row = cursor.fetchone()[1]
    words = last_row.split()
    about_info = " ".join(words[:60])

    cursor.execute("SELECT * FROM vc_corner ORDER BY id DESC LIMIT 1")
    last_row = cursor.fetchone()
    name = last_row[1]
    image = last_row[3]
    words = last_row[2].split()
    speech = " ".join(words[:30])

    cursor.execute("SELECT * FROM news ORDER BY time DESC")
    news = cursor.fetchall()

    cursor.execute("SELECT * FROM notices ORDER BY upload_time DESC")
    notices = cursor.fetchall()

    cursor.execute("SELECT * FROM events ORDER BY event_date DESC")
    events = cursor.fetchall()

    return render_template('index.html', about_info= about_info, vc_name=name, vc_image= image, vc_speech=speech, news=news, events=events, notices=notices)

@app.route('/iit')
def iit():
    return render_template('./academic/institutes/iit.html')

@app.route('/iis')
def iis():
    return render_template('./academic/institutes/iis.html')

@app.route('/faculties')
def faculties():
    return render_template('./academic/faculties/faculties.html')

@app.route('/institutes')
def institutes():
    return render_template('./academic/institutes/institutes.html')

@app.route('/acce')
def acce():
    return render_template('./academic/faculties/acce.html')

@app.route('/agriculture')
def agriculture():
    return render_template('./academic/faculties/agriculture.html')

@app.route('/aplied_math')
def aplied_math():
    return render_template('./academic/faculties/aplied_math.html')

@app.route('/bangla')
def bangla():
    return render_template('./academic/faculties/bangla.html')

@app.route('/bge')
def bge():
    return render_template('./academic/faculties/bge.html')

@app.route('/bmb')
def bmb():
    return render_template('./academic/faculties/bmb.html')

@app.route('/bms')
def bms():
    return render_template('./academic/faculties/bms.html')

@app.route('/chemistry')
def chemistry():
    return render_template('./academic/faculties/chemistry.html')

@app.route('/cste')
def cste():
    return render_template('./academic/faculties/cste.html')

@app.route('/dba')
def dba():
    return render_template('./academic/faculties/dba.html')

@app.route('/economics')
def economics():
    return render_template('./academic/faculties/economics.html')

@app.route('/education_administration')
def education_administration():
    return render_template('./academic/faculties/education_administration.html')

@app.route('/education')
def education():
    return render_template('./academic/faculties/education.html')

@app.route('/eee')
def eee():
    return render_template('./academic/faculties/eee.html')

@app.route('/english')
def english():
    return render_template('./academic/faculties/english.html')

@app.route('/esdm')
def esdm():
    return render_template('./academic/faculties/esdm.html')

@app.route('/fims')
def ftns():
    return render_template('./academic/faculties/ftns.html')

@app.route('/ice')
def ice():
    return render_template('./academic/faculties/ice.html')

@app.route('/law')
def law():
    return render_template('./academic/faculties/law.html')

@app.route('/mis')
def mis():
    return render_template('./academic/faculties/mis.html')

@app.route('/oceanography')
def oceanography():
    return render_template('./academic/faculties/oceanography.html')

@app.route('/pharmacy')
def pharmacy():
    return render_template('./academic/faculties/pharmacy.html')

@app.route('/physics')
def physics():
    return render_template('./academic/faculties/physics.html')

@app.route('/social_work')
def social_work():
    return render_template('./academic/faculties/social_work.html')

@app.route('/sociology')
def sociology():
    return render_template('./academic/faculties/sociology.html')

@app.route('/soil_water_environment')
def soil_water_environment():
    return render_template('./academic/faculties/soil_water_environment.html')

@app.route('/stat')
def stat():
    return render_template('./academic/faculties/stat.html')

@app.route('/thm')
def thm():
    return render_template('./academic/faculties/thm.html')

@app.route('/zoology')
def zoology():
    return render_template('./academic/faculties/zoology.html')

@app.route('/cyber_center')
def cyber_center():
    return render_template('./centers/cyber_center.html')

@app.route('/medical_center')
def medical_center():
    return render_template('./centers/medical_center.html')

@app.route('/academic_program')
def academic_program():
    return render_template('./academic/academic_program/academic_programs.html')

@app.route('/deans')
def deans():
    return render_template('./office/deans.html')

@app.route('/audit_cell')
def audit_cell():
    return render_template('./office/audit_cell.html')

@app.route('/dpdw')
def dpdw():
    return render_template('./office/dpdw.html')

@app.route('/accounts_office')
def accounts_office():
    return render_template('./office/accounts_office.html')

@app.route('/exam_controller')
def exam_controller():
    return render_template('./office/exam_controller.html')

@app.route('/physical_education')
def physical_education():
    return render_template('./office/physical_education.html')

@app.route('/about_nstu')
def about_nstu():
    cursor.execute("SELECT * FROM about_nstu ORDER BY id DESC LIMIT 1")
    last_row = cursor.fetchone()
    return render_template('./about/about_nstu.html', data=last_row)

@app.route('/about')
def about():
    return render_template('./about/about_nstu.html')

@app.route('/location')
def location():
    return render_template('./about/location.html')

@app.route('/mission_vission')
def mission_vision():
    return render_template('./about/mission_vision.html')

@app.route('/visit_nstu')
def visit_nstu():
    return render_template('./about/visit_nstu.html')

@app.route('/acts_and_facts')
def acts_and_facts():
    return render_template('./about/acts_and_facts.html')

@app.route('/central_library')
def central_library():
    return render_template('./about/central_library.html')

@app.route('/academic_buildings')
def academic_buildings():
    return render_template('./miscellaneous/academic_buildings.html')

@app.route('/auditorium')
def auditorium():
    return render_template('./miscellaneous/auditorium.html')

@app.route('/emergency')
def emergency():
    return render_template('./miscellaneous/emergency.html')

@app.route('/forms_and_downloads')
def forms_and_downloads():
    return render_template('./miscellaneous/forms_and_downloads.html')

@app.route('/halls')
def halls():
    return render_template('./miscellaneous/halls.html')

@app.route('/noc_and_go')
def noc_and_go():
    return render_template('./miscellaneous/noc_and_go.html')

@app.route('/officers_association')
def officers_association():
    return render_template('./miscellaneous/officers_association.html')

@app.route('/sexual_harassment_prevention')
def sexual_harassment_prevention():
    return render_template('./miscellaneous/sexual_harassment_prevention.html')

@app.route('/teachers_association')
def teachers_association():
    return render_template('./miscellaneous/teachers_association.html')

@app.route('/welfare')
def welfare():
    return render_template('./miscellaneous/welfare.html')

@app.route('/chancellor')
def chancellor():
    cursor.execute("SELECT * FROM chancellor_corner ORDER BY id DESC LIMIT 1")
    last_row = cursor.fetchone()

    return render_template('./administration/chancellor.html', data= last_row)

@app.route('/provicechancellor')
def provicechancellor():
    cursor.execute("SELECT * FROM provc_corner ORDER BY id DESC LIMIT 1")
    last_row = cursor.fetchone()
    return render_template('./administration/provicechancellor.html', data= last_row)

@app.route('/regentboard')
def regentboard():
    return render_template('./administration/regentboard.html')

@app.route('/register')
def register():
    cursor.execute("SELECT * FROM register_corner ORDER BY id DESC LIMIT 1")
    last_row = cursor.fetchone()
    return render_template('./administration/register.html', data= last_row)

@app.route('/sexualharasshment')
def sexualharasshment():
    return render_template('./administration/sexualharasshment.html')

@app.route('/treasurer')
def treasurer():
    cursor.execute("SELECT * FROM treasurer_corner ORDER BY id DESC LIMIT 1")
    last_row = cursor.fetchone()
    return render_template('./administration/treasurer.html', data= last_row)

@app.route('/vicechancellor')
def vicechancellor():
    cursor.execute("SELECT * FROM vc_corner ORDER BY id DESC LIMIT 1")
    last_row = cursor.fetchone()

    return render_template('./administration/vicechancellor.html', data= last_row)

@app.route('/info_window')
def info_window():
    return render_template('./about/info_window.html')

@app.route('/jobs')
def jobs():
    cursor.execute("SELECT * FROM job ORDER BY time DESC")
    rows = cursor.fetchall()
    return render_template('./other/jobs.html', data= rows)

@app.route('/news')
def news():
    cursor.execute("SELECT * FROM news ORDER BY time DESC")
    rows = cursor.fetchall()
    return render_template('./other/news.html', data= rows)

@app.route('/notices')
def notices():
    cursor.execute("SELECT * FROM notices ORDER BY upload_time DESC")
    rows = cursor.fetchall()
    return render_template('./other/notices.html', data= rows)

@app.route('/events')
def events():
    cursor.execute("SELECT * FROM events ORDER BY event_date DESC")
    rows = cursor.fetchall()
    return render_template('./other/events.html', data= rows)

@app.route('/publications')
def publications():
    cursor.execute("SELECT * FROM publications ORDER BY publication_date DESC")
    rows = cursor.fetchall()
    return render_template('./other/publications.html', data= rows)

@app.route('/teacher')
def teacher():
    if 'teacher_id' in session:
        return  render_template('./teacher/index.html', TITLE="Profile")
    else:
        return redirect('/teacher/login')

@app.route('/teacher/login')
def teacher_login():
    if 'teacher_id' in session:
        return redirect('/teacher')
    else:
        return  render_template('./teacher/login.html')

@app.route('/teacher/profile')
def teacher_profile():
    if 'teacher_id' in session:
        return render_template('./teacher/index.html', TITLE="Profile")
    else:
        return redirect('/teacher/login')

@app.route('/teacher/password')
def teacher_password():
    if 'teacher_id' in session:
        return render_template('./teacher/password.html', TITLE="Change Password")
    else:
        return redirect('/teacher/login')

@app.route('/teacher/contact')
def teacher_contact():
    if 'teacher_id' in session:
        cursor.execute("SELECT `email`, `phone`, `linkedin`, `facebook`, `twitter` FROM teacher WHERE email = %s ",(session["teacher_id"],))
        users = cursor.fetchall()
        return render_template('./teacher/contact.html', TITLE="Contact", info=users[0])
    else:
        return redirect('/teacher/login')

@app.route('/teacher/about')
def teacher_about():
    if 'teacher_id' in session:
        cursor.execute("SELECT `name`, `designation`, `department`, `image`, `about` FROM teacher WHERE email = %s ",(session["teacher_id"],))
        users = cursor.fetchall()        
        return render_template('./teacher/about.html', TITLE="About", info=users[0])
    else:
        return redirect('/teacher/login')

@app.route('/teacher/degree')
def teacher_degree():
    if 'teacher_id' in session:
        cursor.execute("SELECT  `degree` FROM `teacher` WHERE email=(%s)",(session['teacher_id'],))
        degree = cursor.fetchall()
        return render_template('./teacher/degree.html', TITLE="Add Degree",degree_list=json.loads(degree[0][0]))
    else:
        return redirect('/teacher/login')
        
@app.route('/teacher/journal')
def teacher_journal():
    if 'teacher_id' in session:
        cursor.execute("SELECT  `journal` FROM `teacher` WHERE email=(%s)",(session['teacher_id'],))
        journal = cursor.fetchall()
        return render_template('./teacher/journal.html', TITLE="Add Journal", journal_list=json.loads(journal[0][0]))
    else:
        return redirect('/teacher/login')


@app.route('/student_profile')
def student():
    if 'student_id' in session:
        return  render_template('./student_profile/index.html', TITLE="Profile")
    else:
        return redirect('/student_profile/login')

@app.route('/student_profile/login')
def student_login():
    if 'student_id' in session:
        return redirect('/student_profile')
    else:
        return  render_template('./student_profile/login.html')

@app.route('/student_profile/password')
def student_password():
    if 'student_id' in session:
        return render_template('./student_profile/password.html', TITLE="Change Password")
    else:
        return redirect('/student_profile/login')

@app.route('/student_profile/contact')
def student_contact():
    if 'student_id' in session:
        cursor.execute("SELECT `email`, `phone`, `linkedin`, `facebook`, `twitter` FROM student WHERE email = %s ",(session["student_id"],))
        users = cursor.fetchall()
        return render_template('./student_profile/contact.html', TITLE="Contact", info=users[0])
    else:
        return redirect('/student_profile/login')

@app.route('/student_profile/about')
def student_about():
    if 'student_id' in session:
        cursor.execute("SELECT `name`, `designation`, `department`, `image`, `about`, `student_id`, `session` FROM student WHERE email = %s ",(session["student_id"],))
        users = cursor.fetchall()        
        return render_template('./student_profile/about.html', TITLE="About", info=users[0])
    else:
        return redirect('/student_profile/login')

@app.route('/student_profile/degree')
def student_degree():
    if 'student_id' in session:
        cursor.execute("SELECT  `degree` FROM `student` WHERE email=(%s)",(session['student_id'],))
        degree = cursor.fetchall()
        return render_template('./student_profile/degree.html', TITLE="Add Degree", degree_list=json.loads(degree[0][0]))
    else:
        return redirect('/student_profile/login')
        
@app.route('/student_profile/journal')
def student_journal():
    if 'student_id' in session:
        cursor.execute("SELECT  `journal` FROM `student` WHERE email=(%s)",(session['student_id'],))
        journal = cursor.fetchall()
        return render_template('./student_profile/journal.html', TITLE="Add Journal", journal_list=json.loads(journal[0][0]))
    else:
        return redirect('/student_profile/login')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('./not_found.html')

@app.route('/login')
def login():
    if 'user_id' in session:
        return redirect('/')        
    return  render_template('./auth/login.html')

@app.route('/registration')
def registration():
    if 'user_id' in session:
        return redirect('/')
    return  render_template('./auth/registration.html')

@app.route('/otp_verfication')
def otp_verfication():
    if ('email' in session) and ('fname' in session) and ('lname' in session) and ('pwd' in session) and ('otp' in session):
        return  render_template('./auth/otp_verification.html')
    else:
        return  redirect('/registration')

@app.route('/<department>/faculties')
def display_faculties(department):
    cursor.execute("SELECT `id`, `name`, `designation`, `image` FROM `teacher` WHERE department=(%s)",(department,))
    faculty = cursor.fetchall()
    if(len(faculty)>0):
        return render_template('./faculty/faculties.html', info=faculty)    
    else:
        return render_template('./not_found.html')

@app.route('/faculty/<teacher_id>')
def faculty_profile(teacher_id):
    cursor.execute("SELECT `name`, `designation`, `department`, `image`, `about`, `email`, `phone`, `linkedin`, `facebook`, `twitter` FROM `teacher` WHERE id=(%s)",(teacher_id,))
    faculty = cursor.fetchall()

    if(len(faculty)>0):
        cursor.execute("SELECT  `journal` FROM `teacher` WHERE email=(%s)",(faculty[0][5],))
        journal = cursor.fetchall()
        cursor.execute("SELECT  `degree` FROM `teacher` WHERE email=(%s)",(faculty[0][5],))
        degree = cursor.fetchall()

        return render_template('./faculty/faculty.html', info=faculty[0], degree_list=json.loads(degree[0][0]), journal_list=json.loads(journal[0][0]))
    else:
        return render_template('./not_found.html')

@app.route('/<department>/students')
def display_students(department):
    cursor.execute("SELECT `name`, `session`, `designation`, `image`, `student_id` FROM `student` WHERE department=(%s)",(department,))
    students = cursor.fetchall()
    if(len(students)>0):
        return render_template('./student/students.html', info=students)    
    else:
        return render_template('./not_found.html')

@app.route('/student/<student_id>')
def student_profile(student_id):
    cursor.execute("SELECT `name`, `student_id`, `designation`, `department`, `session`, `image`, `about`, `email`, `phone`, `linkedin`, `facebook`, `twitter`, `research_interest` FROM `student` WHERE student_id=(%s)",(student_id,))
    student = cursor.fetchall()

    if(len(student)>0):
        cursor.execute("SELECT  `journal` FROM `student` WHERE email=(%s)",(student[0][7],))
        journal = cursor.fetchall()
        cursor.execute("SELECT  `degree` FROM `student` WHERE email=(%s)",(student[0][7],))
        degree = cursor.fetchall()

        return render_template('./student/student.html', info=student[0], degree_list=json.loads(degree[0][0]), journal_list=json.loads(journal[0][0]))
    else:
        return render_template('./not_found.html')

@app.route('/admin')
def admin():
    if 'admin_id' in session:
        cursor.execute("SELECT * FROM admin WHERE email=(%s)",(session['admin_id'],))
        admin = cursor.fetchall()
        conn.commit()
        return  render_template('./admin/index.html', admin_info = admin[0], TITLE="Dashboard")
    else:
        return redirect('/admin/login')

@app.route('/admin/profile')
def admin_profile():
    if 'admin_id' in session:
        cursor.execute("SELECT * FROM admin WHERE email=(%s)",(session['admin_id'],))
        admin = cursor.fetchall()
        conn.commit()
        return  render_template('./admin/profile.html', admin_info = admin[0], TITLE="Profile")
    else:
        return redirect('/admin/login')

@app.route('/admin/chatbot')
def admin_chatbot():
    if 'admin_id' in session:
        cursor.execute("SELECT * FROM admin WHERE email=(%s)",(session['admin_id'],))
        admin = cursor.fetchall()
        conn.commit()

        cursor.execute("SELECT id,feed_back_msg, user_text, bot_response FROM feed_back WHERE feed_back_type=(%s)",("false",))
        feedback_data = cursor.fetchall()
        conn.commit()

        return  render_template('./admin/chatbot.html', admin_info = admin[0], TITLE="ChatBot", feedback_data=feedback_data)
    else:
        return redirect('/admin/login')

@app.route('/admin/notices')
def admin_notice():
    if 'admin_id' in session:
        cursor.execute("SELECT * FROM admin WHERE email=(%s)",(session['admin_id'],))
        admin = cursor.fetchall()
        conn.commit()

        return render_template('./admin/notices.html', TITLE="Notices", admin_info = admin[0])
    else:
        return redirect('/admin/login')

@app.route('/admin/about_nstu')
def admin_about_nstu():
    if 'admin_id' in session:
        cursor.execute("SELECT * FROM admin WHERE email=(%s)",(session['admin_id'],))
        admin = cursor.fetchall()
        conn.commit()

        return render_template('./admin/about_nstu.html', TITLE="About", admin_info=admin[0])
    else:
        return redirect('/admin/login')

@app.route('/admin/chancellor_corner')
def admin_chancellor_corner():
    if 'admin_id' in session:
        return render_template('./admin/chancellor_corner.html', TITLE="Chancellor")
    else:
        return redirect('/admin/login')

@app.route('/admin/vc_corner')
def admin_vc_corner():
    if 'admin_id' in session:
        return render_template('./admin/vc_corner.html', TITLE="VC")
    else:
        return redirect('/admin/login')

@app.route('/admin/pro_vc_corner')
def admin_pro_vc_corner():
    if 'admin_id' in session:
        return render_template('./admin/pro_vc_corner.html', TITLE="Pro VC")
    else:
        return redirect('/admin/login')

@app.route('/admin/add_teacher')
def add_teacher():
    if 'admin_id' in session:
        return render_template('./admin/add_teacher.html', TITLE="Add Teacher")
    else:
        return redirect('/admin/login')

@app.route('/admin/remove_teacher')
def remove_teacher():
    if 'admin_id' in session:
        return render_template('./admin/remove_teacher.html', TITLE="Remove Teacher")
    else:
        return redirect('/admin/login')

@app.route('/admin/add_student')
def add_student():
    if 'admin_id' in session:
        return render_template('./admin/add_student.html', TITLE="Add Student")
    else:
        return redirect('/admin/login')

@app.route('/admin/remove_student')
def remove_student():
    if 'admin_id' in session:
        return render_template('./admin/remove_student.html', TITLE="Remove Student")
    else:
        return redirect('/admin/login')

@app.route('/admin/treasurer_corner')
def admin_treasurer_corner():
    if 'admin_id' in session:
        return render_template('./admin/treasurer_corner.html', TITLE="Treasurer")
    else:
        return redirect('/admin/login')

@app.route('/admin/register_corner')
def admin_register_corner():
    if 'admin_id' in session:
        return render_template('./admin/register_corner.html', TITLE="Register")
    else:
        return redirect('/admin/login')

@app.route('/admin/job_circular')
def admin_job_circular():
    if 'admin_id' in session:
        return render_template('./admin/job_circular.html', TITLE="Job Circular")
    else:
        return redirect('/admin/login')

@app.route('/admin/add_news')
def admin_add_news():
    if 'admin_id' in session:
        return render_template('./admin/add_news.html', TITLE="Add News")
    else:
        return redirect('/admin/login')

@app.route('/admin/add_event')
def admin_add_event():
    if 'admin_id' in session:
        return render_template('./admin/add_event.html', TITLE="Add Event")
    else:
        return redirect('/admin/login')

@app.route('/admin/add_research')
def admin_add_research():
    if 'admin_id' in session:
        return render_template('./admin/add_research.html', TITLE="Add Research")
    else:
        return redirect('/admin/login')

#=============================================ADD NEW QUERY BASED ON FEEDBACK=============================================#
@app.route('/admin/add_query', methods=['POST'])
def add_query():
    tag=request.form.get('tag')
    patterns=request.form.get('patterns')
    responses=request.form.get('responses')
    context=request.form.get('context')
    query_id=int(request.form.get('query_id'))

    cursor.execute("INSERT INTO new_query_data(id, tag, patterns, responses, context) VALUES (%s,%s,%s,%s,%s)",(query_id,tag,patterns,responses,context))
    cursor.execute("DELETE FROM feed_back WHERE id=(%s)",(query_id,))
    conn.commit()

    flash("Query Added")
    return redirect('/admin/chatbot')

#=============================================REMOVING FEEDBACK=============================================#
@app.route('/delete_feedback', methods=['POST'])
def delete_feedback():
    feed_back_id = int(request.form.get('feed_back_id'))

    cursor.execute("DELETE FROM feed_back WHERE id=%s", (feed_back_id,))
    conn.commit()

    flash("Feedback Deleted")
    return redirect('/admin/chatbot')

@app.route('/admin/login')
def admin_login():
    if 'admin_id' in session:
        return redirect('/admin')
    return  render_template('./admin/login.html')

#=============================================USER REGISTRTION VALIDATION=============================================#
@app.route('/registration_validation', methods=['POST'])
def register_validation():

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    pwd = request.form.get('pwd')

    if not len(pwd) >= 5:
        flash('Password must be at least 5 characters in length')
        return render_template('registration.html')
    else:
        cursor.execute("SELECT * FROM user WHERE email = %s", (email,))
        target = cursor.fetchall()
        conn.commit()

        if len(target)>0:
            flash("Email Already Register")
            return redirect('/registration')
        else:
            otp = random.randint(10000,99999)
            session["otp"]=otp
            session["fname"]=fname
            session["lname"]=lname
            session["email"]=email
            session["pwd"]=pwd

            message = Message('OTP Verfication',sender='nstuchatbot@gmail.com',recipients=[email])
            message.html=render_template('email_template.html',otp=otp)

            mail.send(message)
            flash("Email Sent Successfully")

            return redirect('/otp_verfication')

# =============================================OTP VALIDATION PAGE=============================================#
@app.route('/otp_validation',methods=['POST'])
def otp_validation():
    if int(request.form.get('otp'))==int(session["otp"]):
        cursor.execute("INSERT INTO user (fname,lname,email,pwd) VALUES (%s,%s,%s,%s)", (session["fname"], session["lname"], session["email"], session["pwd"]))
        conn.commit()

        cursor.execute("SELECT * FROM user WHERE email = %s AND pwd = %s ", (session["email"], session["pwd"]))
        users = cursor.fetchall()
        
        if len(users) > 0:
            session['user_id'] = users[0][3]
            flash('Registration Successfully!')
            return redirect('/')
        else:
            flash('Invalid Email Or Password')
            return redirect('/registration')
    else:
        flash("Invalid OTP")
        return  redirect('/otp_verfication')

# =============================================USER LOGIN VALIDATION=============================================#
@app.route('/login_validation', methods=['POST'])
def login_validation():
    if 'admin_id' in session:
        session.pop('admin_id')

    email = request.form.get('email')
    pwd = request.form.get('pwd')

    cursor.execute("SELECT * FROM user WHERE email = %s AND pwd = %s ", (email, pwd))
    users = cursor.fetchall()

    if len(users) > 0:
        session['user_id'] = users[0][3]
        flash('Logged in Successfully!')
        return redirect('/')
    else:
        flash('Invalid Email Or Password')
        return redirect('/')

@app.route('/admin/admin_login_validation', methods=['POST'])
def admin_login_validation():
    if 'user_id' in session:
        session.pop('user_id')

    email = request.form.get('email')
    pwd = request.form.get('pwd')

    cursor.execute("SELECT * FROM admin WHERE email = %s AND password = %s ", (email, pwd))
    users = cursor.fetchall()

    if len(users) > 0:
        session['admin_id'] = users[0][2]
        return redirect('/admin')
    else:
        flash('Invalid Credentials')
        return redirect('/admin/login')
@app.route('/admin/change_admin_password', methods=['POST'])
def change_admin_password():
    name = request.form.get('name')
    password = request.form.get('password')

    cursor.execute("UPDATE admin SET password = %s, name = %s WHERE email = %s", (password, name, session['admin_id']))
    conn.commit()

    return redirect('/admin/profile')

@app.route('/admin/change_admin_picture', methods=['Post'])
def change_admin_picture():
    file = request.files.get('file')
    if file.filename == '':
        flash("No Picture Selected")
        return redirect('/admin/profile')

    filename = secure_filename(file.filename)
    name, ext = os.path.splitext(filename)

    cursor.execute("SELECT * FROM admin WHERE email = %s ",(session["admin_id"],))
    users = cursor.fetchall()

    file_path = os.path.join(app.root_path, 'static', 'images/admin', users[0][4])

    if os.path.exists(file_path):
        os.remove(file_path)

    new_filename = f"{users[0][1]}{ext}"
    file.save(os.path.join(app.root_path, 'static', 'images/admin', new_filename))

    cursor.execute("UPDATE admin SET profile_picture = %s WHERE email = %s", (new_filename, session['admin_id']))
    conn.commit()

    flash("Picture Changed Successfully")
    return redirect('/admin/profile')

@app.route('/admin/upload_notice', methods=['POST'])
def upload_notice():
    title = request.form['titleInput']
    noticefile = request.files['file']
    imagefile = request.files['imagefile']

    if noticefile.filename == '' or imagefile.filename == '':
        flash("No File Selected")
        return redirect('/admin/notices')

    filename = secure_filename(noticefile.filename)
    name, ext = os.path.splitext(filename)
    new_notice_filename = f"{title}{ext}"
    noticefile.save(os.path.join(app.root_path, 'static', 'notices', new_notice_filename))

    filename = secure_filename(imagefile.filename)
    name, ext = os.path.splitext(filename)
    new_image_filename = f"{title}{ext}"
    imagefile.save(os.path.join(app.root_path, 'static', 'images/notices', new_image_filename))

    cursor.execute("INSERT INTO `notices`(`title`, `file_name`, `image`) VALUES (%s,%s,%s)", (title, new_notice_filename, new_image_filename))
    conn.commit()

    flash("Notice Uploaded Successfully")
    return redirect('/admin/notices')

@app.route('/admin/upload_vc_corner', methods=['POST'])
def upload_vc_corner():
    vc_name = request.form['vcNameInput']
    file = request.files['file']
    speech = request.form['vcSpeechInput']

    if file.filename == '':
        flash("No File Selected")
        return redirect('/admin/vc_corner')

    filename = secure_filename(file.filename)
    name, ext = os.path.splitext(filename)

    new_filename = f"{vc_name}{ext}"
    file.save(os.path.join(app.root_path, 'static', 'images/vc', new_filename))

    cursor.execute("INSERT INTO `vc_corner`(`name`, `speech`, `image`) VALUES (%s, %s, %s)", (vc_name, speech, new_filename))
    conn.commit()

    flash("Uploaded Successfully")
    return redirect('/admin/vc_corner')

@app.route('/admin/upload_chancellor_corner', methods=['POST'])
def upload_chancellor_corner():
    chancellor_name = request.form['chancellorNameInput']
    file = request.files['file']
    speech = request.form['chancellorSpeechInput']

    if file.filename == '':
        flash("No File Selected")
        return redirect('/admin/chancellor_corner')

    filename = secure_filename(file.filename)
    name, ext = os.path.splitext(filename)

    new_filename = f"{chancellor_name}{ext}"
    file.save(os.path.join(app.root_path, 'static', 'images/chancellor', new_filename))

    cursor.execute("INSERT INTO `chancellor_corner`(`name`, `speech`, `image`) VALUES (%s, %s, %s)", (chancellor_name, speech, new_filename))
    conn.commit()

    flash("Uploaded Successfully")
    return redirect('/admin/chancellor_corner')

@app.route('/admin/upload_register_corner', methods=['POST'])
def upload_register_corner():
    register_name = request.form['registerNameInput']
    file = request.files['file']
    speech = request.form['registerSpeechInput']

    if file.filename == '':
        flash("No File Selected")
        return redirect('/admin/register_corner')

    filename = secure_filename(file.filename)
    name, ext = os.path.splitext(filename)

    new_filename = f"{register_name}{ext}"
    file.save(os.path.join(app.root_path, 'static', 'images/register', new_filename))

    cursor.execute("INSERT INTO `register_corner`(`name`, `speech`, `image`) VALUES (%s, %s, %s)", (register_name, speech, new_filename))
    conn.commit()

    flash("Uploaded Successfully")
    return redirect('/admin/register_corner')

@app.route('/admin/upload_treasurer_corner', methods=['POST'])
def upload_treasurer_corner():
    treasurer_name = request.form['treasurerNameInput']
    file = request.files['file']
    speech = request.form['treasurerSpeechInput']

    if file.filename == '':
        flash("No File Selected")
        return redirect('/admin/treasurer_corner')

    filename = secure_filename(file.filename)
    name, ext = os.path.splitext(filename)

    new_filename = f"{treasurer_name}{ext}"
    file.save(os.path.join(app.root_path, 'static', 'images/treasurer', new_filename))

    cursor.execute("INSERT INTO `treasurer_corner`(`name`, `speech`, `image`) VALUES (%s, %s, %s)", (treasurer_name, speech, new_filename))
    conn.commit()

    flash("Uploaded Successfully")
    return redirect('/admin/treasurer_corner')

@app.route('/admin/upload_proVc_corner', methods=['POST'])
def upload_proVc_corner():
    proVc_name = request.form['proVcNameInput']
    file = request.files['file']
    speech = request.form['proVcSpeechInput']

    if file.filename == '':
        flash("No File Selected")
        return redirect('/admin/proVc_corner')

    filename = secure_filename(file.filename)
    name, ext = os.path.splitext(filename)

    new_filename = f"{proVc_name}{ext}"
    file.save(os.path.join(app.root_path, 'static', 'images/proVc', new_filename))

    cursor.execute("INSERT INTO `proVc_corner`(`name`, `speech`, `image`) VALUES (%s, %s, %s)", (proVc_name, speech, new_filename))
    conn.commit()

    flash("Uploaded Successfully")
    return redirect('/admin/pro_vc_corner')

@app.route('/admin/change_about_nstu', methods=['POST'])
def change_about_nstu():
    about = request.form['aboutInput']
    cursor.execute("INSERT INTO `about_nstu`(`about`) VALUES (%s)", (about,))
    conn.commit()

    flash("Changed Successfully")
    return redirect('/admin/about_nstu')

@app.route('/admin/admin_add_teacher', methods=['POST'])
def admin_add_teacher():
    teacher_name = request.form['name']
    designation = request.form['designation']
    department = request.form['department']
    file = request.files['file']
    about = request.form['about']
    email = request.form['email']
    phone = request.form['phone']
    linkedin = request.form['linkedin']
    facebook = request.form['facebook']
    twitter = request.form['twitter']
    degree_name = request.form['degree']
    university_name = request.form['university_name']
    university_passing_year = request.form['university_passing_year']
    university_description = request.form['university_description']
    title = request.form['title']
    author = request.form['author']
    journal_name = request.form['journal_name']
    url = request.form['url']
    date = request.form['date']
    password = request.form['password']

    degree_list = []
    degree = []
    degree.append(degree_name)
    degree.append(university_name)
    degree.append(university_description)
    degree.append(university_passing_year)
    degree_list.append(degree)

    journal_list = []
    journal = []
    journal.append(title)
    journal.append(author)
    journal.append(journal_name)
    journal.append(url)
    journal.append(date)
    journal_list.append(journal)

    if file.filename == '':
        flash("No File Selected")
        return redirect('/admin/add_teacher')
    filename = secure_filename(file.filename)
    name, ext = os.path.splitext(filename)
    new_filename = f"{teacher_name}{ext}"
    file.save(os.path.join(app.root_path, 'static', 'images/teacher', new_filename))

    cursor.execute("INSERT INTO `teacher` (`name`, `designation`, `department`, `image`, `about`, `email`, `phone`, `linkedin`, `facebook`, `twitter`, `degree`, `journal`, `password`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)", (teacher_name, designation, department, new_filename, about, email, phone, linkedin, facebook, twitter, json.dumps(degree_list), json.dumps(journal_list), password))
    conn.commit()
    flash("Uploaded Successfully")
    return redirect('/admin/add_teacher')

@app.route('/admin/admin_remove_teacher', methods=['POST'])
def admin_remove_teacher():
    teacher_email = request.form['email']
    cursor.execute("DELETE FROM `teacher` WHERE email=%s",(teacher_email,))
    conn.commit()
    flash("Teacher Removed")
    return redirect('/admin/remove_teacher')

@app.route('/admin/admin_remove_student', methods=['POST'])
def admin_remove_student():
    student_email = request.form['email']
    cursor.execute("DELETE FROM `student` WHERE email=%s",(student_email,))
    conn.commit()
    flash("Student Removed")
    return redirect('/admin/remove_student')

@app.route('/admin/admin_add_student', methods=['POST'])
def admin_add_student():
    student_name = request.form['name']
    studentid = request.form['studentid']
    designation = request.form['designation']
    department = request.form['department']
    session = request.form['session']
    file = request.files['file']
    about = request.form['about']
    email = request.form['email']
    phone = request.form['phone']
    linkedin = request.form['linkedin']
    facebook = request.form['facebook']
    twitter = request.form['twitter']
    degree_name = request.form['degree']
    university_name = request.form['university_name']
    university_passing_year = request.form['university_passing_year']
    university_description = request.form['university_description']
    title = request.form['title']
    author = request.form['author']
    journal_name = request.form['journal_name']
    url = request.form['url']
    date = request.form['date']
    research_topic = request.form['research_topic']
    password = request.form['password']

    degree_list = []
    degree = []
    degree.append(degree_name)
    degree.append(university_name)
    degree.append(university_description)
    degree.append(university_passing_year)
    degree_list.append(degree)

    journal_list = []
    journal = []
    journal.append(title)
    journal.append(author)
    journal.append(journal_name)
    journal.append(url)
    journal.append(date)
    journal_list.append(journal)

    if file.filename == '':
        flash("No File Selected")
        return redirect('/admin/add_student')
    filename = secure_filename(file.filename)
    name, ext = os.path.splitext(filename)
    new_filename = f"{student_name}{ext}"
    file.save(os.path.join(app.root_path, 'static', 'images/student', new_filename))

    # cursor.execute("INSERT INTO `student` (`name`, `student_id`, `designation`, `department`,`session`, `image`, `about`, `email`, `phone`, `linkedin`, `facebook`, `twitter`, `degree`, `journal`,  `research_interest`, `password`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)", (student_name, studentid, designation, department, session, new_filename, about, email, phone, linkedin, facebook, twitter, json.dumps(degree_list), json.dumps(journal_list), research_topic, password))
    cursor.execute("INSERT INTO `student` (`name`, `student_id`, `designation`, `department`,`session`, `image`, `about`, `email`, `phone`, `linkedin`, `facebook`, `twitter`, `degree`, `journal`,  `research_interest`, `password`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)", (student_name, studentid, designation, department, session, new_filename, about, email, phone, linkedin, facebook, twitter, json.dumps(degree_list), json.dumps(journal_list), research_topic, password))
    conn.commit()
    flash("Uploaded Successfully")
    return redirect('/admin/add_student')

@app.route('/admin/upload_news', methods=['POST'])
def upload_news():
    titleInput = request.form['titleInput']
    description = request.form['description']
    file = request.files['file']

    if file.filename == '':
        flash("No File Selected")
        return redirect('/admin/add_teacher')

    filename = secure_filename(file.filename)
    name, ext = os.path.splitext(filename)

    new_filename = f"{titleInput}{ext}"
    file.save(os.path.join(app.root_path, 'static', 'news', new_filename))

    cursor.execute("INSERT INTO `news`(`title`, `description`, `image`) VALUES (%s, %s, %s)",(titleInput, description, new_filename))
    conn.commit()

    flash("Uploaded Successfully")
    return redirect('/admin/add_news')

@app.route('/admin/upload_event', methods=['POST'])
def upload_event():
    title = request.form['title']
    file = request.files['file']
    event_date = request.form['event_date']
    description = request.form['description']

    if file.filename == '':
        flash("No File Selected")
        return redirect('/admin/add_event')

    filename = secure_filename(file.filename)
    name, ext = os.path.splitext(filename)

    new_filename = f"{title}{ext}"
    file.save(os.path.join(app.root_path, 'static', 'event', new_filename))

    cursor.execute("INSERT INTO `events`(`title`, `description`, `event_date`, `image`) VALUES (%s, %s, %s, %s)",(title, description, event_date, new_filename))
    conn.commit()

    flash("Uploaded Successfully")
    return redirect('/admin/add_event')

@app.route('/admin/upload_research', methods=['POST'])
def upload_research():
    title = request.form['title']
    author = request.form['author']
    journal_url = request.form['journal_url']
    publication_date = request.form['publication_date']
    description = request.form['description']

    cursor.execute("INSERT INTO `research`(`title`, `author`, `journal_url`, `publication_date`, `description`) VALUES (%s ,%s ,%s ,%s ,%s )",(title, author, journal_url, publication_date, description))
    conn.commit()

    flash("Uploaded Successfully")
    return redirect('/admin/add_research')

@app.route('/admin/upload_job', methods=['POST'])
def upload_job():
    jobTitle = request.form['titleInput']
    file = request.files['file']

    if file.filename == '':
        flash("No File Selected")
        return redirect('/admin/add_job')

    filename = secure_filename(file.filename)
    name, ext = os.path.splitext(filename)

    new_filename = f"{jobTitle}{ext}"
    file.save(os.path.join(app.root_path, 'static', 'job', new_filename))

    cursor.execute("INSERT INTO `job`(`title`, `file`) VALUES (%s, %s)",(jobTitle, new_filename))
    conn.commit()

    flash("Uploaded Successfully")
    return redirect('/admin/job_circular')



@app.route('/teacher/teacher_login_validation', methods=['POST'])
def teacher_login_validation():
    if 'teacher_id' in session:
        session.pop('teacher_id')

    email = request.form.get('email')
    pwd = request.form.get('pwd')

    cursor.execute("SELECT * FROM teacher WHERE email = %s AND password = %s ", (email, pwd))
    users = cursor.fetchall()

    if len(users) > 0:
        session['teacher_id'] = users[0][6]
        flash('Logged in Successfully!')
        return redirect('/teacher')
    else:
        flash('Invalid Email Or Password')
        return redirect('/teacher/login')

@app.route('/teacher/add_degree', methods=['POST'])
def add_teacher_degree():
    degree_name = request.form['degree']
    university_name = request.form['university_name']
    university_passing_year = request.form['university_passing_year']
    university_description = request.form['university_description']

    cursor.execute("SELECT  `degree` FROM `teacher` WHERE email=(%s)",(session['teacher_id'],))
    faculty = cursor.fetchall()

    degree_list = json.loads(faculty[0][0])
    degree = []
    degree.append(degree_name)
    degree.append(university_name)
    degree.append(university_description)
    degree.append(university_passing_year)

    degree_list.append(degree)

    cursor.execute("UPDATE `teacher` SET `degree`=%s WHERE email=(%s)",(json.dumps(degree_list),session['teacher_id']))
    conn.commit()

    flash("Degree Added Successfully")
    return redirect('/teacher/degree')

@app.route('/teacher/delete_teacher_degree', methods=['POST'])
def delete_teacher_degree():
    degree_id = request.form['degree_id']

    cursor.execute("SELECT  `degree` FROM `teacher` WHERE email=(%s)", (session['teacher_id'],))
    degree = cursor.fetchall()
    degree_list = json.loads(degree[0][0])
    
    updated_list=[]
    for index, item in enumerate(degree_list):
        if index==int(degree_id)-1:
            continue
        updated_list.append(item)

    cursor.execute("UPDATE `teacher` SET `degree`=%s WHERE email=(%s)",(json.dumps(updated_list),session['teacher_id']))
    conn.commit()
    flash("Degree Removed Successfully")

    return redirect('/teacher/degree')

@app.route('/teacher/delete_teacher_journal', methods=['POST'])
def delete_teacher_journal():
    journal_id = request.form['journal_id']

    cursor.execute("SELECT  `journal` FROM `teacher` WHERE email=(%s)", (session['teacher_id'],))
    journal = cursor.fetchall()
    journal_list = json.loads(journal[0][0])
    
    updated_list=[]
    for index, item in enumerate(journal_list):
        if index==int(journal_id)-1:
            continue
        updated_list.append(item)

    cursor.execute("UPDATE `teacher` SET `journal`=%s WHERE email=(%s)",(json.dumps(updated_list),session['teacher_id']))
    conn.commit()
    flash("Journal Removed Successfully")

    return redirect('/teacher/journal')

@app.route('/teacher/add_journal', methods=['POST'])
def add_teacher_journal():
    title = request.form['title']
    author = request.form['author']
    journal_name = request.form['journal_name']
    url = request.form['url']
    date = request.form['date']

    cursor.execute("SELECT  `journal` FROM `teacher` WHERE email=(%s)",(session['teacher_id'],))
    faculty = cursor.fetchall()

    journal_list = json.loads(faculty[0][0])
    journal = []
    journal.append(title)
    journal.append(author)
    journal.append(journal_name)
    journal.append(url)
    journal.append(date)
    
    journal_list.append(journal)
    
    cursor.execute("UPDATE `teacher` SET `journal`=%s WHERE email=(%s)",(json.dumps(journal_list),session['teacher_id']))
    conn.commit()

    flash("Journal Added Successfully")
    return redirect('/teacher/journal')

@app.route('/teacher/change_contact', methods=['POST'])
def change_teacher_contact():
    phone = request.form['phone']
    linkedin = request.form['linkedin']
    facebook = request.form['facebook']
    twitter = request.form['twitter']

    cursor.execute("UPDATE `teacher` SET `phone`=%s, `linkedin`=%s, `facebook`=%s, `twitter`=%s WHERE email=%s", ( phone, linkedin, facebook, twitter, session['teacher_id']))
    conn.commit()

    flash("Contact Changed Successfully")
    return redirect('/teacher/contact')

@app.route('/teacher/change_password', methods=['POST'])
def change_teacher_password():
    prevPassword = request.form['prevPassword']
    password = request.form['password']

    cursor.execute("UPDATE `teacher` SET `password`=%s WHERE email=%s and password=%s", (password, session['teacher_id'], prevPassword))

    if cursor.rowcount:
        flash("Password Changed Successfully")
    else:
        flash("Password Not Changed")

    conn.commit()
    return redirect('/teacher/password')

@app.route('/teacher/change_about', methods=['POST'])
def change_teacher_about():
    teacher_name = request.form['name']
    designation = request.form['designation']
    department = request.form['department']
    file = request.files['file']
    about = request.form['about']

    cursor.execute("SELECT `image` FROM teacher WHERE email = %s ",(session["teacher_id"],))
    users = cursor.fetchall()

    file_path = os.path.join(app.root_path, 'static', 'images/teacher', users[0][0])

    if file.filename == '':
        flash("No File Selected")
        return redirect('/teacher/about')

    filename = secure_filename(file.filename)
    name, ext = os.path.splitext(filename)

    new_filename = f"{teacher_name}{ext}"
    file.save(os.path.join(app.root_path, 'static', 'images/teacher', new_filename))

    cursor.execute("UPDATE `teacher` SET `name`= %s,`designation`= %s,`department`= %s,`image`= %s,`about`= %s  WHERE email=%s", (teacher_name, designation, department, new_filename, about,session['teacher_id']))

    if os.path.exists(file_path):
        os.remove(file_path)

    conn.commit()
    return redirect('/teacher/about')


@app.route('/student_profile/student_login_validation', methods=['POST'])
def student_login_validation():
    if 'student_id' in session:
        session.pop('student_id')

    email = request.form.get('email')
    pwd = request.form.get('pwd')

    cursor.execute("SELECT * FROM student WHERE email = %s AND password = %s ", (email, pwd))
    users = cursor.fetchall()

    if len(users) > 0:
        session['student_id'] = users[0][8]
        flash('Logged in Successfully!')
        return redirect('/student_profile')
    else:
        flash('Invalid Email Or Password')
        return redirect('/student_profile/login')

@app.route('/student_profile/add_degree', methods=['POST'])
def add_student_degree():
    degree_name = request.form['degree']
    university_name = request.form['university_name']
    university_passing_year = request.form['university_passing_year']
    university_description = request.form['university_description']

    cursor.execute("SELECT  `degree` FROM `student` WHERE email=(%s)",(session['student_id'],))
    faculty = cursor.fetchall()

    degree_list = json.loads(faculty[0][0])
    degree = []
    degree.append(degree_name)
    degree.append(university_name)
    degree.append(university_description)
    degree.append(university_passing_year)

    degree_list.append(degree)

    cursor.execute("UPDATE `student` SET `degree`=%s WHERE email=(%s)",(json.dumps(degree_list),session['student_id']))
    conn.commit()

    flash("Degree Added Successfully")
    return redirect('/student_profile/degree')

@app.route('/student_profile/delete_student_degree', methods=['POST'])
def delete_student_degree():
    degree_id = request.form['degree_id']

    cursor.execute("SELECT  `degree` FROM `student` WHERE email=(%s)", (session['student_id'],))
    degree = cursor.fetchall()
    degree_list = json.loads(degree[0][0])
    
    updated_list=[]
    for index, item in enumerate(degree_list):
        if index==int(degree_id)-1:
            continue
        updated_list.append(item)

    cursor.execute("UPDATE `student` SET `degree`=%s WHERE email=(%s)",(json.dumps(updated_list),session['student_id']))
    conn.commit()
    flash("Degree Removed Successfully")

    return redirect('/student_profile/degree')

@app.route('/student_profile/delete_student_journal', methods=['POST'])
def delete_student_journal():
    journal_id = request.form['journal_id']

    cursor.execute("SELECT  `journal` FROM `student` WHERE email=(%s)", (session['student_id'],))
    journal = cursor.fetchall()
    journal_list = json.loads(journal[0][0])
    
    updated_list=[]
    for index, item in enumerate(journal_list):
        if index==int(journal_id)-1:
            continue
        updated_list.append(item)

    cursor.execute("UPDATE `student` SET `journal`=%s WHERE email=(%s)",(json.dumps(updated_list),session['student_id']))
    conn.commit()
    flash("Journal Removed Successfully")

    return redirect('/student_profile/journal')

@app.route('/student_profile/add_journal', methods=['POST'])
def add_student_journal():
    title = request.form['title']
    author = request.form['author']
    journal_name = request.form['journal_name']
    url = request.form['url']
    date = request.form['date']

    cursor.execute("SELECT  `journal` FROM `student` WHERE email=(%s)",(session['student_id'],))
    faculty = cursor.fetchall()

    journal_list = json.loads(faculty[0][0])
    journal = []
    journal.append(title)
    journal.append(author)
    journal.append(journal_name)
    journal.append(url)
    journal.append(date)
    
    journal_list.append(journal)
    
    cursor.execute("UPDATE `student` SET `journal`=%s WHERE email=(%s)",(json.dumps(journal_list),session['student_id']))
    conn.commit()

    flash("Journal Added Successfully")
    return redirect('/student_profile/journal')

@app.route('/student_profile/change_contact', methods=['POST'])
def change_student_contact():
    phone = request.form['phone']
    linkedin = request.form['linkedin']
    facebook = request.form['facebook']
    twitter = request.form['twitter']

    cursor.execute("UPDATE `student` SET `phone`=%s, `linkedin`=%s, `facebook`=%s, `twitter`=%s WHERE email=%s", ( phone, linkedin, facebook, twitter, session['student_id']))
    conn.commit()

    flash("Contact Changed Successfully")
    return redirect('/student_profile/contact')

@app.route('/student_profile/change_password', methods=['POST'])
def change_student_password():
    prevPassword = request.form['prevPassword']
    password = request.form['password']

    cursor.execute("UPDATE `student` SET `password`=%s WHERE email=%s and password=%s", (password, session['student_id'], prevPassword))

    if cursor.rowcount:
        flash("Password Changed Successfully")
    else:
        flash("Password Not Changed")

    conn.commit()
    return redirect('/student_profile/password')

@app.route('/student_profile/change_about', methods=['POST'])
def change_student_about():
    student_name = request.form['name']
    studentid = request.form['studentid']
    designation = request.form['designation']
    department = request.form['department']
    student_session = request.form['session']
    file = request.files['file']
    about = request.form['about']
    cursor.execute("SELECT `image` FROM student WHERE email = %s ",(session["student_id"],))
    users = cursor.fetchall()

    file_path = os.path.join(app.root_path, 'static', 'images/student', users[0][0])

    if file.filename == '':
        flash("No File Selected")
        return redirect('/student_profile/about')

    filename = secure_filename(file.filename)
    name, ext = os.path.splitext(filename)

    new_filename = f"{student_name}{ext}"
    file.save(os.path.join(app.root_path, 'static', 'images/student', new_filename))

    cursor.execute("UPDATE `student` SET `name`= %s, `student_id`=%s, `designation`= %s,`department`= %s, `session`=%s, `image`= %s,`about`= %s  WHERE email=%s", (student_name, studentid, designation, department, student_session, new_filename, about,session['student_id']))

    if os.path.exists(file_path):
        os.remove(file_path)

    conn.commit()
    return redirect('/student_profile/about')


@app.route('/teacher/logout')
def teacher_logout():
    session.pop('teacher_id')
    return redirect('/teacher/login')

@app.route('/student_profile/logout')
def student_logout():
    session.pop('student_id')
    return redirect('/student_profile/login')

@app.route('/user_logout')
def user_logout():
    session.pop('user_id')
    return redirect('/login')

@app.route('/admin_logout')
def admin_logout():
    session.pop('admin_id')
    return redirect('/admin/login')

if __name__ == '__main__':
    app.run()