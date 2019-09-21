# Tech stack demand
An example microservice pipeline to visualize the tech stack demand on the current job market.

#### Show who is using certain technologies:
![Tech stack demand tech demo](demo_pictures/search_by_tech.gif)


#### Search for company:
![Tech stack demand company demo](demo_pictures/search_by_company.gif)


## Installation
* Run `docker-compose up`
* Open in your browser `http://localhost:5000/`
* Collect new data (reload page to see progress; this can take up to 20 min)
![Tech stack demand collect demo](demo_pictures/collect_new_data.gif)


## How to use the UI
Check out this [basic action wiki](https://github.com/Nhogs/popoto/wiki/Basic-action).


## Technical sidenotes
### Architecture 
![Tech stack demand architecture](demo_pictures/architecture.png)


#### Browse kafka topics:
Kafka logs are not mounted. While updating, check `http://localhost:9000/`


#### Manage Neo4j data:
* Data mounted to /neo4j_data_loader/neo4j_data
* Open Neo4j browser: `http://localhost:7474/`


#### Run tests:
`docker-compose -f docker-compose-tests.yml up`


#### Run keywords api update:
* Delete old data saved in `keywords_api/redis_data`
* Run: `docker-compose -f docker-compose-keywords-update.yml up`
