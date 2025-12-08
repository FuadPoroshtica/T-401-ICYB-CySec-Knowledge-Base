---
aliases: [Containers]
date created: Tuesday, 25. November 2025, 22:11
date modified: Monday, 8. December 2025, 19:12
---

# Container

**Term**: Container

**Definition**: An isolated environment that bundles an application and its dependencies, running on a shared OS kernel but separated from other containers.

**Context/Example**: A web app packaged as a Docker container that you can run on any Linux machine with Docker installed, without worrying about library versions.

**Related Concepts**: OS-level virtualization, [image](../Virtualization%20Hardening%20&%20Operations/Image.md), [orchestration](../Virtualization%20Hardening%20&%20Operations/Orchestration.md)

---

## User Space vs Kernel Space

**Term**: User Space vs Kernel Space (in a container context)

**Definition**: Kernel space is where the core OS code runs with high privileges; user space is where normal applications run with restricted privileges.

**Context/Example**: Containers isolate user space (processes, files) but share the same kernel; a kernel bug can break isolation across all containers.

**Related Concepts**: System calls, privilege separation, [containers](Container.md), kernel exploit.
