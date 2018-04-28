# 1: Github Stats

## How To:
    cd Question\ 1
    # modify list_of_repos file for respective repositories 
    docker build -t github_stats .
    docker run --name github_stats -t github_stats
    # Clean up
    docker rm github_stats
    



# 2: Docker Compose setup

## How To:
       cd Question\ 2
       # Start docker containers [press ctrl+z to push to background]
       docker-compose up
       # open nginx custom page 
       open http://localhost
       # open kibana for checking logs processed through fluentd and pshed to elasticsearch
       # check if index got created in elasticsearch
       open http://localhost:9200/_cat/indices
       # create index pattern on kibana as fluentd-*
       open http://localhost:5601/app/kibana#/management/kibana/index
       open http://localhost:5601/app/kibana#/discover
       
       # once done to clean up
       docker-compose down 