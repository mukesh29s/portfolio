# Prometheus & Grafana Monitoring Stack

<div class="badge-row">
  <span class="badge">Prometheus</span>
  <span class="badge">Grafana</span>
  <span class="badge">AWS CloudWatch</span>
  <span class="badge">RDS</span>
  <span class="badge">EC2</span>
  <span class="badge">Terraform</span>
  <span class="badge badge-green">Production</span>
</div>

---

## The Problem

After migrating 100+ databases to AWS, the team had a new challenge — **visibility**. The old on-premises environment had monitoring tools that everyone knew (even if they weren't great). AWS CloudWatch provided metrics, but it wasn't giving the team the kind of intuitive, at-a-glance dashboards they needed to operate confidently.

The questions being asked were: *Is my database healthy? Is query performance degrading? Are we about to run out of storage? How does today compare to last week?* These are simple questions, but they were surprisingly hard to answer quickly.

---

## The Approach

I built a unified observability stack using **Prometheus** for metrics collection and **Grafana** for visualisation. The goal was a single pane of glass — one place where any engineer could immediately understand the health of both the AWS infrastructure and the databases running on it.

```
AWS Infrastructure & Databases
          │
          ├── CloudWatch Metrics Exporter ──────┐
          ├── RDS Enhanced Monitoring           │
          ├── Node Exporter (EC2 instances)     ▼
          └── MySQL / PostgreSQL Exporters ──► Prometheus
                                                │
                                                ▼
                                             Grafana
                                          (Dashboards +
                                           Alerting)
```

---

## What I Built

### Metrics Collection
- Deployed **Prometheus** on a dedicated EC2 instance, configured with appropriate retention and scrape intervals
- Integrated **CloudWatch Exporter** to pull AWS-native metrics (RDS CPU, storage, connections, replication lag) into Prometheus
- Set up **mysqld_exporter** and **postgres_exporter** for deep database-level metrics — query throughput, slow queries, lock waits, buffer pool usage
- Deployed **Node Exporter** on EC2 hosts for OS-level metrics (CPU, memory, disk I/O, network)

### Dashboards
Built purpose-built Grafana dashboards for different audiences:

| Dashboard | Audience | Key Metrics |
|---|---|---|
| Infrastructure Overview | Engineering & Ops | EC2 health, network, storage |
| RDS Database Health | DBAs | Connections, CPU, storage, IOPS |
| MySQL Performance | DBAs | QPS, slow queries, buffer pool hit ratio |
| PostgreSQL Performance | DBAs | Query throughput, vacuum status, bloat |
| Executive Summary | Management | Uptime, incident count, capacity trends |

### Alerting
- Configured **Alertmanager** with routing rules for different severity levels
- Critical alerts (database down, replication stopped) → immediate PagerDuty notification
- Warning alerts (storage > 80%, CPU sustained high) → Slack channel notification
- All alerts included runbook links so on-call engineers knew exactly what to do

---

## Outcome

!!! success "Results"
    - ✅ **Full observability** across 100+ databases and the supporting AWS infrastructure
    - ✅ Mean time to detect (MTTD) issues reduced significantly — problems surfaced in dashboards before users reported them
    - ✅ Capacity planning became data-driven — storage and compute sizing decisions backed by real trend data
    - ✅ On-call engineers had clear runbooks tied to every alert, reducing stress and speeding up resolution

---

## Key Learnings

- **Start with the questions, not the metrics.** The most useful dashboards were the ones built around specific operational questions, not just "show everything available."
- CloudWatch and Prometheus serve different purposes — CloudWatch is great for AWS-native metrics, Prometheus is better for application and database-level detail. Using both together gives you the full picture.
- Alert fatigue is real. We started with too many alerts and gradually tuned them down to only the ones that genuinely required human action.
