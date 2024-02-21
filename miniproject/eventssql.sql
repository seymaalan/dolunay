CREATE TABLE events_table (
	id SERIAL PRIMARY KEY,
	event_name text,
	genre text,
	segment text,
	address text,
	city text,
	localdate date,
	local_time time,
	url text
);
COPY events_table2(event_name, genre, segment, address, city, localdate, local_time, url) FROM 'C:\Users\gulsu\Dolunay\dolunay\miniproject\events.csv' CSV HEADER;
SELECT * FROM events_table2;