from kafka.admin import KafkaAdminClient, NewTopic

# Kafka admin setup
admin = KafkaAdminClient(
    bootstrap_servers='localhost:29092',
)
topics_list = admin.list_topics()
# Admin logic

if "new-updates" not in topics_list:
  topics = [NewTopic(name="new-updates", num_partitions=2, replication_factor=1)]
  admin.create_topics(new_topics=topics, validate_only=False)

else:
       print(topics_list)
