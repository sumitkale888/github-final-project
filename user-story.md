---
name: User Story Template
about: Well-formatted template for user stories using Gherkin syntax
title: "[FEATURE] "
labels: ""
assignees: ""
---

## Feature Description

**Feature**: [feature]

**As a** [role]  
**I need** [function]  
**So that** [benefit]

## Details and Assumptions
- [document what you know]

## Acceptance Criteria
```gherkin
Given [some context]
When [certain action is taken]
Then [the outcome is observed]
```

## Example
```gherkin
Feature: Account service
  Scenario: Create an account
    Given the account service is running
    When I create an account
    Then the account is stored and returned
```
