get_ipython().run_line_magic('run', '"settings.py"')

import joblib

get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'png'")

filepath = 'C:\\Users\\matth\\OneDrive\\Documents\\University\\Third Year\\Work Based Project\\Final\\'

def Interactive_model():
    # Import the csv file that the data is inserted into
    framework_df = pd.read_csv(filepath + 'Framework.csv')
    print("Please see the attached metadata document which shows which values are valid for each of the below input boxes.\n")
    time.sleep(1)
    print("Section 1 - School Characteristics")
    print('')
    time.sleep(1)
    
    while True:
        try:
            PRIMARY = input("1. Does the school offer primary education?: \n")
            if PRIMARY.lower() == 'yes' or PRIMARY.lower() == 'no':
                break
            else:
                print("Error: The value must be 'Yes', 'No'. Please try again.\n")
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter a string.\n")
    if PRIMARY == 'yes':
        framework_df['ISPRIMARY'] = [1]
    if PRIMARY == 'no':
        framework_df['ISPRIMARY'] = [0]
    time.sleep(1)
    
    
    while True:
        try:
            COLLEGE = input("2. Does the school offer post-16 education?: \n")
            if COLLEGE.lower() == 'yes' or COLLEGE.lower() == 'no':
                break
            else:
                print("Error: The value must be 'Yes', 'No'. Please try again.\n")
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter a string.\n")
    if COLLEGE == 'yes':
        framework_df['ISPOST16'] = [1]
    if COLLEGE == 'no':
        framework_df['ISPOST16'] = [0]
    time.sleep(1)
    
    
    while True:
        try:
            RELDENOM = input("3. Is the school religious?: \n")
            if RELDENOM.lower() == 'yes' or RELDENOM.lower() == 'no':
                break
            else:
                print("Error: The value must be 'Yes' or 'No'. Please try again.\n")
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter a string.\n")
    if RELDENOM == 'yes':
        framework_df['RELDENOM'] = [1]
    if RELDENOM == 'no':
        framework_df['RELDENOM'] = [0]
    time.sleep(1)
    
    
    while True:
        try:
            GENDER = input("4. What is the gender of the school? ('Mixed' or 'Single sex'): \n")
            if GENDER.lower() == 'mixed' or GENDER.lower() == 'single sex':
                break
            else:
                print("Error: The value must be 'Mixed' or 'Single sex'. Please try again.\n")
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter a string.\n")
    if GENDER == 'mixed':
        framework_df['GENDER'] = [1]
    if GENDER == 'single sex':
        framework_df['GENDER'] = [0]
    time.sleep(1)
    
    
    while True:
        try:
            SCHOOLTYPE = input("5. What is the school type? ('Academy', 'Academy Convertor', 'Community School' or 'Other'): \n")
            if SCHOOLTYPE.lower() == 'academy' or SCHOOLTYPE.lower() == 'academy converter' or SCHOOLTYPE.lower() == 'community school' or SCHOOLTYPE.lower() == 'other':
                break
            else:
                print("Error: The value must be 'Academy', 'Academy Convertor', 'Community School' or 'Other'. Please try again.\n")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.\n")
        except TypeError:
            print("Error: Please enter a string.")
    if SCHOOLTYPE == 'academy converter':
        framework_df['ACC_NFTYPE_DUMMY'] = [1]
    if SCHOOLTYPE == 'community school':
        framework_df['CY_NFTYPE_DUMMY'] = [1]
    if SCHOOLTYPE == 'other':
        framework_df['OTHER_NFTYPE_DUMMY'] = [1]
    if SCHOOLTYPE == 'academy':
        framework_df['ACADEMY_NFTYPE_DUMMY'] = [1]
    time.sleep(1)
    
    
    while True:
        try:
            ADMPOL = input("6. What is the admission policy of the school? ('Selective' or 'Non-Selective'): \n")
            if ADMPOL.lower() == 'selective' or ADMPOL.lower() == 'non-selective' or ADMPOL.lower() == 'selective':
                break
            else:
                print("Error: The value must be 'Selective' or 'Non-Selective'. Please try again.\n")
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter a string.\n")
    if RELDENOM == 'selective':
        framework_df['ADMPOL'] = [1]
    if RELDENOM == 'non-selective':
        framework_df['ADMPOL'] = [0]
    time.sleep(1)
    
    
    while True:
        try:
            IDACI = int(input("7. What is the IDACI decile of the school?: \n"))
            if IDACI == 1 or IDACI == 2 or IDACI == 3 or IDACI == 4 or IDACI == 5:
                break
            else:
                print("Error: The value must be between 1 and 5. Please try again.\n")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.\n")
    if IDACI == 1:
        framework_df['IDACI_DECILE_1_DUMMY'] = [1]
    if IDACI == 2:
        framework_df['IDACI_DECILE_2_DUMMY'] = [1]
    if IDACI == 3:
        framework_df['IDACI_DECILE_3_DUMMY'] = [1]
    if IDACI == 4:
        framework_df['IDACI_DECILE_4_DUMMY'] = [1]
    if IDACI == 5:
        framework_df['IDACI_DECILE_5_DUMMY'] = [1]  
    time.sleep(1)
    
    
       
    print("Section 2 - Historic Ofsted Information\n")
    print('')
    time.sleep(1)
          
    while True:
        try:
            PREVIOUS_SCORE = input("1. What was the previous Ofsted inspection score? ('Outstanding', 'Good', 'Requires Improvement' or 'Inadequate'): \n")
            if PREVIOUS_SCORE.lower() == 'outstanding' or PREVIOUS_SCORE.lower() == 'good' or PREVIOUS_SCORE.lower() == 'requires improvement' or PREVIOUS_SCORE.lower() == 'special measures':
                break
            else:
                print("Error: The value must be 'Outstanding', 'Good', 'Requires Improvement' or 'Inadequate'. Please try again.\n")
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter a string.\n")
    if RELDENOM == 'outstanding':
        framework_df['OUTSTANDING_PREVIOUS'] = [1]
    if RELDENOM == 'good':
        framework_df['GOOD_PREVIOUS'] = [1]
    if RELDENOM == 'requires improvement':
        framework_df['REQUIRES_IMPROVEMENT_PREVIOUS'] = [1]
    if RELDENOM == 'special measures':
        framework_df['INADEQUATE_PREVIOUS'] = [1]
    time.sleep(1)
    
    
    while True:
        try:
            PREVIOUS_CONCERN = input("2. Was there a previous category of concern at the last inspection?: \n")
            if PREVIOUS_CONCERN.lower() == 'yes' or PREVIOUS_CONCERN.lower() == 'no':
                break
            else:
                print("Error: The value must be 'Yes' or 'No'. Please try again.\n")
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter a string.\n")
    if PREVIOUS_CONCERN == 'yes':
        framework_df['PREVIOUS_CONCERN'] = [1]
    if PREVIOUS_CONCERN == 'no':
        framework_df['PREVIOUS_CONCERN'] = [0]
    time.sleep(1)
    
   
    
    while True:
        try:
            DAYS_SINCE = int(input("3. How many days has it been since the previous Ofsted inspection?: \n"))
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter an integer.\n")
    framework_df['DAYS_SINCE_LAST'] = [DAYS_SINCE]
    time.sleep(1)
    
    
    
    
    print("Section 3 - Pupil Characteristics and Attainment\n")
    print('')
    time.sleep(1)
    
    while True:
        try:
            KS2APS = float(input("1. What is the average Key stage 2 Points Score of the cohort at the end of key stage 4?: \n"))
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter a float value.\n")
    framework_df['KS2APS'] = [KS2APS]
    time.sleep(1)
    
    while True:
        try:
            PTAC5EM = float(input("2. What percentage of pupils achieved Level 2 threshold including standard passes 9-4 in English and Maths GCSEs?: \n"))
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter a float value.\n")
    framework_df['PTAC5EM'] = [PTAC5EM]
    time.sleep(1)
    
    
    while True:
        try:
            PTL2BASICS = float(input("3. What percentage of pupils achieved standard 9-4 passes in English and Maths GCSEs?: \n"))
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter a float value.\n")
    framework_df['PTL2BASICS'] = [PTL2BASICS]
    time.sleep(1)
    
    while True:
        try:
            PTANYQ = float(input("4. What percentage of pupils achieved any qualifications?:\n "))
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter a float value.\n")
    framework_df['PTANYQ'] = [PTANYQ]
    time.sleep(1)
    
    while True:
        try:
            TAVENT_E = float(input("5. What is the average number of GCSE and equivalents entries per pupil?:\n "))
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter a float value.\n")
    framework_df['TAVENT_E'] = [TAVENT_E]
    time.sleep(1)
    
    
    while True:
        try:
            TTAPS = float(input("6. What is the total average point score per pupil?:\n "))
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter a float value.\n")
    framework_df['TTAPS'] = [TTAPS]
    time.sleep(1)
    

    

    
    while True:
        try:
            PERCTOT = float(input("7. What is the overall absence as a percentage?:\n "))
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter a float value.\n")
    framework_df['PERCTOT'] = [PERCTOT]
    time.sleep(1)
    
    while True:
        try:
            PNUMEAL = float(input("8. What percentage of pupils do not have English as their first language?: \n"))
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter a float value.\n")
    framework_df['PNUMEAL'] = [PNUMEAL]
    time.sleep(1)
    
    while True:
        try:
            PTFSMCLA = float(input("9. What percentage of pupils are disadvantaged?: \n"))
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter a float value.\n")
    framework_df['PTFSMCLA'] = [PTFSMCLA]
    time.sleep(1)
    
    
    
    
    print("Section 4 - Teacher Characteristics\n")
    print('')
    time.sleep(1)
    
    while True:
        try:
            SALARY = float(input("1. What is the mean gross salary of full-time teachers?: \n"))
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter a float value.\n")
    framework_df['SALARY'] = [SALARY]
    time.sleep(1)
        
    while True:
        try:
            RATPUPTEA = float(input("2. What is the pupil:teacher ratio?: \n"))
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid entry.\n")
        except TypeError:
            print("Error: Please enter a float value.\n")
    framework_df['RATPUPTEA'] = [RATPUPTEA]
    time.sleep(1)
       
     # Fill all NULL columns with 0
    framework_df.fillna(value = 0, inplace = True)      
    
    # Drop columns to avoid dummy trap
    dropped_columns = ['ACC_NFTYPE_DUMMY',
                       'REQUIRES_IMPROVEMENT_PREVIOUS',
                       'IDACI_DECILE_5_DUMMY']
    
    framework_df = framework_df.drop(columns = dropped_columns)
    
    for col in framework_df[['KS2APS',
                             'PTAC5EM',
                             'PTL2BASICS',
                             'TAVENT_E',
                             'PTANYQ',
                             'PERCTOT',
                             'PTFSMCLA',
                             'SALARY',
                             'PNUMEAL',
                             'RATPUPTEA', 
                             'DAYS_SINCE_LAST', 
                             'TTAPS']]:
    
        framework_df[col] = (framework_df[col] - framework_df[col].mean()) / framework_df[col].std()  
    
    # Load the model
    loaded_model = joblib.load('C:\\Users\\roodm\\OneDrive - Office for National Statistics\\University\\Year 3\\Work Based Project\\tuned_svc.sav')
    
    # Run the data on the model
    predictions = loaded_model.predict(framework_df)    

    if predictions == 1.0:
        predictions = "Outstanding" 
    if predictions == 2.0:
        predictions = "Good"  
    if predictions == 3.0:
        predictions = "Requires Improvement"  
    if predictions == 4.0:
        predictions = "Inadequate"
        

    time.sleep(1)
    print("Computing...\n")
    time.sleep(2)
    print(f"Based upon the model we predict the the school will receive an {predictions} inspection rating (this is 69% accurate).\n")         

Interactive_model()




