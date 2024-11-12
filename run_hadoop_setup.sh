git clone https://github.com/jen1902/14848-project.git && \
                    echo 'enter project' && \
                    cd 14848-project && \
                    echo 'remove' && \
                    hadoop fs -put /input_data.txt / && \
                    hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -file mapper.py -mapper '/opt/conda/default/bin/python mapper.py' -file reducer.py -reducer '/opt/conda/default/bin/python reducer.py' -input /input_data.txt -output /output11 && \
                    hadoop fs -getmerge /output11 result5 && \
                    cat result5
