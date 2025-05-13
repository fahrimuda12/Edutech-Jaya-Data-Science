import streamlit as st
import pandas as pd
import joblib

# Load model dan encoder
model = joblib.load('model/rdf_model.joblib')
encoder = joblib.load('model/label_encoder.joblib')  # encoder kategorikal (jika ada)

st.title("🎓 Prediksi Status Mahasiswa - Jaya Jaya Institut")

st.markdown("Masukkan informasi mahasiswa untuk memprediksi apakah ia akan **Dropout**, **Enrolled**, atau **Graduate**.")

# Input form
with st.form("prediction_form"):
   age = st.number_input("Umur waktu didaftar", min_value=16, max_value=60, value=20)
   marital_status = st.selectbox("Status Perkawinan", ["Single", "Married", "Widower", "Divorced", "Facto Union", "Legally Separated"])
   application_mode = st.selectbox("Pilihan Pendaftaran", [
      '1st phase - general contingent',
      'Ordinance No. 612/93',
      '1st phase - special contingent (Azores Island)',
      'Holders of other higher courses',
      'Ordinance No. 854-B/99',
      'International student (bachelor)',
      '1st phase - special contingent (Madeira Island)',
      '2nd phase - general contingent',
      '3rd phase - general contingent',
      'Ordinance No. 533-A/99, item b2) (Different Plan)',
      'Ordinance No. 533-A/99, item b3 (Other Institution)',
      'Over 23 years old',
      'Transfer',
      'Change of course',
      'Technological specialization diploma holders',
      'Change of institution/course',
      'Short cycle diploma holders',
      'Change of institution/course (International)'
   ])
   application_order = st.number_input("Urutan Pendaftar", min_value=0, max_value=9, value=0)
   course = st.selectbox("Program Studi", [
      'Biofuel Production Technologies',
      'Animation and Multimedia Design',
      'Social Service (evening attendance)',
      'Agronomy',
      'Communication Design',
      'Veterinary Nursing',
      'Informatics Engineering',
      'Equinculture',
      'Management',
      'Social Service',
      'Tourism',
      'Nursing',
      'Oral Hygiene',
      'Advertising and Marketing Management',
      'Journalism and Communication',
      'Basic Education',
      'Management (evening attendance)'
   ])
   attendance = st.selectbox("Jadwal Kuliah", ["Daytime", "Evening"])
   previous_qualification = st.selectbox("Pendidikan Sebelumnya", [
      'Secondary education',
      "Bachelor's degree",
      'Degree',
      "Master's",
      'Doctorate',
      'Frequency of higher education',
      '12th year of schooling - not completed',
      '11th year of schooling - not completed',
      'Other - 11th year of schooling',
      '10th year of schooling',
      '10th year of schooling - not completed',
      'Basic education 3rd cycle (9th/10th/11th year) or equiv.',
      'Basic education 2nd cycle (6th/7th/8th year) or equiv.',
      'Technological specialization course',
      'Higher education - degree (1st cycle)',
      'Professional higher technical course',
      'Higher education - master (2nd cycle)'
   ])
   previous_qualification_grade = st.number_input("Nilai Pendidikan Sebelumnya", min_value=0.0, max_value=100.0, value=0.0)
   mothers_occupation = st.selectbox("Pekerjaan Ibu", [
         'Student',
         'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers',
         'Specialists in Intellectual and Scientific Activities',
         'Intermediate Level Technicians and Professions',
         'Administrative staff',
         'Personal Services, Security and Safety Workers and Sellers',
         'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry',
         'Skilled Workers in Industry, Construction and Craftsmen',
         'Installation and Machine Operators and Assembly Workers',
         'Unskilled Workers',
         'Armed Forces Professions',
         'Other Situation',
         '(blank)',
         'Health professionals',
         'Teachers',
         'Specialists in information and communication technologies (ICT)',
         'Intermediate level science and engineering technicians and professions',
         'Technicians and professionals, of intermediate level of health',
         'Intermediate level technicians from legal, social, sports, cultural and similar services',
         'Office workers, secretaries in general and data processing operators',
         'Data, accounting, statistical, financial services and registry-related operators',
         'Other administrative support staff',
         'Personal service workers',
         'Sellers',
         'Personal care workers and the like',
         'Skilled construction workers and the like, except electricians',
         'Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like',
         'Workers in food processing, woodworking, clothing and other industries and crafts',
         'Cleaning workers',
         'Unskilled workers in agriculture, animal production, fisheries and forestry',
         'Unskilled workers in extractive industry, construction, manufacturing and transport',
         'Meal preparation assistants'
   ])
   fathers_occupation = st.selectbox("Pekerjaan Ayah", [
         'Student',
         'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers',
         'Specialists in Intellectual and Scientific Activities',
         'Intermediate Level Technicians and Professions',
         'Administrative staff',
         'Personal Services, Security and Safety Workers and Sellers',
         'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry',
         'Skilled Workers in Industry, Construction and Craftsmen',
         'Installation and Machine Operators and Assembly Workers',
         'Unskilled Workers',
         'Armed Forces Professions',
         'Other Situation',
         '(blank)',
         'Armed Forces Officers',
         'Armed Forces Sergeants',
         'Other Armed Forces personnel',
         'Directors of administrative and commercial services',
         'Hotel, catering, trade and other services directors',
         'Specialists in the physical sciences, mathematics, engineering and related techniques',
         'Health professionals',
         'Teachers',
         'Specialists in finance, accounting, administrative organization, public and commercial relations',
         'Intermediate level science and engineering technicians and professions',
         'Technicians and professionals, of intermediate level of health',
         'Intermediate level technicians from legal, social, sports, cultural and similar services',
         'Information and communication technology technicians',
         'Office workers, secretaries in general and data processing operators',
         'Data, accounting, statistical, financial services and registry-related operators',
         'Other administrative support staff',
         'Personal service workers',
         'Sellers',
         'Personal care workers and the like',
         'Protection and security services personnel',
         'Market-oriented farmers and skilled agricultural and animal production workers',
         'Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence',
         'Skilled construction workers and the like, except electricians',
         'Skilled workers in metallurgy, metalworking and similar',
         'Skilled workers in electricity and electronics',
         'Workers in food processing, woodworking, clothing and other industries and crafts',
         'Fixed plant and machine operators',
         'Assembly workers',
         'Vehicle drivers and mobile equipment operators',
         'Unskilled workers in agriculture, animal production, fisheries and forestry',
         'Unskilled workers in extractive industry, construction, manufacturing and transport',
         'Meal preparation assistants',
         'Street vendors (except food) and street service providers'
   ])
   admission_grade = st.slider("Nilai Tes Masuk", min_value=0.0, max_value=200.0, step=0.1)
   displaced = st.selectbox("Mahasiswa Terpencil?", ["Ya", "Tidak"])
   special_needs = st.selectbox("Kebutuhan Khusus?", ["Ya", "Tidak"])
   debtor = st.selectbox("Mahasiswa Berhutang?", ["Ya", "Tidak"])
   scholarship = st.selectbox("Penerima Beasiswa?", ["Ya", "Tidak"])
   international = st.selectbox("Mahasiswa Internasional?", ["Ya", "Tidak"])
   curricular_units_1st_sem_enrolled = st.number_input("Jumlah SKS yang Didaftarkan Semester 1", min_value=0, max_value=100, value=0)
   curricular_units_1st_sem_evaluations = st.number_input("Jumlah SKS yang Ditolak Semester 1", min_value=0, max_value=100, value=0)
   curricular_units_1st_sem_approved = st.number_input("Jumlah SKS yang Diterima Semester 1", min_value=0, max_value=100, value=0)
   units_1st = st.slider("Nilai Semester 1", 0.0, 200.0, step=0.1)
   curricular_units_2nd_sem_enrolled = st.number_input("Jumlah SKS yang Didaftarkan Semester 2", min_value=0, max_value=100, value=0)
   curricular_units_2nd_sem_evaluations = st.number_input("Jumlah SKS yang Ditolak Semester 2", min_value=0, max_value=100, value=0)
   curricular_units_2nd_sem_approved = st.number_input("Jumlah SKS yang Diterima Semester 2", min_value=0, max_value=100, value=0)
   units_2nd = st.slider("Nilai Semester 2", 0.0, 200.0, step=0.1)
   
   submitted = st.form_submit_button("Prediksi")

if submitted:
   # Buat DataFrame input

   # Encode marital_status
   marital_status_mapping = {
      'Single': 1,
      'Married': 2,
      'Widower': 3,
      'Divorced': 4,
      'Facto Union': 5,
      'Legally Separated': 6
   }
   marital_status = marital_status_mapping[marital_status]

   # Encode application_mode
   application_mode_mapping = {
      '1st phase - general contingent': 1,
      'Ordinance No. 612/93': 2,
      '1st phase - special contingent (Azores Island)': 5,
      'Holders of other higher courses': 7,
      'Ordinance No. 854-B/99': 10,
      'International student (bachelor)': 15,
      '1st phase - special contingent (Madeira Island)': 16,
      '2nd phase - general contingent': 17,
      '3rd phase - general contingent': 18,
      'Ordinance No. 533-A/99, item b2) (Different Plan)': 26,
      'Ordinance No. 533-A/99, item b3 (Other Institution)': 27,
      'Over 23 years old': 39,
      'Transfer': 42,
      'Change of course': 43,
      'Technological specialization diploma holders': 44,
      'Change of institution/course': 51,
      'Short cycle diploma holders': 53,
      'Change of institution/course (International)': 57
   }
   application_mode = application_mode_mapping[application_mode]

   #Encode course
   course_mapping = {
      'Biofuel Production Technologies': 33,
      'Animation and Multimedia Design': 171,
      'Social Service (evening attendance)': 8014, 
      'Agronomy': 9003,
      'Communication Design': 9070,
      'Veterinary Nursing': 9085,
      'Informatics Engineering': 9119,
      'Equinculture': 9130,
      'Management': 9147,
      'Social Service': 9238,
      'Tourism': 9254,
      'Nursing': 9500,
      'Oral Hygiene': 9556,
      'Advertising and Marketing Management':  9670,
      'Journalism and Communication': 9773,
      'Basic Education': 9853,
      'Management (evening attendance)': 9991,
   }
   course = course_mapping[course]

   # Encode Previous Qualification
   previous_qualification_mapping = {
   'Secondary education': 1,
   "Bachelor's degree": 2,
   'Degree': 3,
   "Master's": 4,
   'Doctorate': 5,
   'Frequency of higher education': 6,
   '12th year of schooling - not completed': 9,
   '11th year of schooling - not completed': 10,
   'Other - 11th year of schooling': 12,
   '10th year of schooling': 14,
   '10th year of schooling - not completed': 15,
   'Basic education 3rd cycle (9th/10th/11th year) or equiv.': 19,
   'Basic education 2nd cycle (6th/7th/8th year) or equiv.': 38,
   'Technological specialization course': 39,
   'Higher education - degree (1st cycle)': 40,
   'Professional higher technical course': 42,
   'Higher education - master (2nd cycle)': 43
   }
   previous_qualification = previous_qualification_mapping[previous_qualification]

   # Emcpde mothers occupation
   mothers_occupation_mapping = {
      'Student': 0,
      'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers': 1,
      'Specialists in Intellectual and Scientific Activities': 2,
      'Intermediate Level Technicians and Professions': 3,
      'Administrative staff': 4,
      'Personal Services, Security and Safety Workers and Sellers': 5,
      'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry': 6,
      'Skilled Workers in Industry, Construction and Craftsmen': 7,
      'Installation and Machine Operators and Assembly Workers': 8,
      'Unskilled Workers': 9,
      'Armed Forces Professions': 10,
      'Other Situation': 90,
      '(blank)': 99,
      'Health professionals': 122,
      'Teachers': 123,
      'Specialists in information and communication technologies (ICT)': 125,
      'Intermediate level science and engineering technicians and professions': 131,
      'Technicians and professionals, of intermediate level of health': 132,
      'Intermediate level technicians from legal, social, sports, cultural and similar services': 134,
      'Office workers, secretaries in general and data processing operators': 141,
      'Data, accounting, statistical, financial services and registry-related operators': 143,
      'Other administrative support staff': 144,
      'Personal service workers': 151,
      'Sellers': 152,
      'Personal care workers and the like': 153,
      'Skilled construction workers and the like, except electricians': 171,
      'Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like': 173,
      'Workers in food processing, woodworking, clothing and other industries and crafts': 175,
      'Cleaning workers': 191,
      'Unskilled workers in agriculture, animal production, fisheries and forestry': 192,
      'Unskilled workers in extractive industry, construction, manufacturing and transport': 193,
      'Meal preparation assistants': 194
   }
   mothers_occupation = mothers_occupation_mapping[mothers_occupation]

   # Encode fathers occupation
   fathers_occupation_mapping = {
      'Student': 0,
      'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers': 1,
      'Specialists in Intellectual and Scientific Activities': 2,
      'Intermediate Level Technicians and Professions': 3,
      'Administrative staff': 4,
      'Personal Services, Security and Safety Workers and Sellers': 5,
      'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry': 6,
      'Skilled Workers in Industry, Construction and Craftsmen': 7,
      'Installation and Machine Operators and Assembly Workers': 8,
      'Unskilled Workers': 9,
      'Armed Forces Professions': 10,
      'Other Situation': 90,
      '(blank)': 99,
      'Armed Forces Officers': 101,
      'Armed Forces Sergeants': 102,
      'Other Armed Forces personnel': 103,
      'Directors of administrative and commercial services': 112,
      'Hotel, catering, trade and other services directors': 114,
      'Specialists in the physical sciences, mathematics, engineering and related techniques': 121,
      'Health professionals': 122,
      'Teachers': 123,
      'Specialists in finance, accounting, administrative organization, public and commercial relations': 124,
      'Intermediate level science and engineering technicians and professions': 131,
      'Technicians and professionals, of intermediate level of health': 132,
      'Intermediate level technicians from legal, social, sports, cultural and similar services': 134,
      'Information and communication technology technicians': 135,
      'Office workers, secretaries in general and data processing operators': 141,
      'Data, accounting, statistical, financial services and registry-related operators': 143,
      'Other administrative support staff': 144,
      'Personal service workers': 151,
      'Sellers': 152,
      'Personal care workers and the like': 153,
      'Protection and security services personnel': 154,
      'Market-oriented farmers and skilled agricultural and animal production workers': 161,
      'Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence': 163,
      'Skilled construction workers and the like, except electricians': 171,
      'Skilled workers in metallurgy, metalworking and similar': 172,
      'Skilled workers in electricity and electronics': 174,
      'Workers in food processing, woodworking, clothing and other industries and crafts': 175,
      'Fixed plant and machine operators': 181,
      'Assembly workers': 182,
      'Vehicle drivers and mobile equipment operators': 183,
      'Unskilled workers in agriculture, animal production, fisheries and forestry': 192,
      'Unskilled workers in extractive industry, construction, manufacturing and transport': 193,
      'Meal preparation assistants': 194,
      'Street vendors (except food) and street service providers': 195
   }
   fathers_occupation = fathers_occupation_mapping[fathers_occupation]


   input_df = pd.DataFrame([{
   'Marital_status': int(marital_status),
   'Application_mode': int(application_mode),
   'Application_order': int(application_order),
   'Course': int(course),
   'Daytime_evening_attendance': int(1 if attendance == "Daytime" else 0),
   'Previous_qualification': int(previous_qualification),
   'Previous_qualification_grade': int(previous_qualification_grade),
   'Mothers_occupation': int(mothers_occupation),
   'Fathers_occupation': int(fathers_occupation),
   'Admission_grade': float(admission_grade),
   'Displaced': int(1 if displaced == "Ya" else 0),
   'Educational_special_needs': int(1 if special_needs == "Ya" else 0),
   'Debtor': int(1 if debtor == "Ya" else 0),
   'Scholarship_holder': int(1 if scholarship == "Ya" else 0),
   'Age_at_enrollment': int(age),
   'International': int(1 if international == "Ya" else 0),
   'Curricular_units_1st_sem_enrolled': int(curricular_units_1st_sem_enrolled),
   'Curricular_units_1st_sem_evaluations': int(curricular_units_1st_sem_evaluations),
   'Curricular_units_1st_sem_approved': float(curricular_units_1st_sem_approved),
   'Curricular_units_1st_sem_grade': int(units_1st),
   'Curricular_units_2nd_sem_enrolled': int(curricular_units_2nd_sem_enrolled),
   'Curricular_units_2nd_sem_evaluations': int(curricular_units_2nd_sem_evaluations),
   'Curricular_units_2nd_sem_approved': int(curricular_units_2nd_sem_approved),
   'Curricular_units_2nd_sem_grade': float(units_2nd)
   }])

   # Encoding (jika diperlukan)
   # Encoding categorical columns (e.g., 'Gender') if necessary
   #  input_df['Gender'] = encoder.transform(input_df[['Gender']])
   #  input_encoded = input_df

   # Prediksi
   pred = model.predict(input_df)[0]
   pred_label = {0: 'Dropout', 1: 'Enrolled', 2: 'Graduate'}[pred]

   st.success(f"✅ Hasil Prediksi: **{pred_label}**")
