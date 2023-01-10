CREATE TABLE drivers (
    id SERIAL PRIMARY KEY,
    passport_num INT UNIQUE NOT NULL,
    fullname VARCHAR(128) NOT NULL,
    address VARCHAR(256) NOT NULL
);



CREATE TABLE rides(
	id SERIAL PRIMARY KEY,
	ride_num INT UNIQUE NOT NULL,
	driver_id INT NOT NULL,
	route_id INT NOT NULL,
    FOREIGN KEY (driver_id) REFERENCES drivers(id)
);



CREATE TABLE services_interruptions(
	id SERIAL PRIMARY KEY,
	interruptions_type VARCHAR(255) CHECK (interruptions_type IN ('delay', 'cancel')),
	time_stamp TIMESTAMP NOT NULL,
	ride_id INT NOT NULL,
	FOREIGN KEY (ride_id) REFERENCES rides(id)
);




CREATE TABLE stops(
	id SERIAL PRIMARY KEY,
	city VARCHAR(128) NOT NULL,
	stop_name VARCHAR(128) NOT NULL
);



CREATE TABLE ride_stops(
	id SERIAL PRIMARY KEY,
	ride_id INT NOT NULL,
	stop_id INT NOT NULL,
	stop_original SERIAL NOT NULL,
	arivel_time time NOT NULL,
	depature_time time NOT NULL,
	FOREIGN KEY (ride_id) REFERENCES rides(id),
	FOREIGN KEY (stop_id) REFERENCES stops(id)
);




CREATE TABLE routes (
    id serial PRIMARY KEY,
    route_num int NOT NULL,
    origin_stop_id int NOT NULL,
    destination_stop_id int NOT NULL,
    FOREIGN KEY (id) REFERENCES rides(id),
    UNIQUE (origin_stop_id),
    UNIQUE (destination_stop_id)
);

