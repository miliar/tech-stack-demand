# jobsearch-keywords


read topic:
docker exec -it jobsearch-keywords_kafka_1 kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic <topic_name> --from-beginning

produce:
docker exec -it jobsearch-keywords_kafka_1 kafka-console-producer.sh --broker-list kafka:9092 --topic <topic_name> --property "parse.key=true" --property "key.separator=:"


https://github.com/Nhogs/popoto/wiki/Basic-action

run tests:
docker-compose -f docker-compose-tests.yml up

run keywords update:
docker-compose -f docker-compose-keywords-update.yml up