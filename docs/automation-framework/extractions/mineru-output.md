5.1

## Automation Services

- Key values and offerings

## End-to-end automation framework

Cloud DevOps

**Continuous integration (CI)**

- Every artefact/GIT event triggers a CI pipeline automatically.
Self-managed CI runners (custom, signed images).
Gates: SAST, SCA , Quality Gate, Checksum
CI Runners carry pre-installed tools (for example, cosign, helm, trivy, robot, jf CLI).
No artefacts are promoted without passing all CI stages.

**Continuous delivery (CD)**

- GitOps deployment where a Git repository is the single source of truth.
Promotion: TAV E2E â†’ Pilot â†’ Production fully automated
Version-controlled and auditable Helm Charts and Kubernetes manifests.
Rollback executed in seconds via Git instructions; minimum manual steps require.
Ephemeral environments per pipeline run. No state drift.

**Continuous testing (CT)**

- Robot framework suites executed at every promotion gate (Solution Integration.
SMO integration enables real network-layer compatibility.
TMS tracks test plans, executions and promotion traceability.
Failed tests block promotion automatically; pipeline gate enforced.
Network Integration: MAIS + Magenta CI/CD perform E2E validation in DTAGâ€™s lab environment.

**Audit and traceability â€“ Full provenance chain**

### **1**

<

**Vendor pushes artefacts**

- SHA-256 checksum
- Scoped token auth

### **2**

<

**CI: Build + Sign**

- Cosign sign (keyless OIDC)
- Record logs

### **3**

**CI: Attest**

- SBOM
- Trivy report attached

### **4**

**CI: Provenance**

- Builder ID, Source URI, Digest

### **5**

**CT: Test Evidence**

### **6**

- TMS report attestation attached to artefact

**CD: Pre-deploy gate**

- Cosign verify, SBOM check, CVE threshold, provenance match

2

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

## Three-phase integration model

DTAG and ORION

**Phase**

Interface pre-integration

**Lab Environment**

Component supplier labs

**CI/CD Platform**

Supplier-owned

**Test Execution**

Supplier-owned

**SI Role**

Supplier-owned - SI supports readiness coordination

**Solution Integration  â˜…**

Network integration

**SI-owned Laboratory**

DTAG labs - Bonn / Budapest

**Vendor Delivers**

### **1**

Artefact pushed to the Registry

### **2**

**SI-cloud-devops Framework**

Magenta CI/CD (DTAG)

**Testing Framework (SI)**

**SI owns lab, CI/CD tooling, test cases, and E2E execution**

MAIS RAN Test Suite (DTAG)

DTAG owns platform and MAIS; SI feeds validated  artefacts & metadata

**SI Integrates**

**DTAG Owns**

Solution Integration: CI/CD Platform + Testing Framework + Laboratory Environment

### **3**

Network Integration: Magenta CI/CD + MAIS

**Guiding Principles**

**Everything as code**

**Shift-left security**

**Immutable artefacts**

**Ephemeral environments**

GIT is the single source of truth for pipelines, tests, IaC and policies

SAST/SCA + Code Quality gate at CI time and Never post-deployment

Co-sign is signed; no runtime mutations guaranteed cryptographically

Per-pipeline isolated test environments torn down at completion

**DORA metrics**

Deploy frequency, lead time, CFR, MTTR tracked per release

3

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

## Automation services

NTT DATAâ€™s framework and services

NTT DATA is aware of the challenges faced in the lifecycle management of network functions (xNF) that must be deployed in Telco Cloud environments. That is why from our Network Centres of Excellence we have worked on a **framework to automate its management**, and it has already been used in test and production environments, working with different operators and industry groups.

This framework covers all the tasks related to the **lifecycle of CNFs and VNFs in Telco Cloud environments**, considering laboratory, pre-production and productive environments.

The framework is aligned with the tools that DTAG is available to carry out the CI/CT processes, which will allow us to support the migration of xNF to the Telco Cloud while **minimising the risks of change**.

We have considered that these capabilities are transversal to the service since they are used in the different domains and we have organised them as shown in the figure. Each of them is deepened in this section.

4

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

**Automation, Orchestration and CD/CT**

**Test environments**

**Governance model**

**Execution model**

**CD/CT framework tools**

## Automation services

NTT DATAâ€™s framework and services

## **Automation, Orchestration and CD/CT**

- **Business drivers**
    - Reduced total cost of ownership (TCO) of infrastructure investment for network functions
    - Swap of "legacy" technology
- **Main challenges**
    - Having an automated process for NF testing to speed up the detection of anomalies or errors.
    - Automating a highly disaggregated, multi-supplier RAN
    - Managing continuous lifecycle updates without service disruption
    - Maintaining accountability across component suppliers
    - Increasing test and validation complexity
    - Immutable CI/CD evidence
- **Technologies**
    - CI/CD: Adoption of platforms capable of managing environments, pipelines and endpoints. Systemic integrations for configuration distribution and development standardisation.
    - CT: Using the tools available to make the entire process of hosting, preparing, deploying, and testing network functions as independent as possible from manual input, completely scalable, inmutable and always available.

**1**

5

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

## Automation services

NTT DATAâ€™s framework and services

## **Test environments**

- **TAV â€“ E2E**
    - CNF packet verification
    - Day-0 to Day-2 automation
    - Interoperability, Functional, Performance and security testing
    - Regression tests
    - Ephemeral environment
    - Not necessarily similar to the production environment
    - **Pilot Technology Phase**
    - Production environment conditions
    - Connected to DTAGâ€™s CORE
    - Focused on lab and field E2E measurements.
    - **Pilot Tunning Phase â€“ Production**
    - Live network validation
    - Interact directly with end users
    - Acceptance evidence

**2**

6

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

## Automation services

NTT DATAâ€™s framework and services

## **Execution model**

**3**


**CONTINOUS**

**MONITORING**

7

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

## Automation services

NTT DATAâ€™s framework and services

### **Governance model**

**4**

Management layer responsible for project management and support, third-party coordination and related tasks

## **Governance**

Test preparation

Test design

Test configuration

Test execution

Test feedback

Operation

Preliminary tasks that make the pre-requisites and scope of the test (for example, infrastructure preparation, CNF artefacts procurement, definition of test objectives, among others).

Alignment of tests with the defined objectives and the availability of necessary tools.

Focus on obtaining the configuration at the CNF application level and developing and modifying pipelines to run the test battery.

Execution of test pipelines, monitoring of tests and acquisition of results.

The test results are delivered to the interested parties. Policy enforcement and concerns about sensitive data leakage need to be addressed.

Operate and support testings environments: incident and request management, SLA compliance, environment monitoring, among others.

8

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

## Automation services

NTT DATAâ€™s framework and services experience

## **CD/CT Framework tools**

### **CNF orquestration automation and CaaS implementation using our CD/CT framework**

**5**


Referential

9

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

5.2

## CI/CD and Software Delivery

- Key values and outcomes

## GitOps event-driven pipeline

Solution integration phase

**Vendor**

Push arteact or commit to the source of truth

***Push***  ***artefact***

**Registry**

CNF Images

Helm Charts

Check sums

Descriptors

***Web hook*** ***git event***

**Source of Truth**

**CI Runner Controller**

Manifest Update

Issue + Label trigger

***CI***  ***event***

Lint

Sign (cosign)
SBOM

Push

CD trigger

***CD***  ***event***

**Target Env
(Lab / Stage / Prod)**

For example, ArgoCD Sync or Helm Install

**Vendor artefact ingestion controls**

**Scoped credentials and short-lived, project-scoped tokens**

**Checksum validation (SHA-256) on every incoming artifact**

**Vulnerability scanning**

**Format compliance check: CNF descriptor schema or OCI image specification**

**Quarantine on failure: artefact never promoted if validation fails**

**GitOps rules**

<table>
  <tr>
    <th>Rule</th>
    <th>Implementation</th>
  </tr>
  <tr>
    <td>No manual deployments</td>
    <td>Every environment change comes from a Git-triggered pipeline, no Kubectl apply</td>
  </tr>
  <tr>
    <td>Event-driven triggers</td>
    <td>Registry webhook â†’ GitLab issue + label â†’ CI pipeline that is fully automated</td>
  </tr>
  <tr>
    <td>Immutable state</td>
    <td>Helm values and Kubernetes manifests version-controlled. Every change is a commit</td>
  </tr>
  <tr>
    <td>Rollback via Git</td>
    <td>Reverting a commit triggers to reconcile</td>
  </tr>
  <tr>
    <td>Ephemeral environments</td>
    <td>Test environments provisioned per run, destroyed on completion. Zero state drift</td>
  </tr>
</table>

11

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

## Pipeline stages

Proposal

### **Stages**

### **Validate**

- Schema check
Checksum
CVE scan
OCI spec check

### **Build**

- Docker build
Helm package
Binary compile
SBOM generate

### **Secure**

- Cosign sign
SBOM attest
Vulnerability attest
SLSA provenance

### **Push**

- Registry push
Git tag create
Registry webhook
Metadata record

### **Deploy to Lab**

- CD sync
Helm install
Health check
Smoke test pass

### **Tests**

- Robot FW suite
SMO integration
TMS report
Regression gate

### **Promote**

- All gates pass
Feed Magenta
Handoff to NI
Evidence package

### **Business Value**

**Supply Chain Integrity**

- Cryptographic proof at every stage
Zero unverified artefacts in production

**Regulatory Compliance**

- SBOM generation
Audit-ready evidence per release

**Incident Response**

- Full artifact lineage enables
Root cause isolation

**Vendor Accountability**

- Signed artefacts prove provenance from
specific vendor release and pipeline

***Pre-Promotion Check***

### **Compliance Evidence per Artefact**

Who pushed it?

Modified after signing?

CVEs inside?

Which pipeline?

Was it tested?

Quality gate passed?

Cosign keyless identity; Registry or repositoru OIDC token

Record transparency log + Cosign verify

e.g., Trivy (or similar) attestation attached to every image

SLSA provenance via Pipeline URL + Commit SHA

TMS test report attestation at Continous Testing gate

12

If custom module, code quality gate passed evidence

Signature valid via cosign verify

Provenance matches expected builder and pipeline

Artifact digest matches Git manifest exactly

Met the proposed tests gates

No critical CVEs using vuln attestation check

12

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

5.3

## Test and Validation

- Key values and outcomes

## Test and Validation

Planning and execution capabilities

**Vision / operating model**

**QA (Quality Assurance)**

**Delivery**

**Enablers**

**Innovation**

**Testing methodology**

### **Test environment planning**

- Define required E2E environments, configuration baselines, connectivity and data provisioning aligned with  DTAG  architecture.
- Ensure env. readiness, including data setup, interfaces, tooling and access controls.
- Plan environment availability and scheduling to avoid contention and monitor usage and uptime.

### **Clear communication**

- Establish a clear, regular and open channel of communication.
- Document and maintain risks, challenges, blockers, open issues and any mitigation plans.
- Document and track changes, risks, assumptions, issues and dependencies.
- Regular reporting via dashboards, KPIs and risk visibility.

### **Risk and mitigation planning**

- Identify potential blockers (environment readiness,  data gaps, integration delays) and outline mitigation actions.
- Defined roles and ownership through clear RACI alignment.
- Controlled change management
- Independent QA oversight through governance forums.

### **Structured approach**

Standard QA frameworks with consistent processes  and templates. Our approach ensures full visibility across functional, nonâ€‘functional, automation and regression coverage. Stageâ€‘gate reviews for entry/exit criteria, risks and defects. Test coverage matrix to give  DTAG  visibility on solution validation. Our approach ensures full visibility across functional, nonâ€‘functional, automation and regression coverage.

14

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

## Test automation suite

Architecture

**NTT DATA will align with DTAGâ€™s MAIS RAN Testing Suite Components**

**Sanity**

### **1**

Deployment health before testing begins

<table>
  <tr>
    <th>Acronym</th>
    <th>Component</th>
    <th>Role</th>
  </tr>
  <tr>
    <td>TMS</td>
    <td>Test Management System</td>
    <td>Scheduling, resource reservation (e.g., RUs/UEs), report generation. Triggered by Magenta CI/CD or GUI.</td>
  </tr>
  <tr>
    <td>TAF</td>
    <td>Test Automation Framework</td>
    <td>Execution engine. Receives context from TMS, runs Robot test cases, and validates results.</td>
  </tr>
  <tr>
    <td>MW</td>
    <td>Middleware (SI-owned)</td>
    <td>Accuver REST Server. Translates HTTP REST from TAF into byte stream for Test Manager.</td>
  </tr>
  <tr>
    <td>RI</td>
    <td>Resource Inventory</td>
    <td>Laboratory configuration DB: connection topology, configuration parameters, real-time lab state.</td>
  </tr>
</table>

**SIT**

### **2**

Network Function interface & integration testing

**Regression**

### **3**

Full known-good suite: detect regressions

**E2E**


### **4**

**Standard Test Execution Phases**

Real traffic + SMO interaction

**UAT**

### **5**

Operator acceptance criteria

**Performance**

### **6**

Referential

KPI baselines

**Security**

### **7**

SAST/SCA/runtime gate

15

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

## Robot framework

Test automation

### **Integrated Test Coverage**

**ðŸ“Š  Execution Report  â€”  CU/DU v2.3.1**

Suite: RAN Full Regression  |  Elapsed: 47 min 32 sec

âœ…  PASS  214  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ 91%

âŒ  FAIL   18  â–ˆâ–ˆ                    8%

âš ï¸   SKIP    3  â–‘                     1%

Result: FAIL  â†’  Promotion to Staging BLOCKED

### **Why Robot Framework?**

**Keyword-driven syntax**

Human-readable tests enable collaboration between engineers and network specialists. Also, no deep development skills are required.

**Library ecosystem**

RESTinstance; SSHLibrary; gRPC; YANG/NETCONF adapters; SeleniumLibrary and custom modules.

**Data-driven testing**

Native parameterisation ideal for RAN configuration tests (like maxCrPgDl variations, bandwidth tables).

**HTML reporting**

Rich built-in HTML logs and reports satisfy operator audit requirements (no extra tooling).

**CI/CD native**

Robot CLI integrates directly into CI pipelines. It could be executed at every promotion gate.

16

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential

### **Regression**

full\_regression.robot
200+ cases < 1 hour (parallel runners)

### **01  Smoke**

- connectivity.robot
api\_health.robot


### **02  Functional**

- cu\_registration.robot
du\_configuration.robot
ue\_attach.robot

### **03  Performance**

- throughput.robot
latency.robot

Referential

### **01 Tests**

- CU/DU Registration
- Heartbeat
- NETCONF/YANG Config

### **02 Tests**

- O-Cloud IMS
- Infrastructure Alignment
- CaaS Lifecycle

â€¦

## NTT DATAâ€™s automation and testing services

Relevant experiences

### **3. NF Automation Deployment Pipelines**

Global CSP

**Main requirements:**

- Test cases to evaluate AMF and NRF, based on their interactions with other emulated network functions.
Migration of test cases to other companies in the Group, adapting them to the new environment and demonstrating their feasibility for deployment in local environments

**E2E Automation of Communications Test (Robot Framework)**

**Emulators to run complex test scenarios (limited IPs)**

**Specific adaptations of local technology, processes and regulations (e.g., UK)**

**Automatic NF test workflow**

### **4. NF Automation Deployment Pipelines**

Tier 1 CSP

**Main requirements:**

- Test cases to evaluate UMF, AMF, and NRF, based on their interactions with other emulated network functions.
**Workflow Lifecycle Management Testing**
- **Workflow development**: development of workflows, based on frameworks such as Serverless Workflows or Ansible.
- **Workflow onboarding**: Definition of workflow onboarding processes in Telco Cloud automation platform (VMware TCA)
- **Workflow scheduling or execution**: Workflow operation automation


17

Â© 2026 NTT DATA Deutschland SE | Proprietary and Confidential
