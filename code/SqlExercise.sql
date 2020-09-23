
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
BULK INSERT #tempresult
FROM 'C:\Users\1146595\TEST\csv\TSV\test_result.tsv'
WITH (
  FIELDTERMINATOR = '\t',
  FIRSTROW = 2
);
SELECT MAX(EffectiveDateTime) AS EffectiveDateTime,Patientid,TestType FROM 
#tempresult
WHERE VALUE >7
AND TESTTYPE ='a1c'
GROUP BY Patientid,TestType
