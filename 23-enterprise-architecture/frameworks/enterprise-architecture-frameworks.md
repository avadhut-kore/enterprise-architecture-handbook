# Pragmatic Analysis of Enterprise Architecture Frameworks

Evaluating frameworks based on practical decision-making utility rather than certification theory.

---

## 1. TOGAF (The Open Group Architecture Framework) 10
* **What It Is**: A comprehensive methodology and Architecture Development Method (ADM) cycle for enterprise planning.
* **Purpose**: Provide a structured, repeatable taxonomy and step-by-step process (Phases A through H) to design target architectures.
* **Strengths**: Common global vocabulary; thorough coverage of artifact deliverables; strong industry recognition.
* **Weaknesses**: Frequently degenerates into bureaucratic diagram generation; overly prescriptive; slow moving in fast agile environments.
* **When Useful**: Large government agencies, traditional banking conglomerates, or organizations establishing their first formal EA function from scratch.
* **When Unnecessary**: High-growth SaaS startups, product-led tech organizations, or teams requiring weekly architectural pivot cycles.
* **How to Use Practically**: Strip away 70% of the formal documentation templates; adopt the core conceptual thinking: `Baseline State -> Target State -> Gap Analysis -> Transition Roadmap`.

---

## 2. The Zachman Framework
* **What It Is**: A 6x6 two-dimensional classification ontology (What, How, Where, Who, When, Why vs Planner, Owner, Designer, Builder, Integrator, Worker).
* **Purpose**: Ensure that every conceivable perspective and interrogative of an enterprise system is cataloged.
* **Strengths**: Exhaustive taxonomy; excellent completeness checklist; technology-agnostic.
* **Weaknesses**: Not a methodology (tells you *what to categorize*, not *how to execute*); paralyzing if attempted to fill completely.
* **When Useful**: As an audit checklist to ensure no major stakeholder view (e.g., security, data ownership) was missed during an enterprise design review.
* **When Unnecessary**: As a daily operational delivery framework.
* **How to Use Practically**: Use as an architectural sanity checklist before major C-suite presentations.

---

## 3. Federal Enterprise Architecture Framework (FEAF)
* **What It Is**: US Government reference model suite (BRM, PRM, ARM, DRM, TRM, SRM) designed for federal agencies.
* **Purpose**: Coordinate cross-agency IT spending, eliminate duplicate citizen services, and enforce federal compliance.
* **Strengths**: Exceptional at tracking inter-agency capability sharing and public-sector transparency.
* **Weaknesses**: Highly bureaucratic; rigid federal reporting cadences.
* **When Useful**: Government, public sector, and defense contractor enterprise architectures.
* **When Unnecessary**: Private commercial enterprise environments.

---

## 4. Gartner-Style Pragmatic Enterprise Architecture
* **What It Is**: Business-outcome-driven EA focused on continuous trend analysis, Business Model Canvases, and the TIME portfolio model.
* **Purpose**: Directly connect IT spend to revenue growth, digital disruption, and cost optimization.
* **Strengths**: High C-suite resonance; minimal academic overhead; focuses on practical decisions (Invest vs Retire).
* **Weaknesses**: Less standardized notation than TOGAF/ArchiMate; can become overly marketing-centric.
* **When Useful**: Corporate environments where the CIO needs to justify architectural investments to the CEO and CFO.
* **How to Use Practically**: Adopt the TIME matrix for application rationalization and the 3-Horizon roadmap for executive strategy.

---

## 5. Domain-Driven & Product-Centric Architecture
* **What It Is**: Modern engineering-led architecture applying Domain-Driven Design (DDD) bounded contexts and Team Topologies to enterprise systems.
* **Purpose**: Align software architecture with autonomous business teams and customer value streams.
* **Strengths**: High developer buy-in; eliminates ivory tower disconnect; optimizes for continuous delivery.
* **Weaknesses**: Can miss enterprise-wide shared platform synergies if not coordinated by a central guild.
* **How to Use Practically**: The recommended standard for digital and software-centric enterprises.
