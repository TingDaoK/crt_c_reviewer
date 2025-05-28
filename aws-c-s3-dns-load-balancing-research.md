# AWS-C-S3 DNS Load Balancing Research

## Overview
This document contains research findings on how the AWS-C-S3 library implements DNS load balancing for Amazon S3 connections.

## Key Features Summary
AWS-C-S3 implements sophisticated DNS load balancing with the following mechanisms:

### 1. Continuous DNS Resolution
- DNS resolver continuously harvests Amazon S3 IP addresses in the background
- Resolves every second while the record is actively being used
- Ensures fresh IP addresses are constantly discovered from the S3 fleet

### 2. Smart TTL Management
- Resolves every second in the background (only while actively using the record)
- Does not expire earlier resolved addresses until max TTL has passed
- Prevents choice between large TTLs (sticky hosts) vs short TTLs (higher latencies)

### 3. Address Pool Management
- Maintains cache of multiple IP addresses for each hostname
- Uses Least Recently Used (LRU) rotation to cycle through available addresses
- Tracks use_count and connection_failure_count for each address
- Enables hitting thousands of hosts in the Amazon S3 fleet instead of just one or two

### 4. Connection Failure Handling
- Moves failed connections to separate list to keep them out of hot path
- Eventually retries failed addresses when endpoint is likely healthy again
- Addresses are not permanently blacklisted - can return to service after TTL expiration

### 5. Background Threading
- Uses threaded implementation to avoid blocking DNS operations
- Each host entry has potentially short-lived background thread based on TTL
- Minimum wait between DNS queries is 100ms to prevent excessive querying

## Specific Code Files and Locations

### Primary Documentation
- **File**: `s3://aws-c-kb/aws-c-kb/aws-c-s3/README.md`
- **Key Quote**: "DNS Load Balancing: DNS resolver continuously harvests Amazon S3 IP addresses. When load is spread across the S3 fleet, overall throughput more reliable than if all connections are going to a single IP."

### Core Implementation Files

#### 1. S3 Client Implementation
- **File**: `s3://aws-c-kb/aws-c-kb/aws-c-s3/source/s3_client.c`
- **Contains**:
  - DNS TTL configuration: `static size_t s_dns_host_address_ttl_seconds = 5 * 60;`
  - Function: `void aws_s3_set_dns_ttl(size_t ttl)`
  - Connection management logic

#### 2. Host Resolver Header
- **File**: `s3://aws-c-kb/aws-c-kb/aws-c-io/include/aws/io/host_resolver.h`
- **Contains**:
  - Core DNS load balancing architecture design
  - `struct aws_host_address` with load balancing fields:
    - `size_t use_count` - for DNS-based load balancing
    - `size_t connection_failure_count` - for failure mitigation
  - Key architectural comment explaining the design philosophy

#### 3. Host Resolver Implementation
- **File**: `s3://aws-c-kb/aws-c-kb/aws-c-io/source/host_resolver.c`
- **Contains**:
  - Background threading logic: `static void aws_host_resolver_thread(void *arg)`
  - TTL management and resolution timing
  - Minimum wait constant: `const uint64_t AWS_MINIMUM_WAIT_BETWEEN_DNS_QUERIES_NS = 100000000; /* 100 ms */`

#### 4. Platform-Specific DNS Resolution
- **File**: `s3://aws-c-kb/aws-c-kb/aws-c-io/source/posix/host_resolver.c`
- **Contains**:
  - `int aws_default_dns_resolve()` function
  - Platform-specific DNS resolution implementation using getaddrinfo()

#### 5. S3 Client Configuration
- **File**: `s3://aws-c-kb/aws-c-kb/aws-c-s3/include/aws/s3/s3_client.h`
- **Contains**:
  - Client configuration options that affect DNS behavior
  - Connection management settings

#### 6. Test Files (Implementation Examples)
- **File**: `s3://aws-c-kb/aws-c-kb/aws-c-io/tests/default_host_resolver_test.c`
- **Contains**:
  - Test cases demonstrating TTL refresh behavior
  - LRU address rotation testing
  - Connection failure and recovery testing

- **File**: `s3://aws-c-kb/aws-c-kb/aws-c-io/tests/channel_test.c`
- **Contains**:
  - Example S3 DNS resolution usage
  - Test showing multiple address resolution for S3 hosts

## Key Architectural Design Quote

From `aws-c-io/include/aws/io/host_resolver.h`:

> "Finally, this entire design attempts to prevent problems where developers have to choose between large TTLs and thus sticky hosts or short TTLs and good fleet utilization but now higher latencies. In this design, we resolve every second in the background (only while you're actually using the record), but we do not expire the earlier resolved addresses until max ttl has passed.
> 
> This for example, should enable you to hit thousands of hosts in the Amazon S3 fleet instead of just one or two."

## Configuration Constants

- **Default DNS TTL**: 5 minutes (300 seconds)
- **Background resolution frequency**: Every 1 second (while active)
- **Minimum DNS query interval**: 100ms
- **Default part size**: 8 MiB (related to connection optimization)
- **Default throughput target**: 10.0 Gbps
- **Minimum connections**: 10

## Benefits

1. **Improved Throughput**: Load distribution across S3 fleet improves reliability
2. **Connection Resilience**: Failed connections don't permanently impact performance  
3. **Fleet Utilization**: Ability to hit thousands of S3 hosts instead of just one or two
4. **Balanced Performance**: Avoids trade-off between TTL length and performance
5. **Automatic Recovery**: Failed endpoints can return to service after TTL expiration

## Research Methodology

This research was conducted by querying the AWS-C knowledge base (ID: 8BRIG4RFWU) with specific queries about DNS load balancing implementation in the aws-c-s3 library. The information was gathered from official source code, documentation, and test files within the aws-c-* libraries.