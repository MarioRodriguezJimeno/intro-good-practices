<!-- Slide number: 1 -->

5.1
# Automation Services
Key values and offerings

<!-- Slide number: 2 -->
# End-to-end automation framework
Cloud DevOps

![Robot con relleno sólido](Gráfico59.jpg)

![Single gear con relleno sólido](Gráfico1023.jpg)

![Rocket con relleno sólido](Gráfico61.jpg)
Continuous integration (CI)
Continuous delivery (CD)
Continuous testing (CT)
Every artefact/GIT event triggers a CI pipeline automatically.
Self-managed CI runners (custom, signed images).
Gates: SAST, SCA , Quality Gate, Checksum
CI Runners carry pre-installed tools (for example, cosign, helm, trivy, robot, jf CLI).
No artefacts are promoted without passing all CI stages.
GitOps deployment where a Git repository is the single source of truth.
Promotion: TAV E2E → Pilot → Production fully automated
Version-controlled and auditable Helm Charts and Kubernetes manifests.
Rollback executed in seconds via Git instructions; minimum manual steps require.
Ephemeral environments per pipeline run. No state drift.
Robot framework suites executed at every promotion gate (Solution Integration.
SMO integration enables real network-layer compatibility.
TMS tracks test plans, executions and promotion traceability.
Failed tests block promotion automatically; pipeline gate enforced.
Network Integration: MAIS + Magenta CI/CD perform E2E validation in DTAG’s lab environment.
Audit and traceability – Full provenance chain

<

<

Vendor pushes artefacts
CI: Build + Sign
CI: Attest
CT: Test Evidence
CD: Pre-deploy gate
CI: Provenance
1
2
3
4
5
6
SHA-256 checksum
Scoped token auth
Cosign sign (keyless OIDC)
Record logs
SBOM
Trivy report attached
Builder ID, Source URI, Digest
TMS report attestation attached to artefact
Cosign verify, SBOM check, CVE threshold, provenance match
2
© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

<!-- Slide number: 3 -->
# Three-phase integration model
DTAG and ORION

Phase
Lab Environment
CI/CD Platform
Test Execution
SI Role

Interface pre-integration
Component supplier labs
Supplier-owned
Supplier-owned
Supplier-owned - SI supports readiness coordination

SI-owned Laboratory
SI-cloud-devops Framework
Testing Framework (SI)
SI owns lab, CI/CD tooling, test cases, and E2E execution
Solution Integration  ★

DTAG labs - Bonn / Budapest
MAIS RAN Test Suite (DTAG)
DTAG owns platform and MAIS; SI feeds validated artefacts & metadata
Network integration
Magenta CI/CD (DTAG)

DTAG Owns

3
Network Integration: Magenta CI/CD + MAIS

Vendor Delivers

1
Artefact pushed to the Registry

SI Integrates

2
Solution Integration: CI/CD Platform + Testing Framework + Laboratory Environment
Guiding Principles

DORA metrics
Deploy frequency, lead time, CFR, MTTR tracked per release

Immutable artefacts
Co-sign is signed; no runtime mutations guaranteed cryptographically

Ephemeral environments
Per-pipeline isolated test environments torn down at completion

Everything as code
GIT is the single source of truth for pipelines, tests, IaC and policies

Shift-left security
SAST/SCA + Code Quality gate at CI time and Never post-deployment
3
© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

<!-- Slide number: 4 -->
# Automation services
NTT DATA’s framework and services
NTT DATA is aware of the challenges faced in the lifecycle management of network functions (xNF) that must be deployed in Telco Cloud environments. That is why from our Network Centres of Excellence we have worked on a framework to automate its management, and it has already been used in test and production environments, working with different operators and industry groups.

This framework covers all the tasks related to the lifecycle of CNFs and VNFs in Telco Cloud environments, considering laboratory, pre-production and productive environments.

The framework is aligned with the tools that DTAG is available to carry out the CI/CT processes, which will allow us to support the migration of xNF to the Telco Cloud while minimising the risks of change.

We have considered that these capabilities are transversal to the service since they are used in the different domains and we have organised them as shown in the figure. Each of them is deepened in this section.

Automation, Orchestration and CD/CT
Test environments
Governance model
Execution model
CD/CT framework tools
4
© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

### Notes:
Incluir esta diapositiva

<!-- Slide number: 5 -->
# Automation services
NTT DATA’s framework and services
Automation, Orchestration and CD/CT
Business drivers
Reduced total cost of ownership (TCO) of infrastructure investment for network functions
Swap of "legacy" technology
Main challenges
Having an automated process for NF testing to speed up the detection of anomalies or errors.
Automating a highly disaggregated, multi-supplier RAN
Managing continuous lifecycle updates without service disruption
Maintaining accountability across component suppliers
Increasing test and validation complexity
Immutable CI/CD evidence
Technologies
CI/CD: Adoption of platforms capable of managing environments, pipelines and endpoints. Systemic integrations for configuration distribution and development standardisation.
CT: Using the tools available to make the entire process of hosting, preparing, deploying, and testing network functions as independent as possible from manual input, completely scalable, inmutable and always available.

1
5
© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

<!-- Slide number: 6 -->
# Automation services
NTT DATA’s framework and services
Test environments

2

TAV – E2E
CNF packet verification
Day-0 to Day-2 automation
Interoperability, Functional, Performance and security testing
Regression tests
Ephemeral environment
Not necessarily similar to the production environment
Pilot Technology Phase
Production environment conditions
Connected to DTAG’s CORE
Focused on lab and field E2E measurements.
Pilot Tunning Phase – Production
Live network validation
Interact directly with end users
Acceptance evidence

![](Imagen2.jpg)

![](Imagen3.jpg)

![](Imagen5.jpg)

![](Imagen6.jpg)
6
© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

### Notes:
Incluir esta diapositiva

<!-- Slide number: 7 -->
# Automation services
NTT DATA’s framework and services
Execution model

3

![](Imagen30.jpg)
CONTINOUS
MONITORING
7
© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

### Notes:

<!-- Slide number: 8 -->
# Automation services
NTT DATA’s framework and services
Governance model

4

Test preparation

Preliminary tasks that make the pre-requisites and scope of the test (for example, infrastructure preparation, CNF artefacts procurement, definition of test objectives, among others).
Alignment of tests with the defined objectives and the availability of necessary tools.
Focus on obtaining the configuration at the CNF application level and developing and modifying pipelines to run the test battery.
Execution of test pipelines, monitoring of tests and acquisition of results.
The test results are delivered to the interested parties. Policy enforcement and concerns about sensitive data leakage need to be addressed.
Operate and support testings environments: incident and request management, SLA compliance, environment monitoring, among others.
Governance
Test design
Management layer responsible for project management and support, third-party coordination and related tasks
Test configuration
Test execution
Test feedback
Operation
8
© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

### Notes:
Incluir esta diapositiva

<!-- Slide number: 9 -->
# Automation services
NTT DATA’s framework and services experience
CD/CT Framework tools
CNF orquestration automation and CaaS implementation using our CD/CT framework

![](Imagen141.jpg)
Referential

5
9
© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

### Notes:
Incluir esta diapositiva

<!-- Slide number: 10 -->

5.2
# CI/CD and Software Delivery
Key values and outcomes

<!-- Slide number: 11 -->
# GitOps event-driven pipeline
Solution integration phase

Target Env
(Lab / Stage / Prod)
CI Runner Controller
Vendor
Registry
Source of Truth
Lint
Sign (cosign)
SBOM
Push
CD trigger
CNF Images
Helm Charts
Check sums
Descriptors
Push arteact or commit to the source of truth
For example, ArgoCD Sync or Helm Install
Manifest Update
Issue + Label trigger
Push artefact
Web hookgit event
CI event
CD event
Vendor artefact ingestion controls
GitOps rules

| Rule | Implementation |
| --- | --- |
| No manual deployments | Every environment change comes from a Git-triggered pipeline, no Kubectl apply |
| Event-driven triggers | Registry webhook → GitLab issue + label → CI pipeline that is fully automated |
| Immutable state | Helm values and Kubernetes manifests version-controlled. Every change is a commit |
| Rollback via Git | Reverting a commit triggers to reconcile |
| Ephemeral environments | Test environments provisioned per run, destroyed on completion. Zero state drift |

Scoped credentials and short-lived, project-scoped tokens

Checksum validation (SHA-256) on every incoming artifact

Vulnerability scanning

Format compliance check: CNF descriptor schema or OCI image specification

Quarantine on failure: artefact never promoted if validation fails
11
© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

<!-- Slide number: 12 -->
# Pipeline stages
Proposal

Stages
Validate
Schema check
Checksum
CVE scan
OCI spec check
Build
Docker build
Helm package
Binary compile
SBOM generate
Secure
Cosign sign
SBOM attest
Vulnerability attest
SLSA provenance
Push
Registry push
Git tag create
Registry webhook
Metadata record
Deploy to Lab
CD sync
Helm install
Health check
Smoke test pass
Tests
Robot FW suite
SMO integration
TMS report
Regression gate
Promote
All gates pass
Feed Magenta
Handoff to NI
Evidence package
Pre-Promotion Check
Business Value

Cryptographic proof at every stage
Zero unverified artefacts in production
Supply Chain Integrity

SBOM generation
Audit-ready evidence per release
Regulatory Compliance

Full artifact lineage enables
Root cause isolation
Incident Response

Signed artefacts prove provenance from
specific vendor release and pipeline
Vendor Accountability

Compliance Evidence per Artefact

Signature valid via cosign verify

Who pushed it?
Cosign keyless identity; Registry or repositoru OIDC token

![Badge Tick1 con relleno sólido](Gráfico198.jpg)

Modified after signing?
Record transparency log + Cosign verify
Provenance matches expected builder and pipeline

![Badge Tick1 con relleno sólido](Gráfico199.jpg)

CVEs inside?
e.g., Trivy (or similar) attestation attached to every image
Artifact digest matches Git manifest exactly

![Badge Tick1 con relleno sólido](Gráfico200.jpg)

Which pipeline?
SLSA provenance via Pipeline URL + Commit SHA
Met the proposed tests gates

![Badge Tick1 con relleno sólido](Gráfico201.jpg)

Was it tested?
TMS test report attestation at Continous Testing gate
12

No critical CVEs using vuln attestation check
Quality gate passed?
If custom module, code quality gate passed evidence

![Badge Tick1 con relleno sólido](Gráfico202.jpg)
12
© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

<!-- Slide number: 13 -->

5.3
# Test and Validation
Key values and outcomes

<!-- Slide number: 14 -->
# Test and Validation
Planning and execution capabilities

![](Picture46.jpg)
Test environment planning
Define required E2E environments, configuration baselines, connectivity and data provisioning aligned with  DTAG  architecture.
Ensure env. readiness, including data setup, interfaces, tooling and access controls.
Plan environment availability and scheduling to avoid contention and monitor usage and uptime.

![](Picture63.jpg)
Clear communication
Establish a clear, regular and open channel of communication.
Document and maintain risks, challenges, blockers, open issues and any mitigation plans.
Document and track changes, risks, assumptions, issues and dependencies.
Regular reporting via dashboards, KPIs and risk visibility.

![](Picture62.jpg)
Risk and mitigation planning
Identify potential blockers (environment readiness, data gaps, integration delays) and outline mitigation actions.
Defined roles and ownership through clear RACI alignment.
Controlled change management
Independent QA oversight through governance forums.

![](Picture69.jpg)
Structured approach
Standard QA frameworks with consistent processes and templates. Our approach ensures full visibility across functional, non‑functional, automation and regression coverage. Stage‑gate reviews for entry/exit criteria, risks and defects. Test coverage matrix to give  DTAG  visibility on solution validation. Our approach ensures full visibility across functional, non‑functional, automation and regression coverage.

![](Graphic34.jpg)

Vision / operating model

![](Graphic36.jpg)
QA (Quality Assurance)

![](Graphic38.jpg)

Delivery

![](Graphic40.jpg)
Enablers

![](Graphic41.jpg)
Innovation

![](Graphic42.jpg)

Testing methodology
14
© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

<!-- Slide number: 15 -->
# Test automation suite
Architecture
NTT DATA will align with DTAG’s MAIS RAN Testing Suite Components

Sanity
1
Deployment health before testing begins
| Acronym | Component | Role |
| --- | --- | --- |
| TMS | Test Management System | Scheduling, resource reservation (e.g., RUs/UEs), report generation. Triggered by Magenta CI/CD or GUI. |
| TAF | Test Automation Framework | Execution engine. Receives context from TMS, runs Robot test cases, and validates results. |
| MW | Middleware (SI-owned) | Accuver REST Server. Translates HTTP REST from TAF into byte stream for Test Manager. |
| RI | Resource Inventory | Laboratory configuration DB: connection topology, configuration parameters, real-time lab state. |

SIT
2
Network Function interface & integration testing

Regression
3
Full known-good suite: detect regressions

E2E

![](Picture2.jpg)
4
Standard Test Execution Phases
Real traffic + SMO interaction

UAT
5
Operator acceptance criteria

Performance
6
Referential
KPI baselines

Security
7
SAST/SCA/runtime gate
15
© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

<!-- Slide number: 16 -->
# Robot framework
Test automation
Integrated Test Coverage

Regression

full_regression.robot
200+ cases < 1 hour (parallel runners)

01  Smoke

connectivity.robot
api_health.robot

02  Functional

cu_registration.robot
du_configuration.robot
ue_attach.robot

03  Performance

throughput.robot
latency.robot

![](Imagen7213.jpg)

01 Tests
CU/DU Registration
Heartbeat
NETCONF/YANG Config
Referential

02 Tests
O-Cloud IMS
Infrastructure Alignment
CaaS Lifecycle
…

📊  Execution Report  —  CU/DU v2.3.1
Suite: RAN Full Regression  |  Elapsed: 47 min 32 sec
  ✅  PASS  214  ████████████████████ 91%
  ❌  FAIL   18  ██                    8%
  ⚠️   SKIP    3  ░                     1%
Result: FAIL  →  Promotion to Staging BLOCKED
Why Robot Framework?
Keyword-driven syntax

Human-readable tests enable collaboration between engineers and network specialists. Also, no deep development skills are required.
Library ecosystem

RESTinstance; SSHLibrary; gRPC; YANG/NETCONF adapters; SeleniumLibrary and custom modules.
Data-driven testing

Native parameterisation ideal for RAN configuration tests (like maxCrPgDl variations, bandwidth tables).
HTML reporting

Rich built-in HTML logs and reports satisfy operator audit requirements (no extra tooling).
CI/CD native

Robot CLI integrates directly into CI pipelines. It could be executed at every promotion gate.
16
© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

### Notes:

<!-- Slide number: 17 -->
# NTT DATA’s automation and testing services
Relevant experiences
3. NF Automation Deployment Pipelines
4. NF Automation Deployment Pipelines

![](Imagen11.jpg)

Tier 1 CSP
Main requirements:
Test cases to evaluate UMF, AMF, and NRF, based on their interactions with other emulated network functions.
Workflow Lifecycle Management Testing
Workflow development: development of workflows, based on frameworks such as Serverless Workflows or Ansible.
Workflow onboarding: Definition of workflow onboarding processes in Telco Cloud automation platform (VMware TCA)
Workflow scheduling or execution: Workflow operation automation

![Interfaz de usuario gráfica Descripción generada automáticamente con confianza media](Imagen10.jpg)

![](Imagen17.jpg)

![Logotipo, nombre de la empresa Descripción generada automáticamente](Imagen14.jpg)

![](Imagen15.jpg)

![](Imagen16.jpg)

Global CSP
Main requirements:
Test cases to evaluate AMF and NRF, based on their interactions with other emulated network functions.
Migration of test cases to other companies in the Group, adapting them to the new environment and demonstrating their feasibility for deployment in local environments

E2E Automation of Communications Test (Robot Framework)

Emulators to run complex test scenarios (limited IPs)

Specific adaptations of local technology, processes and regulations (e.g., UK)

Automatic NF test workflow

![](Imagen26.jpg)
17
© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

### Notes:
Incluir esta diapositiva