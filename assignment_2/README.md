# PolyU AAE6102 Assignment 2 Report

## Task 1 - Differential GNSS Positioning
The pros and cons of the four GNSS techniques for smartphone navigation are presented as follows:
<table><tr><td bgcolor=Black>
<!-- <div style="border:2px solid #ddd; padding:10px; border-radius:20px;"> -->
The integration of Global Navigation Satellite Systems (GNSS) into smartphones has revolutionized personal and commercial navigation. However, as user expectations for precision grow, developers face the challenge of balancing technological performance with practical constraints like cost, power efficiency, and scalability. This essay compares four advanced GNSS algorithms (DGNSS, RTK, PPP, and PPP-RTK) across technological, economic, and operational dimensions to assess their suitability for smartphone navigation.

* **Technological Performance: Accuracy vs. Practicality**:
At the core of GNSS evolution is the pursuit of centimeter-level accuracy. RTK excels here, leveraging carrier-phase measurements and dense base station networks to achieve real-time precision. However, its limited coverage and reliance on infrastructure make it impractical for global smartphone use. PPP, in contrast, offers worldwide coverage using precise satellite orbit data and advanced error modeling, but its 30-minute initialization time frustrates users expecting instant results. DGNSS strikes a middle ground with meter-level accuracy and simplicity, though its dependency on single-station corrections reduces reliability. PPP-RTK merges PPP’s global reach with RTK’s real-time corrections, promising high accuracy without dense infrastructure. Yet, its algorithmic complexity and processing demands remain barriers for resource-constrained devices.

* **Infrastructure and Manufacturing Costs**:
Cost considerations are pivotal for mass-market devices. RTK’s reliance on dense reference stations drives up infrastructure expenses, while its hardware requirements (e.g., high-quality antennas) inflate smartphone manufacturing costs. DGNSS, with its mature technology and minimal infrastructure needs, is cost-effective but increasingly outdated. PPP reduces infrastructure dependency by utilizing global satellite data, lowering deployment costs, though high-precision clock and orbit data licensing may add expenses. PPP-RTK balances infrastructure needs but requires sophisticated software integration, potentially raising R&D costs. For smartphones, PPP and PPP-RTK offer scalable solutions if cloud-based correction services mitigate onboard processing needs.

* **Computational and Power Efficiency**:
Smartphones demand energy-efficient solutions. RTK’s continuous data processing significantly drains batteries, making it unsuitable for mobile devices. PPP’s lengthy initialization consumes power over extended periods, though once converged, its demands stabilize. DGNSS, with straightforward algorithms, imposes minimal computational load, preserving battery life. PPP-RTK’s hybrid approach risks higher power consumption due to real-time corrections and complex computations. Innovations in chipset efficiency and edge computing could alleviate these issues, but current hardware limitations favor DGNSS and PPP for energy-conscious designs.

* **Economic Viability and Market Readiness**:
Market adoption hinges on maturity and scalability. DGNSS is widely deployed but lags in accuracy, limiting its appeal for next-gen applications. RTK thrives in niche markets (e.g., surveying) but faces scalability challenges in consumer electronics due to high costs. PPP gains traction in high-end devices, aided by improving cloud-correction services that reduce initialization times. PPP-RTK, though promising, remains experimental, requiring industry collaboration to standardize correction formats and optimize algorithms. For smartphones, PPP’s incremental advancements offer a pragmatic path, while PPP-RTK represents a future-ready solution pending technological maturation.

No single algorithm perfectly satisfies all smartphone constraints, but a tiered approach could optimize user experience. For mainstream applications, PPP’s global coverage and moderate accuracy, coupled with cloud-assisted initialization, present a viable upgrade from DGNSS. Premium devices might adopt PPP-RTK as processing power improves, offering high accuracy without prohibitive infrastructure. Meanwhile, RTK remains confined to specialized use cases due to cost and power barriers. Manufacturers must prioritize energy efficiency, cost scalability, and user-centric design, ensuring that technological advancements align with practical realities. As GNSS evolves, the synergy between algorithmic innovation and hardware optimization will define the next era of smartphone navigation—where precision meets practicality.
</td></tr></table>
<!-- </div> -->

```
* GenAI model: DeepSeek R1.
* Prompt: "To improve the positioning accuracy of GNSS, several advanced algorithms have been developed. The core concepts and characteristics of these algorithms are presented below:

DGNSS (Differential GNSS)
1.1 Principle: Difference measurements from the same satellite between the receiver and a nearby base station. The base station transmits Pseudorange Corrections (PRC) to the receiver.
1.2 Advantages: Simple mathematical model; straightforward structure and algorithm; well-established technology.
1.3 Limitations: Only receives corrections from one reference station, reducing system reliability; restricted coverage area; meter-level accuracy.

RTK (Real-Time Kinematic)
2.1 Principle: Difference measurements between the base station and the receiver, and between different satellites in the same receiver.
2.2 Advantages: Centimeter-level accuracy.
2.3 Limitations: Limited service area; expensive implementation; operational constraints; requires dense reference station network; continuous data processing increases power consumption significantly compared to standard GNSS.

PPP (Precise Point Positioning)
3.1 Principle: Utilizes high-precision satellite orbit data, improved error modeling, and carrier-phase measurements to enhance positioning accuracy.
3.2 Advantages: Worldwide coverage; lower infrastructure requirements than RTK; better accuracy than DGNSS.
3.3 Limitations: Long initialization period (approximately 30 minutes); moderately lower accuracy and reliability compared to RTK; greater computational requirements; more complex algorithm.

PPP-RTK (Precise Point Positioning Real-Time Kinematic)
4.1 Principle: Combines the strengths of both RTK and PPP approaches.
4.2 Advantages: Provides real-time positioning across wide areas with high accuracy and reliability.
4.3 Limitations: Increased system complexity; demands greater processing capability.

When evaluating these GNSS algorithms for smartphone navigation applications, we must compare their benefits and drawbacks. The comparison should be summarized in an essay of approximately 700 words. Importantly, our comparison should adopt a multidimensional approach: not just examining the technological aspects, but also evaluating key product development considerations such as manufacturing costs, computational efficiency, power consumption, and economic viability. Now help me generate the essay:"
* Comments: DeepSeek R1 has strong reasoning capability and is free. 
```


## Task 2 – GNSS in Urban Areas


## Task 3 – GPS RAIM (Receiver Autonomous Integrity Monitoring)


## Task 4 – LEO Satellites for Navigation
The difficulties and challenges of using LEO communication satellites for GNSS navigation are discussed as below:
<table><tr><td bgcolor=Black>
The integration of Low Earth Orbit (LEO) satellites into Global Navigation Satellite Systems (GNSS) promises to address longstanding limitations of traditional medium-to-high Earth orbit constellations, such as weak signal strength and susceptibility to interference. However, leveraging LEO communication satellites for navigation (mainly through dedicated constellations, hybrid payloads, real-time orbit updates, or opportunistic signal use) introduces multifaceted technical and operational challenges. These hurdles must be carefully navigated to realize LEO’s potential as a GNSS enhancer.

* **Dedicated LEO Navigation Constellations: Scalability and Sustainability:**
Developing LEO-based navigation constellations presents significant technical barriers. Unlike traditional GNSS satellites, which provide wide coverage from high altitudes, LEO satellites operate closer to Earth (500–1,500 km), necessitating a larger constellation to ensure global coverage. For instance, while GPS requires 24 satellites, a LEO system might demand hundreds to maintain continuous visibility, dramatically increasing deployment and maintenance costs. Additionally, LEO satellites experience rapid orbital decay due to atmospheric drag, shortening their operational lifespan and requiring frequent replacements. This raises sustainability concerns, as frequent launches exacerbate space debris proliferation, demanding rigorous collision-avoidance systems. Operationally, coordinating a dedicated LEO constellation with existing GNSS infrastructure poses challenges. Spectrum allocation conflicts could arise, as LEO signals might interfere with legacy GNSS or communication bands. Regulatory frameworks, which vary globally, would need harmonization to avoid geopolitical disputes over orbital slots and frequency rights. Furthermore, the fast-moving nature of LEO satellites complicates ground station operations, necessitating dynamic tracking and handover mechanisms to maintain seamless user connectivity.

* **Integration of Navigation Payloads into LEO Communication Satellites: Design Compromises:**
Adding navigation capabilities to existing LEO communication satellites, such as Starlink or OneWeb, introduces technical trade-offs. Communication satellites prioritize high-throughput data transmission, leaving limited power, weight, and space for navigation payloads. Designing dual-purpose signals that serve both communication and positioning requires precise synchronization and signal integrity, as even minor phase errors could degrade navigation accuracy. Moreover, the signals must resist interference between communication and navigation functions, complicating waveform design. From an operational standpoint, satellite operators may prioritize their primary mission (e.g., broadband internet) over navigation performance. Navigation payloads could divert resources from core services, creating economic disincentives for operators. Additionally, the lack of standardization across LEO constellations complicates interoperability. For example, signals from different providers might use incompatible modulation schemes, forcing receivers to support multiple protocols and increasing complexity for end-users.

* **Real-Time Orbit Tracking and Updates: Infrastructure Demands:**
Using LEO satellites to enhance traditional GNSS through real-time orbit corrections requires ultra-precise tracking of both LEO and GNSS satellites. Technically, the rapid orbital motion of LEO satellites demands frequent positional updates, necessitating a dense global network of ground stations or inter-satellite laser links to ensure continuous monitoring. Processing this data in real time to generate GNSS corrections imposes immense computational burdens, requiring advanced algorithms and edge-computing infrastructure. Operationally, establishing such a system hinges on collaboration between GNSS operators and LEO satellite providers. Existing GNSS ground networks, optimized for high-altitude satellites, may lack the agility to track LEO trajectories. Furthermore, data-sharing agreements and cybersecurity protocols must be established to protect against vulnerabilities in real-time data streams. Without international cooperation, fragmentation in correction services could undermine the universality of GNSS enhancements.

* **Opportunistic Positioning: Signal Limitations and Legal Barriers:**
Extracting navigation observables from existing LEO communication signals (e.g., Doppler shifts from Starlink) faces inherent technical limitations. Communication signals lack the precise timing and structure required for navigation, making pseudorange measurements error-prone. While machine learning techniques could reverse-engineer positioning data from signal characteristics, this approach remains experimental and computationally intensive. Additionally, the dynamic LEO environment causes rapid signal availability changes, leading to positioning gaps in urban canyons or polar regions. Operationally, opportunistic use of LEO signals raises legal and ethical questions. Communication satellites transmit proprietary signals, and repurposing them for navigation without operator consent could violate intellectual property or licensing agreements. Regulatory bodies like the International Telecommunication Union (ITU) have not yet defined standards for dual-use signals, creating uncertainty. Moreover, reliance on third-party satellites introduces risks: operators could alter signal structures or prioritization, destabilizing navigation services.

* **Broader Challenges: Cybersecurity and Regulatory Uncertainty:**
Beyond method-specific issues, systemic challenges persist. The stronger LEO signals, while resistant to jamming, could become attractive targets for spoofing attacks, where malicious actors broadcast false signals to mislead receivers. Securing LEO-augmented GNSS demands robust encryption and authentication protocols, which are not universally implemented. Additionally, the regulatory landscape for LEO remains fragmented. Questions about liability for navigation failures, orbital debris mitigation, and spectrum rights remain unresolved, deterring investment.

While LEO satellites offer transformative potential for GNSS, their integration is far from straightforward. Each enhancement approach faces unique technical and operational hurdles. These range from hardware limitations and orbital dynamics to regulatory gaps and economic viability. Success will depend on interdisciplinary collaboration among engineers, policymakers, and industry stakeholders to standardize protocols, secure funding, and prioritize sustainability. Only then can LEO satellites evolve from a promising concept into a reliable pillar of global navigation.
</td></tr></table>

```
* GenAI model: DeepSeek R1.
* Prompt: "Traditional GNSS constellations operate in middle to high Earth orbits. This characteristic introduces several challenges for positioning and navigation, such as:
1. Satellite visibility: In urban areas or at high latitudes, receivers may experience inaccurate positioning or lose satellite lock.
2. Interference susceptibility: Long signal propagation paths increase vulnerability to disruptions from space weather, radiation belts, and atmospheric conditions.
3. Jamming susceptibility: GNSS signals weaken significantly by the time they reach receivers, making them relatively easy to jam.
4. Precise positioning: Orbital perturbations, space weather, and other factors introduce uncertainty in a satellite’s true position, degrading receiver accuracy.

In contrast, Low Earth Orbit (LEO) satellites are much closer to Earth than traditional GNSS satellites. Consequently, their signals experience less interference and attenuation, resulting in stronger and cleaner reception. This advantage positions LEO satellites as a potential enhancer of traditional GNSS performance. Generally, LEO can improve GNSS in several ways:
1. Developing dedicated LEO navigation constellations;
2. Integrating positioning payloads into existing LEO communication constellations;
3. Enhancing traditional GNSS by using LEO satellites for real-time orbit tracking and updates;
4. Leveraging opportunistic positioning by extracting navigation observables (e.g., Doppler shift, pseudorange, and carrier phase) from current LEO signals.

However, using LEO satellites for GNSS navigation also presents significant challenges. Write a short essay (about 700 words) to discuss the difficulties and challenges of using LEO communication satellites for GNSS navigation. As outlined above, LEO satellites can enhance GNSS in multiple ways, but each approach may face distinct challenges. Notably, these challenges can be examined from both technical and operational perspectives. Now help me generate the essay:"
* Comments: DeepSeek R1 has strong reasoning capability and is free. It is better to provide detailed backgrounds and instructions.
```

## Task 5 – GNSS Remote Sensing
