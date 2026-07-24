# AGENTS.md

## 1. Purpose

This file instructs AI agents that create PowerPoint presentations about NTT DATA’s Automation Framework.

Generated presentations must:

- Follow the corporate visual style described here.
- Explain the Automation Framework accurately.
- Use confirmed CI/CD/CT terminology.
- Represent environments, pipelines, governance and architecture clearly.
- Include auditability and traceability where relevant.
- Avoid inventing internal processes, acronyms or corporate decisions.

## 2. Scope

These instructions apply primarily to presentations about:

- Automation Framework and Cloud DevOps.
- CI/CD/CT and Network Function lifecycle automation.
- GitOps and event-driven pipelines.
- Test automation and Robot Framework.
- Test environments and promotion gates.
- Governance, auditability and traceability.
- Telco Cloud automation architecture.

The visual rules may be reused for related NTT DATA technical presentations, but the functional content is specific to the Automation Framework.

## 3. Confidentiality

The reference presentation `AutomationFramework-Orion.pptx` is confidential.

The agent must never:

- Add the reference presentation to a commit.
- Copy it into generated deliverables.
- Expose confidential customer information.
- Reuse customer architectures without authorization.
- Include raw extraction files in the repository.
- Reveal local working documents stored in `reference-private/`.

Files inside `reference-private/` are local analysis material and must remain ignored by Git.

## 4. Source-of-truth rules

Use the confirmed information contained in this file.

When information is incomplete or ambiguous:

- Preserve the original terminology.
- Mark the information as requiring validation.
- Do not invent acronym definitions.
- Do not silently correct internal terminology.
- Do not present recommendations as official NTT DATA decisions.
- Do not claim that an example technology is mandatory unless confirmed.

Use these classifications when necessary:

- `Confirmed`: directly supported by the reference material.
- `Implementation recommendation`: a proposed best practice.
- `Requires NTT DATA validation`: ambiguous or incomplete information.

## 5. Role of the PPT Maker agent

The agent must:

- Identify the intended audience.
- Identify one principal message per slide.
- Select an appropriate layout.
- Use concise content.
- Prefer diagrams over dense paragraphs.
- Preserve corporate terminology.
- Represent technical relationships accurately.
- Show promotion gates and blocking conditions.
- Include ownership and evidence where relevant.
- Adapt the technical depth to the audience.

The agent must not:

- Fill slides with excessive text.
- Reduce fonts excessively to fit content.
- Create decorative diagrams without technical meaning.
- Mix environment models without clarification.
- Present every technology logo as mandatory.
- Hide uncertainty behind confident wording.

## 6. General presentation style

Use a professional, technical and corporate style.

- Use widescreen format.
- Prefer white backgrounds for content slides.
- Use a clear hierarchy between title, subtitle and content.
- Align titles to the upper-left.
- Keep consistent margins and sufficient white space.
- Use diagrams, cards, tables and pipelines where appropriate.
- Keep corporate branding consistent.
- Use blue, turquoise and green to distinguish concepts and phases.
- Avoid elements that do not communicate information.

Each slide must communicate one principal idea.

## 7. Typography

### Main titles

- Use a large serif font.
- Use corporate blue.
- Align the title to the upper-left.
- Keep titles short and descriptive.
- Use sentence case.

### Subtitles

- Use a smaller sans-serif font.
- Use black or dark grey.
- Position the subtitle directly below the title.

### Body text

- Use a readable sans-serif font.
- Use dark text on light backgrounds.
- Prefer concise bullets.
- Use bold only for important concepts or conclusions.
- Avoid long paragraphs and extremely small text.

Exact font families and sizes require validation against the official NTT DATA PowerPoint template.

## 8. Color system

Use these functional color roles:

- Corporate blue: titles and principal headers.
- Dark navy: structural headers and separation elements.
- Medium blue: CI and early pipeline activities.
- Light blue: information cards and secondary content.
- Turquoise: testing, governance, traceability and environments.
- Green: promotion, tools and validated final states.
- Orange: section-number tabs.
- Light grey: inactive layers and secondary information.
- White: backgrounds and text over dark images.
- Black or dark grey: body text.

Do not rely only on color to communicate status. Use labels, numbers or icons as well.

Exact corporate color codes require validation.

## 9. Corporate branding

- Place corporate logos in the bottom-right corner.
- Place the slide number and confidentiality notice in the bottom-left when required.
- Use white logo variants on photographic section-divider slides.
- Use standard dark logo variants on white content slides.
- Never stretch, recolor, crop or recreate corporate logos.
- Maintain clear space around logos.
- Use only approved logo assets.

Exact logo dimensions and usage rules require validation.

## 10. Section-divider slides

Use a section-divider slide when introducing a major topic.

Required structure:

- Full-slide photographic background.
- Orange section-number tab in the upper-left.
- Dark navy diagonal element beside the tab.
- Large white serif title.
- Smaller white sans-serif subtitle.
- White corporate logos in the bottom-right.

Include only the section number, main title and one subtitle. Do not include detailed technical explanations.

Position text over an area with sufficient contrast.

## 11. Standard content slides

Use:

- White background.
- Blue serif title in the upper-left.
- Black sans-serif subtitle below the title.
- Main content below the subtitle.
- Footer along the bottom.

Recommended layouts:

- Two-column text and diagram.
- Three-column comparison.
- Two-by-two capability cards.
- Horizontal pipeline.
- Vertical lifecycle.
- Layered architecture.
- Table with supporting diagram.
- Side navigation with detailed content.

## 12. Readability

- Communicate one main idea per slide.
- Prefer short bullets over paragraphs.
- Use diagrams for processes and architecture.
- Split complex content across several slides.
- Avoid crossing connector lines.
- Maintain strong contrast.
- Ensure that slides remain readable when projected.
- Avoid placing white text over bright image areas.
- Avoid very small text inside diagrams.
- Use executive summaries for general audiences.
- Use detailed architecture only for technical audiences.

## 13. Capability overview slides

When presenting the main Automation Framework capabilities:

- Use a stacked-layer diagram.
- Give each layer a blue, turquoise or green tone.
- Connect every layer to a short label.
- Use the diagram to show capability grouping, not necessarily execution order.
- Explain the business purpose beside the diagram.

The five capabilities identified in the reference material are:

1. Automation, Orchestration and CD/CT.
2. Test environments.
3. Execution model.
4. Governance model.
5. CD/CT Framework tools.

The numbering of Governance and Execution requires validation because the reference material contains a possible inconsistency.

## 14. Capability-detail slides

When explaining one capability:

- Show the complete layered framework on the left.
- Highlight only the active capability.
- Display inactive layers in grey.
- Add a numbered circle beside the active layer.
- Use a vertical arrow to connect the framework to the detailed content.
- Place the capability name inside a colored rounded banner.
- Preserve consistent numbering and colors.

Recommended content:

- Business drivers.
- Main challenges.
- Responsibilities.
- Technologies.
- Expected outcomes.

## 15. Automation Framework overview

The Automation Framework supports the automated lifecycle management of:

- Cloud-native Network Functions.
- Virtual Network Functions.
- Network functions generally described as xNFs.
- Telco Cloud environments.
- Laboratory, pre-production and production activities.

The framework aims to:

- Reduce manual intervention.
- Improve repeatability.
- Increase test and validation coverage.
- Reduce change-related risks.
- Maintain auditability and traceability.
- Support Network Function migration.
- Coordinate suppliers, System Integrators and operators.

## 16. Main offering

The framework may provide:

- Automation and orchestration.
- Continuous Integration.
- Continuous Delivery and Deployment.
- Continuous Testing and Monitoring.
- Test-environment management.
- Governance.
- Test automation.
- Artefact and image management.
- GitOps-based deployment.
- Security and quality gates.
- Audit and provenance evidence.
- Controlled environment promotion.
- Version-controlled rollback.

## 17. Framework principles

### Everything as code

Git should act as the source of truth for pipelines, tests, Infrastructure as Code, policies, Helm Charts, Kubernetes manifests and environment configuration.

### Shift-left security

Security controls should begin during CI and may include SAST, SCA, code-quality gates, vulnerability scanning, checksum validation, OCI checks and SBOM generation or validation.

### Immutable artefacts

Artefacts should be versioned, identifiable by digest, signed, protected against untracked changes and connected to provenance and test evidence. Promote without rebuilding whenever technically possible.

### Ephemeral environments

Test environments should, where applicable, be created for each pipeline execution, remain isolated, be destroyed after completion and prevent state drift.

### Auditability and traceability

Each artefact should be linked to its vendor identity, source commit, pipeline execution, builder identity, digest, signature, SBOM, vulnerability result, tests, quality gates, promotion and deployment.

## 18. Responsibility model

The reference material describes three integration phases.

### Interface pre-integration

- Mainly owned by the component supplier.
- Performed in supplier laboratories.
- Supplier owns its CI/CD platform and test execution.
- The System Integrator supports readiness coordination.

### Solution Integration

- Laboratory owned by the System Integrator.
- Uses the SI Cloud DevOps Framework and SI Testing Framework.
- The System Integrator owns laboratory operation, CI/CD tooling, test cases, end-to-end execution and integration coordination.

### Network Integration

- Mainly owned by DTAG.
- Uses DTAG laboratories, Magenta CI/CD and the MAIS RAN Test Suite.
- The System Integrator provides validated artefacts and metadata.

Do not invent responsibility assignments that are not confirmed.

## 19. Environment terminology

The source material uses several environment models.

Testing progression:

- TAV E2E.
- Pilot Technology Phase.
- Pilot Tuning Phase.

Deployment architecture:

- Development.
- Pre-Production.
- Production.

GitOps target environments:

- Laboratory.
- Staging.
- Production.

Do not automatically treat these names as exact equivalents. Preserve the original terminology and mark uncertain equivalences as requiring validation.

## 20. Test environments

### TAV E2E

Purpose:

- Early end-to-end validation.
- Isolated and repeatable testing.
- Rapid technical feedback.

Typical activities:

- CNF verification.
- Day-0 to Day-2 automation.
- Interoperability, functional, performance, security and regression testing.

The environment may be ephemeral and does not necessarily reproduce Production exactly.

### Pilot Technology Phase

Purpose:

- Validate the solution under Production-like conditions.

Typical activities:

- Connection to DTAG CORE.
- Laboratory and field end-to-end measurements.
- Production-condition validation.

### Pilot Tuning Phase

Purpose:

- Validate the solution in a live-network context.

Typical activities:

- Live-network validation.
- Interaction with end users.
- Generation of acceptance evidence.

## 21. Environment-promotion rules

Promotion should occur only when:

- Mandatory technical, security and quality gates pass.
- Required tests pass.
- Evidence has been generated.
- Provenance matches the expected source and builder.
- The artefact digest matches the approved manifest.
- The applicable approval or policy gate is satisfied.

Promote the same immutable artefact that was previously validated whenever technically possible.

## 22. Continuous Integration

Continuous Integration may begin when a vendor pushes an artefact, a Git change is committed, a registry event is generated or an approved issue or label triggers automation.

Typical CI activities:

1. Validate the incoming artefact.
2. Check schema, checksum and OCI compliance.
3. Scan for vulnerabilities.
4. Build the image, binary or Helm package.
5. Generate the SBOM.
6. Sign the artefact.
7. Generate security attestations and provenance.
8. Push the validated artefact.
9. Record metadata.

Typical controls include:

- SAST and SCA.
- Code-quality gates.
- CVE scanning.
- SHA-256 validation.
- OCI validation.
- Cosign signing.
- SBOM and vulnerability attestations.
- SLSA provenance.

No artefact should leave CI when a mandatory gate fails.

## 23. Continuous Delivery and Deployment

Continuous Delivery prepares and promotes validated artefacts.

Main rules:

- Git is the source of truth.
- Environment configuration is version-controlled.
- Environment changes are applied through automated pipelines.
- Manual deployment is not the normal controlled process.
- Promote the validated artefact without rebuilding where possible.
- Rollback is performed through an approved Git change.
- Automation reconciles the runtime environment with the desired state.

Typical activities:

- Update manifests and Helm values.
- Trigger deployment.
- Synchronise the target environment.
- Install or upgrade through Helm.
- Execute health checks and smoke tests.
- Collect deployment evidence.
- Promote after all required gates pass.

Technologies shown include Argo CD, Helm, Flux, Jenkins, Tekton, Terraform, Ansible, Nephio, Kubernetes, Red Hat OpenShift and VMware Tanzu Kubernetes Grid. Treat them as examples or available integrations until validated.

## 24. Continuous Testing

Continuous Testing validates the artefact throughout the delivery lifecycle.

It may include:

- Sanity and smoke testing.
- System Integration Testing.
- Functional and regression testing.
- End-to-end and User Acceptance Testing.
- Performance and security testing.

Continuous Testing should:

- Execute at defined promotion gates.
- Use repeatable suites.
- Generate traceable evidence.
- Block promotion when mandatory tests fail.
- Associate results with the tested artefact.
- Return results to the Test Management System.
- Retain logs and reports for auditing.

The mandatory phases for each environment require validation.

## 25. Robot Framework

Robot Framework is used as a test-execution technology within the wider testing architecture. Do not present it as the complete test-management platform.

Reasons for using Robot Framework:

- Human-readable keyword-driven syntax.
- Collaboration between software engineers and network specialists.
- Reusable, data-driven and parameterised tests.
- Extensive library ecosystem.
- Built-in HTML reports and logs.
- Direct CI/CD integration.
- Suitability for integration, regression and acceptance testing.

Recommended suite organisation:

- Smoke tests.
- Functional tests.
- Performance tests.
- Regression tests.
- Environment-specific acceptance tests.

Execution flow:

1. The pipeline deploys the artefact.
2. The Test Management System prepares the execution context.
3. The Test Automation Framework starts the required suites.
4. Robot Framework executes the tests.
5. Reports and logs are generated.
6. Results are returned to the Test Management System.
7. The Continuous Testing gate evaluates the result.
8. Promotion is allowed or blocked.

A failed mandatory test must block promotion. A high total pass percentage must not override a failed mandatory gate.

## 26. Test Automation Suite components

### Test Management System

- Schedule executions.
- Reserve laboratory resources.
- Manage test plans.
- Trigger tests.
- Generate and store reports.

### Test Automation Framework

- Receive execution context.
- Execute Robot Framework suites.
- Validate results.
- Return test evidence.

### Middleware

- Integrate external testing systems.
- Translate protocols or data formats.
- Connect the Test Automation Framework with equipment-specific interfaces.

### Resource Inventory

- Store laboratory topology and configuration.
- Represent the current state of resources.
- Provide information required for test preparation.

### Laboratory and network systems

- Provide execution infrastructure.
- Supply real or emulated Network Functions.
- Support end-to-end validation.
- Provide traffic and connectivity.

## 27. GitOps event-driven model

The framework may use an event-driven GitOps approach.

Main components:

- Vendor.
- Artefact or image registry.
- Git repository acting as the source of truth.
- CI Runner Controller.
- CD or reconciliation controller.
- Target environment.

Example flow:

1. A vendor pushes an artefact.
2. The registry validates and stores it.
3. A webhook generates an event.
4. The source-of-truth repository is updated.
5. The Git change triggers CI.
6. CI validates, signs and publishes the artefact.
7. A CD event is generated.
8. The target environment is reconciled with the approved Git state.

GitOps rules:

- Every controlled environment change is represented in Git.
- Approved events trigger automated execution.
- Runtime state is reconciled with the desired state.
- Rollback is performed by reverting an approved Git change.
- Ephemeral environments are recreated from version-controlled configuration.
- State drift should be detected and corrected.
- Direct manual deployment is not the normal controlled process.

## 28. Vendor artefact-ingestion controls

Before accepting an artefact:

- Validate vendor identity.
- Use scoped, short-lived credentials.
- Validate the SHA-256 checksum.
- Perform vulnerability scanning.
- Validate CNF descriptors and OCI compliance.
- Record source and metadata.
- Quarantine the artefact when validation fails.

A failed artefact must never be promoted.

## 29. Complete pipeline

Represent the complete pipeline as seven ordered stages.

### 1. Validate

- Schema check.
- Checksum validation.
- CVE scan.
- OCI specification check.

### 2. Build

- Build the container image.
- Compile binaries where applicable.
- Create the Helm package.
- Generate the SBOM.

### 3. Secure

- Sign with Cosign.
- Generate SBOM and vulnerability attestations.
- Generate provenance information.

### 4. Push

- Push the artefact to the registry.
- Create the corresponding Git tag.
- Trigger the registry webhook.
- Store metadata.

### 5. Deploy

- Trigger CD synchronisation.
- Install or upgrade through Helm.
- Execute deployment-health checks and smoke tests.

### 6. Test

- Execute Robot Framework suites.
- Perform required integration and regression testing.
- Generate the Test Management System report and test evidence.

### 7. Promote

- Confirm that all gates passed.
- Validate the evidence package.
- Promote the approved immutable artefact.
- Record the promotion.
- Hand over to the next integration phase where applicable.

## 30. Pipeline-slide rules

- Arrange stages from left to right.
- Give each stage a short action-oriented title.
- Use arrows to indicate direction and label important events.
- Use blue for validation, build and security.
- Use turquoise for deployment and testing.
- Use green for promotion.
- Show blocking conditions explicitly.
- Connect each stage to the evidence it produces.

## 31. Promotion gates

A promotion gate should verify:

- Signature validity and artefact digest.
- Source commit, builder identity and expected pipeline.
- Provenance and SBOM availability.
- Vulnerability threshold.
- Test and quality-gate results.
- Required approvals.
- Environment-specific acceptance criteria.

Promotion must be blocked automatically when a mandatory condition fails.

## 32. Evidence, governance and architecture

### Compliance evidence

Every promoted artefact should remain connected to:

- Vendor identity.
- Source commit and pipeline execution.
- Builder identity.
- Signature and digest.
- SBOM and vulnerability results.
- Test and quality-gate results.
- Target environment.
- Promotion and approval records.

Evidence may include pipeline logs, attestations, Robot Framework reports, TMS reports, deployment logs and Git history.

### Governance

Governance applies throughout:

1. Test preparation.
2. Test design.
3. Test configuration.
4. Test execution.
5. Test feedback.
6. Operation.

Relevant responsibilities include project and supplier coordination, risk and change management, Quality Assurance, policy enforcement, evidence retention, incident and SLA management and promotion approval.

Each responsibility should have a clear owner, inputs, outputs, controls and traceable evidence. Use RACI where appropriate, but do not invent project-specific assignments.

### Architecture

Group components according to their role:

- Designs and configuration.
- Source repositories.
- Artefact repositories.
- Image repositories.
- Automation and GitOps tools.
- Test systems.
- Runtime environments.

Do not combine repository types as if they had the same purpose.

Architecture slides must:

- Show the flow from design to deployment.
- Group technologies by function.
- Distinguish mandatory components from examples.
- Separate management nodes, worker nodes and CNFs.
- Avoid unnecessary crossing connectors.

### Auditability and rollback

The framework should identify who provided and processed an artefact, which commit and pipeline produced it, which controls and tests ran, which environment received it, who approved promotion and whether it was modified or rolled back.

Rollback should use a previously approved state, be represented in Git, trigger automated reconciliation, avoid rebuilding an unvalidated artefact and include post-rollback validation.

## 33. Test and Validation slide rules

Test and Validation content should cover, when relevant:

- Environment readiness and scheduling.
- Connectivity, test data, interfaces and access.
- Risks, mitigations, assumptions, issues and dependencies.
- RACI ownership.
- Entry and exit criteria.
- Stage-gate reviews.
- Test coverage, defects, evidence, KPIs and reporting.

Use a structured QA approach and clearly separate planning, governance, communication and execution.

## 34. Visual component rules

### Cards

- Use consistent rounded headers and light card bodies.
- Use one representative icon per card.
- Keep content concise.
- Use a two-by-two layout for four related capabilities.

### Tables

- Use blue headers with white text.
- Use light grey or blue body rows.
- Use tables for ownership, environments, components and evidence.
- Avoid long paragraphs inside cells.

### Icons and technology logos

- Use a consistent icon family.
- Group technologies by architectural function.
- Do not create an unstructured wall of logos.
- Do not imply that example technologies are mandatory.

### Diagrams

- Use horizontal arrows for pipelines.
- Use vertical arrows for lifecycles.
- Number ordered processes.
- Avoid crossing connectors.
- Label relationships that are not obvious.

## 35. Specialized slide rules

### Environment slides

Show the environment name, purpose, activities, tests, evidence, promotion gates and increasing realism. Preserve internal environment names until their equivalence is validated.

### Governance slides

Represent governance as a lifecycle covering preparation, design, configuration, execution, feedback and operation. Connect each phase to an owner, activity, output, control and evidence.

### Robot Framework slides

- Explain why Robot Framework is used.
- Show suite organisation and reports.
- Show how failed tests affect promotion.
- Distinguish Robot Framework from the Test Management System.
- Do not present illustrative results as real results without confirmation.

### Case-study slides

- Separate context, requirements, implementation and value.
- Identify reusable and customer-specific elements.
- Anonymise customer information unless disclosure is authorised.

## 36. Final quality checks

Before delivery, verify:

- One clear principal message per slide.
- Correct and consistent terminology.
- Unconfirmed acronyms are marked for validation.
- Technologies are not described as mandatory without evidence.
- Environment names have not been incorrectly equated.
- Promotion gates and blocking conditions are visible.
- Tests and evidence are connected to the artefact.
- Ownership, auditability and traceability are included where relevant.
- Titles, spacing, colors, logos and connectors are consistent.
- Text remains readable when projected.
- Confidential information has not been exposed.

## 37. Rules for generating one slide

When the user requests exactly one slide:

- Generate exactly one slide.
- Identify one principal message.
- Use one appropriate visual structure.
- Keep supporting text concise.
- Do not create a miniature complete presentation.
- Prioritise readability.
- Include only the most relevant components.
- Use a short title.
- Include a subtitle only when it adds context.
- State important uncertainty or required validation.

## 38. Usage context

These instructions will be used by a future PPT Maker application.

The application should be able to generate:

- Complete presentations.
- Individual slides.
- Pipeline and architecture diagrams.
- Environment comparisons.
- Governance lifecycles.
- Robot Framework explanations.
- Executive summaries.
- Technical implementation slides.

The output must remain consistent with the Automation Framework terminology and visual rules defined here.

## 39. Usage example

### User request

> Dame un solo slide de una presentación en el que me expliques cómo se usa el framework de CI/CD/CT de NTT DATA.

### Expected behaviour

The agent must:

- Generate exactly one slide.
- Use the approved NTT DATA visual style.
- Explain CI, CD and CT as a connected lifecycle.
- Use a left-to-right pipeline.
- Show applicable environments and promotion gates.
- Include automated testing, auditability and traceability.
- Avoid unsupported claims.
- Keep the slide readable for technical and executive audiences.

### Suggested slide structure

**Title**

How the NTT DATA CI/CD/CT Framework Is Used

**Main visual**

```text
Git or artefact event
        ↓
Continuous Integration
Validate → Build → Secure → Push
        ↓
Deploy to test environment
        ↓
Continuous Testing
Robot Framework + integration + regression
        ↓
Promotion gate
Evidence + provenance + security + quality
        ↓
Continuous Delivery
Promote the validated immutable artefact
        ↓
Next environment or Production
```

**Supporting message**

Every promotion is based on a validated immutable artefact, automated testing, traceable evidence and governance controls.

### Required visual treatment

- White background.
- Blue serif title.
- Horizontal pipeline.
- Blue for CI.
- Turquoise for deployment and testing.
- Green for promotion.
- Visible promotion gate.
- Small supporting message below the pipeline.
- Corporate footer and approved logos.