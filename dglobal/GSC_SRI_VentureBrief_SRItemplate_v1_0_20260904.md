# SRI GSC — Venture Brief

**Company:** PhaseShift Technologies (pre-incorporation team, Japan)
**Point of Contact Name:** Junichi Kato — Business lead / CEO candidate
**Email Address:** junichi3112btm@gmail.com

*Prepared on the SRI GSC Venture Brief template, 4 September 2026. Figures follow our internal business plan v1.9 (29 Aug 2026) and the pricing revision of 1 Sep 2026. "Estimate" means our own calculation from public data; "not yet measured" means open. Two Japanese producers we are working with are named Producer A and Producer B because those discussions are confidential.*

---

## 1. Problem & Approach

**What our future customers struggle with today.** Japan is the world's second-largest iodine producer, and about 80% of that output comes from natural-gas brine on one gas field in Chiba Prefecture. Producers there cannot grow. Brine pumping is capped by ground-subsidence agreements with local governments, so the one input that determines output is fixed by regulation rather than by demand or capital.

At the same time they are throwing iodine away. Blow-out and ion exchange are economical at raw-brine concentrations of tens of ppm and stop paying below that. We separate what is published, what a customer has told us, and what we have inferred:

| Basis | Figure |
| :-- | :-- |
| Published plant operating data | 35 ppm brine; 60,000 t/day processed; 1,400 kg/day of iodine produced |
| Disclosed to us by Producer B | its discharge carries about 10 ppm |
| **Our estimate**, derived from the rows above | only about two-thirds of the incoming iodine is recovered; the remainder leaves with the discharge at 7–12 ppm; **700–1,000 t/yr uncaptured nationwide**, on the order of **JPY 10 bn/yr** at market price (700–1,000 t × JPY 11,782/kg = JPY 8.2–11.8 bn) |
| Being verified | the national figure, with the Society of Iodine Science |

Recovering iodine from their own discharge is one of the few ways a Japanese producer can increase output at all.

**How our technology addresses it, in plain language.** A polymer developed at Doshisha University grabs iodine out of water at single-digit ppm and, when the water is warmed slightly, separates into a small concentrated phase that carries the iodine with it. Warm it further and the iodine comes back off, so the polymer is reused. Because the trigger is temperature, desorption is designed to need no reducing agents or solvents. The equipment is a small side-stream unit bolted onto the discharge line: 3.5–6.8% of the flow is diverted, treated and returned, and the main line never stops. The producer owns the unit and keeps the iodine. We supply the polymer and charge a per-kilogram fee on what is recovered.

**Why now.** Three things changed. First, the producers themselves opened the door: two majors have agreed to supply real wastewater, and one gave us a written list of adoption requirements. Second, demand acquired a supply-security dimension. Japanese industrial policy names iodine a principal raw material for perovskite solar cells, which Japan intends to manufacture domestically at scale; and in space, iodine is displacing xenon as an electric-propulsion propellant, with the first in-orbit demonstration published in *Nature* in 2021, xenon output concentrated in Russia and Ukraine, and third-party projections of more than 20,000 satellites within a decade. Propulsion volumes are small today against a roughly 34,000 t/yr iodine market and we put none of that in our financials; the point is that two industries governments care about now draw on the same constrained primary supply. Third, the same recovery structure exists at far larger scale in US produced water, and someone has already proved the business there.

---

## 2. Technology Edge

**What is genuinely new.** Selective iodine capture at single-digit ppm has been demonstrated in laboratory batch tests, including a model brine wastewater; performance in real high-salinity wastewater remains to be validated. What is novel is the release mechanism: desorption driven by temperature rather than by a consumed chemical. Incumbent adsorption routes regenerate with a reducing agent, which is a recurring cost and a waste stream. Ours is designed to regenerate on a temperature swing using low-grade heat: only the concentrated phase, about 1–3% of the flow, is heated, an estimated 10.5 kW per unit, and one producer has disclosed a steam-drain stream at 80–90 °C on site. Whether waste heat alone suffices depends on heat-exchanger efficiency and is not yet demonstrated.

**Results and IP behind the claims (laboratory, batch, as of August 2026).**

| System | Conventional polymer (PVP) | PhaseShift agent | Basis |
| :-- | :-- | :-- | :-- |
| Iodine in hexane | 73.9% | 91.4% | capture |
| Pure water, 7 ppm (two conditions) | — | 96.8% / 97.2% | capture, UV-vis 351 nm, supernatant |
| Model brine wastewater, 7 ppm | — | supernatant below detection limit | capture |
| Reuse, second cycle | — | 79.4% | dose not recorded; cause unresolved |

These are **capture** figures from the fall in supernatant absorbance. They exclude desorption and collection, so **recovery on real wastewater has not yet been measured**; our plan carries a 92.9% placeholder that we flag wherever it drives a number. A foundational patent covering the polymer family is filed and published in Japan (Doshisha University, sole applicant; inventor: the PI). A first application patent, jointly filed by the university and Kato, cleared the university invention committee on 7 August 2026 and is scheduled for filing in October 2026; its content is withheld until then.

**Where we are weak, stated plainly.** Polymer loss is about 30% per cycle (up to 50%) in the current liquid-liquid separation, because the dilute phase retains dissolved polymer; a copolymer that precipitates as a solid has been made but its loss rate is not yet measured. There is no continuous-flow data at all: the protocol uses static settling and centrifugation, while the producer's plant runs continuously and has named continuous flow its heaviest requirement. Discharge may carry residual reducing agent, leaving iodide rather than iodine, so pre-oxidation requirements are still being defined. Behaviour above 100,000 mg/L TDS is untested.

**Differentiation against the alternatives.** Blow-out and ion exchange work above our band and neither they nor we have published performance data at 7–12 ppm, so we do not claim the band is empty. The closest patent, WO2025258648A1, targets 10 ppm and above and desorbs with a reducing agent. Reverse osmosis loses rejection below about 15 ppm. Iofina's IOsorb resin operates on far richer water. The real alternative for a customer is to keep discharging, which is free to them today, so our claim has to be positive economics, not compliance.

---

## 3. Global Market Hypothesis

**First overseas market and customer type.** Produced water in Oklahoma's Anadarko Basin. Two customer groups: water-midstream and saltwater-disposal operators whose aggregated produced water is not connected to an iodine plant, and the low-concentration streams downstream of plants that are. Iofina runs eight plants there (each 10,000–50,000 bbl/day) and has announced a Permian plant for late 2026, which proves the business is real; back-calculating from disclosed output we estimate those plants take 59–108 ppm water and leave residuals comparable to or richer than Japan's tails.

**Who we compete against, including doing nothing.** Iofina — a potential competitor if it chooses to miniaturise and move down in concentration, and equally a potential partner, since our unit works on water its plants have already stripped. Incumbent Japanese processes, in our home market. The closest patent family. And above all disposal: today the operator simply injects the water, at USD 0.60–1.25/bbl. Iodine value equals disposal cost only at **51–106 ppm** (at USD 74.27/kg), which is why nobody builds a dedicated plant below that band, and why a low-CAPEX retrofit owned by the water operator is the only form that can work there. Our asset-light model is a consequence of that arithmetic, not a preference.

**Why we believe it, and what would change our mind.** We believe it because the economics of the band are arithmetic rather than opinion, because one Japanese design site (about 13,000 bbl/day) already matches the lower end of a US plant intake so the unit transfers without redesign, and because the water is already aggregated: one operator alone reports 60 disposal facilities and 1.2 million bbl/day of capacity.

> **Two questions decide Phase 2, and they are why we are applying.**
> **1. Does the target water exist at meaningful volume?** Our central assumption is 20–40 ppm streams at 5,000+ bbl/day at aggregation points, and it is unproven. Oklahoma's commercial producing formation has been reported at 300–350 mg/L, which tells us richer water exists but not that thin water is collected anywhere. If it is not, the answer is No-Go, not "wait".
> **2. Does the polymer survive above 100,000 mg/L TDS?** Untested. If it fails, US produced water is closed to us.

Iodine is not on the US critical minerals list, so no subsidy assumption rescues either case.

**Scale of impact we are seeking.** In Japan, our addressable customer-value pool is JPY 4.0–5.8 bn/yr at market price (49% of the national figure above: Chiba holds about 82% of output and the top five municipalities 59.8% of that), and a single site recovers 4,316 kg/yr and adds JPY 50.85M of sales for its owner. That is modest in revenue terms and large in what it represents: additional supply of a resource Japan already leads, obtained without drilling more, at a moment when contrast media, perovskite manufacturing and satellite propulsion all pull on the same production. The North American prize is larger by an order of magnitude in volume, and we will only claim it after the two questions above are answered.

---

## 4. Your Team

**How the team formed.** The chemistry is Associate Professor Shinnosuke Nishimura's at Doshisha University; he is the inventor on the foundational patent. Kato was introduced to the work through Japan's university-startup executive-matching route in Kyoto and has worked with the laboratory since spring 2026, taking the commercial side: customer development with producers, public-funding applications, and IP and contract strategy with the university. On 19 August 2026 Nishimura agreed to serve as principal researcher for our JST D-Global application. One research staff member runs synthesis and process validation. The division is deliberate: the PI stays a university researcher and technical advisor to the venture rather than an operating officer, and the commercial risk sits with Kato.

**Current gaps and how we intend to close them.** We state these plainly because three of the five are exactly what we hope to work on during the sprint.

| Gap | How it gets closed |
| :-- | :-- |
| Technical leadership | PI plus one research staff member today; recruiting a technical co-lead. Active search |
| Engineering / manufacturing of the unit | No partner yet, and continuous-flow hardware is our first technical task. Partner search active; introductions welcome |
| US market access | No presence and no operator relationship. **A primary objective of this sprint** |
| Offtake for concentrated iodine in the US | Unknown. To be tested during the sprint (Milestone 3) |
| Corporate form | Pre-incorporation, with incorporation planned around our public-funding and technical-validation milestones rather than a fixed date |

**Other responsibilities.** Kato works full-time on PhaseShift and treats the sprint as his primary activity. The PI carries a normal university teaching and supervision load, so his committed effort is about one day a week, concentrated on mentoring sessions and the experimental plan; his autumn-semester schedule is the reason our bootcamp answer carries a caveat. We deliberately do not promise more of the PI's time than a working academic can give.

**How we decide, and how we handle disagreement.** Technical judgements are the PI's and commercial judgements are Kato's, but the mechanism that matters is that we set numerical thresholds before we have the data and then hold ourselves to them. Our plan carries pre-agreed exit and pivot thresholds and a set of gate conditions for North America; the current gate score for starting a US feasibility study is zero of nine, which is why we are not doing US business development today. When we disagree, the question becomes which measurement would settle it and when we will have it. We also keep a single register of every number and its source, so a figure cannot quietly diverge between documents. Twice this year that discipline has forced us to disclose things we would rather not: the 30% polymer loss, and the fact that our recovery rate is a placeholder.

---

## 5. Milestones — what we will validate between October 2026 and February 2027

| # | Assumption to test | How we will know it is wrong | Where in the program we test it |
| :-: | :-- | :-- | :-- |
| 1 | Thin, unconnected produced-water streams exist at aggregation points in Oklahoma at volumes worth a unit | A concentration-and-volume map built from operator and state data shows no 20–40 ppm streams at 5,000+ bbl/day, or every such stream is already contracted to an existing plant | US customer discovery; mentor introductions; Silicon Valley bootcamp |
| 2 | A US water operator will own the unit and pay a per-kilogram fee | Operators tell us they will only accept a tolling or build-own-operate model, or will not take title to a chemical product | Customer interviews during the sprint and the bootcamp |
| 3 | Concentrated iodine has a buyer in the US | No refiner will state receiving conditions (form, purity, minimum lot) or an indicative price | Business-model mentoring; partner introductions |
| 4 | The polymer functions above 100,000 mg/L TDS | Phase separation or selectivity fails on a high-salinity sample at a third-party lab | Third-party validation partner introduced through the program |
| 5 | Our IP position supports a US entry | Freedom-to-operate review finds our route blocked by IOsorb-type or competing adsorbent claims | IP strategy sessions, aligned with our October 2026 filing |
| 6 | The venture is fundable on a Japan-first, resource-recovery narrative | Deep-tech and climate investors tell us the milestones we plan do not de-risk what they price | Investor readiness sessions |

Two results land just before and during the sprint and feed it: a TRL4 assessment on real wastewater from Producers A and B, scheduled for late September 2026 with a predefined go / conditional-go / pivot / stop rule, and the filing of our first application patent in October 2026. **What we want to hand back in February is a defensible go or no-go on North America, not a slide that says the market is large.**

---

## 6. 3–5 Year Vision

**Where we want to be by 2030–2031.** The default retrofit for recovering iodine from streams that existing plants cannot economically treat, first in Japan and then in North America. Concretely, in Japan that is on the order of five installed sites in our base case, each recovering about 4.3 t/yr for its owner, with our own revenue coming from unit sales, polymer supply at JPY 10M per unit per year and a JPY 2,000/kg-I₂ process fee: roughly JPY 293M of revenue in FY2030. That figure reflects our pricing revision of 1 September 2026 and supersedes the JPY 239M shown in our earlier business plan, which used the pre-revision prices; it is illustrative, and we do not quote operating profit because the cost base is still being rebuilt on the new prices. In North America, one field demonstration with a water-midstream operator and a path to units that do not need us on site.

**What success looks like at scale.** A customer's decision to install becomes routine because the payback is short and the plant never stops: today's design case shows the owner gaining JPY 31.62M a year against a JPY 100M unit, a 3.16-year payback, and roughly 2.2 years where Japanese investment tax incentives apply. The recurring layers, not the hardware, become the business. Beyond iodine, the same machine with a different binding group is the natural extension, bromine from the same brine being the obvious first candidate; we treat that as an option and keep it out of the financials until the first extension is demonstrated.

**What has to be true.** The recovery rate has to be verified on real wastewater rather than assumed. Continuous-flow hardware has to exist and run without operator attention. Polymer loss has to come down far enough that consumables are a margin, not a leak. Producers have to buy a unit rather than wait for the next one; and in the US the thin streams have to be real and the polymer has to survive the salt. We would rather reach February 2027 having disproved one of these than having avoided testing it.

*End of brief.*
