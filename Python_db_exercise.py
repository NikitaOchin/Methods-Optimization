import psycopg2
import datetime
from dateutil.relativedelta import relativedelta

def create_hosp_AND_doctor_Tables(cur):
        #Create table Hospital
        postgreSQL_select_Query = "CREATE TABLE hospital (\
                                   hosp_id serial NOT NULL PRIMARY KEY, \
                                   hosp_name VARCHAR(30) NOT NULL, \
                                   beg_count INT NOT NULL);"
        cursor.execute(postgreSQL_select_Query)

        #Create table Doctor
        postgreSQL_select_Query = "CREATE TABLE doctor (\
                                   doctor_id serial NOT NULL PRIMARY KEY, \
                                   doctor_name VARCHAR(30) NOT NULL, \
                                   joining_date DATE NOT NULL, \
                                   speciality VARCHAR(30) NOT NULL, \
                                   salary INT NOT NULL, \
                                   expirience INT NOT NULL, \
                                   hosp_id INT REFERENCES hospital(hosp_id));"                              
        cursor.execute(postgreSQL_select_Query)

def insert_into_doctor(cur,doctor_name,joining_date,speciality,salary,expirience,hosp_id):
    psql_in_query = "INSERT INTO doctor\
                         (doctor_name,joining_date,speciality,salary,expirience,hosp_id)\
                                 VALUES(%s, %s, %s, %s, %s, %s);"
    record_to_in = (doctor_name,joining_date,speciality,salary,expirience,hosp_id,)
    cur.execute(psql_in_query, record_to_in)

def insert_into_hospital(cur, hosp_name, beg_count):
    cur.execute("INSERT INTO hospital(hosp_name,beg_count)\
                        VALUES(%s,%s);",(hosp_name, beg_count,))

#First question
def getDbConnection(name_of_database):
    print("Pyton is connection to PostgreSQL\n")
    # Connect to an existing database
    return psycopg2.connect(user="postgres",
                                  password="prglxtp46",
                                  database=name_of_database)

def closeDbConnection(conn, cursor):
    #closing database connection.
    if(conn):
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")

def readDbVersion(cur):
    cur.execute("SELECT version();")
    print(cur.fetchone()[0])

#Second question
def readHospitalDetails(cur,hosp_id):
    #Read data from Hospital table
    postgreSQL_select_Query = "SELECT * FROM hospital WHERE hosp_id = %s"
    cur.execute(postgreSQL_select_Query,(hosp_id,))
    return cur.fetchall()


def readDoctorDetails(cur, doc_id):
    # Read data from Doctor table
    postgreSQL_select_Query = "SELECT * FROM doctor WHERE doctor_id = %s"
    cur.execute(postgreSQL_select_Query,(doc_id,))
    return cur.fetchall()

def print_HospitalDetails(H):
    for h in H:
        print("Hospital record:")
        print("hosp_id = ",h[0])
        print("hosp_name = ",h[1])
        print("beg_count = ",h[2],'\n')

def print_DoctorDetails(cur, D):
    for h in D:
        print("Doctor record:")
        print("doc_id = ",h[0])
        print("name_name = ",h[1])
        print("joining_date = ",h[2])
        print("speciality = ",h[3])
        print("salary = ",h[4])
        print("expirience = ",h[5])
        print("hosp_id = ",h[6])
        print("hosp_id = ",getHospitalName(cur,h[0]),'\n')

#Third question
def getSpecialistDoctorsList(cur, speciality, salary):
    #Fetch doctor's details as per Speciality and Salary
    print("Printing Doctors record as per given Speciality:")
    postgreSQL_select_Query = "SELECT * FROM doctor WHERE speciality = %s AND salary >%s"
    cur.execute(postgreSQL_select_Query,(speciality, salary,))
    return cur.fetchall()

#Fourth question
def getHospitalName(cur,hosp_id):
    #Fetch Hospital Name using Hospital Id
    postgreSQL_select_Query = "SELECT hosp_name FROM hospital WHERE hosp_id = %s"
    cur.execute(postgreSQL_select_Query,(hosp_id,))
    return cur.fetchone()[0]

def GetDoctordWithinHospital(cur,hosp_id):
    #Fetch All doctors within given Hospital
    postgreSQL_select_Query = "SELECT * FROM doctor WHERE hosp_id = %s"
    cur.execute(postgreSQL_select_Query,(hosp_id,))
    return cur.fetchall()

#Fifth question
def getDoctorJoiningDate(cur, doc_id):
    #Get Doctor's joining date using doctor ID
    postgreSQL_select_Query = "SELECT joining_date FROM doctor WHERE hosp_id = %s"
    cur.execute(postgreSQL_select_Query,(doc_id,))
    return cur.fetchone()

def updateDoctorsExperience(cur, doc_id):
    #Update Doctor Experience in Years

    #Get joining date
    joningDate = getDoctorJoiningDate(cur, doc_id)

    #calculate Experience in years
    joningDate = datetime.datetime.strptime(''.join(map(str, joningDate)), '%Y-%m-%d')
    todays_Date = datetime.datetime.now()
    Experience_in_years = relativedelta(todays_Date, joningDate).years

    #Update doctor's Experience now
    postgreSQL_select_Query = "UPDATE doctor SET expirience = %s WHERE doctor_id = %s"
    cur.execute(postgreSQL_select_Query,(Experience_in_years,doc_id))

def Test_Ex():
    print("Start of a Python Database Programming Exercise")    
    try:
     ## 1st question
        # Connect to an existing database
        conn = getDbConnection("python_db")
        # Open a cursor to perform database operations
        cur = conn.cursor()
        
     ## 2nd question
        h = readHospitalDetails(cur,1)
        #print_HospitalDetails(h)
        d = readDoctorDetails( cur,1)
        #print_DoctorDetails(cur,d)
        
     ## 3rd question
        s = getSpecialistDoctorsList(cur,'Hirurg', 5000)
        #print_DoctorDetails(cur,s)
        
     ## 4th question
        DL = GetDoctordWithinHospital(cur,1)
        #print_DoctorDetails(cur,DL)

     ## 5th question
        #Before Update
        print("___Before Update___")
        d = readDoctorDetails(cur,1)
        print_DoctorDetails(cur,d)
        #UPDATE
        updateDoctorsExperience(cur, 1)
        #After Update
        print("___After Update___")
        d = readDoctorDetails(cur,1)
        print_DoctorDetails(cur,d)
        
     ## Make the changes to the database persistent
        if input("Press 't' if you want to commit: ") == 't':
            conn.commit()
            print("Commit has done\n")
        else: print("Commit has NOT done\n")
        
    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)
    finally:
        # Close communication with the database
        closeDbConnection(conn, cur)
    print("End of a Python Database Programming Exercise\n")

if __name__ == "__main__":
    Test_Ex()
