# MySQL Zero ETL → Amazon Redshift

<div class="badge-row">
  <span class="badge">AWS Zero ETL</span>
  <span class="badge">MySQL / Aurora MySQL</span>
  <span class="badge">Amazon Redshift</span>
  <span class="badge">AWS Glue</span>
  <span class="badge badge-green">Production</span>
  <span class="badge badge-blue">Analytics</span>
</div>

---

## The Problem

The data analytics team at Sopra Financial Technology was working with production MySQL data — but getting that data into their Redshift analytics environment was painful. The existing process involved scheduled ETL jobs that extracted data from MySQL, transformed it, and loaded it into Redshift on a delay.

The problems were clear:

- **Latency** — analysts were always working with data that was hours old
- **Complexity** — the ETL pipeline had multiple moving parts that could (and did) break
- **Maintenance burden** — someone had to own and support the pipeline, which consumed engineering time that could be better spent elsewhere

The analytics team wanted **real-time data**. The engineering team wanted **less pipeline complexity**. Both were reasonable asks.

---

## The Solution — AWS Zero ETL

AWS Zero ETL integration is a relatively new feature that creates a **direct, managed replication channel** between Aurora MySQL and Amazon Redshift — with no ETL code to write, no pipelines to manage, and no meaningful lag.

```
Aurora MySQL (Source)
        │
        │  AWS Zero ETL Integration
        │  (managed by AWS, near real-time)
        ▼
Amazon Redshift (Target)
        │
        ▼
Analytics Team Queries ✅
```

Data changes in MySQL are automatically propagated to Redshift, typically within seconds. The analytics team queries Redshift as they normally would — they just get current data instead of yesterday's.

---

## What I Set Up

- **Assessed compatibility** — Zero ETL has requirements around Aurora MySQL versions, Redshift cluster types, and table structures. I ran a pre-flight check across all candidate tables before committing to the approach.
- **Configured the integration** — set up the Zero ETL integration between the Aurora MySQL cluster and the Redshift Serverless endpoint via the AWS Console and CLI, with IAM roles and resource policies correctly scoped
- **Schema management** — Redshift automatically creates a database from the integration, but I worked with the analytics team to ensure their existing queries and BI tools pointed to the right schemas
- **Validated data consistency** — built a simple Python comparison script to periodically check row counts and spot-check field values between source and destination
- **Documented the setup** — wrote a runbook covering how the integration works, how to monitor it, and what to do if replication falls behind or stops

---

## Outcome

!!! success "Results"
    - ✅ **Real-time data** available in Redshift — analysts now query data that is seconds old, not hours
    - ✅ **Entire ETL pipeline decommissioned** — reduced infrastructure complexity and eliminated a maintenance burden
    - ✅ **Measurable performance improvement** for analytics queries — Redshift's columnar storage and MPP architecture processes analytical queries significantly faster than MySQL
    - ✅ Analytics team able to build dashboards and reports on current data for the first time

---

## Key Learnings

- Zero ETL is genuinely impressive when it works, but the **prerequisites matter**. Tables need proper primary keys, and certain data types aren't supported. Checking this upfront saves a lot of pain later.
- The **operational simplicity** is the real win here. There's no pipeline to monitor, no failure modes to handle, no transformation code to maintain. AWS manages the replication — you just use the data.
- This isn't a replacement for all ETL workloads — if you need complex transformations or data from multiple sources, you still need a proper pipeline. But for straightforward MySQL → Redshift replication, Zero ETL is the right tool.
