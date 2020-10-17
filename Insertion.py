import mysql.connector 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="course_vila"
)

mycursor = mydb.cursor()


    
def insertCourseData(course_group_id,name,search_keywords,description,course_provider,course_url,tutor_id,rating,rating_count,student_count,last_updated,supported_lang,price,course_content_id,accessibility,devices,certification,created_on,updated_on): 
    sql = "INSERT INTO cv_course (course_group_id,name,search_keywords,description,course_provider,course_url,tutor_id,rating,rating_count,student_count,last_updated,supported_lang,price,course_content_id,accessibility,devices,certification,created_on,updated_on) VALUES (%s, %s, %s, %s ,%s, %s, %s, %s, %s ,%s, %s, %s, %s, %s ,%s, %s, %s, %s, %s)"
    val = (course_group_id,name,search_keywords,description,course_provider,course_url,tutor_id,rating,rating_count,student_count,last_updated,supported_lang,price,course_content_id,accessibility,devices,certification,created_on,updated_on)
    mycursor.execute(sql, val)
    mydb.commit()  
    mycursor.execute('select max(id) from cv_course_group;')
    course_id_tuple=mycursor.fetchall()
    course_id=list(course_id_tuple[0])
    return (course_id[0])

def insertCourseContent(course_id,duration,resource_count,lecture_count,section_count):
    sql = "INSERT INTO cv_course_content (course_id,duration,resource_count,lecture_count,section_count) VALUES (%s, %s, %s, %s ,%s)"
    val = (course_id,duration,resource_count,lecture_count,section_count)
    mycursor.execute(sql, val)
    mydb.commit()
def cv_course_group():
    sql="select id,name,search_keywords from cv_course_group"
    mycursor.execute(sql)
    courses=mycursor.fetchall()
    return_course_name_list=[]
    for course in courses:
        
        lst=list(course)
        return_course_name_list.append(lst)
    return (return_course_name_list)
    
