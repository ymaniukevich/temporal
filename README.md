- MTLS configuration
```bash
tls:
  internode:
    server:
      certFile: /etc/temporal/certs/server.crt
      keyFile: /etc/temporal/certs/server.key
      requireClientAuth: true
      clientCaFiles:
        - /etc/temporal/certs/ca.crt
    client:
      serverName: staging.goconsensus.com
      rootCaFiles:
        - /etc/temporal/certs/ca.crt
  frontend:
    server:
      certFile: /etc/temporal/certs/server.crt
      keyFile: /etc/temporal/certs/server.key
      requireClientAuth: true
      clientCaFiles:
        - /etc/temporal/certs/ca.crt
    client:
      serverName: staging.goconsensus.com
      rootCaFiles:
        - /etc/temporal/certs/ca.crt

```
