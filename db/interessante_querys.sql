/* welche additional_text sind häufig */

select additional_text, COUNT(*) as c from trains group by additional_text order by c desc;

/* welche Züge haben die häufigsten einträge */
select  station_id, number, COUNT(*) as c from trains group by station_id, number HAVING c>1 order by c desc;

/* wieviele Züge haben wir Pro Bahnhof */
select  station_id, COUNT(*) as c from trains group by station_id order by c desc;