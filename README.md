
# Sample Application for data layering with multiple data sources

## data sources

[国土交通省　関東地方整備局](http://www.douro-kouji-meter.ktr.mlit.go.jp/index.php)

 get the data from MLIT with UNIX date
 Unix epoch time: 1616659623616 -> Thursday, March 25, 2021 8:07:03.616 AM
 
`curl -o work_data.json http://www.douro-kouji-meter.ktr.mlit.go.jp/work_data.php?_=1616659623616`

# convert data from the output

python3 geojson.py source.json output.geojson

# Update data as tileset

# tichimura.cknlaf6jd0rev29mujnmieui4-35t3b
# ~/Downloads/work_data.geojson 


## video sources

Video's are those allowing playback videos

https://support.google.com/youtube/answer/6301625?hl=en