# Pet Management Ontology - Phase 2 (Extended)

[cite_start]This project is an OWL-based ontology developed as part of the Knowledge Engineering and Ontologies course[cite: 4, 12]. [cite_start]It aims to model a pet management system that tracks ownership, veterinary treatments, and health data[cite: 5].

## Group Members
* [cite_start]Sema Nur YAĞÇI 
* [cite_start]Osman Melih KARADAĞ 
* [cite_start]Hayrunisa ÖZTÜRK 

## Project Scope (Version 2.0)
The ontology has been expanded to include:
* [cite_start]**Advanced Hierarchy:** Added specific subclasses for the Pet class, including Cat, Dog, and Bird[cite: 29, 37].
* [cite_start]**Inverse Properties:** Formally defined `ownsPet` as the inverse of `hasOwner` and `treatsPet` as the inverse of `isTreatedBy`[cite: 30, 32].
* [cite_start]**Functional Restrictions:** The `hasAge` property is now a Functional Property to ensure data integrity[cite: 31, 38].
* [cite_start]**Treatment Tracking:** Integration of treatment details, including relationships between pets and veterinarians[cite: 32, 40].

## Research & Methodology
* [cite_start]**Development Methodology:** METHONTOLOGY[cite: 27].
* [cite_start]**Research Integration:** Exploration of Ontology Population using Large Language Models (LLMs) for automated data acquisition[cite: 13, 16].
* [cite_start]**Predictive Modeling:** Adaptation of GRU-RNN based behavioral prediction methods for pet health trend analysis[cite: 17, 18].

## Technologies Used
* [cite_start]**OWL 2 DL** (Ontology Language)[cite: 6].
* **Protégé** (Ontology Editor).
* **Widoco** (Documentation Tool).
