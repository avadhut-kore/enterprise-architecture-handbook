# Cloud Capacity Calculators Guide

## Executive Summary

This guide provides practical mathematical templates for calculating compute, database, and bandwidth capacity.

---

## 1. Database Storage Growth Formula
$$\text{Annual Storage (GB)} = \frac{\text{Daily Transactions} \times \text{Row Size (KB)} \times \text{Indexing Overhead (1.3)} \times 365}{1,048,576} + \text{WAL Logs}$$

## 2. Network Bandwidth Formula
$$\text{Bandwidth (Gbps)} = \frac{\text{Peak Requests per Sec} \times \text{Average Response Payload Size (KB)} \times 8}{1,000,000}$$
- Example: $20,000 \text{ req/sec} \times 50\text{ KB} \times 8 / 1,000,000 = 8.0 \text{ Gbps}$ egress bandwidth required.
