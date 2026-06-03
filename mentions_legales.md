# Mentions Légales, Conditions d'Utilisation et Politique de Confidentialité

## Préambule
Ce document formalise les mentions légales, les conditions générales d'utilisation (CGU) et la politique de protection des données personnelles applicables au prototype de chatbot juridique dénommé **« [Nom du Projet / Chatbot] »** (ci-après « l'Application »). 

L'Application intègre l'API Gemini de Google LLC pour assister les professionnels du droit dans la recherche, l'analyse de documents et l'aide à la rédaction d'actes juridiques.

---

## 1. Éditeur et Directeur de la Publication
L'Application est éditée par :
* **Nom / Dénomination :** JurisIA
* **Forme juridique :** SELARL
* **Adresse du siège social :** Viroflay
* **Numéro SIRET :** 176253387151837
* **Numéro de TVA intracommunautaire :** 1763858
* **Contact courriel :** contact@cabinet.com
* **Téléphone :** 9868758769
* **Directeur de la publication :** Laura Sery

En sa qualité d'avocat, l'Éditeur est soumis aux règles déontologiques de la profession, régies notamment par la Loi n° 71-1130 du 31 décembre 1971, le Décret n° 91-1197 du 27 novembre 1991 et le Règlement Intérieur National (RIN) du Conseil National des Barreaux (CNB).

---

## 2. Hébergement et Infrastructure Technique
L'infrastructure technique de ce prototype repose sur deux tiers technologiques distincts :

1. **Hébergement de l'interface applicative (Frontend & Logique applicative) :**
   * **Prestataire :** Streamlit Inc. (Streamlit Cloud)
   * **Adresse :** 1045 14th Street, San Francisco, CA 94114, États-Unis
   * **Localisation des serveurs :** Principalement situés aux États-Unis (USA)

2. **Infrastructure d'Intelligence Artificielle (Fournisseur de LLM via API) :**
   * **Prestataire :** Google Ireland Limited (pour les utilisateurs de l'EEE) / Google LLC (USA)
   * **Technologie :** API Gemini (Google AI Studio / Vertex AI)
   * **Localisation du traitement de l'API :** Les données soumises sont traitées de manière dynamique dans les centres de données sécurisés de Google (régions configurées par l'Éditeur, pouvant inclure l'Union Européenne et/ou les États-Unis).

---

## 3. Clause de Non-Responsabilité et Limitations Techniques (Disclaimer IA)

### 3.1. Nature expérimentale du prototype
L'Application est un **prototype expérimental** basé sur une technologie d'intelligence artificielle générative (Grand Modèle de Langage - LLM). Elle est fournie « en l'état », à des fins de démonstration technique et d'évaluation interne.

### 3.2. Absence de consultation juridique
L'utilisation de l'Application et les contenus qu'elle génère **ne constituent en aucun cas une consultation juridique ou un avis juridique** au sens de la Loi n° 71-1130 du 31 décembre 1971. Le chatbot ne saurait se substituer à l'analyse critique, aux recherches doctrinales et jurisprudentielles, ni au jugement professionnel d'un avocat qualifié. Aucun rapport de type "avocat-client" n'est créé entre l'Éditeur et l'utilisateur du fait de l'usage de l'Application.

### 3.3. Risque d'erreurs techniques (« Hallucinations »)
L'utilisateur est expressément averti que les modèles d'intelligence artificielle sont susceptibles de produire des résultats factuellement inexacts, obsolètes, incomplets, voire d'inventer des sources textuelles ou jurisprudentielles (phénomène d'« hallucination »). 

**La vérification systématique de l'intégralité des outputs (textes, clauses, citations) générés par l'Application est une obligation impérative pour l'utilisateur avant toute exploitation, intégration dans un acte ou communication à des tiers.**

### 3.4. Exonération de responsabilité
L'Éditeur ne pourra être tenu responsable des dommages directs ou indirects (notamment perte de chance, erreur de procédure, préjudice financier ou réputationnel) résultant :
* De l'utilisation des contenus ou des suggestions rédigées par l'Application ;
* D'une interruption de service, d'un bug ou d'une indisponibilité du prototype ;
* D'une mauvaise interprétation des réponses fournies par l'IA.

L'utilisateur professionnel du droit conserve la **responsabilité exclusive, finale et entière** des actes juridiques qu'il valide, signe et produit.

---

## 4. Secret Professionnel et Recommandations de Sécurité

Le secret professionnel de l'avocat est d'ordre public. Il est général, absolu et illimité dans le temps (Article 66-5 de la loi du 31 décembre 1971 et Article 2 du RIN).

Compte tenu de l'architecture du prototype connecté à des API tierces (Streamlit et Google) :
* **Obligation stricte d'anonymisation :** Il est **formellement interdit** d'insérer dans les invites de commande (*prompts*) ou dans les documents téléversés des données nominatives ou confidentielles permettant d'identifier directement ou indirectement des clients réels, des parties adverses physiques ou morales, ou des dossiers en cours couverts par le secret professionnel.
* **Méthodologie recommandée :** L'utilisateur s'engage à cavarder ou pseudonymiser rigoureusement ses textes avant saisie (ex : remplacer *« Jean Dupont »* par *« Monsieur X »*, *« Société Alpha »* par *« Société Y »*, ou modifier les montants et éléments trop spécifiques).

---

## 5. Politique de Confidentialité et Protection des Données (RGPD)

Conformément au Règlement Général sur la Protection des Données (RGPD) et à la loi « Informatique et Libertés », l'Éditeur s'engage à assurer la protection de la vie privée des utilisateurs.

### 5.1. Responsable du traitement
Le responsable du traitement des données est l'Éditeur mentionné à l'Article 1 des présentes.

### 5.2. Données collectées et Finalités
* **Données techniques :** Adresse IP, logs de connexion, métadonnées du navigateur.
  * *Finalité :* Assurer la sécurité, la maintenance technique du prototype et prévenir les abus.
  * *Base légale :* Intérêt légitime de l'Éditeur (Art. 6.1.f du RGPD).
* **Données de saisie (*Prompts* et documents) :** Textes juridiques, questions, clauses soumises au chatbot.
  * *Finalité :* Transmission éphémère à l'API Gemini pour générer la réponse demandée par l'utilisateur.
  * *Base légale :* Exécution des conditions d'utilisation / Consentement de l'utilisateur (Art. 6.1.b / Art. 6.1.a du RGPD).

### 5.3. Politique d'utilisation des données par l'API Gemini
L'Éditeur déclare utiliser les services de l'**API professionnelle / entreprise** de Google (via Google AI Studio ou Vertex AI) et non la version grand public de Gemini. 
Selon les conditions contractuelles applicables aux API développeurs de Google :
* **Non-entraînement des modèles :** Les données soumises par l'utilisateur (prompts) et les réponses générées **ne sont pas utilisées** par Google pour entraîner, améliorer ou affiner ses modèles de langage de base (*Foundation Models*).
* **Rétention éphémère :** Les données transitent via des protocoles sécurisés (chiffrement TLS) et ne font l'objet d'aucun stockage permanent par Google. Elles peuvent être conservées de manière temporaire en mémoire tampon par le prestataire (généralement moins de 30 jours) exclusivement pour des raisons de diagnostic technique et de conformité (détection des abus), avant d'être définitivement supprimées.

### 5.4. Absence de stockage local (Architecture sans état / *Stateless*)
L'Application est conçue de manière volatile : l'Éditeur ne stocke l'historique des conversations dans aucune base de données pérenne propre au cabinet. Dès que la session de navigation ou l'onglet Streamlit est fermé, l'historique de la conversation est irrémédiablement effacé de la mémoire vive du serveur.

### 5.5. Transferts hors Union Européenne
L'utilisation de Streamlit Cloud et de l'API Gemini implique un transfert de données techniques et de flux textuels vers les États-Unis. Ces transferts sont juridiquement encadrés :
* Google LLC et Streamlit Inc. s'engagent sur le respect des **Clauses Contractuelles Types (CCT)** approuvées par la Commission Européenne et/ou sont certifiés conformes au **Data Privacy Framework (DPF)** UE-USA, garantissant un niveau de protection substantiellement équivalent aux standards européens.

### 5.6. Droits des personnes concernées
Conformément à la réglementation, vous disposez d'un droit d'accès, de rectification, de limitation, d'opposition et d'effacement de vos données. En raison de l'absence de stockage persistant des conversations, le droit d'accès ne pourra s'exercer que sur les logs techniques résiduels, sous réserve qu'ils contiennent des éléments permettant de vous identifier.

Pour toute demande, vous pouvez contacter l'Éditeur à l'adresse email spécifiée à l'Article 1. Si vous estimez que vos droits ne sont pas respectés, vous disposez du droit d'introduire une réclamation auprès de la Commission Nationale de l'Informatique et des Libertés (CNIL) sur son site internet (cnil.fr).

---

## 6. Propriété Intellectuelle

### 6.1. Propriété de l'Application
L'architecture, le code source propre développé par le cabinet (hors frameworks *open-source* tels que Streamlit), la charte graphique, les logos et la marque de l'Éditeur sont protégés par le droit d'auteur et la propriété intellectuelle. Toute reproduction non autorisée est interdite.

### 6.2. Statut des contenus générés par l'IA
Les droits sur les outputs (textes, réponses, clauses générées) sont régis par le droit commun. En l'état actuel de la législation française et européenne, les créations purement générées par une intelligence artificielle sans intervention créative et originale de l'esprit humain ne bénéficient pas de la protection par le droit d'auteur. 

L'Éditeur ne revendique aucun droit de propriété intellectuelle sur les réponses fournies par l'Application et concède à l'utilisateur une licence d'utilisation libre, gratuite et non exclusive des résultats pour ses besoins professionnels, sous sa seule et unique responsabilité.

---

## 7. Modification des Mentions Légales
L'Éditeur se réserve le droit de modifier, compléter ou mettre à jour les présentes mentions à tout moment, notamment pour se conformer aux évolutions législatives, réglementaires, jurisprudentielles, déontologiques (recommandations du CNB sur l'IA) ou techniques. Les utilisateurs sont invités à les consulter régulièrement.

*Dernière mise à jour : Juin 2026*
