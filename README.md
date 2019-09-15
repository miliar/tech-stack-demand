# Tech stack demand
A tool to visualize the tech stack demand on the current job market.
![Tech stack demand demo](demo_pictures/collect_new_data.gif)


## How to use the UI
Check out this [basic action wiki](https://github.com/Nhogs/popoto/wiki/Basic-action).

## Technical sidenotes
Run tests:
`docker-compose -f docker-compose-tests.yml up`

Run keywords api update:
* delete old data saved in `keywords_api/redis_data`
* Run: `docker-compose -f docker-compose-keywords-update.yml up`
