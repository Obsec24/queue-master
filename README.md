## Queue

# Install

We have used docker RabbitMQ from from Docker Hub:

```
docker pull rabbitmq
```

# Running

```
docker run -d --network host --hostname privapp-rabbit --name 1.0 -e RABBITMQ_DEFAULT_USER=privapp -e RABBITMQ_DEFAULT_PASS=******** rabbitmq:3-management
```
# Producing 'messages'
```
python send.py  <server> <queue> <message>
```
# Consuming 'messages'
```
python receive.py <server> <queue> <message>
```
