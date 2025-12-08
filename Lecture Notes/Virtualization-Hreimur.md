#### Key Ideas
Abstract physical resources allowing them to shared or replicated in software <br>
Like a big apartment building (physical server) and individual apartments (virtual machines) each got their own stuff going on but share the same underlying structure <br>
#### Purpose
- Resource Util: maximize the usage of expensive hardware
- Cost Saving: Reduces power usage, cooling, data center space and hardware purchases
- Flexibility: just start up a new vm instead of deploying new physical hardware
- Isolation and Security: VMs are isolated from each other preventing issues in one affecting the rest
- Business continuity and disaster recovery: Easier to backup, replicate and restore systems <br>
#### Comon Uses
- Running dozens of virtual server on a single pyhsical server
- Quickly spinning upp VMs for testing software without affecting production systems
- Foundation for services like AWS EC2, Azure VMs and Google Cloud compute engine
- Virtual desktop for users, allowing access from anywhere
- Replicating and restoring entire virtualized environments
- Runnig older OS or apps that require specific hardware/environments
- Safely run untrusted apps or browsing the web in an isolated environment <br>
#### Terms
- Host/OS: The physicial computer
- Guest: the software based computer that runs on the host, has its own virtual hardware
- Hypervisor: The software that creates, runs and manages the virtual machine, acts as a mediator between host and guest <br>
#### Types of hypervisors
- Type 1: runs directly on the host hardware without underlying OS, 
    - Pros: High performance, greater security and enterprise grade
    - Examples like VMware ESXi, Microsoft Hyper-v and KVM
- Type 2: Runs as an application on top of the host OS
    - Pros: Easy setup, good for desktop development/testing
    - Example: Virtualbox, VMware
#### Virtualization Methods
- Full Virtualization: Fully simulates hardware, guet OS runs unmodified
    - How it works: Hypervisor fully simulates all hardware for the guest OS. The guest runs unmodified beliving it has direcet access to hardware
    - Hardware assisted: Moderns CPUs include features that offload much of the virtualization burden from the hypervisor = improved performance
    - Pros: Guest OS runs undmodified = high compatibility, Strong isolation as the vms are highly isolated from eachother and host, Can run different OS families and near native performance with hardware assistance
    - Cons: Higher overhead without hardware assistance, can be resource intensive compared to lighter methods and requires CPU support for hardware-assisted features for optimal speed
- Paravirtualization: Guest OS is modified and aware its virtualized and communicates directly with hypervisor
    - How it works: Guest OS is modified to be aware its running in a virtual environment, it makes special hypercalls instead of talking directly to hardware
    - Key Idea: OS and hypervisor cooperate to achive better performance
    - Pros: lower overhead and better performance than pure full virtualization (without hardware assistance) and more efficient use of resources.
    - Cons: Requires modification or special drivers for the guest kernel, reducing compatibility. Can be more complex to setup because of mods to the guest OS
    - Less common as a primary method since hardware assistance is popping off
- Hardware assisted: Uses special CPU instructuions to accelerate virtulaization
- OS-Level Virtualization: Shares the host OS kernel but isolates apps in "containers"
    - How it works: Containers share the host OS kernel, each container has its own isolated user space, process, file system and network interface
    - Key Idea: Focuses on isolateing apps and their dependencies not enitre OS's
    - Pros: Extremely lightweight and fast startups, Very efficient resource wise, Highly portable (Build once, run anywhere) on compatible OS, good for microservices and continuous integration/delivery
    - Cons: Less isolation than VMs: shared kernel is a single point of vulnerability/failure. All containers must ron on the same host OS kernel
- Emulation: Simulates an entire hardware platform often for different cpu architectures
    - How it works: Completly simulate the hardware and instruction set of a different system, The gues code is translated on the fly to run on the host native architecture
    - Key Idea: allows for software designed for one type of hardware to run on entirely different hardware
    - Pros: Runs software for incompatible hardware architectures, the guest software need no mods and useful for running legacy software or retro games.
    - Cons: Very high performance overhead, signifanctly slower then virtualization due to constant intsruction translation. Highly resource intensive, Primarly used when virtualization is not an optiopn due to fundamental architectural diffrences
    - Not typically used for general purpose server consolidation ro cloud infrastructure because of performance

#### Security
Virtualization abstracts physical hardware but introduces new attack vectors, since multiple VMs share a single host a security breach can have a wider impact than on isolated physical machines.
#### Common Security Challanges
- VM/Container Escape: Breaking out of a guest to compromise the host, the "holy grail" for attackers
- Hypervisor Vulnerabilites: Flaws in the core software that can affect all guests, critical single point of failure
- Resource Exhaustion: one guest consuming excessive host resources starving the rest of the guests
- Management plane security: Compromise of virtualization management tools gives full control
- Insecure Images: deploying guests with known vulnerabilities or misconfigurations

#### Security by method: Fullt virtualization
Architecture: Hypervisor runs directly on hardware, guests are fully isolated with virtual hardware. Key Risks: Hypervisor vulnerabilties and VM escape
- Pros: Strong isolation: Hardware level separation between VMs. Small attack surface: hypervisor is purpose built lean?? and independant guest OSes
- Cons: Hypervisor bugs impact all VMs. Management tools are high value targets
#### Security by method: Hosted
Architecture: Hypervisor runs as an application on a host OS.
Key risks: host OS vulnerabilties, VM escape and hypervisor app flaws
- Pros: good isolation between VMs, leverage host OS security tools
- Cons: Larger attack surface: host os + hypervisor app. Host OS vulnerabilties impact guests and weaker overall isolation
#### Security by method: OS-Level virtualization
Architecture: Containers share the host OS kernel
Key risks: Shared kernel vulnerabilities, container escape, insecure images, orchestration flaws.
- Pros: Smaller per container attack surface and rapid pathcing/deployment of immutable images
- Cons: Weaker isolation: Shared kernel is a single point of failure, Kernel explots affects all containers and high reliance on secure images.
#### Security by method: Emulation
Architecture: Simulate entire hardware/instruction set
Key risks: Emulator software vulnerabilties and high performance overhead.
- Pros: Strong isolation from host due to full translation
- Cons: Net designed for secure, multi tenant production. High performance overhead and vulnerabilties in emulator can be exploited by guests
#### Most Secure?
- Physical hardware: ultimate isolation but inefficient
- Full Virtualization (Type 1): highest isolation among other virtualization methods, best for mutly tenancy and cloud providers, minimal hypervisor attack surface
- Full Virtualization (Type 2): Less secure due to reliance on underlying host OS and larger attack surface
- OS-Level (containers): Least isolation compared to other virtualization methods. Shared kernel is a critical security trade off for efficiency and require strong host OS security, image hygiene and orchestration controls
- Emulation: Niche use, not typically for general infrastructure security
#### Mitigating Security Risks
- Patch manangement: Keep hypervisors, hosts, guests and containers up to date
- Secure Configs: Apply principle of least privilege, disable unused ports and features and enforce strong access control
- Network segmentations: Isolate management networks, guest networks and host networks
- Secure image/Template management: Scan for vulnerabilties use trusted sources
- Monitoring and logging: Detect unusal activity, VM escapes or resource abuse
- Guest hardening: apply security best practices withing each VM
- Hypervisor/Host hardening: follow vendor guidelines, remove unnecesarry software

