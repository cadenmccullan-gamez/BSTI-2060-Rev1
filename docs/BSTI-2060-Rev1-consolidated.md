# Technical Specification
## Biometric Support and Telemetry Interface (BSTI-2060-Rev.1)

**Document status:** Consolidated engineering draft for human review

**Authors:** Alexis M Adams; Nicholas Michael Grossi

**System designation:** BSTI-2060-Rev.1

> This document converts the supplied concept parameters into testable system requirements. It is not a regulatory approval, clinical-use authorization, sterilization validation, or substitute for review by qualified biomedical, materials, safety, and systems engineers.

## 1. Purpose and scope

BSTI-2060-Rev.1 is a dual-node wearable system intended to provide epidermal protection, thermal regulation, and dual-rate vital-sign telemetry between a human-worn node and an artificial-intelligence monitoring node. The design is specified for varied surface traversal under the stated 2060 survival constraints. The present revision covers the body-contact interface, microfiber suit, sensing electronics, telemetry, cybersecurity controls, power architecture, fail-safe behavior, and verification requirements.

The term **skin-contact interface layer** is used in this revision instead of “bio-organic interstitial fluid layer.” The latter term ordinarily suggests fluid located within tissue. If a microinvasive or transdermal interface is intended, the design requires a separate biological-interface specification, clinical risk assessment, and materially different validation program.

The system shall not use unverified “local precursors” in contact with human skin. Any precursor-derived formulation shall be chemically characterized, purified, manufactured under controlled conditions, and evaluated in its final finished form. FDA guidance on ISO 10993-1 emphasizes risk-based biological evaluation, final-form testing, chemical assessment, degradation assessment, and special consideration for nanotechnology components and skin-contact devices [1].

## 2. System architecture

The system shall consist of two logical nodes: the **Human Interface Node (HIN)**, which contains the suit, skin-contact interface, sensors, local processing, power subsystem, and communications hardware; and the **Artificial Intelligence Monitoring Node (AIMN)**, which receives authenticated data, records system state, performs monitoring functions, and communicates status or alerts to an authorized human operator.

The AIMN shall be treated as a monitoring and decision-support component. It shall not be the sole control maintaining human physiological safety. The HIN shall maintain local sensing, local fault detection, local safe-state behavior, and sufficient local data buffering to preserve operation during communications loss.

| Subsystem | Primary function | Required boundary |
|---|---|---|
| Skin-contact interface | Provide conformal coupling, thermal transfer, and sensor contact | Must not migrate, weep, abrade skin, or introduce uncharacterized substances |
| Microfiber suit | Mechanical protection, thermal management, and sensor distribution | Must retain essential performance after environmental and flex-cycle testing |
| HIN electronics | Acquire, timestamp, filter, classify, buffer, and transmit data | Must continue local safety monitoring during link loss |
| Telemetry link | Convey authenticated measurements and status | Must detect corruption, replay, loss, delay, and stale data |
| AIMN | Receive, validate, store, display, and analyze telemetry | Must declare uncertainty and stale-data state rather than silently extrapolate |
| Isolation function | Place degraded channels into a defined safe state | Must be local, deterministic, auditable, and recoverable only under defined conditions |

## 3. Skin-contact interface layer

### 3.1 Composition and biological controls

The baseline formulation may contain an isotonic aqueous phase, a defined amino-acid or compatible osmolyte complex, lipid stabilizers, and a biocompatible gelling system. Each ingredient, impurity profile, degradation product, extractable, and leachable shall be identified before human-contact testing. “Derived from available local precursors” shall not be an acceptance criterion by itself.

The formulation shall be evaluated as a finished interface article for cytotoxicity, irritation, sensitization, and any additional endpoints identified by a documented ISO 10993-1 risk assessment. Testing shall account for the intended contact duration, surface area, temperature, mechanical loading, sterilization or bioburden-control method, and possible degradation products [1].

### 3.2 Physical requirements

| Parameter | Baseline target | Testable requirement |
|---|---:|---|
| Apparent pH | 7.35–7.45 | Measured at the defined test temperature using a calibrated method; acceptance limits shall include measurement uncertainty and stability over the deployment interval |
| Viscosity | 50–100 cP | Reported with temperature, spindle or rheometer geometry, and shear rate; the requirement applies to a thin film and shall be supplemented by a migration/weep test |
| Film function | Thin interfacial layer | No visible migration beyond the defined boundary, no leakage under the specified shear and compression profile, and no loss of sensor coupling beyond the system limit |
| Deployment duration | Maximum 72 hours | Application shall be removed, flushed or otherwise remediated, inspected, and replaced before the limit; the limit shall be shortened if stability or skin-contact results require it |
| Sterility or bioburden status | To be selected by contact-risk assessment | Do not assume SAL ≤10^-6 is universally required. The selected sterility claim, SAL, sterilization method, packaging, and release criteria shall be justified for the actual contact category and validated using applicable sterilization standards. |
| Osmolality and ionic strength | Isotonic target | Define numerical acceptance ranges and test at release and end-of-life; “isotonic” alone is insufficient |
| Stability | 72-hour minimum | Demonstrate pH, viscosity, composition, coupling, and microbial-control performance at beginning, midpoint, and end of deployment |

A 72-hour maximum is a design constraint, not evidence of safe use. The final duration shall be established through chemical stability, microbial-control, skin-compatibility, mechanical, and human-factors evaluation.

### 3.3 Interface safety

The interface shall include a containment geometry or barrier that prevents fluid contact with electronics except where such contact is explicitly part of the sensor design. The HIN shall detect loss of coupling, excessive drying, abnormal impedance, leakage, and local temperature outside the defined range. The HIN shall enter a local degraded-interface state when a condition could compromise measurement validity or skin safety.

## 4. Microfiber suit

The suit shall use a woven synthetic-polymer microfiber composite reinforced with carbon nanotubes or an equivalent controlled reinforcement architecture. The material specification shall identify polymer chemistry, CNT type and loading, yarn construction, weave, coating, orientation, areal density, thickness, electrical behavior, and manufacturing tolerances. The supplier shall control CNT release or shedding under abrasion, flexing, washing or cleaning, and thermal cycling.

| Parameter | Supplied baseline | Revised requirement |
|---|---:|---|
| Tensile strength | 300 MPa | 300 MPa minimum or declared directional value for the finished woven composite, with warp, weft, seam, and conditioned-state results reported separately |
| Thermal conductivity | 0.05–0.40 W/m·K | Specify direction, temperature, moisture condition, and test method. A range alone does not demonstrate active modulation. The design shall define the actuator, control range, response time, and maximum skin-contact temperature. |
| Sensor spacing | 10 cm over major muscle groups and core torso | Maintain nominal 10 cm spacing with documented placement tolerance, anatomical coverage map, and calibration procedure. Spacing may be locally adjusted where signal quality or anatomy requires it. |
| Mechanical durability | Not supplied | Define minimum flex, stretch, seam, abrasion, compression, and environmental cycles before loss of essential performance. |
| Electrical isolation | Not supplied | Demonstrate patient-contact electrical safety, leakage-current limits, insulation, and single-fault behavior under the applicable medical-electrical-equipment classification. |

The material shall be tested in finished-suit form because woven geometry, seams, coatings, moisture, and bending can materially change performance relative to coupon data. CNT-specific handling and exposure controls shall be included in the manufacturing and maintenance plan.

## 5. Sensors and acquisition

The HIN shall acquire thermal and hydration indices at a continuous nominal rate of 10 Hz. These indices shall be labeled as indirect or derived measurements unless the sensing method has been validated against a defined reference method for the intended environment.

The HIN shall acquire cardiac or ECG channels at a continuous nominal rate of 250 Hz as the minimum baseline for the stated HRV use case. A published study found 250 Hz acceptable for HRV analysis under its tested conditions [2]. This baseline shall not be interpreted as automatically sufficient for every diagnostic morphology, ST-segment, QT, or high-fidelity waveform use case. The final ECG requirement shall define electrode configuration, analog bandwidth, anti-alias filtering, ADC resolution, amplitude accuracy, timing accuracy, motion-artifact performance, missing-sample behavior, and intended clinical or nonclinical use.

Each measurement record shall include a synchronized timestamp, channel identifier, units, calibration state, quality indicator, sequence number, acquisition status, and source-node identifier. Sensor-quality flags shall distinguish valid, degraded, unavailable, stale, and safety-isolated data.

## 6. Power architecture

The primary power source shall be a solid-state micro-battery array sized for continuous base load, peak acquisition and transmission load, thermal-control load, startup transients, aging, temperature derating, and reserve energy. The design shall include an independent estimate of remaining usable energy and shall generate an early low-energy state before loss of essential monitoring.

Body-worn kinetic energy harvesters shall be supplemental only. The 1–3 mW generation target shall be verified over defined movement profiles and shall not be credited as the sole source of continuous operation. The power budget shall include a no-motion case, because the harvester output may be negligible during rest or constrained movement.

The battery, charging path, and harvesters shall be evaluated for thermal runaway, overcharge, short circuit, mechanical damage, electromagnetic compatibility, and single-fault behavior. The safety case shall identify the energy state at which the HIN isolates nonessential functions while preserving local safety monitoring.

## 7. Telemetry and data integrity

The telemetry design shall use decoupled measurement streams. Thermal and hydration indices shall be transmitted or made available at 10 Hz continuous nominal rate. Cardiac or ECG data shall be transmitted at a rate sufficient to preserve the validated acquisition stream; if bandwidth constraints require compression, the compression method shall be lossless for waveform data unless a separate validation demonstrates acceptable error for the intended use.

The protocol shall provide authenticated integrity protection rather than an unspecified “cryptographic checksum.” Each message or framed block shall include a cryptographic message authentication code or authenticated-encryption tag, protocol version, source identity, sequence number, timestamp, payload length, quality state, and anti-replay information. Keys shall be provisioned, rotated, revoked, and recovered under documented lifecycle controls. Corrupt, unauthenticated, duplicated, replayed, reordered, or excessively delayed data shall be rejected or marked invalid.

The HIN shall retain a bounded local buffer covering the defined communications-outage interval. The AIMN shall not silently interpolate or extrapolate safety-relevant data. It shall show link loss, stale data, sensor degradation, and authentication failure as distinct states.

ISO/IEEE 11073 is a candidate interoperability framework for standardized medical-device nomenclature and device communication [3]. Wireless medical telemetry shall also be assessed for radio coexistence, spectrum use, electromagnetic compatibility, antenna placement, link budget, and local regulatory constraints; FDA describes wireless medical telemetry as RF transmission used to monitor vital signs [4].

## 8. Fail-safe and isolation behavior

The phrase “non-destruction parameter” shall be replaced by a defined **essential-safety limit set**. The limit set shall contain measurable thresholds for human-contact temperature, electrical exposure, interface leakage, battery and thermal state, sensor validity, mechanical integrity, and communications integrity. The AIMN shall have a separate limit set for its own computing, storage, power, thermal, and data-integrity states.

The HIN shall contain a local isolation function that can disable the affected telemetry, thermal-control, charging, or auxiliary subsystem without waiting for the AIMN. Isolation shall be deterministic and shall not depend on an unverified incoming command. The isolation event shall preserve a tamper-evident local event record containing time, trigger, affected subsystem, measured values, and recovery state.

The system shall define three states: **nominal**, **degraded**, and **safe-isolated**. Transition thresholds, hysteresis, debounce time, recovery prerequisites, and human-authorized reset behavior shall be specified for every monitored hazard. A communications failure shall not automatically imply a human-hazard state; it shall produce a defined local monitoring and buffering state unless another hazard is present.

## 9. Cybersecurity and lifecycle controls

Security requirements shall be incorporated into the system risk process and software lifecycle. FDA cybersecurity guidance emphasizes device integrity and cybersecurity considerations for premarket submissions [5]. IEC 81001-5-1 provides a health-software cybersecurity lifecycle framework [6]. The implementation shall include authenticated boot, signed firmware, protected keys, least-privilege services, secure logging, vulnerability handling, update rollback protection, and a documented incident-recovery process.

The design shall minimize retained personal data, separate identity from measurement data where feasible, restrict administrative access, and record security-relevant events. Security controls shall not prevent the HIN from entering a local safe state during a link or authentication failure.

## 10. Engineering assumptions and open decisions

The following decisions remain mandatory before design freeze. First, the intended regulatory and operational classification must be established. Second, the skin-contact layer must be classified as external skin contact, a noninvasive sensor interface, or a microinvasive interface. Third, the exact ECG use case must be selected: wellness monitoring, rhythm monitoring, HRV analysis, or diagnostic morphology. Fourth, the thermal-control actuator and maximum allowable skin temperature must be specified. Fifth, the radio technology, operating band, outage tolerance, and maximum end-to-end latency must be defined. Sixth, the meaning of the “AI monitoring system” as a non-safety-critical advisory node or safety-related control node must be formally assigned.

## References

[1]: https://www.fda.gov/media/142959/download "FDA, Use of International Standard ISO 10993-1: Biological evaluation of medical devices—Part 1: Evaluation and testing within a risk management process, 2023."

[2]: https://pubmed.ncbi.nlm.nih.gov/30109153/ "Kwon et al., Electrocardiogram Sampling Frequency Range Acceptable for HRV Analysis, 2018."

[3]: https://standards.ieee.org/ieee/11073-10101/4670/ "IEEE, ISO/IEEE 11073-10101 Point-of-Care Medical Device Communication—Nomenclature."

[4]: https://www.fda.gov/medical-devices/wireless-medical-devices/wireless-medical-telemetry-systems "FDA, Wireless Medical Telemetry Systems."

[5]: https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity "FDA, Cybersecurity for Medical Devices."

[6]: https://www.iso.org/standard/76097.html "ISO/IEC 81001-5-1: Health software and health IT systems safety, effectiveness and security—Part 5-1: Security—Activities in the product life cycle."

[7]: https://www.iso.org/standard/72704.html "ISO 14971: Medical devices—Application of risk management to medical devices."

[8]: https://www.iso.org/standard/38421.html "IEC 62304: Medical device software—Software life cycle processes."

## 11. Verification, validation, and acceptance matrix

The verification program shall maintain bidirectional traceability from each requirement to its design implementation, test method, result, deviation record, and approval. Risk controls shall be evaluated for effectiveness under normal operation, reasonably foreseeable misuse, environmental extremes, communications loss, power reduction, and single-fault conditions. The structure is consistent with a risk-management approach such as ISO 14971 [7] and a controlled medical-software lifecycle such as IEC 62304 [8].

| Verification area | Minimum test activity | Acceptance evidence |
|---|---|---|
| Fluid chemistry | Measure pH, osmolality, viscosity, composition, degradation, evaporation, and leachables at release, midpoint, and 72-hour endpoint across the specified temperature range | Validated laboratory method, calibrated instruments, uncertainty statement, and all results within approved limits |
| Biological compatibility | Conduct a risk-based final-form evaluation for irritation, sensitization, cytotoxicity, and other required endpoints | Approved biological evaluation plan, test reports, disposition of every endpoint, and documented residual-risk acceptance |
| Sterility or microbial control | Validate the selected sterilization or controlled-bioburden process, packaging, storage, and use conditions | Process validation, bioburden or sterility results, packaging integrity, and justified SAL or microbial-control claim |
| Film retention | Apply defined compression, shear, flex, sweat, temperature, and movement profiles | No unacceptable migration, weeping, leakage, loss of coupling, or contamination of electronics |
| Mechanical material performance | Test finished-suit tensile strength in warp, weft, seams, conditioned and aged states; perform flex, abrasion, tear, and environmental cycling | Finished-article results meet the declared 300 MPa directional requirement and durability limits |
| Thermal regulation | Test thermal conductivity by direction and moisture state; exercise active modulation through the full control range | Thermal response, uniformity, control stability, maximum skin temperature, and fault-state behavior meet approved limits |
| Sensor placement and coverage | Verify sensor coordinates, anatomical coverage, calibration, cable or conductive-path continuity, and repeatability after donning and movement | Placement tolerance, channel availability, and quality metrics remain within specification |
| ECG acquisition | Use calibrated ECG simulators and representative motion profiles to test sampling, amplitude, frequency response, timing, anti-aliasing, noise, artifact rejection, and missing samples | The validated use-case performance is met at 250 Hz or a higher selected rate; no unsupported diagnostic claim is made |
| Thermal and hydration indices | Compare outputs with defined reference methods across temperature, exertion, hydration, motion, and skin-condition ranges | Accuracy, repeatability, drift, quality flagging, and out-of-range behavior meet the approved performance envelope |
| Power autonomy | Test full load, base load, peak transmission, no-motion harvesting, movement harvesting, battery aging, cold and hot conditions, and recovery from low energy | Continuous base-load autonomy and reserve duration meet the power budget without relying on kinetic harvesting as the primary source |
| Telemetry integrity | Inject corruption, truncation, duplication, replay, reordering, delay, loss, authentication failure, and clock drift | Invalid data is rejected or marked; valid data is ordered, timestamped, authenticated, and logged; no silent substitution occurs |
| Communications resilience | Test RF coexistence, attenuation, obstruction, link outage, reconnection, bandwidth reduction, and node restart | Local monitoring remains available; buffering and recovery meet the specified outage and latency limits |
| Isolation function | Inject every defined essential-safety-limit violation and selected combinations of faults | Isolation occurs within the specified response time, affects only the intended subsystem, records the event, and reaches a verified safe state |
| Cybersecurity | Perform threat modeling, authenticated-boot tests, key-management tests, update verification, access-control tests, logging tests, and vulnerability assessment | Security controls meet the approved threat model and lifecycle requirements; unresolved findings have documented risk disposition |
| Human factors | Evaluate donning, removal, replenishment, alarm interpretation, safe-state indication, maintenance, and recovery with representative operators | Critical tasks are completed without unsafe dependence on undocumented knowledge; instructions and status indicators are unambiguous |

## 12. Required acceptance criteria before design freeze

Design freeze shall not occur until the following artifacts are approved: a system requirements specification; interface-control document; material and formulation master specification; biological evaluation plan; sterilization or microbial-control validation plan; thermal and electrical safety analysis; power budget with no-motion case; telemetry protocol and key-management specification; hazard analysis and risk-control traceability; software architecture and verification plan; cybersecurity threat model; environmental qualification plan; and a human-factors and maintenance procedure.

Any requirement that cannot be tested because its measurement method, use case, threshold, or environmental condition is undefined shall be classified as incomplete rather than marked compliant. In particular, the current document requires explicit closure of the terms “local precursors,” “interstitial fluid,” “non-destruction parameter,” “AI monitoring system,” and “dual-rate transmission.”

## 13. Revision disposition summary

The supplied baseline is retained in intent but corrected in implementation language. The fluid layer is reframed as an external skin-contact interface unless a separate microinvasive design is approved. The sterility statement is changed from an unconditional SAL value to a justified process and contact-category requirement. The 250 Hz ECG rate is retained as a baseline for the stated HRV objective but is decoupled from any unsupported claim of complete waveform or diagnostic sufficiency. The cryptographic checksum requirement is upgraded to authenticated integrity protection with replay and key-management controls. Kinetic harvesting remains supplemental. Finally, the fail-safe concept is converted into local, measurable, auditable isolation states with explicit thresholds and recovery rules.

**End of specification.**
