select * from superstore_data;
select id, income, teenhome from superstore_data;
select * from superstore_data where income > 100000

SELECT *
FROM superstore_data
WHERE income > 100000;

select id, education, marital_status  from superstore_data where income > 10000 and kidhome > 1;

select id, education, marital_status  from superstore_data where (income > 10000) and (kidhome > 1 or teenhome > 1);

SELECT COUNT(*) FROM superstore_data;

SELECT * FROM superstore_data WHERE teenhome = 4

SELECT COUNT(id) FROM superstore_data;

select
	round(avg(income), 2) as avg_income,
	round(avg(mntwines), 2) as avg_mntwines,
	round(avg(mntfruits), 2) as avg_fruits
from superstore_data sd;

select s.id from superstore_data s;


select sum(sd.teenhome) from superstore_data sd;

select id, teenhome + kidhome as total_kids from superstore_data s;

select sum(teenhome + kidhome) from superstore_data;

select * from superstore_data where id=837;

select id from
	(select * from superstore_data where id=837) as new_table;

select * from superstore_data limit 10;

select * from superstore_data limit 1 offset 6; --seven's row

select education, 
	 count(id),
	 round(avg(income), 0) as avg_income,
	 round(min(income), 0) as minimum,
     round(max(income), 0) as maximum			  
from superstore_data
group by education, marital_status 
order by education, marital_status;


select education, 
	 count(id),
	 round(avg(income), 0) as avg_income,
	 round(min(income), 0) as minimum,
     round(max(income), 0) as maximum			  
from superstore_data 
group by education, marital_status 
order by education
having education != 'Basic';


select * form_top where lower(movie_name) like '%king%';








































