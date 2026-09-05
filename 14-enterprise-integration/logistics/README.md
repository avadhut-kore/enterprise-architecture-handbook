# Supply Chain & Logistics Integration Architecture

## 1. Overview
Supply chain integration connects Transportation Management Systems (TMS - SAP TM, Blue Yonder, Manhattan Associates), Warehouse Management Systems (WMS), third-party logistics (3PL) carriers, freight brokers, and IoT container tracking sensors.

## 2. Standard Logistics EDI Protocols (ANSI X12)
- **EDI 204**: Motor Carrier Load Tender (Shipper requests carrier to pick up shipment).
- **EDI 990**: Response to a Load Tender (Carrier accepts or declines).
- **EDI 211**: Motor Carrier Bill of Lading.
- **EDI 214**: Transportation Carrier Shipment Status Message (Real-time tracking updates).
- **EDI 210**: Motor Carrier Freight Details and Invoice.

## 3. Real-Time Telematics & IoT Event Processing
High-frequency GPS and temperature sensors on refrigerated pharmaceutical containers stream telematics into an IoT event bridge. Temperature breaches exceeding allowed thresholds trigger automated FDA compliance breach events and carrier alerts.
