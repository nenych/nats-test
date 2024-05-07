# Test NATS
### Steps to run
1. Build the docker image:
```
docker build -t test/nats:latest .
```
2. Install NATS cli: https://docs.nats.io/using-nats/nats-tools/nats_cli
3. Run docker-compose (will start NATS, prometheus and 2 consumers):
```
docker-compose -f ./docker-compose.yaml up -d
```
4. Start NATS benchmark:
```
nats bench updates --pub=4 --msgs 1000000000 --size=1000
```
5. Wait a little and start the slow consumer:
```
docker run --rm -it --network=nats-test_default test/nats:latest python3 slow-consumer.py
```

### Explore metrics
1. Open prometheus: http://localhost:9091/graph
2. Insert query:
```
sum by (job) (rate(nats_varz_in_msgs[30s]))
```
