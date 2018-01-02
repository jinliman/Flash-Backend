from elasticsearch import Elasticsearch

host = "127.0.0.1"
port = 9200
indexAlerts = "ews2017.1"
indexCve= "ewscve"
indexPackets = "packets"

es = Elasticsearch([{'host': host, 'port': 9200}])

settings = {
    "settings": {
        "number_of_shards": 5,
        "number_of_replicas": 1
    },
    "mappings": {
        "Alert": {
            "properties": {
                "createTime": {
                    "type": "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                },
                "recievedTime": {
                    "type": "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                },
                "sourceEntryIp": {
                    "type": "ip"
                },
                "targetEntryIp": {
                    "type": "ip"
                },
                "clientDomain": {
                    "type": "boolean"
                },
                "externalIP": {
                    "type": "ip"
                },
                 "internalIP": {
                    "type": "ip"
                }
            }
        }
    }
}

# create index
res = es.indices.create(index=indexAlerts, ignore=400, body=settings)
print("Result: " + res)

print("Index for Alerts successful?:" + str(res['acknowledged']))




settings2 = {
    "settings": {
        "number_of_shards": 5,
        "number_of_replicas": 1
    },
    "mappings": {
        "CVE": {
            "properties":  {
                    "createTime": {
                        "type": "date",
                        "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                    },
                    "recievedTime": {
                        "type": "date",
                        "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                    },
                    "sourceEntryIp": {
                        "type": "ip"
                    },
                    "targetEntryIp": {
                        "type": "ip"
                    },
                    "clientDomain": {
                        "type": "boolean"
                    },
                    "externalIP": {
                        "type": "ip"
                    },
                     "internalIP": {
                        "type": "ip"
                    }
            }
        }
    }
}

# create index for cve
res = es.indices.create(index=indexCve, ignore=400, body=settings2)
print("Result: " + res)

print("Index for CVEs successful?:" + str(res['acknowledged']))


settingsPackets = {
    "settings": {
        "number_of_shards": 5,
        "number_of_replicas": 1
    },
    "mappings": {
        "Packet": {
            "properties":  {
                    "createTime": {
                        "type": "date",
                        "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
                    },
                     "initialIP": {
                        "type": "ip"
                    }
            }
        }
    }
}

# create index for cve
res = es.indices.create(index=indexPackets, ignore=400, body=settingsPackets)
print("Result: " + res)

print("Index for Packets successful?:" + str(res['acknowledged']))

