---
title: The Big Challenge of Big Data and Hadoop Integration
date: 2013-03-17
categories:
  - hadoop
  - big-data
  - integration
  - enterprise
description: Cloud Computing Journal on the integration challenges of adding Hadoop to existing enterprise data infrastructure — connecting it to RDBMS systems, BI tools, and existing ETL pipelines. The 2013 reality check on big data adoption.
params:
  source: pinboard
  sourceUrl: http://cloudcomputing.sys-con.com/node/2581404
---

![The Big Challenge of Big Data and Hadoop Integration](/images/notes/big-challenge-hadoop-integration.png)

## Summary

While much of the 2013 big data discourse focused on what Hadoop could do, this Cloud Computing Journal piece addressed a harder problem: how do you integrate Hadoop into an existing enterprise data environment? Most enterprises adopting Hadoop weren't replacing their RDBMS systems — they were adding Hadoop alongside Oracle, SQL Server, and existing data warehouse infrastructure.

The integration challenges were real. Sqoop could shuttle data between relational systems and HDFS, but performance and data type mapping were tricky. Existing ETL pipelines built for batch warehouse loads didn't map cleanly onto MapReduce programming. Business intelligence tools like Tableau, MicroStrategy, and Business Objects couldn't query Hadoop directly — they needed Hive or connectors like Cloudera Impala to provide a SQL interface. And security: Hadoop in 2013 had weak authentication and authorization compared to enterprise RDBMS systems, creating compliance headaches.

The integration challenge explains why commercial Hadoop distributions gained traction: Cloudera, Hortonworks, and MapR each invested heavily in connectors, management tools, and certification with BI vendor partners. The raw Apache open-source stack worked, but enterprise integration required significant additional engineering.

## Key points

- Sqoop handled RDBMS-to-Hadoop bulk transfers but wasn't a seamless integration — data type mapping, incremental updates, and CDC were all complex
- Hive provided a SQL abstraction but had high query latency — Cloudera Impala and Apache Tez emerged to close the interactive query gap
- BI tools needed JDBC/ODBC connectors to reach Hadoop data — Hortonworks and Cloudera both invested in certified integrations
- Hadoop security in 2013 relied on Kerberos for authentication and was significantly harder to operate than RDBMS security
- The integration complexity was a key driver of managed cloud services: Amazon EMR abstracted most of this away

[Original](http://cloudcomputing.sys-con.com/node/2581404)
