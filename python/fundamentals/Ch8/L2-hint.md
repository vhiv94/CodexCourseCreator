# Hints — Use Polymorphism for Summaries

- Define one shared summary method name on the base class contract.
- Let each child class decide how to format its own summary.
- In the renderer, loop over items and call the same method on each.
- Avoid `if isinstance(...)` as your first approach.
