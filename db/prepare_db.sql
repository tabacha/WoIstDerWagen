DELETE FROM stations WHERE id="ID";

UPDATE trains SET track_id="4", track_name="Gleis Fern 4" WHERE track_name="Gleis Fern 4 /";
UPDATE trains SET track_id="5", track_name="Gleis Fern 5" WHERE track_name="Gleis Fern 5 /";
UPDATE trains SET track_id="6", track_name="Gleis Fern 6" WHERE track_name="Gleis Fern 6 /";
UPDATE trains SET track_id="7", track_name="Gleis Fern 7" WHERE track_name="Gleis Fern 7 /";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="SM 20";
DELETE FROM trains WHERE track_id="SM 20";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="parke";
DELETE FROM trains WHERE track_id="parke";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="ohne";
DELETE FROM trains WHERE track_id="ohne";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="Muste";
DELETE FROM trains WHERE track_id="Muste";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="MA";
DELETE FROM trains WHERE track_id="MA";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="IC-2";
DELETE FROM trains WHERE track_id="IC-2";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="Mitar";
DELETE FROM trains WHERE track_id="Mitar";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="Geis";
DELETE FROM trains WHERE track_id="Geis";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="BR";
DELETE FROM trains WHERE track_id="BR";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="Blank";
DELETE FROM trains WHERE track_id="Blank";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="Bau J";
DELETE FROM trains WHERE track_id="Bau J";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="a";
DELETE FROM trains WHERE track_id="a";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="?";
DELETE FROM trains WHERE track_id="?";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="1   T";
DELETE FROM trains WHERE track_id="1   T";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="2016";
DELETE FROM trains WHERE track_id="2016";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="2 Lin";
DELETE FROM trains WHERE track_id="2 Lin";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="301 Z";
DELETE FROM trains WHERE track_id="301 Z";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="0102";
DELETE FROM trains WHERE track_id="0102";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="05";
DELETE FROM trains WHERE track_id="05";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="07";
DELETE FROM trains WHERE track_id="07";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="3ab";
DELETE FROM trains WHERE track_id="3ab";

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id="99+";
DELETE FROM trains WHERE track_id="99+";

ALTER TABLE trains MODIFY track_id int(5);

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id>302;
DELETE FROM trains WHERE track_id>302;

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id>54 and t.track_id<100;
DELETE FROM trains  WHERE track_id>54 and track_id<100;

ALTER TABLE waggons ADD PRIMARY KEY (train_id, position);
ALTER TABLE trains ADD PRIMARY KEY (id);
ALTER TABLE stations ADD PRIMARY KEY (id);

CREATE INDEX eva_id_idx ON stations (eva_id);
CREATE INDEX train_number_idx ON trains (number);

ALTER TABLE trains MODIFY number int(5);


ALTER TABLE trains MODIFY additional_text varchar(256) CHARACTER SET utf8;
UPDATE trains SET additional_text=CAST(CONVERT(additional_text USING latin1) AS BINARY);

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id=33 AND t.station_id='FF';
DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id=33 AND t.station_id='FFS';
DELETE FROM trains WHERE track_id=33 and station_id='FFS';
DELETE FROM trains WHERE track_id=33 and station_id='FF';

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.track_id=0;
DELETE FROM trains WHERE track_id=0;

DELETE w FROM waggons w INNER JOIN trains t WHERE t.id=w.train_id AND t.number=71 and t.type='RB';
DELETE FROM trains  WHERE  number=71 and type='RB';