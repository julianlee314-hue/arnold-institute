# Privacy Policy — The Arnold Institute of Broscience

**Effective date:** 2026-10-11
**Last updated:** 2026-10-11
**Contact:** arnoldinstitute@mail.grokbot.com

---

## 1. Introduction and Scope

The Arnold Institute of Broscience (the "**Institute**") is a personal, non-commercial health research project operated by Julius, an individual resident in Thailand. The Institute conducts single-subject ("n-of-1") self-experiments in which Julius is both the investigator and the only research subject, and it publishes the results as written papers.

This Privacy Policy (the "**Policy**") describes:

- what personal data the Institute processes, and why;
- the legal bases it relies on;
- with whom data is shared;
- how long data is kept and how it is protected; and
- what rights apply.

It covers:

- (a) the Institute's private WHOOP developer application (the "**App**"), which connects to the WHOOP platform through the WHOOP Developer API;
- (b) the Institute's private research datasets, analyses, and drafts; and
- (c) the Institute's public website hosted on GitHub Pages (the "**Site**") and the papers published there (the "**Papers**").

**The App is private and for personal use only.** It is not offered to the public and has no other users. It accesses data from exactly one WHOOP account, the account belonging to Julius. No one else can sign up for, authorize, or use the App.

## 2. Definitions

In this Policy:

- **"Account Holder"** means Julius, the holder of the single WHOOP account the App is authorized to access. He is the only Data Subject of the Institute's research.
- **"Aggregate Data"** means totals, averages, or other summary statistics computed over a period of at least one week. Aggregate Data contains no individual daily, per-session, or per-night values.
- **"Controller"** means the person who determines the purposes and means of processing personal data. Julius is the Controller for all processing described in this Policy.
- **"Data Subject"** means the identified or identifiable natural person to whom personal data relates. For the Institute's research and the App, the only Data Subject is the Account Holder.
- **"De-identification"** means the measures described in Section 23 that remove or generalize identifiers. Because the only research subject is publicly identified as the Institute's operator, de-identified data under this Policy is **pseudonymized** data, not anonymous data (see Section 23.1).
- **"Health Data"** means personal data concerning physical or mental health. This includes physiological measurements such as heart rate, heart rate variability, respiratory rate, skin temperature, blood oxygen saturation, sleep metrics, recovery scores, strain metrics, and body measurements. It also includes Inferences about health (Section 12).
- **"Inference"** means any information derived, extrapolated, or predicted from other data, by any means, including statistical analysis, algorithms, or AI tools.
- **"OAuth Tokens"** means the access tokens and refresh tokens issued by WHOOP under the OAuth 2.0 protocol that allow the App to retrieve data from the Account Holder's WHOOP account, including tokens obtained through the `offline` scope.
- **"Personal Data"** means any information relating to an identified or identifiable natural person.
- **"Processing"** means any operation performed on Personal Data, including collection, recording, storage, retrieval, analysis, disclosure, transfer, and deletion.
- **"Processor"** means a person or organization that processes Personal Data on behalf of the Controller.
- **"Raw WHOOP Data"** means WHOOP Data in the form returned by the WHOOP API, or any record-level copy of it (for example, an individual workout, sleep, recovery, or cycle record).
- **"Synthetic Data"** means artificially generated values that do not correspond to any real measurement of the Account Holder. They are used to illustrate methods, formats, or analyses.
- **"Vice Data"** means any data about smoking or tobacco or nicotine use, or about cannabis use, including Inferences about either.
- **"Weekly Summary"** means Aggregate Data covering one calendar week, produced from Raw WHOOP Data and self-reported data, with Vice Data excluded.
- **"WHOOP Data"** means data retrieved from the WHOOP platform through the WHOOP Developer API.

## 3. Who Is Responsible

Julius, operating as The Arnold Institute of Broscience, is the Controller. The Institute is not a company, clinic, hospital, health plan, health care provider, or accredited research institution, and it does not provide health care or medical services. Questions about this Policy may be sent to the contact address in Section 26.

## 4. Binding Commitments

The following commitments are binding on the Institute. They take precedence over any other statement in this Policy:

1. **No real data in public.** No real record-level data, whether Raw WHOOP Data, individual self-reported entries, or individual daily values, is placed on GitHub or in any public Paper. Papers contain only Aggregate Data (totals or averages) or Synthetic Data.
2. **Labeling.** Every table, figure, and numerical statement in a Paper is labeled as either "Aggregate (totals/averages)" or "Synthetic."
3. **Raw WHOOP Data stays private.** Raw WHOOP Data remains in the Institute's private, access-restricted storage. Outside that storage, only Weekly Summaries are shared, as described in Section 15.
4. **Minimum necessary data.** Each Processor, AI assistant, or automated tool (each a "bot") receives only the minimum data it needs for its specific task.
5. **12-month limit on raw data.** Raw WHOOP Data and record-level self-reported data are deleted no later than 12 months after collection.
6. **Vices clause.** Vice Data is never published in any form, including in aggregate (Section 13).
7. **Never sold.** Personal Data is never sold, rented, licensed, or traded, and is never used for advertising.
8. **Not a business asset.** Personal Data will not be transferred as an asset in any bankruptcy, acquisition, or similar transaction (Section 18).
9. **No re-identification.** The Institute will not attempt to re-identify, or to link to an individual, any data it holds or publishes in de-identified form beyond the identification inherent in the single-subject design. It will not permit others acting on its behalf to do so.

## 5. Data Collected

The Institute processes only data about the Account Holder. It does not collect Personal Data about any other individual through the App or the research program.

### 5.1 WHOOP Data (via the App)

Using only the read scopes it has been granted, the App may retrieve the following categories from the Account Holder's WHOOP account:

| Category | WHOOP scope | Examples of data elements |
|---|---|---|
| Workouts | `read:workout` | Activity type, start and end times, duration, strain, average and maximum heart rate, heart-rate zone durations, energy expenditure, distance and altitude where available |
| Recovery | `read:recovery` | Recovery score, heart rate variability, resting heart rate, blood oxygen saturation, skin temperature |
| Sleep | `read:sleep` | Sleep and nap timing, time in each sleep stage, sleep performance, efficiency, consistency, respiratory rate, sleep need and debt |
| Cycles | `read:cycles` | Physiological cycle start and end times, day strain, average and maximum heart rate, energy expenditure |
| Profile | `read:profile` | WHOOP user ID, first and last name, email address |
| Body measurements | `read:body_measurement` | Height, weight, maximum heart rate |

The App also processes:

- the **OAuth Tokens** needed to access these categories; and
- technical request metadata generated when calling the WHOOP API, such as timestamps, status codes, and error messages.

The App requests no write access, and it does not access data belonging to any other WHOOP member.

### 5.2 Self-Reported Research Data

For individual experiments, the Account Holder may record additional data about himself:

- protocol details, such as training programs, supplementation, diet, caffeine, alcohol, or sleep interventions;
- subjective ratings, such as mood, energy, soreness, or perceived exertion;
- body measurements; and
- experiment notes.

This may include Vice Data. Vice Data is handled under the additional restrictions in Section 13.

### 5.3 Derived Data and Inferences

The Institute creates derived data from the above, such as Weekly Summaries, trends, statistical estimates, model outputs, charts, and written conclusions. Derived data that relates to the Account Holder's health is Health Data (Section 12).

### 5.4 Location Data

The Institute does not collect precise geolocation. Where location is relevant to an experiment, it is recorded **only as a country**, using the ISO 3166-1 alpha-2 code (for example, `TH`). Any finer-grained location data received from a source, such as GPS-derived workout routes, is discarded or generalized to country level before storage.

### 5.5 Data Not Collected

The Institute does not collect payment information, government identifiers, biometric templates, genetic data, contact lists, or precise location.

### 5.6 Site Visitors and Correspondents

The Site is a static publication. The Institute does not operate accounts, comments, forms, cookies, analytics, or tracking on the Site, and it does not itself collect information about visitors (see Section 16). GitHub, as the hosting provider, may process technical information such as IP addresses under GitHub's own privacy statement, which the Institute does not control.

If someone writes to the contact address, the Institute receives the sender's email address and message. It uses them only to read and respond. Correspondence is never added to research datasets and is deleted when no longer needed (Section 20). Correspondents are not users of the App and are not research subjects.

## 6. Sources of Data

Personal Data is obtained only from:

1. **WHOOP**, through the WHOOP Developer API, after the Account Holder authorizes the App on WHOOP's OAuth consent screen;
2. **the Account Holder directly**, through records he creates; and
3. **the Institute's own analysis**, which produces derived data and Inferences.

The Institute does not purchase data, use data brokers, or combine its datasets with third-party data about the Account Holder or anyone else.

## 7. Purposes of Processing

Personal Data is processed only to:

- (a) design, run, and monitor n-of-1 self-experiments;
- (b) analyze results, including with AI assistance (Section 14);
- (c) write, review, and publish Papers that contain only Aggregate Data or Synthetic Data;
- (d) operate, maintain, debug, and secure the App; and
- (e) respond to correspondence and comply with legal obligations and platform terms.

Personal Data is never used for advertising, marketing profiles, credit, insurance, or employment decisions, or for any automated decision with legal or similarly significant effects. It is never used to provide medical diagnosis, treatment, or advice.

## 8. Legal Bases for Processing

The Institute processes data about one individual, Julius, who is also the Controller. Some laws may exclude purely personal processing, or may not apply territorially. The Institute nonetheless adopts the following standards.

**Thailand — Personal Data Protection Act B.E. 2562 (2019) ("PDPA").** For Health Data and Vice Data, the Institute relies on the Data Subject's **explicit consent** (see Section 10). The Account Holder gives that consent by authorizing the App through WHOOP's OAuth flow, by recording self-reported data, and by expressly approving each Paper before publication. For correspondence, the Institute relies on legitimate interests in responding to inquiries.

**European Union — General Data Protection Regulation ("GDPR").** The Institute is not established in the EU and does not offer goods or services to, or monitor, individuals in the EU, so the GDPR is not expected to apply. If it does, the Institute relies on explicit consent for special-category Health Data, and on legitimate interests for correspondence.

**Withdrawal.** Consent may be withdrawn at any time (Section 20.3). Withdrawal does not affect processing that took place before it, and it cannot recall Papers already published (Section 23.5).

## 9. Health Data as a Special Category

Health Data receives heightened protection. The Institute applies the following standards:

- **Explicit consent.** Health Data is processed only with explicit consent (Sections 8 and 10).
- **Purpose limitation.** Health Data is used only for the purposes in Section 7. It is never sold, never used for advertising, and never disclosed to employers, insurers, or data brokers.
- **Minimization.** The App requests only the scopes in Section 5.1. Each experiment dataset contains only the elements that experiment needs. Each Processor receives only the minimum necessary data (Section 15).
- **U.S. state consumer-health-data laws.** Some U.S. states regulate "consumer health data," for example Washington's My Health My Data Act. These laws generally apply to entities that do business in, or target consumers in, those states. The Institute does neither, and its only Data Subject does not live in the United States, so these laws are not expected to apply. The Institute nonetheless adopts their core protections as standards:
  - consent before collection;
  - no sale;
  - no sharing beyond the Processors in Section 15;
  - deletion on request; and
  - treatment of Inferences as Health Data (Section 12).
- **Not medical advice.** Papers describe one individual's data and experiences. They are not medical advice, not clinical research, and not a basis for anyone's diagnosis or treatment decisions.

## 10. Sensitive-Data Notice for Thailand (PDPA Section 26)

The Account Holder resides in Thailand. This notice is given to him as the Data Subject under the PDPA.

Section 26 of the PDPA prohibits collecting certain categories of sensitive personal data without the Data Subject's explicit consent, unless a statutory exception applies. Health data is one of those categories. The list also includes, among others, criminal records, biometric data, and genetic data.

The Institute confirms the following:

- **What sensitive data is collected:** Health Data as described in Sections 5.1 through 5.3, and Vice Data as described in Section 13. The Institute does not collect biometric templates, genetic data, or criminal records.
- **Legal basis:** explicit consent, given as described in Section 8. The Institute does not rely on any of the statutory exceptions in Section 26 for medical or health-care purposes, because it is not a medical or health-care service.
- **Publication:** Papers are made public only with the Data Subject's explicit consent, and contain only Aggregate Data or Synthetic Data (Section 4). Vice Data is never published (Section 13).
- **Withdrawal:** explicit consent may be withdrawn at any time (Section 20.3).
- **Complaints:** the Data Subject may lodge a complaint with the Personal Data Protection Committee of Thailand.

## 11. Not a HIPAA Covered Entity

The U.S. Health Insurance Portability and Accountability Act ("HIPAA") and its Privacy and Security Rules (45 C.F.R. Parts 160 and 164) apply to "covered entities" and their "business associates." Covered entities are health plans, health care clearinghouses, and health care providers that transmit health information electronically in connection with certain standard transactions, such as insurance billing.

**The Institute is not a HIPAA covered entity or business associate**, because:

- it is an individual's personal research project, not a health plan or a health care clearinghouse;
- it does not provide health care to anyone and does not bill or conduct standard electronic health transactions; and
- it does not create, receive, maintain, or transmit health information on behalf of any covered entity.

WHOOP's API terms also state that WHOOP makes no representation that its APIs satisfy HIPAA requirements.

Accordingly, data held by the Institute is not "protected health information" under HIPAA, and HIPAA does not grant rights or impose obligations with respect to it. The Institute nonetheless voluntarily uses HIPAA concepts as design guidance: minimum-necessary disclosure, de-identification before disclosure, access controls, and incident response. Using HIPAA concepts does not mean the Institute is "HIPAA-compliant" or subject to HIPAA.

## 12. Inferences Are Personal Data

The Institute treats **Inferences about the Account Holder's health as Health Data**, with the same protections as directly measured data. Inferences include:

- conclusions drawn by statistical analysis;
- outputs of AI tools;
- predictions of future health status; and
- conclusions drawn from non-health data, such as schedules, purchases, or travel.

This standard follows the approach of Washington's My Health My Data Act. Its definition of "consumer health data" expressly includes information derived or extrapolated from non-health information, including proxy, derivative, inferred, or emergent data produced by any means, including algorithms or machine learning, when that information is used to associate a person with a health status.

Accordingly:

- Inferences are covered by the minimization, sharing, retention, security, and rights provisions of this Policy.
- An Inference is not de-identified merely because it is expressed as a summary or a conclusion. Published Inferences are subject to Sections 4, 13, and 23.
- Inferences generated by AI tools are reviewed by Julius before they are relied on or published (Section 14).

## 13. Vices Clause

**Vice Data is never published.** This covers smoking, tobacco, and nicotine data, cannabis data, and Inferences about any of these. It is not published in any form: not as record-level data, not as Aggregate Data, not as Synthetic Data modeled on real use, and not as a named covariate or confounder in a Paper. Papers will not state or imply whether the Account Holder smokes or uses cannabis.

Additional safeguards:

- **Private by default.** Vice Data is kept separately from other research data in private, access-restricted storage, and is excluded from Weekly Summaries.
- **Processor minimization.** Vice Data is provided to a Processor only where it is strictly necessary for a specific private analysis that Julius has requested. In that case, only the minimum necessary Vice Data is provided.
- **Retention.** Vice Data is subject to the 12-month limit for record-level data (Section 20) and may be deleted sooner.
- **Legal sensitivity.** The legal treatment of cannabis in Thailand has changed several times in recent years, and current rules restrict its lawful use, sale, and supply, chiefly to medical purposes under regulatory control. Information about cannabis use can therefore carry legal and reputational sensitivity beyond that of ordinary health data. This clause reflects that sensitivity. It is not a statement about any particular conduct or about whether any conduct was lawful.

## 14. AI Processing and What AI Providers May Retain

The Institute uses **Grok Bot**, an AI assistant service, to help with data retrieval, analysis, visualization, coding, and drafting and editing Papers. Grok Bot acts as a Processor on the Institute's behalf.

**Minimum necessary data.** Each AI task receives only the data it needs:

- The App's retrieval and storage function, which runs in an access-restricted environment, is the only function that handles Raw WHOOP Data and OAuth Tokens.
- Analysis and drafting tasks receive Weekly Summaries, Aggregate Data, or Synthetic Data wherever that is sufficient.
- Vice Data is excluded unless Section 13 permits its use.

**No model training.** The Institute does not use WHOOP Data or other Personal Data to create, train, fine-tune, or improve any machine-learning or AI model, and it does not authorize its Processors to do so. AI assistants are used only to perform tasks for the Institute.

**What AI providers may retain.** Even when data is not used for training, an AI service and its underlying infrastructure providers may retain the following, depending on the service's terms and the account's settings:

- prompts, uploaded files, and outputs, for a limited period, to provide the service, maintain conversation history, and support debugging;
- copies kept for safety, abuse, and misuse monitoring;
- copies kept for legal compliance, including responding to lawful requests or legal holds;
- metadata such as timestamps, usage, and account information; and
- backups that persist for a period after deletion from active systems.

The Institute manages this retention risk by:

- (a) sending AI tools the minimum data necessary;
- (b) preferring Weekly Summaries, Aggregate Data, and Synthetic Data;
- (c) never sending OAuth Tokens or client secrets in conversational prompts;
- (d) using available settings that disable training on its data and limit retention; and
- (e) deleting conversations and files containing record-level Health Data when they are no longer needed, where the service allows it.

The Institute cannot guarantee deletion from a provider's backups or legally required retention.

**Human review and no automated decisions.** All AI output is treated as a draft and reviewed by Julius, who is responsible for every published Paper. AI processing produces no automated decisions with legal or similarly significant effects.

## 15. Sharing and Processors

**The Institute never sells Personal Data, Health Data, or WHOOP Data, and never shares it for targeted or cross-context behavioral advertising.**

Data is shared only with the following recipients, and each receives only the minimum necessary:

| Recipient | Role | Data received (minimum necessary) | Purpose |
|---|---|---|---|
| **WHOOP** (Whoop, Inc.) | Source platform and API provider | OAuth Tokens and API request metadata. WHOOP already holds the underlying WHOOP Data under the Account Holder's membership. | Authenticating the App and providing the Account Holder's data |
| **Grok Bot** (retrieval and storage function) | Processor | Raw WHOOP Data and OAuth Tokens, in an access-restricted environment only | Retrieving, storing, summarizing, and deleting data |
| **Grok Bot** (analysis and drafting tasks) | Processor | Weekly Summaries, Aggregate Data, or Synthetic Data. Record-level data only where strictly necessary for a specific private analysis. | Analysis and drafting (Section 14) |
| **GitHub** (GitHub, Inc.) | Hosting provider | Published Papers and Site content only. These contain Aggregate Data or Synthetic Data, never real record-level data, and never Vice Data. | Hosting the public Site and repository |

**Public publication.** Papers are public. Section 4 and Section 23 govern what they may contain.

**Exposure of WHOOP Data.** The Institute does not expose WHOOP Data to anyone other than the recipients above. Publishing Aggregate Data derived from WHOOP Data in Papers occurs only with the Account Holder's explicit opt-in consent for each Paper.

**Legal requests.** Section 17 governs disclosures in response to legal requests.

## 16. No Tracking Pixels, SDKs, or Advertising

The Institute does not use, and will not add to the Site, the App, or the Papers, any of the following:

- tracking pixels, web beacons, or session-replay scripts;
- third-party analytics, advertising, attribution, or marketing software development kits (SDKs);
- advertising, ad networks, retargeting, or affiliate tracking; or
- third-party embeds that transmit visitor or health information to advertising or analytics providers.

This commitment reflects regulatory concern about health information leaking through such tools. In 2023, the U.S. Federal Trade Commission brought its first enforcement action under its Health Breach Notification Rule against GoodRx. The FTC alleged that GoodRx shared users' health information with advertising and analytics platforms, including through tracking technologies, contrary to its privacy promises. The resulting order included a civil penalty and a ban on sharing health data for advertising. In 2021, the FTC settled allegations that Flo Health, the developer of a period- and fertility-tracking app, disclosed users' health data to third-party marketing and analytics services despite promising to keep it private.

If the Institute ever proposes to add any analytics tool, it will first update this Policy as described in Section 25.

## 17. Law-Enforcement and Government Requests

The Institute will disclose Personal Data to a government authority or law-enforcement agency only:

- in response to a valid, legally binding demand, such as a court order, warrant, or other compulsory legal process, under a law that applies to the Institute; or
- where disclosure is necessary to prevent imminent danger to life or physical safety.

When it receives a request, the Institute will:

- (a) verify the request's authenticity and legal basis;
- (b) decline requests that are informal, overbroad, or not legally binding;
- (c) narrow its response to the minimum data legally required;
- (d) record the request and the response; and
- (e) where lawful, inform the Data Subject.

Because of the minimization and retention rules in this Policy, record-level data older than 12 months is not available for disclosure.

Processors, including WHOOP, GitHub, and AI service providers, may receive legal requests directly for data they hold. They respond under their own policies, which the Institute does not control. Vice Data is subject to the same process, and no additional disclosure of it will be made voluntarily.

## 18. No Transfer of Data as a Business Asset

Personal Data held by the Institute is not an asset of any business. It will not be sold, assigned, licensed, or otherwise transferred:

- as part of a bankruptcy, insolvency, or receivership;
- in a merger, acquisition, or financing;
- in a sale of the Site, the Papers, or the Institute's name; or
- in any similar transaction.

If the Institute ceases operation, or if the Site, the Institute's name, or the Papers are transferred to anyone else, the Institute will:

- delete all non-public Personal Data, including Raw WHOOP Data, self-reported data, Vice Data, and OAuth Tokens; and
- revoke the App's access to WHOOP.

Published Papers may be transferred or archived, but no private data will accompany them.

## 19. Cross-Border Transfers

Julius lives in Thailand. The Institute's Processors may store or process data in other countries, including the United States, where WHOOP and GitHub are headquartered. Personal Data may therefore be transferred out of Thailand.

**PDPA Section 28.** Section 28 of the PDPA permits personal data to be sent or transferred to a foreign country only if the destination has adequate data-protection standards, unless an exception applies. One exception is the Data Subject's consent, given after he has been informed of any inadequacy in the destination's data-protection standards.

The Institute makes the following disclosure to satisfy this requirement:

- **No adequacy decision.** The Institute is not relying on any official determination that the destination countries, including the United States, have adequate data-protection standards. Those countries may not provide protection equivalent to the PDPA. For example, they may not provide the same data-subject rights, the same remedies, or an equivalent supervisory authority.
- **Basis for transfer.** The Data Subject consents to the transfers described in this Policy with that knowledge.
- **Additional safeguards.** Transfers are also supported by the Processors' contractual and security commitments, and by the minimization rules in Sections 4 and 15. Only the minimum necessary data, preferably Weekly Summaries, is transferred for analysis.

**GDPR.** If the GDPR applies, the Institute would rely on the transfer mechanisms available under it, including explicit consent and the Processors' contractual commitments.

Published Papers are accessible worldwide.

## 20. Retention and Deletion

### 20.1 Retention Periods

| Data | Retention |
|---|---|
| OAuth Tokens | Kept only while the App is authorized. Replaced on refresh. Deleted immediately on revocation or termination. |
| Raw WHOOP Data | **Deleted no later than 12 months after retrieval**, on a rolling basis. Deleted sooner when no longer needed for an active experiment. Not kept as a permanent archive. |
| Record-level self-reported data, including Vice Data | Deleted no later than 12 months after collection. |
| Weekly Summaries and other Aggregate Data supporting a Paper | Kept while the Paper remains published, for reproducibility and correction. Then deleted. |
| AI conversations and files containing record-level Health Data | Deleted when no longer needed, where the service allows (Section 14). |
| Published Papers | Public until withdrawn (Section 23.5). |
| Correspondence | Deleted within 12 months of the last exchange, unless needed for a legal obligation or claim. |
| App logs | Kept for no more than 90 days. Limited to operational metadata, with no Health Data values. |

The 12-month limit is designed to avoid creating permanent copies of WHOOP Data. Where the WHOOP API Terms of Use or WHOOP's technical controls, such as cache headers, require a shorter period, the shorter period applies.

### 20.2 Deletion on Termination

If the App is disconnected, or the Institute's access to the WHOOP API ends, the Institute will:

- immediately stop calling the API;
- delete all OAuth Tokens; and
- delete all stored or cached Raw WHOOP Data.

Only the Weekly Summaries and Aggregate Data supporting published Papers are retained.

### 20.3 Revoking Access

The Account Holder may revoke the App's access at any time, by either method:

1. **In WHOOP:** remove the App from the connected apps or integrations area of the WHOOP account settings. This invalidates the App's authorization.
2. **By request:** email arnoldinstitute@mail.grokbot.com. The Institute will revoke the authorization through the WHOOP API's access-revocation endpoint and delete the stored OAuth Tokens.

After revocation, the App can retrieve no further data, and Section 20.2 applies.

### 20.4 Requesting Deletion

To request deletion, email arnoldinstitute@mail.grokbot.com with the subject line "Deletion Request." The Institute will:

- delete the requested data from its systems;
- instruct its Processors to delete it where applicable; and
- confirm completion within 30 days.

Data held by WHOOP under the Account Holder's WHOOP membership is governed by WHOOP's privacy policy and must be deleted through WHOOP.

## 21. Security

The Institute maintains administrative, technical, and physical safeguards appropriate to Health Data and Vice Data, including the following:

- **Secure token storage.** OAuth Tokens and the App's client secret are stored only in an access-restricted environment, encrypted at rest. They are never committed to the public GitHub repository or its history, never embedded in client-side code, never written to logs, never included in AI prompts, and never shared.
- **Encryption.** All communication with WHOOP and other Processors uses HTTPS/TLS. WHOOP Data and research datasets are encrypted at rest.
- **Access limited to the Account Holder.** Access to the App, its credentials, and private data is limited to Julius and to Processors acting on his instructions, each with the minimum necessary access.
- **Separation of public and private data.** Private data is never stored in the repository that serves the Site. Each Paper is checked against Sections 4 and 13 before publication. Repository secret-scanning is enabled.
- **Least privilege.** The App holds read-only scopes, with no write access to the WHOOP account.
- **Incident response.** If the Institute discovers unauthorized access to, or disclosure of, WHOOP Data or credentials, it will:
  - contain the incident;
  - revoke and rotate affected credentials;
  - notify WHOOP within the period required by the WHOOP API Terms of Use; and
  - make any notification required by applicable law.

No method of transmission or storage is completely secure.

## 22. Rights

Subject to applicable law, the Data Subject has the right to:

- **be informed** about the processing of his Personal Data, which this Policy provides;
- **access** his Personal Data and obtain a copy, including WHOOP Data the App has collected;
- **data portability**, meaning receipt of his data in a machine-readable format;
- **rectification** of inaccurate data;
- **erasure** of his data (Section 20.4);
- **restriction** of processing;
- **objection** to processing;
- **withdrawal of consent** at any time (Section 20.3); and
- **complaint** to a supervisory authority, including the Personal Data Protection Committee of Thailand.

Requests may be sent to arnoldinstitute@mail.grokbot.com. The Institute will respond within 30 days. Because the Data Subject is also the Controller, these rights are in practice exercised directly. They are stated here for completeness and to meet platform requirements. Correspondents may use the same address to ask about, or request deletion of, their correspondence.

## 23. Anonymization: Limits and Publication Rules

### 23.1 The Limits of Anonymization

The Institute does not claim that its published or shared data is anonymous. Research has repeatedly shown that removing names and identifiers does not reliably prevent re-identification:

- **Sweeney.** In a 2000 working paper based on 1990 U.S. Census data, Latanya Sweeney estimated that about 87% of the U.S. population was likely uniquely identifiable from just three attributes: 5-digit ZIP code, sex, and date of birth. A later study using different methods estimated a lower but still majority figure. Sweeney also showed that supposedly anonymized hospital records could be linked to a named individual, a sitting governor.
- **Rocher, Hendrickx, and de Montjoye.** In a 2019 study in *Nature Communications* ("Estimating the success of re-identifications in incomplete datasets using generative models"), the authors estimated that 99.98% of Americans would be correctly re-identified in any dataset using 15 demographic attributes. They concluded that even heavily sampled, de-identified datasets are unlikely to meet modern legal standards for anonymization.

The Institute's situation is more direct still: there is one research subject, and he is publicly identified as the operator. **Any data the Institute publishes about its research is, by design, about Julius.** De-identification measures reduce incidental detail. They do not make the data anonymous, and this Policy treats such data as pseudonymized personal data.

### 23.2 Why Papers Use Only Aggregate and Synthetic Data

Since de-identification cannot protect a known single subject, the Institute protects him by limiting what is published:

- only Aggregate Data (totals or averages over at least one week) or Synthetic Data;
- no record-level data; and
- no Vice Data (Sections 4 and 13).

### 23.3 De-identification Measures

Before any data leaves private storage, whether as a Weekly Summary for a Processor or as content for a Paper, the Institute:

- removes direct identifiers: name, email, WHOOP user ID, device and account identifiers, and OAuth and API identifiers;
- generalizes location to an ISO 3166-1 alpha-2 country code;
- generalizes time to the experiment week (for example, "Week 3"), rather than calendar dates, where dates are not essential;
- expresses body measurements as ranges or relative changes where exact values are not essential; and
- screens free text to remove references to other people, places, employers, health-care providers, and Vice Data.

### 23.4 Publication Rules

- Each Paper is published only after Julius has reviewed it and expressly approved its publication.
- Every number, table, and figure is labeled "Aggregate (totals/averages)" or "Synthetic."
- No Paper contains information about any other identifiable person.
- Each Paper states its methodology and the limitations of single-subject designs, and carries a not-medical-advice disclaimer.
- Papers may name WHOOP as a data source only factually, without implying endorsement, sponsorship, or partnership, and without using WHOOP's logos or brand features.

### 23.5 Published Material

Published material may be copied, cached, archived, or indexed by others beyond the Institute's control. The Institute can withdraw a Paper from the Site and its repository, but it cannot guarantee removal of third-party copies. Withdrawing consent stops future publication. It cannot fully reverse past publication.

## 24. Children

The Institute's research involves one adult subject. The App, the Site, and the Papers are not directed to children. The Institute does not knowingly collect Personal Data from anyone under 20 (the age of majority in Thailand) or under any other applicable age of digital consent. If such data is received, for example through correspondence, it will be deleted.

## 25. Changes to This Policy

The Institute may update this Policy to reflect changes in its practices, Processors, the WHOOP API Terms of Use, or the law. Updates are published on the Site with a new "Last updated" date, and earlier versions remain available in the repository history.

The Institute will not do any of the following until a revised Policy has been published:

- relax a Binding Commitment in Section 4;
- add analytics or tracking (Section 16);
- add a Processor; or
- extend processing to anyone other than the Account Holder.

Any additional consents that such a change requires will be obtained before the change takes effect.

## 26. Contact

The Arnold Institute of Broscience
Attn: Julius
Email: **arnoldinstitute@mail.grokbot.com**

Privacy questions, access and deletion requests, and requests to revoke the App's access may all be sent to this address.
