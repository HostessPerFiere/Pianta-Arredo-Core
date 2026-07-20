# Ports and Adapters

Document ID: DOC-014

Version: 0.1

Status: Draft

Owner: Spatial Intelligence Platform

## Purpose

Ports and Adapters isolate the domain and public Services from external
technology choices.

## Port

A Port is a contract required or exposed by the platform.

## Adapter

An Adapter connects a Port to a specific external technology.

## Examples

Persistence Port

↓

JSON Adapter

SQLite Adapter

PostgreSQL Adapter

Cloud Adapter

Geometry Port

↓

OpenCascade Adapter

custom Kernel Adapter

Export Port

↓

DXF Adapter

SVG Adapter

IFC Adapter

## Dependency direction

Domain Services depend on Ports.

Adapters depend on Ports.

Ports do not depend on Adapters.

## Core isolation

The Core must not directly depend on:

- file systems;
- databases;
- GitHub;
- ChatGPT;
- CAD products;
- cloud providers;
- messaging vendors.

## Adapter replacement

Replacing an Adapter should not require changing the public domain
contract.

## Testing

Ports should support test doubles and compliance suites.

## Configuration

Adapter selection belongs to the Application composition layer.
