INSERT INTO
	drivers (passport_num, "name", address)
values
	('111111111', 'Israel Israeli', 'Tel Aviv');

INSERT INTO
	drivers (passport_num, "name", address)
values
	('222222222', 'Moshe Cohen', 'Hod Hasharon');

INSERT INTO
	drivers (passport_num, "name", address)
values
	('333333333', 'David Shwimmer', 'Tveriya');

INSERT INTO
	drivers (passport_num, "name", address)
values
	('444444444', 'Tali Shani', 'Tel Aviv');

INSERT INTO
	drivers (passport_num, "name", address)
values
	('555555555', 'Sagi Shem Tov', 'Tel Aviv');


INSERT INTO stops (city, "name")
VALUES('Tel Aviv', 'Central bus station');

INSERT INTO stops (city, "name")
VALUES('Tel Aviv', 'Alenby');

INSERT INTO stops (city, "name")
VALUES('Tel Aviv', 'University');

INSERT INTO stops (city, "name")
VALUES('Haifa', 'Matam');

INSERT INTO stops (city, "name")
VALUES('Haifa', 'Technion');



INSERT INTO routes (route_num, orig_stop_id, dest_stop_id)
VALUES(100, 1, 4);

INSERT INTO routes (route_num, orig_stop_id, dest_stop_id)
VALUES(200, 1, 3);

INSERT INTO routes (route_num, orig_stop_id, dest_stop_id)
VALUES(300, 4, 5);

INSERT INTO routes (route_num, orig_stop_id, dest_stop_id)
VALUES(400, 3, 5);

INSERT INTO routes (route_num, orig_stop_id, dest_stop_id)
VALUES(500, 3, 2);



INSERT INTO rides (weekday, route_id, driver_id)
VALUES('sun', 1, 1);

INSERT INTO rides (weekday, route_id, driver_id)
VALUES('tue', 2, 1);

INSERT INTO rides (weekday, route_id, driver_id)
VALUES('tue', 1, 3);

INSERT INTO rides (weekday, route_id, driver_id)
VALUES('thu', 4, 2);

INSERT INTO rides (weekday, route_id, driver_id)
VALUES('sun', 1, 5);


-- T
INSERT INTO ride_stops (stop_ordinal, arrival_time, departure_time, ride_id, stop_id)
VALUES(1, '10:30', '10:31', 1, 1);

INSERT INTO ride_stops (stop_ordinal, arrival_time, departure_time, ride_id, stop_id)
VALUES(2, '10:50', '10:55', 1, 3);

INSERT INTO ride_stops (stop_ordinal, arrival_time, departure_time, ride_id, stop_id)
VALUES(3, '11:30', '11:32', 1, 5);

INSERT INTO ride_stops (stop_ordinal, arrival_time, departure_time, ride_id, stop_id)
VALUES(4, '11:50', '11:50', 1, 4);


INSERT INTO service_interruptions (interrupt_type, ts, ride_id)
VALUES('cancelation', '2023-01-08 04:05:06', 1);

INSERT INTO service_interruptions (interrupt_type, ts, ride_id)
VALUES('delay', '2023-01-09 17:05:00', 2);

INSERT INTO service_interruptions (interrupt_type, ts, ride_id)
VALUES('delay', '2023-01-06 14:00:00', 1);

INSERT INTO service_interruptions (interrupt_type, ts, ride_id)
VALUES('cancelation', '2023-01-05 09:05:10', 3);

INSERT INTO service_interruptions (interrupt_type, ts, ride_id)
VALUES('cancelation', '2023-01-08 12:00:00', 1);


SELECT * FROM rides;
SELECT * FROM routes;





--1 Display amount of rides for each route

SELECT s.id AS route,
	   count(r.*)
FROM routes s
JOIN rides r on r.route_id = s.id
GROUP BY route;



--2 display amount of rides for each route and each weekday

SELECT s.id AS route,
	  r.weekday AS day_of,
	   count(r.*)
FROM routes s
JOIN rides r on r.route_id = s.id
GROUP BY route, day_of;



--3 display route with most rides

select r.route_num, count(r.*) as number_of_rides
from routes r
join rides s on s.route_id = r.id
group by r.id
order by count(r.*) desc
limit 1;



--4 get the weekday that has most rides for route 200

select r.route_num, count(r.*) as number_of_rides
from routes r
join rides s on s.route_id = r.id
where r.route_num = 200
group by r.id
order by count(r.*) desc
limit 1;


--5 Get all the routes that have stops in Haifa Matam


SELECT DISTINCT routes.*
FROM routes
JOIN ride_stops ON routes.id = ride_stops.ride_id
JOIN stops ON ride_stops.stop_id = stops.id
WHERE stops.city = 'Haifa' AND stops.name = 'Matam';


--6 Get driver names and amount of routes they drove

SELECT d."name" , COUNT(r.route_id)
FROM drivers d
JOIN rides r ON r.driver_id =  d.id
JOIN routes r2 on r2.id = r.route_id
GROUP BY d.name;


--7 Display driver names and total time they drove. Note, you should not take into account canceled rides.


SELECT d.name ,COUNT(DATE_PART('hour', rs.departure_time - rs.arrival_time)) + COUNT(DATE_PART('minute', rs.departure_time - rs.arrival_time))/60
FROM drivers d
JOIN rides r ON r.driver_id =  d.id
JOIN ride_stops rs ON rs.ride_id = r.id
JOIN service_interruptions si ON si.ride_id = r.id
WHERE si.interrupt_type != 'cancelation'
GROUP BY d.name;


--8 Get all the driver names who drive on route 100


SELECT d.name
FROM drivers d
JOIN rides r ON r.driver_id =  d.id
JOIN routes r2 on r2.id = r.route_id
WHERE r2.route_num = 100;


--9 Get all the routes which rides last more than 1 hour


SELECT d.name , SUM(DATE_PART('hour', rs.departure_time - rs.arrival_time)) +
SUM(DATE_PART('minute', rs.departure_time - rs.arrival_time))/60 AS ride_time
FROM drivers d
JOIN rides r ON r.driver_id =  d.id
JOIN ride_stops rs ON rs.ride_id = r.id
GROUP BY d.name
HAVING SUM(DATE_PART('hour', rs.departure_time - rs.arrival_time)) +
SUM(DATE_PART('minute', rs.departure_time - rs.arrival_time))/60 > 1;


--10 Display driver names, and amount of delays for each in the rides they drove


SELECT d.name, COUNT(CASE WHEN rs.arrival_time > rs.arrival_time THEN 1 END) as delay
FROM drivers d
JOIN rides r ON r.driver_id = d.id
JOIN ride_stops rs ON rs.ride_id = r.id
GROUP BY d.name
ORDER BY delay desc;








































