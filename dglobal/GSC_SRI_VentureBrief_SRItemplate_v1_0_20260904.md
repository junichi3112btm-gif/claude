# SRI GSC — Venture Brief

**Company:** PhaseShift Technologies (pre-incorporation team, Japan)
**Point of Contact Name:** Junichi Kato — Business lead / CEO candidate
**Email Address:** junichi3112btm@gmail.com

*Prepared on the SRI GSC Venture Brief template, 4 September 2026. Figures follow our internal business plan v1.9 (29 Aug 2026) and the pricing revision of 1 Sep 2026. "Estimate" means our own calculation from public data; "not yet measured" means open. Two Japanese producers we are working with are named Producer A and Producer B because those discussions are confidential.*

---

## 1. Problem & Approach

**What our future customers struggle with today.** Japan is the world's second-largest iodine producer, and about 80% of that output comes from natural-gas brine on one gas field in Chiba Prefecture. Those producers face a structural limit on growth: brine pumping is capped by ground-subsidence agreements with local governments, so the single input that sets output is bounded by regulation rather than by demand or capital.

At the same time they are throwing iodine away. Blow-out and ion exchange are economical at raw-brine concentrations of tens of ppm and stop paying below that. We separate what is published, what a customer has told us, and what we have inferred:

| Basis | Figure |
| :-- | :-- |
| Published plant operating data | 35 ppm brine; 60,000 t/day processed; 1,400 kg/day of iodine produced |
| Disclosed to us by Producer B | its discharge carries about 10 ppm |
| **PhaseShift working estimate**, derived from the rows above | about two-thirds of the incoming iodine is recovered; the remainder leaves with the discharge at 7–12 ppm; **700–1,000 t/yr uncaptured nationwide**, on the order of **JPY 10 bn/yr** at market price (700–1,000 t × JPY 11,782/kg = JPY 8.2–11.8 bn). Assumptions: the published plant is representative of national practice; discharge sits in the 7–12 ppm band; value is taken at the market price, not at a price we would receive |
| Being verified | the national figure, with the Society of Iodine Science |

Recovering iodine from that discharge is one potential way to increase supply without increasing brine pumping.

**How our technology addresses it, in plain language.** A polymer developed at Doshisha University grabs iodine out of water at single-digit ppm and, when the water is warmed slightly, separates into a small concentrated phase that carries the iodine with it. Warm it further and the iodine comes back off, so the polymer is reused. Because the trigger is temperature, the regeneration step is designed to avoid a consumed reducing agent. That is a claim about regeneration only: feed-side pre-treatment may still be required, and we say so below. The equipment is a small side-stream unit bolted onto the discharge line: 3.5–6.8% of the flow is diverted, treated and returned, and the main line never stops. The producer owns the unit and keeps the iodine. We supply the polymer and charge a per-kilogram fee on what is recovered.

**Strategic-resource context.** Iodine is a relatively small commodity, but its supply chain is strategically sensitive: production is geographically concentrated and the element is difficult to substitute in several high-value applications. Japan is itself a major producer, yet its output is concentrated in Chiba's natural-gas brine and further pumping faces physical and regulatory constraints. That points to a different route to supply resilience than conventional mining: recovering more from resources already produced, rather than extracting more. **We do not assume iodine is a designated critical mineral — it is not on the US list.** Our thesis is narrower: where supply is concentrated, extraction is constrained, and the applications matter, secondary recovery can contribute to supply resilience.

**Why now.** Three things changed. First, the producers themselves opened the door: two majors have agreed to supply real wastewater, and one gave us a written list of adoption requirements. Second, demand-side pull is strengthening in two places, which we treat as context rather than as the basis of the plan: Japanese industrial policy names iodine a principal raw material for perovskite solar cells, which Japan intends to manufacture domestically at scale; and iodine has demonstrated potential as an alternative propellant to xenon for electric propulsion, which could reduce dependence on a more geographically concentrated propellant supply. Neither carries revenue in any of our financials. Third, the same recovery structure exists at much larger scale in US produced water, where recovery at higher concentrations is already a commercial operation.

---

## 2. Technology Edge

**What is genuinely new.** Selective iodine capture at single-digit ppm has been demonstrated in laboratory batch tests, including a model brine wastewater; performance in real high-salinity wastewater remains to be validated. What is novel is the release mechanism: desorption driven by temperature rather than by a consumed chemical. UV-vis behaviour (a shift of the absorption maximum from 351 to 370 nm) indicates complexation with polyiodide species; the mechanism itself is still being characterised, and we do not assert it as settled. Incumbent adsorption routes regenerate with a reducing agent, which is a recurring cost and a waste stream. Ours is designed to regenerate on a temperature swing using low-grade heat: only the concentrated phase, about 1–3% of the flow, is heated — an engineering estimate of about 10.5 kW per unit, not a measured plant figure — and one producer has disclosed a steam-drain stream at 80–90 °C on site. Whether waste heat alone suffices depends on heat-exchanger efficiency and is not yet demonstrated.

**Results and IP behind the claims (laboratory, batch, as of August 2026).**

| System | Conventional polymer (PVP) | PhaseShift agent | Basis |
| :-- | :-- | :-- | :-- |
| Iodine in hexane | 73.9% | 91.4% | capture |
| Pure water, 7 ppm (two conditions) | — | 96.8% / 97.2% | capture, UV-vis 351 nm, supernatant |
| Model brine wastewater, 7 ppm | — | supernatant below detection limit | capture |
| Reuse, second cycle | — | 79.4% | dose not recorded; cause unresolved |

These are **capture** figures from the fall in supernatant absorbance. They exclude desorption and collection, so **recovery on real wastewater has not yet been measured**; our plan carries a 92.9% placeholder that we flag wherever it drives a number. A foundational patent covering the polymer family is filed and published in Japan (Doshisha University, sole applicant; inventor: the PI). A first application patent, jointly filed by the university and Kato, cleared the university invention committee on 7 August 2026 and is scheduled for filing in October 2026; its content is withheld until then.

**What happens to IP created during this programme.** The call requires that intellectual property newly created through its support vest, in principle, in a domestic Japanese entity. We are pre-incorporation, so we propose to agree the following in writing before the sprint: results arising in the PI's laboratory vest in Doshisha University, a domestic entity, under the exclusive-option arrangement we already use for public R&D; results arising from the business lead's work — market and customer data, commercial design — vest in the Japanese company on incorporation and are held by Kato under an assignment undertaking until then. Nothing in the sprint is structured to place new IP outside Japan.

**Known gaps, and the engineering answer to each.** We state these because they are the work, not because they are footnotes.

1. **Polymer containment and discharge compliance.** The current liquid-liquid separation loses about 30% of the polymer per cycle (up to 50%) into the dilute phase. That is both a consumables cost and, more seriously, a substance that must not leave with the discharge: our own design limit is under 0.1 wt% carryover. Our proposed mitigation, not a solved problem, is a copolymer that precipitates as a solid — synthesised, but its loss rate is not yet measured — together with a downstream polishing trap on the return line.
2. **Continuous flow.** There is no continuous-flow data at all; the protocol uses static settling and centrifugation, while the plant runs continuously and Producer B has named continuous-flow compatibility its heaviest adoption requirement. Designing a continuous contactor and phase separator, and building a test skid with an engineering partner we are recruiting, is our first hardware milestone.
3. **Speciation and salinity.** Tail water may carry residual sulfite, leaving iodine as iodide rather than the species we capture, so a controlled pre-oxidation step using the plant's existing infrastructure may be required; the requirement is being defined against real samples. Behaviour above 100,000 mg/L TDS is untested.

**Differentiation against the alternatives.** Blow-out and ion exchange work above our band and neither they nor we have published performance data at 7–12 ppm, so we do not claim the band is empty. The closest patent, WO2025258648A1, targets 10 ppm and above and desorbs with a reducing agent. Reverse osmosis loses rejection below about 15 ppm. Iofina's IOsorb resin operates on far richer water. The real alternative is that the customer keeps discharging. The economics of that differ by market, and we state both: in Japan the producer pays no disposal charge on this stream, so we remove no cost and must create new revenue; in the US the operator already pays to inject the water but receives nothing for the iodine in it. Either way the case has to rest on positive economics, not on compliance.

---

## 3. Global Market Hypothesis

**First overseas market and customer type.** Produced water in Oklahoma's Anadarko Basin. Two customer groups: water-midstream and saltwater-disposal operators whose aggregated produced water is not connected to an iodine plant, and the low-concentration streams downstream of plants that are. Iofina runs eight plants there (each 10,000–50,000 bbl/day) and has announced a Permian plant for late 2026, which demonstrates the commercial viability of iodine recovery from produced water **at higher concentrations** — not that our lower-concentration case works. From its disclosed output we estimate, as a PhaseShift calculation rather than a published figure, that those plants take 59–108 ppm water and leave residuals comparable to or richer than Japan's tails.

**Who actually decides, and what we have not tested.** The buyer is not an abstraction, and what we have learned in Japan shapes how we will approach US operators. At a producer the case is assembled by a plant or technology manager who must satisfy three people: the operations head, whose first question is whether the main line ever stops; the environmental manager, who asks what leaves with the discharge; and the finance side, which weighs payback against a capital budget set a year ahead. That is why the unit is a side stream rather than an inline stage, why polymer carryover is treated as a discharge question and not merely a cost, and why we quote payback rather than IRR. What we have **not** tested is willingness to pay: no producer has committed to buy a unit, and the paid field unit is that test. Infrastructure operators buy on someone else's operating data, so the order in which sites are won matters more to us than the size of the market.

**Who we compete against, including doing nothing.** Iofina — a potential competitor if it chooses to miniaturise and move down in concentration, and equally a potential partner, since our unit works on water its plants have already stripped. Incumbent Japanese processes, in our home market. The closest patent family. And above all disposal: today the operator simply injects the water, at USD 0.60–1.25/bbl. Iodine value equals disposal cost only at **51–106 ppm** (at USD 74.27/kg), which is why a dedicated plant is hard to justify below that band. Our leading commercial hypothesis follows from that arithmetic: a low-CAPEX retrofit owned by the water operator. It is a hypothesis, and Milestone 2 is designed to test it rather than to assume it.

**Why we believe it, and what would change our mind.** We believe it because the economics of the band are arithmetic rather than opinion, because one Japanese design site (about 13,000 bbl/day) gives a comparable flow-rate reference for initial US skid sizing — process compatibility still requires validation — and because the water is already aggregated: one operator alone reports 60 disposal facilities and 1.2 million bbl/day of capacity.

> **Two questions decide Phase 2, and they are why we are applying.**
> **1. Does the target water exist at meaningful volume?** Our central assumption is 20–40 ppm streams at 5,000+ bbl/day at aggregation points, and it is unproven. Oklahoma's commercial producing formation has been reported at 300–350 mg/L, which tells us richer water exists but not that thin water is collected anywhere. If it is not, the answer is No-Go, not "wait".
> **2. Does the polymer survive above 100,000 mg/L TDS?** Untested. If it fails, US produced water is closed to us.

Iodine is not on the US critical minerals list, so no subsidy assumption rescues either case.

**Scale of impact we are seeking.** In Japan, our addressable customer-value pool is JPY 4.0–5.8 bn/yr at market price (49% of the national figure above: Chiba holds about 82% of output and the top five municipalities 59.8% of that), and a single site recovers 4,316 kg/yr and adds JPY 50.85M of sales for its owner. That is modest in revenue terms and large in what it represents: additional supply of a resource Japan already leads, obtained without drilling more, at a moment when contrast media, perovskite manufacturing and satellite propulsion all pull on the same production. The North American opportunity is larger in volume, though we have not sized it in a way we would defend, and we will not claim it before the two questions above are answered.

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

**Commitment during the five-month sprint.** The two roles are complementary by design, and neither is a side project.

- **Business lead (Kato) — 100%.** PhaseShift is his full-time work. He leads the sprint, owns overseas customer discovery, and attends the entire two-week Silicon Valley bootcamp in person.
- **Principal researcher (Nishimura) — about one day a week, the maximum a serving academic can commit under university rules, and all of it directed at sprint milestones.** That covers weekly mentoring sessions, the experimental plan and analysis of results. Laboratory execution is staffed by a research associate, so the experimental loop continues between sessions rather than stopping when he is teaching.

We would rather state a number we can hold to for five months than one that looks better on an application.

**How we decide, and how we handle disagreement.** Technical judgements are the PI's and commercial judgements are Kato's, but the mechanism that matters is that we set numerical thresholds before we have the data and then hold ourselves to them. Our plan carries pre-agreed exit and pivot thresholds, and nine conditions that must hold before we start a US feasibility study — domestic technical validation, a paid field unit or equivalent commitment, the October patent filing, ring-fenced funding, dedicated staffing, a US partner candidate, a demonstration-site candidate, cost-share, and a third-party verification lab. **None of the nine is met today**, which is why we are not doing US business development. When we disagree, the question becomes which measurement would settle it and when we will have it. We also keep a single register of every number and its source, so a figure cannot quietly diverge between documents. Twice this year that discipline has forced us to disclose things we would rather not: the 30% polymer loss, and the fact that our recovery rate is a placeholder.

---

## 5. Milestones — what we will validate between October 2026 and February 2027

| # | Assumption to test | How we will know it is wrong | Where in the program we test it |
| :-: | :-- | :-- | :-- |
| **A. Commercial feasibility** | | | |
| 1 | Thin, unconnected produced-water streams exist at aggregation points in Oklahoma at volumes worth a unit | A concentration-and-volume map built from operator and state data shows no 20–40 ppm streams at 5,000+ bbl/day, or every such stream is already contracted to an existing plant | US customer discovery; mentor introductions; Silicon Valley bootcamp |
| 2 | A US water operator will own the unit and pay a per-kilogram fee | Operators tell us they will only accept a tolling or build-own-operate model, or will not take title to a chemical product | Customer interviews during the sprint and the bootcamp |
| 3 | Concentrated iodine has a buyer in the US | No refiner will state receiving conditions (form, purity, minimum lot) or an indicative price | Business-model mentoring; partner introductions |
| **B. Technical feasibility** | | | |
| 4 | The polymer functions above 100,000 mg/L TDS | Phase separation or selectivity fails on a high-salinity sample at a third-party lab | Third-party validation partner introduced through the program |
| **C. Defensibility and financing** | | | |
| 5 | Our IP position supports a US entry | Freedom-to-operate review finds our route blocked by IOsorb-type or competing adsorbent claims | IP strategy sessions, aligned with our October 2026 filing |
| 6 | The venture is fundable on a Japan-first, resource-recovery narrative | Deep-tech and climate investors tell us the milestones we plan do not de-risk what they price | Investor readiness sessions |

Two results land just before and during the sprint and feed it: a TRL4 assessment on real wastewater from Producers A and B, scheduled for late September 2026 with a predefined go / conditional-go / pivot / stop rule, and the filing of our first application patent in October 2026. **What we want to hand back in February is a defensible GO / PIVOT / NO-GO decision on North America, not a slide that says the market is large.** We are not asking SRI to validate a market-size estimate; we are asking for help resolving the technical and commercial uncertainties that decide whether North America is worth pursuing. We note that the programme may discontinue support against agreed criteria, and we welcome that: we already run the venture on pre-committed numerical gates, and a programme willing to stop funding a hypothesis it has disproved is applying the discipline we apply to ourselves.

---

## 6. 3–5 Year Vision

**Where we want to be by 2030–2031.** The default retrofit for recovering iodine from streams that existing plants cannot economically treat, first in Japan and then in North America. Concretely, in Japan that is on the order of five installed sites in our base case, each recovering about 4.3 t/yr for its owner, with our own revenue coming from unit sales, polymer supply at JPY 10M per unit per year and a JPY 2,000/kg-I₂ process fee: roughly JPY 293M of revenue in FY2030 on our current prices. **This is an illustrative base case, not a forecast**, and we do not quote operating profit because the cost base is still being rebuilt on the revised prices. In North America, one field demonstration with a water-midstream operator and a path to units that do not need us on site.

**What success looks like at scale.** A customer's decision to install becomes routine because the payback is short and the plant never stops: today's design case shows the owner gaining JPY 31.62M a year against a JPY 100M unit, a 3.16-year payback, and roughly 2.2 years where Japanese investment tax incentives apply. Those figures rest on an unverified recovery rate, so here is the sensitivity rather than the headline alone: at 70% recovery the payback is about 4.7 years, and at 50% about 8.3 years, which no infrastructure operator would accept. That is why the September measurement on real wastewater is a gate and not a milestone. The recurring layers, not the hardware, become the business. To be precise about status: customer ownership of the unit is our current commercial hypothesis — the producer owns it, keeps the recovered iodine, and pays us for polymer and per kilogram recovered — and Milestone 2 exists to test whether operators will accept it rather than demand a build-own-operate structure. Beyond iodine, the same machine with a different binding group is the natural extension, bromine from the same brine being the obvious first candidate; we treat that as an option and keep it out of the financials until the first extension is demonstrated.

**Two-step trajectory: primary supply first, then circularity.** Step 1 is what this brief is about: become the standard retrofit for recovering iodine that primary production leaves behind, in brine and in produced water, expanding supply without drilling more. Step 2 applies the same temperature-responsive separation to iodine-bearing waste from perovskite solar-cell manufacturing and, later, end-of-life modules — the same element, the same capture chemistry, a different feed. Japan's policy intent to manufacture perovskite cells domestically is what makes that a real second market rather than a slide. **Step 2 is a concept: it is unproven, we have run no experiments on perovskite process waste, and it carries no revenue in any of our financials.** We include it because it is where the same separation chemistry points, not because it is planned income.

**What has to be true.** The recovery rate has to be verified on real wastewater rather than assumed. Continuous-flow hardware has to exist and run without operator attention. Polymer loss has to come down far enough that consumables are a margin, not a leak. Producers have to buy a unit rather than wait for the next one; and in the US the thin streams have to be real and the polymer has to survive the salt. We would rather reach February 2027 having disproved one of these than having avoided testing it.

**What we can contribute to the programme itself.** The call states that selected teams are expected to be partners in building a Japanese model for globally oriented deep-tech commercialization, not only recipients of support. Two things we can put in. First, a documented gate framework that decides go/no-go on numbers fixed in advance, which we already operate and would open to the programme. Second, a deliberately unglamorous case: a materials venture selling into conservative infrastructure operators, where the hard part is adoption rather than invention. If the model works only for software-shaped ventures it will not travel across Japanese deep tech, and we would rather be the awkward test case than the easy one.

*End of brief.*
