---
aliases: []
date created: Tuesday, 25. November 2025, 21:11
date modified: Monday, 8. December 2025, 18:12
---

# Image
**Term**: Image / Template ([VM](../Virtual%20Machine%20(VM).md) or [Container](../Virtualization%20methods/Container.md))

**Definition**: A preconfigured disk or filesystem snapshot used as a base to create new [VMs](../Virtual%20Machine%20(VM).md) or [containers](../Virtualization%20methods/Container.md) quickly and consistently.

**Context/Example**: A “Ubuntu server base image” used to spin up dozens of identical web-server [VMs](../Virtual%20Machine%20(VM).md), or a [Docker](https://en.wikipedia.org/wiki/Docker_(software)) image pushed to a registry for deployments.

**Related Concepts**:

---

## Immutable Image

**Term**: Immutable Image

**Definition**: An image that is not modified after deployment; if you need a change, you rebuild a new image instead of patching the running instance.

**Context/Example**: [Containers](../Virtualization%20methods/Container.md) are often treated as immutable: when you need a new version of the app, you build a new container image and redeploy, rather than SSH-ing in to edit things.

**Related Concepts**:
