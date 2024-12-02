CREATE TABLE Patients (
    PatientID SERIAL PRIMARY KEY,
    sex VARCHAR(10),
    AgeCategory VARCHAR(10),
    Race VARCHAR(50)
);

CREATE TABLE Medications (
    medicationID SERIAL PRIMARY KEY,
    PatientID INT NOT NULL,
    medicationname VARCHAR(100),
    dosage VARCHAR(20),
    frequency VARCHAR(50),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);

CREATE TABLE Insurance (
    InsuranceID SERIAL PRIMARY KEY,
    PatientID INT NOT NULL,
    providername VARCHAR(100),
    policyname VARCHAR(100),
    coveragedetails TEXT,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);

CREATE TABLE PatientMedications (
    PatientmedicationID SERIAL PRIMARY KEY,
    PatientID INT NOT NULL,
    medicationID INT NOT NULL,
    startdate DATE,
    enddate DATE,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (medicationID) REFERENCES Medications(medicationID)
);

CREATE TABLE Healthrecords (
    recordID SERIAL PRIMARY KEY,
    PatientID INT NOT NULL,
    bmi NUMERIC(5, 2),
    smoking BOOLEAN,
    alcoholdrinking BOOLEAN,
    heartdisease BOOLEAN,
    physicalactivity BOOLEAN,
    mentalhealth BOOLEAN,
    physicalhealth BOOLEAN,
    diabetic BOOLEAN,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);

CREATE TABLE Tests (
    testID SERIAL PRIMARY KEY,
    PatientID INT NOT NULL,
    testtype VARCHAR(50),
    testdate DATE,
    result VARCHAR(50),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);

CREATE TABLE Appointments (
    AppointmentID SERIAL PRIMARY KEY,
    PatientID INT NOT NULL,
    appointmentdate DATE,
    providername VARCHAR(100),
    notes TEXT,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);
