# Create a Plugin

Version: 0.1

Status: Draft

## Purpose

Plugins extend the platform without placing specialised behaviour in
the generic Core.

## Suitable Plugin content

A Plugin may provide:

- Knowledge Packages;
- Capabilities;
- validators;
- Export Adapters;
- persistence Adapters;
- commands;
- Events;
- application components.

## Required manifest fields

A Plugin manifest should declare:

- identifier;
- name;
- version;
- compatible SIS version;
- required Capabilities;
- provided Capabilities;
- dependencies;
- permissions;
- entry points;
- license.

## Isolation rules

A Plugin must:

- use public contracts;
- avoid direct access to undocumented internal state;
- declare all required permissions;
- fail without corrupting the Project;
- report unsupported behaviour explicitly.

## Example lifecycle

Discovered

↓

Validated

↓

Loaded

↓

Activated

↓

Deactivated

↓

Unloaded

## Compatibility

A Plugin must state which contract and platform versions it supports.

Breaking Plugin API changes require migration guidance.

## Current status

The Plugin SDK is planned for Release 0.5.

This guide currently defines architectural expectations only.
