# 🌐 Smart Static Website

A globally distributed, secure, and cost-effective static website built using AWS. This project demonstrates how to host and deliver static content with low latency, HTTPS encryption, and DDoS protection — without the complexity of managing backend servers.

---

## 📦 Services Used

| Service               | Purpose                                               |
|-----------------------|--------------------------------------------------------|
| **Amazon S3**         | Static website storage (HTML, CSS, JS)                |
| **Amazon CloudFront** | Global CDN for fast and cached content delivery       |
| **ACM (SSL/TLS)**     | HTTPS certificate provisioning and management         |
| **AWS WAF**           | Web Application Firewall to protect against threats   |
| **Amazon CloudWatch** | Logging and monitoring of performance and security    |

---

## 🧠 Business Problem

Traditional static websites often suffer from:

- Slow loading for users outside the host region
- Lack of HTTPS or proper security
- Manual and costly scaling when traffic increases

### ✅ Our Solution

By using **S3 + CloudFront + ACM + WAF + CloudWatch**, we provide:

- **Lightning-fast global delivery**
- **SSL out-of-the-box**
- **Layer-7 protection via WAF**
- **Scalable, serverless hosting**
- **Cost-effective & highly available**

---

## 📊 Architecture Diagram

> Upload your architecture diagram (e.g. `architecture.png`) and link it here:

![AWS Architecture](architecture.png)

---

## 🛠️ Project Setup Guide

### 1. 🎯 Create an S3 Bucket

- Enable **Static Website Hosting**
- Set `index.html` as default document
- Disable "Block All Public Access"
- Upload your website files (`website/` folder)

---

### 2. 🔐 Add Public Read Bucket Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "PublicReadGetObject",
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::smart-static-site/*"
  }]
}

---

### 3. 🌍 Configure CloudFront

* Origin: Your S3 **website endpoint**
* Set default root object: `index.html`
* Enable GZIP/Brotli compression
* (Optional) Enable logging to a second S3 bucket

---

### 4. 🛡️ Set Up HTTPS with ACM

* Use **AWS Certificate Manager** to request an SSL certificate
* Add it to your CloudFront distribution
* Set viewer policy to **Redirect HTTP to HTTPS**

---

### 5. 🔧 Add WAF (Optional but Recommended)

* Go to **AWS WAF**, create a Web ACL
* Attach to CloudFront
* Add rules like:

  * Rate limiting
  * SQLi/XSS protections
  * Geo-blocking (if needed)

---

### 6. 📈 Enable Monitoring with CloudWatch

* Enable CloudFront metrics and logs
* Set alarms on:

  * 5xx errors
  * High request latency
  * Unusual traffic patterns

---

## 🔐 Security Best Practices

* HTTPS enforced via **CloudFront + ACM**
* Only `GET` access via S3 bucket policy
* WAF provides OWASP Top 10 protection
* CloudWatch allows early alerting of suspicious activity

---

## 💰 Why This Is Cost Effective

* **S3 + CloudFront** scales without any server management
* **No EC2** = No compute cost
* Pay only for storage, requests, and data transfer
* Ideal for personal sites, startups, marketing pages, and product landing pages

---

## 🧹 Cleanup Guide

To avoid AWS charges, delete:

* S3 buckets (static + logs)
* CloudFront distribution
* WAF ACLs
* ACM certificate
* CloudWatch log groups

---

## 📄 License & Credits

MIT License © 2025 Abdul Raheem
Part of the [`AWS-Projects`](https://github.com/yourusername/aws-projects)

