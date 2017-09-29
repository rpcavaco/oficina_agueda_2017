
from pyexcel_ods import get_data

from os.path import join as path_join

basepath = "/mnt/Dados/DADOS/DadosAbertoAgueda/"

outfile = "GTFS/stop_times.txt"
#trip_id,arrival_time,departure_time,stop_id,stop_sequence,pickup_type,drop_off_type
#AWE1,0:06:10,0:06:10,S1,1,0,0
#AWE1,,,S2,2,1,3
#AWE1,0:06:20,0:06:30,S3,3,0,0

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# ############################################################
#fname = "carreira7311.ods"

#ROUTE_ID = "7311"

#START_COL = 4
#COLS = 4
#FIRST_REV_COL = 7
#FIRST_ROW = 9
#LAST_ROW = 37
# ############################################################
# ############################################################
fname = "carreira7326.ods"

ROUTE_ID = "7326"

START_COL = 4
COLS = 4
FIRST_REV_COL = 6
FIRST_ROW = 8
LAST_ROW = 29
# ############################################################

def do_read(full_path):

	data = get_data(full_path)
	outfp = path_join(basepath, outfile)
	print(outfp)
	
	for ci in range(START_COL, START_COL+COLS):
		
		syntcol = ci - START_COL
		#print("col",ci)
		seqval = 0
		
		if ci >= FIRST_REV_COL:

			for ri in range(LAST_ROW, FIRST_ROW-1, -1):
				#print(ri,data['Folha1'][ri])
				
				stop_id = data['Folha1'][ri][1]
				try:
					rawtime = data['Folha1'][ri][ci]
				except:
					print(ri,ci)
					raise
				
				strp = rawtime.strip()
				if len(strp) == 0 or strp == '-':
					continue
					
				seqval += 1
				time = rawtime[:-1] + ":00"
				tripid = ROUTE_ID + LETTERS[syntcol]
				with open(outfp, 'a') as out:
					out.write(tripid+','+time+','+time+','+str(stop_id)+','+str(seqval) + '\n')
				#print(tripid, time, time, stop_id, seqval)
			
		else:
			
			for ri in range(FIRST_ROW, LAST_ROW+1):
				#print(ri,data['Folha1'][ri])

				stop_id = data['Folha1'][ri][1]
				rawtime = data['Folha1'][ri][ci]
				
				strp = rawtime.strip()
				if len(strp) == 0 or strp == '-':
					continue

				seqval += 1
				time = rawtime[:-1] + ":00"
				tripid = ROUTE_ID + LETTERS[syntcol]
				with open(outfp, 'a') as out:
					out.write(tripid+','+time+','+time+','+str(stop_id)+','+str(seqval) + '\n')
				#print(tripid, time, time, stop_id, seqval)
	
#>>> import json
#>>> print(json.dumps(data))
#{"Sheet 1": [[1, 2, 3], [4, 5, 6]], "Sheet 2": [["row 1", "row 2", "row 3"]]}


if __name__ == "__main__":
	fp = path_join(basepath, fname)
	do_read(fp)
	

