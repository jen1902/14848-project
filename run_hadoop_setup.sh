git clone https://github.com/jen1902/14848-project.git && \
                    echo 'enter project' && \
                    cd 14848-project && \
                    hadoop fs -put input_data.txt / && \
                    hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -file mapper.py -mapper '/opt/conda/default/bin/python mapper.py' -file reducer.py -reducer '/opt/conda/default/bin/python reducer.py' -input /input_data.txt -output /output && \
                    hadoop fs -getmerge /output result && \
                    cat result
