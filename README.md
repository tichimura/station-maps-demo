
# get the data from MLIT with UNIX date
# Unix epoch time: 1616659623616 -> Thursday, March 25, 2021 8:07:03.616 AM
curl -o work_data.json http://www.douro-kouji-meter.ktr.mlit.go.jp/work_data.php?_=1616659623616

# convert data from the output
python3 geojson.py ~/Downloads/work_data.json ~/Downloads/work_data.geojson

# Update data as tileset
# tichimura.cknlaf6jd0rev29mujnmieui4-35t3b
# ~/Downloads/work_data.geojson 
