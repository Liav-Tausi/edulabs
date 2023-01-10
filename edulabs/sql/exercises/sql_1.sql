--1
select * from superstore_data; 


--2
select count(*) from superstore_data;


--3
select * from superstore_data limit 10;


--4
select * from superstore_data limit 25 offset 20;


--5
select id, year_birth, marital_status from superstore_data limit 20;


--6
select id, mntwines from superstore_data where mntwines > 1000;


--7
select date_part('year', now())  - year_birth,
	marital_status from superstore_data
where mntfishproducts < 500 and mntmeatproducts > 500;


--8
select count(response) as total_response from superstore_data;


--9
select education from superstore_data group by education order by education;


--10
select min(date_part('year', now())  - year_birth) FR superstore_data;


--11
SELECT id, marital_status, date_part('year', now()) - year_birth AS age
FROM superstore_data
GROUP BY id, marital_status, date_part('year', now()) - year_birth;


--12 
SELECT round(avg(income)) FROM superstore_data WHERE complain >= 1 GROUP BY income ;


--13
SELECT id, kidhome FROM superstore_data GROUP BY id, kidhome ;


--14 
SELECT id, income,  date_part('year', now()) - year_birth AS age  
FROM superstore_data
WHERE numwebpurchases > numstorepurchases;

--15
SELECT id, (kidhome  + teenhome) 
FROM superstore_data
WHERE recency >= 1;

--16
SELECT COUNT(*) 
FROM superstore_data
WHERE mntfishproducts = 0 or mntmeatproducts  = 0; 

--17
SELECT *
FROM superstore_data
ORDER BY mntgoldprods DESC limit 1;

--18
SELECT id, date_part('year', now()) - year_birth AS age_between
FROM superstore_data
WHERE date_part('year', now()) - year_birth BETWEEN 20 AND 40
ORDER BY date_part('year', now()) - year_birth;

--19
SELECT year_birth 
FROM superstore_data 
GROUP BY year_birth
ORDER BY year_birth;

--20
SELECT *
FROM superstore_data
ORDER BY mntsweetproducts DESC
LIMIT 10;

--21
SELECT count(*), marital_status 
FROM superstore_data 
GROUP BY marital_status; 

--22
SELECT education, SUM(mntsweetproducts + mntwines) AS total_sweets_wine
FROM superstore_data
GROUP BY education;

--23
SELECT marital_status,
       MAX(date_part('YEAR', NOW()) - year_birth) AS max_year,
       MIN(date_part('YEAR', NOW()) - year_birth) AS min_year
FROM superstore_data 
GROUP BY marital_status, education 
ORDER BY education, MIN(date_part('YEAR', NOW()) - year_birth);

--24
SELECT COUNT(date_part('YEAR', NOW()) - year_birth) 
FROM superstore_data
WHERE response >= 1 AND complain = 0; 



--25 
SELECT
	education,
	MIN(date_part('YEAR', NOW()) - year_birth) AS min_year
FROM
	superstore_data
GROUP BY
	education
ORDER BY
	min_year;

--25
SELECT 
	  DISTINCT ON (education)
	  education, 
	  MIN(date_part('YEAR', NOW()) - year_birth) AS min_year,
	  id
FROM superstore_data 
ORDER BY education, min_year;


--26
SELECT
	kidhome + teenhome, 
	   ROUND(AVG(mntfishproducts), 2) AS avg_fish,
	   ROUND(AVG(mntmeatproducts), 2) AS avg_meat,
	   ROUND(AVG(mntsweetproducts), 2) AS avg_sweet, 
	   ROUND(AVG(mntgoldprods), 2) AS avg_gold,
	   ROUND(AVG(mntwines), 2) AS avg_wine
FROM
	superstore_data
GROUP BY
	kidhome + teenhome;


--27 
SELECT teenhome ,
	   MIN(date_part('YEAR', NOW()) - year_birth) AS min_year,
       year_birth
FROM superstore_data
GROUP BY teenhome, year_birth 
ORDER BY min_year;


--28
SELECT COUNT(*)
FROM superstore_data
WHERE response >= 0;


--29
SELECT marital_status,
	   ROUND(AVG(kidhome), 2) AS avg_kids,
	   ROUND(AVG(teenhome), 2) AS avg_teen
FROM superstore_data  
GROUP BY marital_status;

--30
SELECT education,
	   MIN(income) AS minimum_income,
	   MAX(income) AS maximum_income,
	   ROUND(AVG(income)) AS avg_income
FROM superstore_data
GROUP BY education;







































 