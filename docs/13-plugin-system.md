# Plugin System

Document ID: DOC-013

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

The Plugin System allows the platform to support domain-specific or
implementation-specific extensions without placing them in the Core.

## Example Plugins

- Residential Plugin
- Office Plugin
- Retail Plugin
- Healthcare Plugin
- Accessibility Plugin
- Export Plugin
- Geometry Plugin

## Plugin contents

A Plugin may provide:

- Capabilities;
- Knowledge Packages;
- Validators;
- Adapters;
- application components;
- commands;
- Events;
- schemas.

## Plugin manifest

Every Plugin should declare:

- identifier;
- version;
- compatible SIS version;
- required Capabilities;
- provided Capabilities;
- permissions;
- entry points;
- dependencies;
- license.

## Isolation

Plugins must not directly modify internal state outside published
contracts.

## Security

Plugin permissions should follow least privilege.

## Compatibility

A Plugin must declare which platform and contract versions it supports.

## Failure handling

Plugin failure must not silently corrupt the project model.

## Core rule

Generic concepts belong in the Core.

Domain specialisation belongs in Plugins or Packages.
