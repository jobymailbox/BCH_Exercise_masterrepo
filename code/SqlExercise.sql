SELECT MAX(EffectiveDateTime) AS EffectiveDateTime,Patientid,TestType FROM 
TEST_RESULT
WHERE VALUE >7
AND TestType ='a1c'
GROUP BY Patientid,TestType
