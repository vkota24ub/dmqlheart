COPY Patients(sex, AgeCategory, Race)
FROM 'C:\Users\varun kumar kota\CSE560\patients.csv'
DELIMITER ','
CSV HEADER;

COPY Medications(PatientID, medicationname, dosage, frequency)
FROM 'C:\Users\varun kumar kota\CSE560\medications.csv'
DELIMITER ','
CSV HEADER;

COPY Insurance(PatientID, providername, policyname, coveragedetails)
FROM 'C:\Users\varun kumar kota\CSE560\insurance.csv'
DELIMITER ','
CSV HEADER;

COPY PatientMedications(PatientID, medicationID, startdate, enddate)
FROM 'C:\Users\varun kumar kota\CSE560\patient_medications.csv'
DELIMITER ','
CSV HEADER;

COPY Healthrecords(PatientID, bmi, smoking, alcoholdrinking, heartdisease, physicalactivity, mentalhealth, physicalhealth, diabetic)
FROM 'C:\Users\varun kumar kota\CSE560\healthrecords.csv'
DELIMITER ','
CSV HEADER;

COPY Tests(PatientID, testtype, testdate, result)
FROM 'C:\Users\varun kumar kota\CSE560\tests.csv'
DELIMITER ','
CSV HEADER;

COPY Appointments(PatientID, appointmentdate, providername, notes)
FROM 'C:\Users\varun kumar kota\CSE560\Appointments.csv'
DELIMITER ','
CSV HEADER;
