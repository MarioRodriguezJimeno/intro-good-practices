# Automation Services

- Key values and offerings

5.1

# End-to-end automation framework

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

2

Cloud DevOps

1

&lt;

Vendor pushes artefacts

- SHA-256 checksum
- Scoped token auth

2

&lt;

CI: Build + Sign

- Cosign sign (keyless OIDC)
- Record logs

3

CI: Attest

- SBOM
- Trivy report attached

4

CI: Provenance

- Builder ID, Source URI, Digest

5

CT: Test Evidence

- TMS report attestation attached to artefact

6

CD: Pre-deploy gate

- Cosign verify, SBOM check, CVE threshold, provenance match

Audit and traceability â€“ Full provenance chain

Continuous integration (CI)

Continuous delivery (CD)

Continuous testing (CT)

- Every artefact/GIT event triggers a CI pipeline automatically.
Self-managed CI runners (custom, signed images).
Gates: SAST, SCA , Quality Gate, Checksum
CI Runners carry pre-installed tools (for example, cosign, helm, trivy, robot, jf CLI).
No artefacts are promoted without passing all CI stages.

- GitOps deployment where a Git repository is the single source of truth.
Promotion: TAV E2E â†’ Pilot â†’ Production fully automated
Version-controlled and auditable Helm Charts and Kubernetes manifests.
Rollback executed in seconds via Git instructions; minimum manual steps require.
Ephemeral environments per pipeline run. No state drift.

- Robot framework suites executed at every promotion gate (Solution Integration.
SMO integration enables real network-layer compatibility.
TMS tracks test plans, executions and promotion traceability.
Failed tests block promotion automatically; pipeline gate enforced.
Network Integration: MAIS + Magenta CI/CD perform E2E validation in DTAGâ€™s lab environment.

# Three-phase integration model

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

3

DTAG and ORION

Artefact pushed to the Registry

1

Vendor Delivers

Solution Integration: CI/CD Platform + Testing Framework + Laboratory Environment

SI Integrates

2

Network Integration: Magenta CI/CD + MAIS

DTAG Owns

3

Everything as code

GIT is the single source of truth for pipelines, tests, IaC and policies

Shift-left security

SAST/SCA + Code Quality gate at CI time and Never post-deployment

Immutable artefacts

Co-sign is signed; no runtime mutations guaranteed cryptographically

Ephemeral environments

Per-pipeline isolated test environments torn down at completion

DORA metrics

Deploy frequency, lead time, CFR, MTTR tracked per release

Guiding Principles

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

Network integration

DTAG labs - Bonn / Budapest

Magenta CI/CD (DTAG)

MAIS RAN Test Suite (DTAG)

DTAG owns platform and MAIS; SI feeds validated  artefacts &amp; metadata

Solution Integration  â˜…

SI-owned Laboratory

SI-cloud-devops Framework

Testing Framework (SI)

SI owns lab, CI/CD tooling, test cases, and E2E execution

# Automation services

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

4

NTT DATAâ€™s framework and services

NTT DATA is aware of the challenges faced in the lifecycle management of network functions (xNF) that must be deployed in Telco Cloud environments. That is why from our Network Centres of Excellence we have worked on a framework to automate its management, and it has already been used in test and production environments, working with different operators and industry groups.


This framework covers all the tasks related to the lifecycle of CNFs and VNFs in Telco Cloud environments, considering laboratory, pre-production and productive environments.


The framework is aligned with the tools that DTAG is available to carry out the CI/CT processes, which will allow us to support the migration of xNF to the Telco Cloud while minimising the risks of change.


We have considered that these capabilities are transversal to the service since they are used in the different domains and we have organised them as shown in the figure. Each of them is deepened in this section.

Automation, Orchestration and CD/CT

Test environments

Execution model

Governance model

CD/CT framework tools

# Automation services

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

5

NTT DATAâ€™s framework and services

- Business drivers
- Reduced total cost of ownership (TCO) of infrastructure investment for network functions
- Swap of "legacy" technology
- Main challenges
- Having an automated process for NF testing to speed up the detection of anomalies or errors.
- Automating a highly disaggregated, multi-supplier RAN
- Managing continuous lifecycle updates without service disruption
- Maintaining accountability across component suppliers
- Increasing test and validation complexity
- Immutable CI/CD evidence
- Technologies
- CI/CD: Adoption of platforms capable of managing environments, pipelines and endpoints. Systemic integrations for configuration distribution and development standardisation.
- CT: Using the tools available to make the entire process of hosting, preparing, deploying, and testing network functions as independent as possible from manual input, completely scalable, inmutable and always available.
-

Automation, Orchestration and CD/CT

1

# Automation services

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

6

NTT DATAâ€™s framework and services





- TAV â€“ E2E
- CNF packet verification
- Day-0 to Day-2 automation
- Interoperability, Functional, Performance and security testing
- Regression tests
- Ephemeral environment
- Not necessarily similar to the production environment
- Pilot Technology Phase
- Production environment conditions
- Connected to DTAGâ€™s CORE
- Focused on lab and field E2E measurements.
- Pilot Tunning Phase â€“ Production
- Live network validation
- Interact directly with end users
- Acceptance evidence

Test environments

2

# Automation services

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

7

NTT DATAâ€™s framework and services


CONTINOUS

MONITORING

Execution model

3

# Automation services

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

8

NTT DATAâ€™s framework and services

Test design

Test configuration

Test execution

Test feedback

Operation

Governance

Test preparation

Management layer responsible for project management and support, third-party coordination and related tasks

Preliminary tasks that make the pre-requisites and scope of the test (for example, infrastructure preparation, CNF artefacts procurement, definition of test objectives, among others).

Alignment of tests with the defined objectives and the availability of necessary tools.

Focus on obtaining the configuration at the CNF application level and developing and modifying pipelines to run the test battery.

The test results are delivered to the interested parties. Policy enforcement and concerns about sensitive data leakage need to be addressed.

Operate and support testings environments: incident and request management, SLA compliance, environment monitoring, among others.

Execution of test pipelines, monitoring of tests and acquisition of results.

Governance model

4

# Automation services

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

9

NTT DATAâ€™s framework and services experience


CNF orquestration automation and CaaS implementation using our CD/CT framework

Referential

CD/CT Framework tools

5

# CI/CD and Software Delivery

- Key values and outcomes

5.2

# GitOps event-driven pipeline

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

11

Solution integration phase

GitOps rules

Vendor

Push arteact or commit to the source of truth

Push  artefact

Registry

CNF Images

Helm Charts

Check sums

Descriptors

Web hook git event

Source of Truth

Manifest Update

Issue + Label trigger

CI  event

CI Runner Controller

Lint

Sign (cosign)
SBOM

Push

CD trigger

CD  event

Target Env
(Lab / Stage / Prod)

For example, ArgoCD Sync or Helm Install

Vendor artefact ingestion controls

Scoped credentials and short-lived, project-scoped tokens

Quarantine on failure: artefact never promoted if validation fails

Checksum validation (SHA-256) on every incoming artifact

Vulnerability scanning

Format compliance check: CNF descriptor schema or OCI image specification

| Rule                   | Implementation                                                                    |
|------------------------|-----------------------------------------------------------------------------------|
| No manual deployments  | Every environment change comes from a Git-triggered pipeline, no Kubectl apply    |
| Event-driven triggers  | Registry webhook â†’ GitLab issue + label â†’ CI pipeline that is fully automated     |
| Immutable state        | Helm values and Kubernetes manifests version-controlled. Every change is a commit |
| Rollback via Git       | Reverting a commit triggers to reconcile                                          |
| Ephemeral environments | Test environments provisioned per run, destroyed on completion. Zero state drift  |

# Pipeline stages

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

12

Proposal

Stages

Signature valid via cosign verify

No critical CVEs using vuln attestation check

Provenance matches expected builder and pipeline

Artifact digest matches Git manifest exactly

Met the proposed tests gates

12

Who pushed it?

Cosign keyless identity; Registry or repositoru OIDC token

Modified after signing?

Record transparency log + Cosign verify

CVEs inside?

e.g., Trivy (or similar) attestation attached to every image

Which pipeline?

SLSA provenance via Pipeline URL + Commit SHA

Was it tested?

TMS test report attestation at Continous Testing gate

Compliance Evidence per Artefact

Quality gate passed?

If custom module, code quality gate passed evidence

Pre-Promotion Check

- Schema check
Checksum
CVE scan
OCI spec check

Validate

- Docker build
Helm package
Binary compile
SBOM generate

Build

- Cosign sign
SBOM attest
Vulnerability attest
SLSA provenance

Secure

- Registry push
Git tag create
Registry webhook
Metadata record

Push

- CD sync
Helm install
Health check
Smoke test pass

Deploy to Lab

- Robot FW suite
SMO integration
TMS report
Regression gate

Tests

- All gates pass
Feed Magenta
Handoff to NI
Evidence package

Promote

Business Value

- Cryptographic proof at every stage
Zero unverified artefacts in production

- SBOM generation
Audit-ready evidence per release

- Full artifact lineage enables
Root cause isolation

- Signed artefacts prove provenance from
specific vendor release and pipeline

Supply Chain Integrity

Regulatory Compliance

Incident Response

Vendor Accountability

# Test and Validation

- Key values and outcomes

5.3

# Test and Validation

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

14

Planning and execution capabilities

QA (Quality Assurance)

Delivery

Enablers

Innovation

Testing methodology

Vision / operating model

- Define required E2E environments, configuration baselines, connectivity and data provisioning aligned with  DTAG  architecture.
- Ensure env. readiness, including data setup, interfaces, tooling and access controls.
- Plan environment availability and scheduling to avoid contention and monitor usage and uptime.

Test environment planning

- Establish a clear, regular and open channel of communication.
- Document and maintain risks, challenges, blockers, open issues and any mitigation plans.
- Document and track changes, risks, assumptions, issues and dependencies.
- Regular reporting via dashboards, KPIs and risk visibility.
-

Clear communication



Standard QA frameworks with consistent processes  and templates. Our approach ensures full visibility across functional, nonâ€‘functional, automation and regression coverage. Stageâ€‘gate reviews for entry/exit criteria, risks and defects. Test coverage matrix to give  DTAG  visibility on solution validation. Our approach ensures full visibility across functional, nonâ€‘functional, automation and regression coverage.

- Identify potential blockers (environment readiness,  data gaps, integration delays) and outline mitigation actions.
- Defined roles and ownership through clear RACI alignment.
- Controlled change management
- Independent QA oversight through governance forums.

Risk and mitigation planning

Structured approach



# Test automation suite

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

15

Architecture

Sanity

Deployment health before testing begins

SIT

Network Function interface &amp; integration testing

Regression

Full known-good suite: detect regressions

E2E

Real traffic + SMO interaction

UAT

Operator acceptance criteria

Performance

KPI baselines

Security

SAST/SCA/runtime gate

Standard Test Execution Phases


1

2

3

4

5

6

7

NTT DATA will align with DTAGâ€™s MAIS RAN Testing Suite Components

| Acronym   | Component                 | Role                                                                                                    |
|-----------|---------------------------|---------------------------------------------------------------------------------------------------------|
| TMS       | Test Management System    | Scheduling, resource reservation (e.g., RUs/UEs), report generation. Triggered by Magenta CI/CD or GUI. |
| TAF       | Test Automation Framework | Execution engine. Receives context from TMS, runs Robot test cases, and validates results.              |
| MW        | Middleware (SI-owned)     | Accuver REST Server. Translates HTTP REST from TAF into byte stream for Test Manager.                   |
| RI        | Resource Inventory        | Laboratory configuration DB: connection topology, configuration parameters, real-time lab state.        |

Referential

# Robot framework

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

16

Test automation

ðŸ“Š  Execution Report  â€”  CU/DU v2.3.1

Suite: RAN Full Regression  |  Elapsed: 47 min 32 sec

  âœ…  PASS  214  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ 91%

  âŒ  FAIL   18  â–ˆâ–ˆ                    8%

  âš ï¸   SKIP    3  â–‘                     1%

Result: FAIL  â†’  Promotion to Staging BLOCKED

Regression

full\_regression.robot
200+ cases &lt; 1 hour (parallel runners)

01  Smoke

- connectivity.robot
api\_health.robot

02  Functional

- cu\_registration.robot
du\_configuration.robot
ue\_attach.robot

03  Performance

- throughput.robot
latency.robot


01 Tests

- CU/DU Registration
- Heartbeat
- NETCONF/YANG Config

02 Tests

- O-Cloud IMS
- Infrastructure Alignment
- CaaS Lifecycle

â€¦

Integrated Test Coverage

Referential

Why Robot Framework?

Human-readable tests enable collaboration between engineers and network specialists. Also, no deep development skills are required.

Keyword-driven syntax

RESTinstance; SSHLibrary; gRPC; YANG/NETCONF adapters; SeleniumLibrary and custom modules.

Library ecosystem

Native parameterisation ideal for RAN configuration tests (like maxCrPgDl variations, bandwidth tables).

Data-driven testing

Rich built-in HTML logs and reports satisfy operator audit requirements (no extra tooling).

HTML reporting

Robot CLI integrates directly into CI pipelines. It could be executed at every promotion gate.

CI/CD native

# NTT DATAâ€™s automation and testing services

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

17

Relevant experiences

4. NF Automation Deployment Pipelines

Tier 1 CSP

Main requirements:

- Test cases to evaluate UMF, AMF, and NRF, based on their interactions with other emulated network functions.
Workflow Lifecycle Management Testing
- Workflow development: development of workflows, based on frameworks such as Serverless Workflows or Ansible.
- Workflow onboarding: Definition of workflow onboarding processes in Telco Cloud automation platform (VMware TCA)
- Workflow scheduling or execution: Workflow operation automation
-



3. NF Automation Deployment Pipelines

Global CSP





Main requirements:

- Test cases to evaluate AMF and NRF, based on their interactions with other emulated network functions.
Migration of test cases to other companies in the Group, adapting them to the new environment and demonstrating their feasibility for deployment in local environments

E2E Automation of Communications Test (Robot Framework)

Emulators to run complex test scenarios (limited IPs)

Specific adaptations of local technology, processes and regulations (e.g., UK)


Automatic NF test workflow
