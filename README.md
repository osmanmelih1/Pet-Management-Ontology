# 🐾 Pet Management Ontology & Knowledge Graph System

[![Ontology Language](https://img.shields.io/badge/Ontology-OWL%202%20DL-blue.svg)](https://www.w3.org/TR/owl2-overview/)
[![Database](https://img.shields.io/badge/Triple%20Store-Ontotext%20GraphDB-orange.svg)](https://www.ontotext.com/products/graphdb/)
[![Documentation](https://img.shields.io/badge/Documentation-WIDOCO-green.svg)](https://osmanmelih1.github.io/Pet-Management-Ontology/)

This repository contains the complete semantic web and knowledge engineering solution developed as part of the **Knowledge Engineering and Ontologies** course. The project formally bridges the structural data gaps within contemporary veterinary clinics and animal management registers by integrating automated data ingestion, advanced reasoning, and semantic data governance.

## 👥 Group Members
* **Hayrunisa ÖZTÜRK**
* **Sema Nur YAĞÇI**
* **Osman Melih KARADAĞ**

---

## 🚀 1. Project Architecture & Scope

The ontology has been comprehensively re-engineered and deployed inside **Ontotext GraphDB** using a strict `No inference` repository ruleset to process **42,443 semantic triples** flawlessly. The production pipeline incorporates:

* **Advanced Taxonomy (TBox):** Organized under strict mono-inheritance paths including `Person` (with `Owner` and `Veterinarian` behavioral roles), `Pet` (with taxonomical sub-classes: `Cat`, `Dog`, `Bird`, `Reptile`, and `Rodent`), and `Treatment` (with explicit clinical subdivisions: `Vaccination`, `Surgery`, `Emergency`, and `Checkup`).
* **Multi-Directional Properties:** Fully defined domain/range constraints with functional restrictions (`pet:hasAge` and `pet:hasOwner` are locked as functional properties to assert absolute data integrity) and dynamic logical inverses (`ownsPet` ↔ `hasOwner`, `treatsPet` ↔ `isTreatedBy`, `hasTreatment` ↔ `isAppliedTo`).
* **Automated Data Pipeline (ETL):** Built via a specialized Python script (`pipeline.py`) leveraging `rdflib` and `pandas` to ingest, clean, and process up to 5,000 real clinical records from open-source Kaggle sources directly into an absolute Turtle (`.ttl`) graph storage structure.
* **Semantic Governance (SHACL Validation):** Enforced via a robust shapes layer (`pet_validation_shapes.ttl`) operating under Closed World Assumption (CWA) variables to intercept datatype anomalies or unlinked clinical logs before injection.
* **LLM Integration & Natural Language Interface:** Grounded few-shot prompt architecture utilizing a Large Language Model as a reliable translation interface to convert raw administrative questions into validated, safe SPARQL code directly executed over GraphDB without risk of token hallucinations.

---

## 📂 2. Repository Structure

```text
├── PetManagement.owl          # Core TBox structural schema definitions built inside Protégé
├── pet_validation_shapes.ttl  # Formal SHACL constraints protecting graph data quality
├── pipeline.py                # Automated Python processing and ingestion ETL framework 
├── populated_clinic.ttl       # Scalable production-ready Knowledge Graph database (Turtle)
├── pet_adoption_dataset.csv   # Raw, open-source Kaggle clinical source matrix data
└── README.md                  # Comprehensive project repository documentation gateway
