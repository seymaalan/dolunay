DELETE FROM events WHERE event_name = 'Açık Mikrofon' OR event_name = 'Nefis Terbiyesi';
INSERT INTO events(
	event_name, genre, segment, address, city, event_date, event_time, url)
	VALUES ('DATE', 'eğlence', 'bo sohbet', 'beytepe', 'Ankara', '2024-02-19','12:00:00' , 'https://www.youtube.com/@sumeyrakoc8926/featured'),
	('Nefis Terbiyesi', 'Eğitici', 'muhabbet', 'beytepe kız yurdu', 'Ankara', '2024-02-23','20:30:00' , 'http://localhost:8888/tree'),
	('ismini unuttumm','türsüzsün senn','uyuma artık segment kollarımdaaa','adresini yaktımm','kalma bu şehirdeee','tüm tarihlerin çöpte','sensiz zaman çok aceleee','bağlantımız kalmasın git ebediyeteee'),
	('Açık Mikrofon', 'Comedy', 'Arts & Theatre', 'Fevzi Çakmak-1 Sokak NO 11, Kızılay', 'Ankara', '2024-02-20','20:30:00' , 'https://www.instagram.com/p/C1Bt-K8CQK8/?utm_source=ig_web_button_share_sheet&igsh=ODdmZWVhMTFiMw== ');
UPDATE events SET event_name = 'GİZZLİ' WHERE event_name = 'ismini unuttumm';