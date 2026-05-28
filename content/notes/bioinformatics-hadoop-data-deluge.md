---
title: "BioInformatics: A Data Deluge with Hadoop to the Rescue"
date: 2013-03-21
categories:
  - bioinformatics
  - hadoop
  - genomics
  - big-data
  - sequencing
description: Datanami on using Apache Hadoop for bioinformatics data pipelines — how genomic sequencing data had outpaced traditional computational biology infrastructure and why Hadoop's distributed file system and MapReduce were being adopted to handle the deluge.
params:
  source: pinboard
  sourceUrl: http://www.datanami.com/datanami/2012-11-19/bioinformatics:_a_data_deluge_with_hadoop_to_the_rescue.html
---

## Summary

The genomics field was facing a data scale problem that arrived faster than its computational infrastructure could handle. The cost of DNA sequencing had been dropping faster than Moore's Law since the introduction of next-generation sequencing (Illumina's HiSeq was standard by 2012): genome sequencing cost fell from ~$100M per genome in 2001 to ~$1,000 by 2013. But the data volume per sequencing run was also exploding — a single HiSeq run produced 600 gigabytes of raw sequence data. Multiply by the throughput of a major genomics center and you had petabytes of sequence data to store, align, variant-call, and analyze.

Traditional bioinformatics infrastructure — Unix clusters with shared filesystems, tools like BWA and GATK for alignment and variant calling, R/Bioconductor for statistical analysis — was being overwhelmed. The compute model (jobs submitting to SGE or PBS schedulers on HPC clusters) was sound but lacked the storage scalability that HDFS provided: HDFS's rack-aware replication and ability to scale to petabytes across commodity hardware was directly applicable to the genomics data volume problem.

Adam (Avocado + ADAM) was the emerging approach: porting GATK variant calling and sequence alignment to run on Apache Spark and HDFS, enabling genome processing at scales that SGE clusters couldn't handle. The Broad Institute (GATK's home) and groups at UC Berkeley (including the AMPLab) were leading this work. The Datanami piece captured the moment when bioinformatics was recognizing that its data had become a big data problem requiring the same infrastructure solutions as web companies.

## Key points

- Sequencing cost curve: DNA sequencing costs dropping faster than Moore's Law — from $100M (2001) to ~$1,000 (2013) per genome — creating a data flood.
- HDFS for genomics: Hadoop's distributed filesystem handles petabyte-scale sequence data across commodity hardware — directly applicable to sequencing center infrastructure.
- MapReduce for bioinformatics: sequence alignment and variant calling parallelized as MapReduce jobs — enables population-scale genomics.
- ADAM: Apache Spark-based genome analysis toolkit developed at UC Berkeley AMPLab — next-generation alternative to GATK's HPC model.
- The broader pattern: life sciences as an early adopter of "big data" infrastructure because its data volume growth outpaced what traditional HPC could handle.

[Original](http://www.datanami.com/datanami/2012-11-19/bioinformatics:_a_data_deluge_with_hadoop_to_the_rescue.html)
