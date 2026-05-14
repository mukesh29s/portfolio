# AWS Database Migration — Near-Zero Downtime

<div class="badge-row">
  <span class="badge">AWS DMS</span>
  <span class="badge">PostgreSQL</span>
  <span class="badge">MySQL</span>
  <span class="badge">AWS RDS</span>
  <span class="badge">Terraform</span>
  <span class="badge badge-green">Production</span>
</div>

---

## The Problem

Sopra Financial Technology was running its entire database fleet on-premises in a traditional data centre. The infrastructure was ageing, expensive to maintain, and didn't have the elasticity the business needed to grow. The decision was made to migrate everything to AWS — but with **100+ live databases**, the risk of downtime during migration was a serious concern.

A failed migration or extended outage during a cutover window would have directly impacted financial services customers. The stakes were high, and there was very little margin for error.

---

## The Approach

Rather than using a traditional "lift and shift" approach (which typically involves planned downtime), I used **AWS Database Migration Service (AWS DMS)** to achieve near-zero downtime migration. Here's how it worked at a high level:

```
On-Premises Source DB
        │
        ▼
[AWS DMS Replication Instance]
        │
   Full Load ──────────────────► AWS RDS (Target)
        │
   CDC (Change Data Capture) ──► Keeps target in sync with source
        │
   Cutover when lag = 0 ────────► Application switched to RDS
```

The key insight is that DMS keeps the source and target **in continuous sync** using Change Data Capture. This means you can run both environments in parallel, verify the target is healthy, and then cut over with minimal disruption — often in a matter of minutes.

---

## What I Built

- **Replication infrastructure** — provisioned DMS replication instances, source/target endpoints, and replication tasks using Terraform
- **Full load + CDC pipeline** — configured DMS tasks to first perform a full initial load, then switch to ongoing replication via CDC
- **Validation framework** — built Python scripts to compare row counts, checksums, and sample data between source and target databases throughout the migration
- **Cutover runbooks** — documented step-by-step procedures for each database cutover, including rollback steps if anything went wrong
- **Target environments** — provisioned RDS instances (PostgreSQL and MySQL) with appropriate parameter groups, security groups, and storage configurations via Terraform

---

## Outcome

!!! success "Results"
    - ✅ **100+ databases** migrated successfully across multiple migration waves
    - ✅ **Near-zero downtime** — most cutovers completed in under 10 minutes
    - ✅ No data loss incidents across the entire programme
    - ✅ Significant reduction in infrastructure costs post-migration
    - ✅ Teams gained access to native AWS features (automated backups, Multi-AZ, read replicas) that weren't available on-premises

---

## Key Learnings

- DMS is powerful, but it has quirks — particularly around **LOB (Large Object) handling** and certain Oracle-specific data types. Thorough pre-migration assessment is essential.
- **CDC lag monitoring** is critical during the replication phase. We built custom CloudWatch alarms to alert if replication fell behind.
- Having a well-practiced rollback procedure gave the team confidence to proceed. We never had to use it, but knowing it existed made the cutovers much calmer.
