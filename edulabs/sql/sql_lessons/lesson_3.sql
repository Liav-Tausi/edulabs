SELECT COUNT(*) FROM jan;



EXPLAIN ANALYSE(
	SELECT count(*) FROM jan WHERE distance > 1000
);



CREATE INDEX jan_distance_idx on jan(distance);


EXPLAIN ANALYSE(
	SELECT count(*) FROM jan WHERE day_of_week > 3
);

CREATE INDEX jan_day_of_week_idx on jan(day_of_week);


CREATE INDEX
	jan_2_idx on jan(day_of_week, distance);



EXPLAIN ANALYSE(
	SELECT count(*) FROM jan WHERE day_of_week > 5 and distance > 1000
);



