# Effective Code Review Comment Guidelines

Based on an analysis of multiple GitHub Pull Request reviews, this document summarizes key patterns and best practices for writing effective code review comments.

## General Principles

### 1. Comment Classification

* **Use clear prefixes to indicate severity:**
  + `trivial:` - Minor issues that should be fixed but don't block approval
  + `debatable:` or `extremely debatable:` - Suggestions open to discussion
  + `nit:` - Extremely minor stylistic preferences
  + `important:` - Issues that should be addressed before merging
  + `blocking:` - Critical issues that must be resolved

* **Be explicit about expectations:**
  + Distinguish between mandatory changes and optional suggestions
  + Indicate when comments are informational rather than requesting changes

### 2. Comment Structure

* **Be specific and actionable:**
  + Refer to specific lines or sections of code
  + Explain both what the issue is and why it matters
  + Provide concrete solutions when possible

* **Use GitHub suggestion blocks for direct code changes:**
  

```
  ```suggestion
  actual code change goes here
  ```

  

```

- **Group related issues together:**
  - Number multiple points for clarity
  - Address similar issues in a single comment when possible

- **Provide context:**
  - Link to relevant documentation, PRs, or issues
  - Reference cross-repository standards when applicable
  - Explain reasoning behind suggestions, not just what to change

### 3. Comment Scope

- **Focus on the right level of detail:**
  - For simple PRs: Brief approvals may be sufficient
  - For complex PRs: Detailed, organized feedback is necessary

- **Consider multiple aspects of code quality:**
  - Functional correctness
  - Error handling and edge cases
  - Performance implications
  - Security considerations
  - Consistency with existing patterns
  - Documentation and readability
  - Cross-platform compatibility
  - API design and usability

## Technical Focus Areas

### 1. Code Architecture and Design

- **API Usability:**
  - Consider the developer experience of using the API
  - Question potentially confusing or redundant API requirements
  - Think about cross-language compatibility

- **Error Handling:**
  - Verify proper cleanup in error cases
  - Ensure appropriate error propagation
  - Check for consistent error handling patterns
  - In C code, prefer unified error paths with consolidated cleanup

- **Consistency:**
  - Flag inconsistent naming conventions
  - Highlight deviations from established patterns
  - Ensure consistency across related repositories

### 2. Code Style and Readability

- **Prioritize clear organization:**
  - Suggest clearer code structure when logic is hard to follow
  - Flag complex conditionals that could be simplified
  - Recommend extracting complex logic into well-named helper functions

- **Comment on documentation:**
  - Ensure comments accurately describe behavior
  - Request documentation for parameters with specific usage requirements
  - Verify public API documentation clarity

- **Focus on maintainability:**
  - Consider how code might evolve in the future
  - Identify fragile patterns that could break with future changes
  - Suggest explicit guards against potential future bugs

### 3. Cross-Team and Ecosystem Considerations

- **Coordinate across teams:**
  - Flag changes that might affect other teams or services
  - Recommend cross-team communication when necessary

- **Verify ecosystem consistency:**
  - Check if behavior matches related SDKs or libraries
  - Confirm conformance to broader project standards

## Review Process

### 1. Reviewing Approach

- **Progressive reviews:**
  - Start with critical issues and architectural concerns
  - Follow up on remaining issues after major concerns are addressed
  - Provide final approval once all necessary changes are made

- **Approval comments:**
  - Use "fix & ship" for PRs with only minor issues
  - Include verification steps if needed before merging
  - Acknowledge when previous feedback has been addressed

### 2. Review Tone

- **Be direct but constructive:**
  - Focus on the code, not the person
  - Frame feedback as improvements rather than criticisms
  - Use a professional, collaborative tone

- **Acknowledge good work:**
  - Provide positive feedback on well-implemented features
  - Recognize when authors have addressed previous feedback well
  - Use phrases like "nice job" or "this looks good" where appropriate

- **Balance criticism with encouragement:**
  - Point out both strengths and areas for improvement
  - Recognize the effort that went into the implementation

## Comment Examples by Category

### Effective Trivial Comments

```

trivial: undoing needless changes to whitespace

```

```

trivial: it's weird to use the `_10MB` and then upload 5MB

```

```

trivial: I found this if-statement confusing, and the helper function that did different things depending on how it's called...

```

### Effective Technical Suggestions

```

if there's an error, we need to cleanup out_checksum

```

```

So, if users already added a checksum header, they ALSO need to set this enum?

```

```

Instead of the `on_error:` label sharing 90% the same cleanup code as `s_s3_client_finish_destroy_default()` , have them share code

```

### Effective Process Comments

```

I'd advise checking this branch from aws-crt-cpp, and making sure it all works nicely, before merging

```

```

Checked the C++ SDK and Java SDK and they also retry on TLS errors.

```

```

need to coordinate with python teams on this...
```

### Silent Approvals (When Appropriate)

Silent approvals (no comments, just approval) are appropriate for:
* Simple, straightforward changes
* Well-understood code
* Follow-up to previous discussions
* Self-explanatory code
* Trivial fixes
* When there's an established trust relationship between reviewer and author

## Special Cases

### 1. Automated/Routine Changes

* **Minimize comments for routine updates:**
  + For automated changes or version bumps, simple approvals may be sufficient
  + Focus comments on any unexpected deviations from expected patterns

### 2. Cross-Repository Changes

* **Consider broader impacts:**
  + For changes affecting multiple repositories, test across all affected codebases
  + Verify consistency with related repositories' standards

### 3. Documentation Changes

* **Focus on accuracy and clarity:**
  + Ensure documentation correctly describes behavior
  + Verify examples work as described
  + Check for consistent formatting and terminology

## Conclusion

Effective code review comments are specific, actionable, appropriately categorized, and delivered in a constructive tone. They focus on technical accuracy while maintaining readability and consistency with project standards. The level of detail should match the complexity of the change, ranging from brief approvals for simple changes to detailed, structured feedback for complex modifications.
