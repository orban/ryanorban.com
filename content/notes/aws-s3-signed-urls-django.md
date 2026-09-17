---
title: AWS S3 Signed URLs in Django
date: 2023-06-03
categories:
  - django
  - aws
  - s3
  - python
  - storage
description: A guide to generating AWS S3 presigned URLs in Django — allowing clients to upload or download files directly to S3 without routing through your application server. Standard pattern for handling file storage in Django applications at scale.
params:
  source: pinboard
  sourceUrl: https://theyashshahs.medium.com/aws-s3-signed-urls-in-django-d9e66853a42f
---

![AWS S3 Signed URLs in Django](/images/notes/aws-s3-signed-urls-django.png)

## Summary

This Medium article covers generating AWS S3 presigned URLs in Django — the standard pattern for giving clients temporary, direct access to S3 objects without routing file data through your application server. The pattern matters at scale: uploading a 100MB video through your Django server ties up a worker process for the entire upload duration; with presigned URLs, the client uploads directly to S3 and your server just generates a short-lived URL.

The Django implementation uses boto3 to generate the presigned URL — a few lines of Python that call `s3.generate_presigned_url()` or `s3.generate_presigned_post()` with the bucket, key, and expiration parameters. The client receives a URL (and for POST, a set of form fields) and uploads or downloads directly. Your server never touches the file bytes.

The pattern extends to download URLs too: instead of serving files through Django's file views (which require the file to pass through your server), you generate a presigned GET URL with a short expiration. The client receives a signed URL that expires after (say) 5 minutes and downloads directly from S3. This separates authorization (your server decides who gets a URL) from delivery (S3 handles the bytes).

## Key points

- Presigned URLs let clients upload/download directly to S3 — file bytes bypass your app server.
- Upload: server generates presigned POST URL + fields; client posts multipart form directly to S3.
- Download: server generates presigned GET URL with expiration; client fetches directly from S3.
- boto3: `generate_presigned_url()` / `generate_presigned_post()` — a few lines of Python.
- Authorization stays server-side (who gets a URL); delivery is S3-side (handling actual bytes).

[Original](https://theyashshahs.medium.com/aws-s3-signed-urls-in-django-d9e66853a42f)
