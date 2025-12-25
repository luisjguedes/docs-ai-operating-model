# ADR-0001: Use GitHub Pages with a custom workflow

## Status
Accepted

## Context
We want a documentation site that:
- is easy to publish
- is reviewable via pull requests
- supports automated quality gates

## Decision
Use **GitHub Pages** with a custom GitHub Actions workflow:
- build MkDocs into a static site
- upload as a Pages artifact
- deploy with `actions/deploy-pages`

## Consequences
- Requires Pages to be configured with **Source = GitHub Actions**
- CI must set permissions for Pages deployment (OIDC + pages write)

