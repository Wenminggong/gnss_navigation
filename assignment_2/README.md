# PolyU AAE6102 Assignment 2 Report

## Task 1 - Differential GNSS Positioning

<table><tr><td bgcolor=LightGrey>
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


## Task 5 – GNSS Remote Sensing
