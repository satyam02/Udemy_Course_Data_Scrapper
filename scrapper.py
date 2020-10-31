from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import date
import datetime
import mysql.connector
import Insertion as db
from mysql.connector import errorcode
today = date.today()

try:
  cnx = mysql.connector.connect(user='scott',
                                database='employ')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Connecting")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
def tutorDetailsInsertion(driver):
    tutor_name=''
    tutor=driver.find_elements_by_xpath('//*[@id="udemy"]/div[2]/div[3]/div[1]/div[3]/div/div/div[4]/div/div[1]/div[3]/div/div/div/div/span/a[1]/span')
    for item in tutor:
        tutor_name=item.text
    tutor_id=db.insertTutorData(tutor_name)
    return tutor_id[0]
def courseContentFindingInsertion(driver,course_id):
    course_content_list=[]
    resource_count='1'
    lecture_count=driver.find_elements_by_xpath('//*[@id="udemy"]/div[2]/div[3]/div[1]/div[4]/div[4]/div/div/div/div/div[1]/div/span')
    for item in lecture_count:
        course_content_list=list((item.text).split("•"))
    content=driver.find_elements_by_xpath('//*[@id="udemy"]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div/div[3]/ul/li[2]/div/span/span')
    for item in content:
        course_content_list.append(item.text)
    print(course_content_list)
    
    duration_detail=course_content_list[2].split(" ")
    duration=float(duration_detail[1].rstrip('h')+'.'+duration_detail[2].rstrip('m'))
    lecture_count_str=course_content_list[1].split(" ")
    lectures=lecture_count_str[1]
    section_count=course_content_list[0].split(" ")
    sections=section_count[0]
    
    print(course_id,duration,resource_count,lectures,sections)
    db.insertCourseContent(course_id,duration,resource_count,lectures,sections)


def course(driver,course_name,count,course_group_id,search_keywords):
    
    if count<=2:
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys(course_name,Keys.ENTER)
        time.sleep(10)
        course_list=driver.find_elements_by_xpath('//div[@class="popper--popper--19faV popper--popper-hover--4YJ5J"]')
        course_list_size=len(course_list)
    #if count<course_list_size and count<=1:
        courseDetails(driver,course_list,course_list_size,count,course_name,course_group_id,search_keywords)
    else:
        return
    
def courseDetails(driver,course_list,course_list_size,count,course_name,course_group_id,search_keywords):
    course_link=course_list[count].find_element_by_tag_name('a')
    course_specific_url=course_link.get_attribute('href')
    driver.get(course_specific_url)
    time.sleep(10)
    course_details_list=[]
    course_heading=driver.find_elements_by_xpath('//*[@id="udemy"]/div[2]/div[3]/div[1]/div[3]/div/div/div[4]/div/div[1]/div[1]/h1')
    for item in course_heading:
        course_details_list.append(item.text)
    course_description=driver.find_elements_by_xpath('//*[@id="udemy"]/div[2]/div[3]/div[1]/div[3]/div/div/div[4]/div/div[1]/div[1]/div')
    for item in course_description:
        course_details_list.append(item.text)
    
    rating_details=driver.find_elements_by_xpath('//*[@id="udemy"]/div[2]/div[3]/div[1]/div[3]/div/div/div[4]/div/div[1]/div[2]/div[2]/div[1]/div/div/div')
    for item in rating_details:
        rating_count_data=(item.text).splitlines()
        for rating_count_item in rating_count_data:
            course_details_list.append(rating_count_item)
    rating_count_details=[]
    rating_count_details=(course_details_list[4].split(" "))
    rating_count=rating_count_details[0].strip('()')
    rating_count=rating_count.replace(',','')
    
    students_enrolled=driver.find_elements_by_xpath('//*[@id="udemy"]/div[2]/div[3]/div[1]/div[3]/div/div/div[4]/div/div[1]/div[2]/div[2]/div[2]/div')
    for item in students_enrolled:
        course_details_list.append(item.text)
    student_count_str=course_details_list[5].split(" ")   
    student_count=student_count_str[0].replace(',','')
    
    last_update=driver.find_elements_by_xpath('//*[@id="udemy"]/div[2]/div[3]/div[1]/div[3]/div/div/div[4]/div/div[1]/div[4]/div[1]/div/div/span[2]')
    for item in last_update:
        course_details_list.append(item.text)
    last_update_str=course_details_list[6].split(" ")
    last_updated='01-'+last_update_str[2].replace("/","-")
    todayDate=datetime.datetime.strptime(last_updated, "%d-%m-%Y").strftime('%Y-%m-%d')
    last_updated=todayDate 
    lang=''
    language=driver.find_elements_by_xpath('//*[@id="udemy"]/div[2]/div[3]/div[1]/div[3]/div/div/div[4]/div/div[1]/div[4]/div[3]/div/div/div/span[1]')
    for item in language:
        lang=item.text
    course_price=driver.find_elements_by_xpath('//*[@id="udemy"]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/span[2]/span')
    for item in course_price:
        course_details_list.append(item.text)
        
    accessibility=driver.find_elements_by_xpath('//*[@id="udemy"]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div/div[3]/ul/li[3]/div/span/span')
    for item in accessibility:
        course_details_list.append(item.text)
    
    device=driver.find_elements_by_xpath('//*[@id="udemy"]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div/div[3]/ul/li[4]/div/span/span')
    for item in device:
        course_details_list.append(item.text)
        
    certification=driver.find_elements_by_xpath('//*[@id="udemy"]/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div/div[3]/ul/li[5]/div/span/span')
    for item in device:
        course_details_list.append(item.text)
    print(course_details_list)
    
    date = today.strftime("%d-%m-%Y")
    date=datetime.datetime.strptime(date, "%d-%m-%Y").strftime('%Y-%m-%d')
    name=course_details_list[0]
    description=course_details_list[1]
    rating=course_details_list[3]
    price=course_details_list[7].replace("₹","")
    accessibility=course_details_list[8]
    devices=course_details_list[9]
    certification=1
    tutor_id=tutorDetailsInsertion(driver)
    print(course_group_id,name,search_keywords,description,'udemy',course_specific_url,tutor_id,rating,rating_count,student_count,last_updated,lang,price,count,accessibility,devices,certification,date,date)
    
    course_id_list=db.insertCourseData(course_group_id,name,search_keywords,description,'udemy',course_specific_url,tutor_id,rating,rating_count,student_count,last_updated,"ENG",price,count,accessibility,devices,certification,date,date)
    course_id=int(course_id_list[0])
    courseContentFindingInsertion(driver,course_id)
    count+=1
    course(driver,course_name,count,course_group_id,search_keywords)
    
def main():
    driver = webdriver.Chrome(r"lib\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.udemy.com/") 
    course_file=db.cv_course_group()
    for course_name_list in course_file:
        course_name=course_name_list[1]
        course_group_id=course_name_list[0]
        search_keywords=course_name_list[2]
        course(driver,course_name,1,course_group_id,search_keywords)
    driver.quit()
main()         
