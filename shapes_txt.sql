
copy (
	select shape_id, st_y(geom) shape_pt_lat, st_x(geom) shape_pt_lon, 
	row_number() over (order by path) shape_pt_sequence
	from
	(select shape_id, (dp).path path, ST_Transform((dp).geom, 4326) geom
	  from
	  (select shape_id, St_DumpPoints(geom) dp
	   from dadosagueda.carreiras_tp
	   where not shape_id is null) a
	) b
)
to '/var/lib/pgsql/data/shapes.txt' CSV

