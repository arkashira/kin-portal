# Dataflow Architecture
## Overview
The kin-portal system dataflow architecture is designed to simplify access and management for non-technical family members. The architecture consists of six tiers: External data sources, Ingestion layer, Processing/transform layer, Storage tier, Query/serving layer, and Egress to user.

## External Data Sources
```
                                  +---------------+
                                  |  External    |
                                  |  Services    |
                                  +---------------+
```
* External services such as JSONLint and GeeksforGeeks
* Market data and research queries from various sources

## Ingestion Layer
```
                                  +---------------+
                                  |  Ingestion    |
                                  |  Layer       |
                                  +---------------+
                                   |
                                   |
                                   v
```
* Components:
	+ API Gateway (auth boundary)
	+ Data Ingestion Service
	+ JSON Parsing Service
* Responsibilities:
	+ Handle incoming requests from external services
	+ Parse JSON data and handle errors
	+ Forward parsed data to processing layer

## Processing/Transform Layer
```
                                  +---------------+
                                  |  Processing  |
                                  |  Layer       |
                                  +---------------+
                                   |
                                   |
                                   v
```
* Components:
	+ Data Processing Service
	+ Data Transformation Service
	+ Error Handling Service
* Responsibilities:
	+ Process and transform parsed JSON data
	+ Handle errors and exceptions
	+ Forward transformed data to storage tier

## Storage Tier
```
                                  +---------------+
                                  |  Storage     |
                                  |  Tier        |
                                  +---------------+
                                   |
                                   |
                                   v
```
* Components:
	+ Database (auth boundary)
	+ Data Warehouse
* Responsibilities:
	+ Store transformed data
	+ Provide data for query/serving layer

## Query/Serving Layer
```
                                  +---------------+
                                  |  Query/Serving|
                                  |  Layer       |
                                  +---------------+
                                   |
                                   |
                                   v
```
* Components:
	+ Query Service
	+ Serving Service
	+ API Gateway (auth boundary)
* Responsibilities:
	+ Handle queries from users
	+ Serve data to users
	+ Provide API for external services

## Egress to User
```
                                  +---------------+
                                  |  Egress to  |
                                  |  User        |
                                  +---------------+
```
* Components:
	+ User Interface
	+ API Documentation
* Responsibilities:
	+ Provide user interface for users to interact with system
	+ Provide API documentation for external services

Auth boundaries are marked with (auth boundary) and indicate where authentication and authorization checks are performed. The system dataflow architecture is designed to be scalable, secure, and easy to maintain.