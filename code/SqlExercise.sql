--temp table creation

IF OBJECT_ID('tempdb..#tempresult') IS NOT NULL
	DROP TABLE #tempresult;
create table #tempresult
(
Id INT,
PatientId INT,
TestType varchar(10),
EffectiveDateTime varchar(50),
Value INT
);
-- Insert data from tsv file to temp table

BULK INSERT #tempresult
FROM 'C:\Users\JJ\TSV\test_result.tsv'
WITH (
  FIELDTERMINATOR = '\t',
  FIRSTROW = 2
);
-- Select the latest records based on effective date from test type 'a1c'

SELECT MAX(EffectiveDateTime) AS EffectiveDateTime,Patientid,TestType FROM 
#tempresult
WHERE VALUE >7
AND TESTTYPE ='a1c'
GROUP BY Patientid,TestType
