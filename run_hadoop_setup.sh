git clone https://github.com/jen1902/14848-project.git
&& echo "enter project"

&& cd 14848-project
&& echo "remove"
&& hadoop fs -rm /input_data.txt
&& hadoop fs -put /input_data.txt /
&& hadoop jar /usr/lib/hadoop/hadoop-streaming.jar     -file mapper.py -mapper '/opt/conda/default/bin/python mapper.py'     -file reducer.py -reducer '/opt/conda/default/bin/python reducer.py'     -input /input_data.txt -output /output10
&& hadoop fs -getmerge /output10 result4
&& cat result4
