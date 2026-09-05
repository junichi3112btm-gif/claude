# SRI GSC — Venture Brief

**Company:** PhaseShift Technologies (pre-incorporation team, Japan)
**Point of Contact:** Junichi Kato — Business lead / CEO candidate
**Email:** junichi3112btm@gmail.com

> **Recover more iodine from what is already being produced — without pumping more brine.**

*Prepared on the SRI GSC Venture Brief template, 4 September 2026. Figures follow our business plan v1.9 (29 Aug 2026) and the pricing revision of 1 Sep 2026. "Estimate" means our own calculation from public data; "not yet measured" means open. Figures are rounded; measured laboratory results and published third-party data are given as recorded, with exact values in our business plan. The two Japanese producers we work with are named Producer A and Producer B because those discussions are confidential.*

---

## 1. Problem & Approach

**What our future customers struggle with today.** Japan is the world's second-largest iodine producer (USGS), and roughly 80% of that output comes from natural-gas brine on one gas field in Chiba Prefecture (prefectural production and water-use records for FY2024). Those producers face a structural limit on growth: brine pumping is capped by ground-subsidence agreements between producers and the prefecture — we hold the text of those agreements — so the single input that sets output is bounded by regulation rather than demand or capital.

**Strategic-resource context.** Iodine is a relatively small commodity, but its supply chain is strategically sensitive on two structural counts. **Supply concentration:** production is geographically concentrated worldwide and, within Japan, in a single gas field, while the element has important applications where substitution can be technically or economically difficult. **Limited supply elasticity:** additional brine pumping faces physical and regulatory constraints, so rising demand cannot simply be met by pumping more. **Supply resilience** is therefore the opening we target — recovering more iodine from resources already being produced, rather than extracting more. We do not assume iodine is a designated critical mineral, and we do not argue that a shortage is under way. Our thesis is narrower: where supply is concentrated and extraction is constrained, secondary recovery from existing production can strengthen resilience.

**Iodine left in the discharge.** Iodine remains in discharge at concentrations that existing processes do not currently recover economically: blow-out and ion exchange pay at raw-brine concentrations of tens of ppm and stop paying below that. We separate what is published, what a customer has told us, and what we have inferred:

| Basis | Figure |
| :-- | :-- |
| Published plant operating data | 35 ppm brine; 60,000 t/day processed; 1,400 kg/day iodine produced |
| Disclosed by Producer B | Discharge carries about 10 ppm |
| **PhaseShift working estimate** | About two-thirds of incoming iodine is recovered; remainder leaves at 7–12 ppm; **700–1,000 t/yr uncaptured nationwide**, worth **on the order of JPY 10 bn/yr** at market price (700–1,000 t × about JPY 11,800/kg ≈ JPY 8–12 bn) |
| Verification | National estimate being checked with the Society of Iodine Science |

Assumptions: the published plant is representative; discharge sits in the 7–12 ppm band; value is at market price, not a price PhaseShift would receive. Recovering iodine from that discharge is one potential way to increase supply without pumping more.

**How our technology addresses it.** A polymer developed at Doshisha University binds iodine at single-digit ppm. Warming the water makes it separate into a small concentrated phase carrying the iodine; a further temperature step releases the iodine so the polymer can be reused. Because the trigger is temperature, regeneration is designed to avoid a consumed reducing agent — a claim about regeneration only, since feed-side pre-treatment may still be required. The equipment is a side-stream unit on the discharge line: about 4–7% of plant flow is diverted, treated and returned, while the main line continues operating; within that diverted stream, only the concentrated phase — about 1–3% — is heated. The producer owns the unit and keeps the iodine; PhaseShift supplies the polymer and charges per kilogram recovered.

**Why now.** Two major producers have agreed to supply real wastewater, one with a written list of adoption requirements. Demand-side pull is strengthening in two areas — context rather than the basis of the plan, and carrying no revenue in our financials: Japanese policy names iodine a principal raw material for perovskite solar cells intended for domestic manufacture, and iodine has demonstrated potential as an alternative propellant to xenon. The same recovery structure also exists at much larger scale in US produced water, where recovery at higher concentrations is already commercial.

---

## 2. Technology Edge

**What is genuinely new.** The key question is no longer whether the polymer can capture iodine in the laboratory. **It is whether that capture can be turned into economically recoverable iodine from real wastewater in continuous operation.**

**Capture is not recovery.** Selective iodine capture at single-digit ppm has been demonstrated in laboratory batch tests, including model brine wastewater; performance in real, high-salinity wastewater has not yet been validated. Our differentiating mechanism is temperature-driven desorption rather than regeneration with a consumed chemical. UV-vis behaviour — an absorption maximum shifting from 351 to 370 nm — is consistent with complexation involving polyiodide species, although the underlying mechanism is still being characterised. Conventional adsorption approaches typically regenerate with a reducing agent, creating recurring chemical consumption and waste; PhaseShift instead uses a temperature swing, with the potential to use low-grade heat. Only the concentrated phase is heated: current engineering estimates suggest roughly 10 kW per unit, which is an engineering estimate and not a measured plant figure. One producer has disclosed an on-site steam-drain stream at 80–90 °C as a potential heat source. **Whether waste heat alone is sufficient for regeneration remains unproven.**

**Results behind the claims** (laboratory, batch, as of August 2026).

| Test condition | Conventional polymer (PVP) | PhaseShift agent | Metric |
| :-- | :-- | :-- | :-- |
| Iodine in hexane | 73.9% | **91.4%** | capture |
| Pure water, 7 ppm | not measured | **96.8%** | capture |
| Model brine wastewater, 7 ppm | not measured | **below detection limit** | capture |
| Reuse, second cycle | not measured | **79.4%** | capture; dose not recorded, cause unresolved |

The figures above are **capture** results, calculated from the reduction in supernatant absorbance. They do not include desorption or collection. **Recovery from real wastewater has not yet been measured.** Our model therefore uses a provisional recovery assumption of about 93% only where a calculation requires one; it is not presented as demonstrated performance.

**Research base and IP.** The technology originates from a Japanese university laboratory, consistent with the call requirements. The PI is an associate professor at Doshisha University and the inventor of the foundational patent; the laboratory's peer-reviewed publication record can be provided as supporting material. A foundational patent covering the polymer family has been filed and published in Japan, with Doshisha University as sole applicant and the PI as inventor. A first application patent, jointly filed by Doshisha University and Kato, cleared the university invention committee on 7 August 2026 and is scheduled for filing in October 2026; its contents are withheld until filing.

**IP created during this programme.** The call requires IP newly created through its support to vest, in principle, in a domestic Japanese entity. As PhaseShift is pre-incorporation, we will document before the sprint that laboratory results remain vested in Doshisha University under the exclusive-option arrangement already used for public R&D. Commercial outputs — market and customer data and commercial design — will vest in the Japanese company upon incorporation, with Kato holding them under an assignment undertaking until then. **Nothing is structured to place newly created IP outside Japan.**

**Known gaps and engineering responses.**

1. **Polymer containment and discharge compliance.** Current liquid-liquid separation loses about 30% of the polymer per cycle, up to 50%, into the dilute phase. That is both a consumables cost and a potential discharge-compliance issue; our design target is under 0.1 wt% carryover. The proposed mitigation combines a solid-precipitating copolymer — already synthesised but not yet quantitatively tested for loss rate — with a polishing trap on the return line.
2. **Continuous flow.** There is no continuous-flow performance data. The laboratory protocol uses static settling and centrifugation while the target plant operates continuously, and Producer B has identified continuous-flow compatibility as its most significant adoption requirement. Our first hardware milestone is therefore a continuous contactor and phase separator, built as a test skid with an engineering partner currently being recruited.
3. **Speciation and salinity.** Tail water may contain residual sulfite, potentially leaving iodine predominantly as iodide rather than the species captured by the current polymer, so controlled pre-oxidation using existing plant infrastructure may be required; the exact requirement is being defined using real wastewater samples. Performance at TDS above 100,000 mg/L has not yet been tested.

**Differentiation.** We do not claim that existing technologies cannot operate at 7–12 ppm: neither incumbent technologies nor PhaseShift currently have published performance data at this concentration range. The closest identified patent, WO2025258648A1, targets 10 ppm and above and uses a reducing agent for desorption; reverse osmosis shows declining rejection below about 15 ppm; Iofina's IOsorb resin is designed for considerably richer water. Our most important alternative is therefore not another technology — **it is doing nothing, and continuing to discharge the iodine.** The economics differ by market. In Japan the producer currently pays no disposal charge for this stream, so PhaseShift removes no existing cost and the case must come from creating new iodine value. In the United States operators already pay to dispose of or inject produced water but receive no value from the iodine in it. In both markets the proposition must stand on positive economics, not compliance savings.

**What is actually new**, stated precisely, is not capturing iodine at low concentration on its own. It is the potential of a complete recovery pathway — low-concentration capture, temperature-driven concentration, iodine release, polymer reuse — and the purpose of this programme is to determine whether that laboratory concept can become a continuous, economically viable recovery process for real wastewater.

## 3. Global Market Hypothesis

Our intent is not a Japan-only wastewater business. We aim for a resource-recovery approach deployable in more than one country, with Japan as the first validation market and North America as the first overseas test case.

**Why the US is the right test case.** Not because the market is large, but because it tests whether the same recovery logic holds under different water chemistry, production structure and infrastructure — produced water from oil and gas rather than iodine-plant brine. If it holds, the model strengthens iodine supply resilience across regions rather than being a Japan-specific wastewater technology. Whether the target water exists there at all is unproven.

**First market and customer type.** Our first overseas hypothesis is produced water in Oklahoma's Anadarko Basin, with two customer groups: water-midstream and saltwater-disposal operators whose aggregated produced water is not connected to an iodine plant, and low-concentration streams downstream of plants that are. Iofina runs eight plants there, each at 10,000–50,000 bbl/day, and has announced a Permian plant for late 2026. That demonstrates the commercial viability of iodine recovery from produced water **at higher concentrations**, not that our lower-concentration case works. From its disclosed output we estimate roughly 60–110 ppm feed water, with residuals comparable to or richer than Japan's tails — a PhaseShift calculation, not a published figure.

**Decision-maker and willingness to pay.** At a producer the case must satisfy three functions: operations, where the main line must never stop; environmental, where polymer carryover and discharge must be controlled; and finance, where payback must justify the capital budget. That is why we use a side-stream design and quote payback rather than IRR. What we have **not** tested is willingness to pay: no producer has committed to buy a unit, and the paid field unit is that test. Infrastructure operators buy on someone else's operating data, so the order in which sites are won matters more than headline market size.

**Competition, including doing nothing.** Iofina is a potential competitor if it moves into lower concentrations, and a potential partner because PhaseShift could work on water its plants have already stripped. Other alternatives are the incumbent Japanese processes, the closest patent family, and above all disposal: today the operator can simply inject the water at USD 0.60–1.25/bbl, and at about USD 74/kg iodine, iodine value equals disposal cost only at roughly 50–105 ppm, which is why a dedicated plant is difficult to justify below that range. Our leading commercial hypothesis is therefore a low-CAPEX retrofit owned by the water operator; milestone A2 tests this rather than assuming it.

**Why we believe it.** The economics of the band are arithmetic rather than opinion; the water is already aggregated, with one operator alone reporting 60 disposal facilities and 1.2 million bbl/day of capacity; and one Japanese design site (about 13,000 bbl/day) gives a comparable flow-rate reference for initial US skid sizing, though process compatibility still requires validation.

> **What would change our mind — two questions decide the North American case.**
> **1. Does the target water exist at meaningful volume?** Our central assumption is 20–40 ppm streams at 5,000+ bbl/day at aggregation points, and it is unproven. Oklahoma's commercial producing formation has been reported at 300–350 mg/L, showing that richer water exists but not that thin water is collected anywhere. If the target streams do not exist, the answer is No-Go.
> **2. Does the polymer survive above 100,000 mg/L TDS?** Untested. If it fails under that salinity, US produced water is closed to us.

We do not rely on critical-mineral subsidies or policy support for the US case.

**Scale of impact.** In Japan our addressable customer-value pool is about JPY 4–6 bn/yr at market price — roughly half the national figure above, based on Chiba's roughly 80% share of output and the top five municipalities' roughly 60% share. One site recovers about 4,300 kg/yr, adding roughly JPY 50M of sales for its owner. The North American opportunity is larger in volume, but we have not sized it in a way we would defend and will not claim it before the two questions above are answered.

---

## 4. Your Team

**How the team formed.** The chemistry is Associate Professor Shinnosuke Nishimura's at Doshisha University; he is the inventor on the foundational patent. Kato was introduced through Japan's university-startup executive-matching route in Kyoto and has worked with the laboratory since spring 2026, leading customer development, public-funding applications, and IP and contract strategy with the university. On 19 August 2026 Nishimura agreed to serve as principal researcher for the JST D-Global application; one research staff member runs synthesis and process validation. The division is deliberate: the PI remains a university researcher and technical advisor rather than an operating officer, while commercial risk sits with Kato.

**Current gaps and how we intend to close them.**

| Gap | Current status / how it gets closed |
| :-- | :-- |
| Technical leadership | PI plus one research staff member; recruiting a technical co-lead |
| Engineering / manufacturing | No partner yet; continuous-flow hardware is the first technical task; partner search active |
| US market access | No presence or operator relationship; primary sprint objective |
| US iodine offtake | Unknown; tested during the sprint (milestone A3) |
| Corporate form | Pre-incorporation; incorporation planned around public-funding and technical-validation milestones |

Three of these — US market access, iodine offtake and an engineering partner — are explicit sprint objectives.

**Commitment during the five-month sprint.** The two roles are complementary by design, and neither is a side project.

- **Business lead — Kato: 100%.** PhaseShift is his full-time work. He leads the sprint, owns overseas customer discovery, and attends the entire two-week Silicon Valley bootcamp in person.
- **Principal researcher — Nishimura: about one day a week**, the maximum a serving academic can commit under university rules, directed to sprint milestones: mentoring, experimental planning and analysis. Laboratory execution is staffed by a research associate.

We would rather state a number we can hold to for five months than one that looks better on an application.

**Compliance.** We will support checks on export control, research integrity and conflict of interest. This is current practice, not intention: the business lead prepared export-control filings for an international joint-research application this August, and university procedures govern the laboratory side.

**Decision-making.** Technical judgements are the PI's; commercial judgements are Kato's. More importantly, numerical thresholds are set before data are available. The six milestones below are what we test during the sprint. Separately, US commercialization requires pre-agreed conditions: domestic technical validation, a paid field unit or equivalent commitment, patent filing, ring-fenced funding, dedicated staffing, a US partner candidate, a site candidate, cost-share and a third-party verification lab. **None is met today.** These are pre-conditions for US commercialization, not prerequisites for entering this programme; the sprint is designed to establish which can be reached and which assumptions should be abandoned. When we disagree, the question becomes which measurement settles it and when. We maintain a single register of every number and its source; that discipline has already forced us to disclose the 30% polymer loss and the placeholder recovery rate.

---

## 5. Milestones — what we will validate between October 2026 and February 2027

Each hypothesis has both a success criterion and a falsifier; the falsifier is stated here because it is the harder half to write honestly.

| # | Assumption to test | Success criterion / falsifier | Where tested |
| :-: | :-- | :-- | :-- |
| A1 | Thin, unconnected produced-water streams exist at aggregation points in Oklahoma at volumes worth a unit | No 20–40 ppm streams at 5,000+ bbl/day, or every such stream is already contracted to an existing plant | US customer discovery; mentor introductions; Silicon Valley bootcamp |
| A2 | A US water operator will own the unit and pay a per-kg fee | Operators require tolling or build-own-operate, or will not take title to the chemical product | Customer interviews; bootcamp |
| A3 | Concentrated iodine has a US buyer | No refiner states receiving conditions, purity/form, minimum lot or indicative price | Business-model mentoring; partner introductions |
| B1 | Polymer functions above 100,000 mg/L TDS | Phase separation or selectivity fails on a high-salinity sample at a third-party lab | Third-party validation partner |
| C1 | IP position supports US entry | FTO review finds the route blocked by IOsorb-type or competing adsorbent claims | IP strategy sessions; October filing |
| C2 | Venture is fundable on a Japan-first resource-recovery narrative | Investors conclude the planned milestones do not de-risk what they price | Investor readiness sessions |

Two results feed the sprint: a TRL4 assessment on real wastewater from Producer A and Producer B in late September 2026, under a predefined go / conditional-go / pivot / stop rule, and the first patent filing in October 2026.

By February we want a defensible **GO / PIVOT / NO-GO** decision on North America, not a slide saying the market is large. We are not asking SRI to validate a market-size estimate; we are asking for help resolving the technical and commercial uncertainties that determine whether North America is worth pursuing. If the programme discontinues support against agreed criteria, we welcome that discipline: our own venture process already operates on pre-committed numerical gates.

---

## 6. 3–5 Year Vision

**Where we want to be by 2030–2031.** The goal is to become the default retrofit for iodine in streams existing plants cannot economically treat, first in Japan and then in North America — a standard retrofit layer for iodine supply resilience. In Japan our base case is about five installed sites, each recovering about 4 t/yr for its owner, with revenue from unit sales, polymer supply at JPY 10M per unit per year and a JPY 2,000/kg-I₂ process fee: roughly JPY 290M in FY2030 at current prices. This is an illustrative base case, not a forecast, and we do not quote operating profit because the cost base is still being rebuilt. In North America the target is one field demonstration with a water-midstream operator.

**What success looks like at scale.** The design case gives the owner roughly JPY 32M a year against a JPY 100M unit — about a 3-year payback, or about 2 years where Japanese investment tax incentives apply. These figures depend on an unverified recovery rate, so sensitivity matters more than the headline: at 70% recovery payback is about 5 years; at 50%, about 8 years. That is why the September measurement is a gate, not merely a milestone. The recurring layers, rather than the hardware alone, become the business. **Strategic importance is not willingness to pay:** we assume no price premium and no subsidy, and the purchase must clear recoverable iodine value against unit cost, polymer and process fees. Customer ownership remains a commercial hypothesis; milestone A2 tests whether operators accept ownership or instead require a build-own-operate structure. Beyond iodine, the same machine with a different binding group could extend to bromine from the same brine — an option, excluded from the financials.

**Two-step trajectory: primary supply first, then circularity.** Step 1 recovers iodine that primary production leaves behind in brine and produced water, expanding supply without additional drilling or pumping. Step 2 applies the same temperature-responsive separation to iodine-bearing waste from perovskite solar-cell manufacturing and, later, end-of-life modules. **Step 2 is a concept: no experiments have been run on perovskite process waste, and no revenue from it is included in our financials.**

**What has to be true.** Recovery verified on real wastewater; continuous-flow hardware operating unattended; polymer loss low enough for consumables to remain economically manageable; producers willing to buy rather than wait; US target streams proven to exist; and a polymer that survives the required salinity. We would rather reach February 2027 having disproved one of these than having avoided testing it.

**What we contribute to the programme.** Two things: a documented gate framework that makes go/no-go decisions against numbers fixed in advance, and a deliberately difficult deep-tech case — a materials venture selling into conservative infrastructure operators, where adoption matters as much as invention. The sequence is deliberate: technical validation, then commercial validation, then additional domestic supply without additional extraction. SRI is therefore not being asked to validate a market-size story; we are asking it to help us determine whether the assumptions support a globally deployable resource-recovery business. **By February 2027, we intend to know whether that proposition survives real wastewater, industrial salinity, continuous operation and customer economics.**

---

**Sources.** Japan's production rank: USGS. Domestic concentration and pumping constraints: Chiba Prefecture production and water-use records (FY2024) and the ground-subsidence agreements held by the team. Plant operating data (35 ppm, 60,000 t/day, 1,400 kg/day): published process compendium, Society of Chemical Engineers, Japan. Discharge at about 10 ppm and the steam-drain stream: disclosed by the producers. Iofina plant count, capacity and Permian announcement: company disclosures. Aggregation capacity (60 facilities, 1.2 million bbl/day): operator disclosure, 2022. Disposal cost of USD 0.60–1.25/bbl: Permian saltwater-disposal market, May 2026. Formation concentration of 300–350 mg/L: reported for Oklahoma's commercial producing formation. All other figures are PhaseShift estimates or internal design values, labelled accordingly.

*End of brief.*
