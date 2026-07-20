# Knowledge Service

Document ID: DOC-008

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

The Knowledge Service provides versioned, traceable and queryable
domain knowledge to other Services.

## Knowledge examples

- residential planning rules;
- office planning rules;
- furniture dimensions;
- circulation guidance;
- accessibility criteria;
- domain taxonomies;
- export mappings;
- local project conventions.

## Knowledge Packages

Knowledge is grouped into Packages.

A Package contains:

- package identifier;
- version;
- jurisdiction or scope;
- source references;
- effective dates;
- rules;
- assumptions;
- limitations;
- compatibility information.

## Public operations

Example Capabilities:

- ResolveRule
- ListApplicableRules
- ResolveDefault
- ResolveClassification
- ExplainRule
- CompareKnowledgeVersions

## No hardcoded rules

Domain rules should not be embedded directly in unrelated Service code.

## Traceability

Every applied rule should be traceable to:

- Package;
- version;
- source;
- rule identifier;
- effective context.

## Conflicts

When multiple rules conflict, the Service must return an explicit
conflict result rather than silently selecting one.

## Legal and standards material

The repository must not reproduce proprietary standards without
permission.

Knowledge Packages may reference external sources and store original
project interpretations where legally permitted.

## AI use

AI may assist with rule interpretation, but AI-generated conclusions
remain provisional until verified against an authoritative source.
